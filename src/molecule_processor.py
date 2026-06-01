from __future__ import annotations
"""
分子处理器 - 基于 RDKit 的分子数据获取与处理
===============================================
从 PubChem API 获取分子数据，使用 RDKit 进行结构验证和属性计算
"""

import json
import time
import logging
from typing import Optional
from dataclasses import dataclass, field, asdict

try:
    from rdkit import Chem
    from rdkit.Chem import Descriptors, Draw, AllChem, rdMolDescriptors
    from rdkit.Chem.QED import qed
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    print("Warning: RDKit not installed. Install with: pip install rdkit-pypi")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

logger = logging.getLogger(__name__)


@dataclass
class MoleculeIdentity:
    """分子标识信息"""
    pubchem_cid: Optional[int] = None
    chembl_id: Optional[str] = None
    drugbank_id: Optional[str] = None
    cas_number: Optional[str] = None


@dataclass
class SmilesInfo:
    """SMILES 标识符"""
    canonical: str = ""
    isomeric: Optional[str] = None
    inchi: str = ""
    inchikey: str = ""


@dataclass
class NamesInfo:
    """分子命名"""
    iupac_name: Optional[str] = None
    common_name: Optional[str] = None
    synonyms: list = field(default_factory=list)


@dataclass
class PhysicochemicalProps:
    """物化属性"""
    molecular_weight: float = 0.0
    exact_mass: Optional[float] = None
    logp: Optional[float] = None
    tpsa: Optional[float] = None
    hydrogen_bond_donors: Optional[int] = None
    hydrogen_bond_acceptors: Optional[int] = None
    rotatable_bonds: Optional[int] = None
    heavy_atoms: Optional[int] = None
    ring_count: Optional[int] = None
    formal_charge: Optional[int] = None


@dataclass
class DruglikenessProps:
    """类药性"""
    lipinski_violations: Optional[int] = None
    synthetic_accessibility: Optional[float] = None
    qed_score: Optional[float] = None


class MoleculeProcessor:
    """分子数据处理器"""

    PUBCHEM_REST_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

    def __init__(self, output_dir: str = "data/processed"):
        self.output_dir = output_dir
        self._cache = {}

    def validate_smiles(self, smiles: str) -> bool:
        """验证 SMILES 合法性"""
        if not RDKIT_AVAILABLE:
            logger.warning("RDKit not available, skipping SMILES validation")
            return True
        mol = Chem.MolFromSmiles(smiles)
        return mol is not None

    def canonicalize_smiles(self, smiles: str) -> Optional[str]:
        """标准化 SMILES"""
        if not RDKIT_AVAILABLE:
            return smiles
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return Chem.MolToSmiles(mol)

    def compute_properties(self, smiles: str) -> tuple[PhysicochemicalProps, DruglikenessProps]:
        """计算分子属性"""
        physico = PhysicochemicalProps()
        druglike = DruglikenessProps()

        if not RDKIT_AVAILABLE:
            return physico, druglike

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return physico, druglike

        physico.molecular_weight = round(Descriptors.MolWt(mol), 2)
        physico.exact_mass = round(Descriptors.ExactMolWt(mol), 4)
        physico.logp = round(Descriptors.MolLogP(mol), 2)
        physico.tpsa = round(Descriptors.TPSA(mol), 2)
        physico.hydrogen_bond_donors = Descriptors.NumHDonors(mol)
        physico.hydrogen_bond_acceptors = Descriptors.NumHAcceptors(mol)
        physico.rotatable_bonds = Descriptors.NumRotatableBonds(mol)
        physico.heavy_atoms = mol.GetNumHeavyAtoms()
        physico.ring_count = Descriptors.RingCount(mol)
        physico.formal_charge = Chem.GetFormalCharge(mol)

        # Lipinski violations
        violations = 0
        if physico.molecular_weight > 500:
            violations += 1
        if physico.logp > 5:
            violations += 1
        if physico.hydrogen_bond_donors > 5:
            violations += 1
        if physico.hydrogen_bond_acceptors > 10:
            violations += 1
        druglike.lipinski_violations = violations

        # QED score
        try:
            druglike.qed_score = round(qed(mol), 4)
        except Exception:
            pass

        # Synthetic Accessibility (simplified estimate)
        try:
            from rdkit.Chem import RDConfig
            import os
            sa_model_path = os.path.join(RDConfig.RDContribDir, 'SA_Score', 'sascore.py')
            if os.path.exists(sa_model_path):
                import importlib.util
                spec = importlib.util.spec_from_file_location("sascore", sa_model_path)
                sa_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(sa_module)
                druglike.synthetic_accessibility = round(sa_module.calculateScore(mol), 2)
        except Exception:
            pass

        return physico, druglike

    def get_smiles_info(self, smiles: str) -> SmilesInfo:
        """获取完整的 SMILES 信息"""
        info = SmilesInfo()

        if RDKIT_AVAILABLE:
            mol = Chem.MolFromSmiles(smiles)
            if mol is not None:
                info.canonical = Chem.MolToSmiles(mol)
                info.isomeric = Chem.MolToSmiles(mol, isomericSmiles=True)
                info.inchi = Chem.MolToInchi(mol)
                info.inchikey = Chem.MolToInchiKey(mol)
        else:
            info.canonical = smiles

        return info

    def generate_2d_image(self, smiles: str, output_path: str, size: tuple = (512, 512)) -> bool:
        """生成 2D 分子结构图"""
        if not RDKIT_AVAILABLE:
            logger.warning("RDKit not available, cannot generate 2D image")
            return False

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return False

        try:
            img = Draw.MolToImage(mol, size=size)
            img.save(output_path)
            return True
        except Exception as e:
            logger.error(f"Failed to generate 2D image: {e}")
            return False

    def generate_3d_conformer(self, smiles: str, output_path: str) -> bool:
        """生成 3D 分子构象 (SDF 格式)"""
        if not RDKIT_AVAILABLE:
            return False

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return False

        mol = Chem.AddHs(mol)
        result = AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())
        if result == -1:
            return False

        try:
            AllChem.MMFFOptimizeMolecule(mol)
            writer = Chem.SDWriter(output_path)
            writer.write(mol)
            writer.close()
            return True
        except Exception as e:
            logger.error(f"Failed to generate 3D conformer: {e}")
            return False

    def fetch_pubchem_data(self, cid: int) -> dict:
        """从 PubChem REST API 获取分子数据"""
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required")

        cache_key = f"pubchem_{cid}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        result = {}

        # Fetch compound properties
        props_url = f"{self.PUBCHEM_REST_BASE}/compound/cid/{cid}/property/CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,MolecularWeight,ExactMass,XLogP,TPSA,Complexity,HeavyAtomCount,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,Charge/JSON"
        try:
            resp = requests.get(props_url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                props = data.get("PropertyTable", {}).get("Properties", [{}])[0]
                result["properties"] = props
                result["smiles"] = props.get("CanonicalSMILES", "")
        except Exception as e:
            logger.error(f"Failed to fetch PubChem properties for CID {cid}: {e}")

        time.sleep(0.2)  # Rate limiting

        # Fetch synonyms
        syn_url = f"{self.PUBCHEM_REST_BASE}/compound/cid/{cid}/synonyms/TXT"
        try:
            resp = requests.get(syn_url, timeout=30)
            if resp.status_code == 200:
                synonyms = resp.text.strip().split("\n")
                result["synonyms"] = [s.strip() for s in synonyms[:50]]  # Top 50
        except Exception as e:
            logger.error(f"Failed to fetch synonyms for CID {cid}: {e}")

        time.sleep(0.2)

        # Fetch description
        desc_url = f"{self.PUBCHEM_REST_BASE}/compound/cid/{cid}/description/JSON"
        try:
            resp = requests.get(desc_url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                descriptions = data.get("InformationList", {}).get("Information", [])
                result["descriptions"] = descriptions
        except Exception as e:
            logger.error(f"Failed to fetch description for CID {cid}: {e}")

        self._cache[cache_key] = result
        return result

    def fetch_pubchem_by_name(self, name: str) -> Optional[int]:
        """通过名称查找 PubChem CID"""
        if not REQUESTS_AVAILABLE:
            return None

        url = f"{self.PUBCHEM_REST_BASE}/compound/name/{name}/cids/JSON"
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                cids = data.get("IdentifierList", {}).get("CID", [])
                return cids[0] if cids else None
        except Exception:
            pass
        return None

    def build_alignment_record(
        self,
        record_id: str,
        smiles: str,
        pubchem_cid: Optional[int] = None,
        common_name: Optional[str] = None,
        text_descriptions: Optional[list] = None,
        entity_relations: Optional[list] = None,
        mineru_usage: Optional[list] = None,
        source_papers: Optional[list] = None
    ) -> dict:
        """
        构建一条完整的跨模态对齐记录

        Args:
            record_id: 记录 ID (e.g. "MOL-000001")
            smiles: 分子 SMILES
            pubchem_cid: PubChem CID (可选)
            common_name: 通用名称
            text_descriptions: 文本描述列表
            entity_relations: 实体关系列表
            mineru_usage: MinerU 使用记录
            source_papers: 来源论文 DOI 列表

        Returns:
            完整的对齐记录 dict
        """
        # 获取 SMILES 信息
        smiles_info = self.get_smiles_info(smiles)

        # 计算属性
        physico, druglike = self.compute_properties(smiles)

        # PubChem 数据补充
        names = NamesInfo(common_name=common_name)
        pubchem_data = {}
        if pubchem_cid:
            pubchem_data = self.fetch_pubchem_data(pubchem_cid)
            pc_props = pubchem_data.get("properties", {})
            if pc_props.get("IUPACName"):
                names.iupac_name = pc_props["IUPACName"]
            synonyms = pubchem_data.get("synonyms", [])
            if synonyms:
                names.synonyms = synonyms[:20]
                if not common_name and synonyms:
                    names.common_name = synonyms[0]

        # 构建记录
        record = {
            "record_id": record_id,
            "molecule_id": {
                "pubchem_cid": pubchem_cid,
                "chembl_id": None,
                "drugbank_id": None,
                "cas_number": None
            },
            "smiles": {
                "canonical": smiles_info.canonical,
                "isomeric": smiles_info.isomeric,
                "inchi": smiles_info.inchi,
                "inchikey": smiles_info.inchikey
            },
            "names": asdict(names),
            "modalities": {
                "structure_2d": {
                    "rdkit_generated": f"images/2d/{record_id}.png",
                    "image_format": "png",
                    "image_size": "512x512"
                },
                "structure_paper": None,
                "structure_3d": {
                    "sdf_path": f"models/3d/{record_id}.sdf",
                    "conformer_method": "RDKit_ETKDG"
                },
                "table_data": None
            },
            "properties": {
                "physicochemical": asdict(physico),
                "drug_likeness": asdict(druglike),
                "experimental": None
            },
            "text_descriptions": text_descriptions or [],
            "entity_relations": entity_relations or [],
            "alignment_metadata": {
                "alignment_confidence": 0.95 if pubchem_cid else 0.80,
                "validation_status": "automated_pass" if self.validate_smiles(smiles) else "flagged_for_review",
                "mineru_usage": mineru_usage or [],
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0"
            }
        }

        return record
