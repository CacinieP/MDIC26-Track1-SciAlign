"""
跨模态对齐验证器
================
验证分子数据各模态之间的一致性和完整性
"""

import json
import logging
from typing import List, Tuple, Dict, Any

try:
    from rdkit import Chem
    from rdkit.Chem import Descriptors
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False

from src.schema import ALIGNMENT_RECORD_REQUIRED_FIELDS, VALID_RELATION_TYPES

logger = logging.getLogger(__name__)


class AlignmentValidator:
    """跨模态对齐数据验证器"""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def validate_record(self, record: dict) -> Tuple[bool, List[str], List[str]]:
        """
        验证一条对齐记录的完整性和一致性

        Returns:
            (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []

        # 1. 必填字段检查
        self._check_required_fields(record)

        # 2. SMILES 合法性
        smiles_data = record.get("smiles", {})
        canonical = smiles_data.get("canonical", "")
        if canonical:
            self._validate_smiles(canonical)
        else:
            self.errors.append("Missing canonical SMILES")

        # 3. 属性一致性
        self._validate_properties(record)

        # 4. 文本描述完整性
        self._validate_descriptions(record)

        # 5. 实体关系格式
        self._validate_relations(record)

        # 6. 模态完整性
        self._validate_modalities(record)

        # 7. 元数据检查
        self._validate_metadata(record)

        is_valid = len(self.errors) == 0
        return is_valid, self.errors.copy(), self.warnings.copy()

    def _check_required_fields(self, record: dict):
        """检查必填字段"""
        for field_name in ALIGNMENT_RECORD_REQUIRED_FIELDS:
            if field_name not in record:
                self.errors.append(f"Missing required field: {field_name}")

    def _validate_smiles(self, smiles: str):
        """验证 SMILES 合法性和一致性"""
        if not RDKIT_AVAILABLE:
            self.warnings.append("RDKit not available, cannot validate SMILES")
            return

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            self.errors.append(f"Invalid SMILES: {smiles}")
            return

        # 检查是否为 canonical SMILES
        canonical = Chem.MolToSmiles(mol)
        if canonical != smiles:
            self.warnings.append(
                f"SMILES not canonical. Got: {smiles}, Expected: {canonical}"
            )

    def _validate_properties(self, record: dict):
        """验证分子属性与 SMILES 的一致性"""
        if not RDKIT_AVAILABLE:
            return

        smiles = record.get("smiles", {}).get("canonical", "")
        if not smiles:
            return

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return

        physico = record.get("properties", {}).get("physicochemical", {})

        # 验证分子量（PubChem 用平均 MW，RDKit 用精确 MW，允许较大容差）
        expected_mw = round(Descriptors.ExactMolWt(mol), 2)
        actual_mw = physico.get("molecular_weight")
        if actual_mw and abs(actual_mw - expected_mw) > 5.0:
            self.errors.append(
                f"Molecular weight mismatch: record={actual_mw}, calculated={expected_mw}"
            )
        elif actual_mw and abs(actual_mw - expected_mw) > 1.0:
            self.warnings.append(
                f"Molecular weight difference (PubChem vs RDKit): record={actual_mw}, calculated={expected_mw}"
            )

        # 注：PubChem 和 RDKit 对 HBD/HBA 定义不同
        # PubChem: 基于 Lipinski 原始定义; RDKit: 基于 Wildman-Crippen logP 方法
        # 这些差异作为 warning 而非 error 处理
        expected_hbd = Descriptors.NumHDonors(mol)
        actual_hbd = physico.get("hydrogen_bond_donors")
        if actual_hbd is not None and actual_hbd != expected_hbd:
            self.warnings.append(
                f"HBD difference (PubChem={actual_hbd}, RDKit={expected_hbd})"
            )

        expected_hba = Descriptors.NumHAcceptors(mol)
        actual_hba = physico.get("hydrogen_bond_acceptors")
        if actual_hba is not None and actual_hba != expected_hba:
            self.warnings.append(
                f"HBA difference (PubChem={actual_hba}, RDKit={expected_hba})"
            )

    def _validate_descriptions(self, record: dict):
        """验证文本描述"""
        descriptions = record.get("text_descriptions", [])
        if not descriptions:
            self.warnings.append("No text descriptions provided")
            return

        for i, desc in enumerate(descriptions):
            if "type" not in desc:
                self.errors.append(f"Description {i}: missing 'type' field")
            if "content" not in desc or not desc["content"]:
                self.errors.append(f"Description {i}: missing or empty 'content'")
            if "source" not in desc:
                self.warnings.append(f"Description {i}: missing 'source' field")

    def _validate_relations(self, record: dict):
        """验证实体关系"""
        relations = record.get("entity_relations", [])
        for i, rel in enumerate(relations):
            if "subject" not in rel:
                self.errors.append(f"Relation {i}: missing 'subject'")
            if "relation" not in rel:
                self.errors.append(f"Relation {i}: missing 'relation'")
            if "object" not in rel:
                self.errors.append(f"Relation {i}: missing 'object'")

            relation_type = rel.get("relation", "")
            if relation_type and relation_type not in VALID_RELATION_TYPES:
                self.warnings.append(
                    f"Relation {i}: uncommon relation type '{relation_type}'"
                )

    def _validate_modalities(self, record: dict):
        """验证模态数据完整性"""
        modalities = record.get("modalities", {})

        if not modalities.get("structure_2d"):
            self.errors.append("Missing 2D structure modality (required)")
        else:
            s2d = modalities["structure_2d"]
            if not s2d.get("rdkit_generated"):
                self.warnings.append("No RDKit-generated 2D image path")

        # Paper-sourced images are a coverage metric, not a per-record
        # requirement. Dataset-level stats report how many records have them.

    def _validate_metadata(self, record: dict):
        """验证元数据"""
        meta = record.get("alignment_metadata", {})
        if not meta:
            self.errors.append("Missing alignment_metadata")
            return

        if "alignment_confidence" not in meta:
            self.warnings.append("Missing alignment_confidence")
        elif not (0 <= meta["alignment_confidence"] <= 1):
            self.errors.append("alignment_confidence must be between 0 and 1")

        if "validation_status" not in meta:
            self.warnings.append("Missing validation_status")

        # Per-record MinerU evidence is optional. The competition requires the
        # dataset construction process to use MinerU, but records sourced only
        # from PubChem should keep an empty list instead of template evidence.

    def validate_dataset(self, records: List[dict]) -> Dict[str, Any]:
        """
        验证整个数据集

        Returns:
            {
                "total": int,
                "valid": int,
                "invalid": int,
                "errors": {record_id: [errors]},
                "warnings": {record_id: [warnings]},
                "statistics": {...}
            }
        """
        results = {
            "total": len(records),
            "valid": 0,
            "invalid": 0,
            "errors": {},
            "warnings": {},
            "statistics": {
                "avg_descriptions": 0,
                "avg_relations": 0,
                "with_paper_image": 0,
                "with_experimental_data": 0,
                "mineru_used_count": 0,
            }
        }

        total_descs = 0
        total_rels = 0

        for record in records:
            rid = record.get("record_id", "unknown")
            is_valid, errors, warnings = self.validate_record(record)

            if is_valid:
                results["valid"] += 1
            else:
                results["invalid"] += 1

            if errors:
                results["errors"][rid] = errors
            if warnings:
                results["warnings"][rid] = warnings

            # Statistics
            total_descs += len(record.get("text_descriptions", []))
            total_rels += len(record.get("entity_relations", []))

            if record.get("modalities", {}).get("structure_paper"):
                results["statistics"]["with_paper_image"] += 1
            if record.get("properties", {}).get("experimental"):
                results["statistics"]["with_experimental_data"] += 1
            if record.get("alignment_metadata", {}).get("mineru_usage"):
                results["statistics"]["mineru_used_count"] += 1

        n = len(records) or 1
        results["statistics"]["avg_descriptions"] = round(total_descs / n, 1)
        results["statistics"]["avg_relations"] = round(total_rels / n, 1)

        return results
