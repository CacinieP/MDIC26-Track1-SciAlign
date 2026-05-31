"""
Expand Molecule Database
========================
Expands the molecule database from 120 to ~1200 molecules.
Uses PubChem Name→CID batch API to resolve compound IDs.
"""

import os
import sys
import json
import time
import logging

try:
    import requests
except ImportError:
    print("ERROR: requests library required. pip install requests")
    sys.exit(1)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from scripts.molecule_db import MOLECULE_DB as EXISTING_DB

PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# ============================================================
# New molecules by category (~1100 additional molecules)
# ============================================================
NEW_MOLECULES = {
    # NSAID Drugs (adding 24 to existing 6 = 30)
    "NSAID Drug": [
        "meloxicam", "piroxicam", "sulindac", "etodolac", "ketorolac",
        "nabumetone", "mefenamic acid", "diclofenac sodium", "flurbiprofen",
        "ketoprofen", "fenoprofen", "tolmetin", "oxaprozin", "indomethacin sodium",
        "diflunisal", "salsalate", "valdecoxib", "rofecoxib", "parecoxib",
        "dexibuprofen", "dexketoprofen", "aceclofenac", "phenylbutazone",
        "tenoxicam",
    ],
    # Antibiotics (adding 72 to existing 8 = 80)
    "Antibiotic": [
        # Cephalosporins
        "cephalexin", "ceftriaxone", "ceftazidime", "cefazolin", "cefuroxime",
        "cefepime", "cefixime", "cefotaxime", "cefdinir", "cefadroxil",
        "cefprozil", "cefpodoxime", "cefotetan", "cefoxitin",
        # Macrolides
        "erythromycin", "clarithromycin", "telithromycin", "fidaxomicin",
        # Aminoglycosides
        "amikacin", "tobramycin", "neomycin", "kanamycin", "streptomycin",
        # Tetracyclines
        "tetracycline", "minocycline", "tigecycline", "demeclocycline",
        # Sulfonamides
        "trimethoprim", "sulfamethoxazole", "sulfadiazine", "sulfasalazine",
        # Fluoroquinolones
        "levofloxacin", "moxifloxacin", "ofloxacin", "gatifloxacin", "gemifloxacin",
        "norfloxacin", "lomefloxacin", "sparfloxacin", "trovafloxacin",
        # Glycopeptides
        "teicoplanin", "dalbavancin", "oritavancin", "telavancin",
        # Others
        "clindamycin", "lincomycin", "chloramphenicol", "nitrofurantoin",
        "fosfomycin", "bacitracin", "polymyxin B", "colistin", "daptomycin",
        "linezolid", "tedizolid", "quinupristin", "dalfopristin",
        "rifampin", "rifabutin", "rifapentine", "pyrazinamide",
        "ethambutol", "isoniazid", "clofazimine", "dapsone",
        "spectinomycin", "fusidic acid", "mupirocin", "nitrofurazone",
    ],
    # Antiviral Drugs (adding 35 to existing 5 = 40)
    "Antiviral Drug": [
        # HIV
        "efavirenz", "tenofovir", "emtricitabine", "dolutegravir", "bictegravir",
        "raltegravir", "elvitegravir", "abacavir", "lamivudine", "stavudine",
        "didanosine", "nevirapine", "etravirine", "rilpivirine", "darunavir",
        "lopinavir", "atazanavir", "fosamprenavir", "tipranavir", "maraviroc",
        "enfuvirtide", "dolutegravir sodium",
        # Hepatitis
        "sofosbuvir", "ledipasvir", "daclatasvir", "simeprevir", "ombitasvir",
        "paritaprevir", "velpatasvir", "entecavir", "telbivudine", "ribavirin",
        # COVID / Other
        "nirmatrelvir", "molnupiravir", "favipiravir", "baloxavir",
        "penciclovir", "ganciclovir", "valganciclovir", "foscarnet",
        "cidofovir", "amantadine", "rimantadine",
    ],
    # Anticancer Drugs (adding 72 to existing 8 = 80)
    "Anticancer Drug": [
        # Platinum compounds
        "carboplatin", "oxaliplatin", "cisplatin",
        # Antimetabolites
        "gemcitabine", "capecitabine", "pemetrexed", "raltitrexed",
        "cladribine", "clofarabine", "nelarabine", "fludarabine",
        "cytarabine", "mercaptopurine", "thioguanine", "floxuridine",
        # Alkylating agents
        "temozolomide", "ifosfamide", "busulfan", "carmustine", "lomustine",
        "melphalan", "chlorambucil", "bendamustine", "cyclophosphamide",
        "dacarbazine", "procarbazine", "thiotepa",
        # Hormonal therapy
        "anastrozole", "letrozole", "exemestane", "tamoxifen citrate",
        "fulvestrant", "bicalutamide", "flutamide", "enzalutamide",
        "abiraterone", "leuprolide", "goserelin", "degarelix",
        # Topoisomerase inhibitors
        "etoposide", "teniposide", "irinotecan", "topotecan",
        # Vinca alkaloids & taxanes
        "vinblastine", "vincristine", "vinorelbine", "docetaxel",
        "cabazitaxel", "paclitaxel albumin",
        # Anthracyclines
        "daunorubicin", "epirubicin", "idarubicin", "mitoxantrone",
        # Others
        "bleomycin", "dactinomycin", "mitomycin", "hydroxycarbamide",
        "bortezomib", "carfilzomib", "ixazomib",
        "lenalidomide", "pomalidomide", "thalidomide",
        "vorinostat", "romidepsin", "panobinostat",
        "venetoclax", "azacitidine", "decitabine",
        "asparaginase", "pegaspargase", "arsenic trioxide",
        "all-trans retinoic acid",
    ],
    # Targeted Therapy (adding 55 to existing 5 = 60)
    "Targeted Therapy": [
        # EGFR inhibitors
        "afatinib", "osimertinib", "alectinib", "brigatinib", "lorlatinib",
        "crizotinib", "ceritinib", "gefitinib", "erlotinib",
        # Multi-kinase inhibitors
        "sorafenib", "sunitinib", "pazopanib", "regorafenib", "cabozantinib",
        "lenvatinib", "vandetanib", "axitinib", "tivozanib",
        # CDK inhibitors
        "palbociclib", "ribociclib", "abemaciclib",
        # PARP inhibitors
        "olaparib", "rucaparib", "niraparib", "talazoparib",
        # BRAF/MEK inhibitors
        "vemurafenib", "dabrafenib", "trametinib", "cobimetinib", "binimetinib",
        "encorafenib",
        # PI3K/mTOR inhibitors
        "everolimus", "temsirolimus", "idelalisib", "duvelisib", "copanlisib",
        "alpelisib",
        # BTK/JAK inhibitors
        "ibrutinib", "acalabrutinib", "zanubrutinib",
        "ruxolitinib", "fedratinib", "pacritinib",
        # HER2 inhibitors
        "lapatinib", "neratinib", "tucatinib", "pyrotinib",
        # ALK/ROS1
        "entrectinib", "larotrectinib", "selpercatinib",
        # HDAC
        "tucidinostat",
        # Other targeted
        "sonidegib", "vismodegib", "siponimod",
    ],
    # Antidiabetic Drugs (adding 35 to existing 5 = 40)
    "Antidiabetic Drug": [
        # Sulfonylureas
        "glimepiride", "glipizide", "glyburide", "gliclazide", "tolbutamide",
        "chlorpropamide",
        # SGLT2 inhibitors
        "dapagliflozin", "canagliflozin", "empagliflozin", "ertugliflozin",
        "ipragliflozin", "tofogliflozin", "luseogliflozin",
        # GLP-1 agonists (small molecule components)
        "semaglutide", "liraglutide", "exenatide", "dulaglutide", "lixisenatide",
        # DPP-4 inhibitors
        "sitagliptin", "vildagliptin", "saxagliptin", "alogliptin", "linagliptin",
        "gemigliptin", "teneligliptin", "anagliptin", "omarigliptin",
        # Thiazolidinediones
        "pioglitazone", "rosiglitazone", "troglitazone",
        # Alpha-glucosidase inhibitors
        "acarbose", "miglitol", "voglibose",
        # Meglitinides
        "repaglinide", "nateglinide", "mitiglinide",
        # Others
        "pramlintide", "bromocriptine", "colesevelam",
    ],
    # Antidepressants (adding 34 to existing 6 = 40)
    "Antidepressant": [
        # SSRIs
        "sertraline", "paroxetine", "citalopram", "escitalopram", "fluvoxamine",
        # SNRIs
        "duloxetine", "desvenlafaxine", "venlafaxine", "milnacipran", "levomilnacipran",
        # TCAs
        "nortriptyline", "imipramine", "amitriptyline", "clomipramine", "doxepin",
        "protriptyline", "desipramine", "trimipramine",
        # Atypical
        "bupropion", "mirtazapine", "trazodone", "nefazodone", "vortioxetine",
        "vilazodone",
        # MAOIs
        "moclobemide", "selegiline", "phenelzine", "tranylcypromine", "isocarboxazid",
        # Others
        "agomelatine", "reboxetine", "amoxapine", "maprotiline",
    ],
    # Antihypertensives (adding 44 to existing 6 = 50)
    "Antihypertensive": [
        # ARBs
        "telmisartan", "irbesartan", "valsartan", "candesartan", "olmesartan",
        "eprosartan", "fimasartan", "azilsartan",
        # CCBs
        "nifedipine", "diltiazem", "verapamil", "felodipine", "isradipine",
        "nicardipine", "nimodipine", "clevidipine", "lercanidipine", "manidipine",
        # ACE inhibitors
        "ramipril", "captopril", "enalapril", "fosinopril", "benazepril",
        "quinapril", "moexipril", "perindopril", "trandolapril", "lisinopril",
        # Beta-blockers
        "atenolol", "carvedilol", "nebivolol", "bisoprolol", "metoprolol tartrate",
        "propranolol", "labetalol", "sotalol", "acebutolol", "pindolol",
        "nadolol", "timolol", "penbutolol",
        # Alpha-blockers
        "doxazosin", "prazosin", "terazosin",
        # Direct vasodilators
        "hydralazine", "minoxidil", "sodium nitroprusside",
        # Others
        "clonidine", "methyldopa", "reserpine",
    ],
    # Statins (adding 11 to existing 4 = 15)
    "Statin": [
        "fluvastatin", "lovastatin", "pitavastatin", "rosuvastatin calcium",
        "pravastatin sodium", "simvastatin sodium", "atorvastatin calcium",
        "fluvastatin sodium", "cerivastatin", "compactin", "mevastatin",
    ],
    # Antihistamines (adding 16 to existing 4 = 20)
    "Antihistamine": [
        "levocetirizine", "desloratadine", "hydroxyzine", "cyproheptadine",
        "fexofenadine", "loratadine", "azelastine", "ketotifen",
        "chlorpheniramine", "diphenhydramine", "promethazine", "clemastine",
        "dimenhydrinate", "meclizine", "ebastine", "bepotastine",
    ],
    # Opioid Analgesics (adding 16 to existing 4 = 20)
    "Opioid Analgesic": [
        "oxycodone", "hydrocodone", "hydromorphone", "buprenorphine",
        "methadone", "fentanyl", "codeine", "tramadol", "tapentadol",
        "meperidine", "morphine sulfate", "sufentanil", "alfentanil",
        "remifentanil", "pentazocine", "nalbuphine",
    ],
    # Bronchodilators (adding 12 to existing 3 = 15)
    "Bronchodilator": [
        "salbutamol", "terbutaline", "formoterol", "salmeterol",
        "indacaterol", "olodaterol", "vilanterol", "tiotropium",
        "ipratropium", "aclidinium", "umeclidinium", "glycopyrrolate",
    ],
    # Anticoagulants (adding 12 to existing 3 = 15)
    "Anticoagulant": [
        "apixaban", "edoxaban", "dabigatran", "enoxaparin", "fondaparinux",
        "heparin", "warfarin sodium", "rivaroxaban", "argatroban",
        "bivalirudin", "phenprocoumon", "ticagrelor",
    ],
    # Immunosuppressants (adding 11 to existing 4 = 15)
    "Immunosuppressant": [
        "azathioprine", "mycophenolic acid", "everolimus", "sirolimus",
        "tacrolimus", "cyclosporine", "belatacept", "gusperimus",
        "fingolimod", "dimethyl fumarate", "teriflunomide",
    ],
    # Antifungal Drugs (adding 16 to existing 4 = 20)
    "Antifungal Drug": [
        "voriconazole", "posaconazole", "caspofungin", "terbinafine",
        "griseofulvin", "anidulafungin", "micafungin", "flucytosine",
        "ketoconazole", "miconazole", "clotrimazole", "econazole",
        "itraconazole", "fluconazole", "nystatin", "amphotericin B liposomal",
    ],
    # Antimalarial Drugs (adding 11 to existing 4 = 15)
    "Antimalarial Drug": [
        "primaquine", "atovaquone", "proguanil", "lumefantrine",
        "mefloquine", "artemether", "artesunate", "dihydroartemisinin",
        "chloroquine phosphate", "piperaquine", "tafenoquine",
    ],
    # Natural Products (adding 54 to existing 6 = 60)
    "Natural Product": [
        # Flavonoids
        "luteolin", "apigenin", "kaempferol", "quercetin", "myricetin",
        "genistein", "daidzein", "baicalein", "wogonin", "naringenin",
        "hesperetin", "chrysin", "fisetin", "morin", "tangeretin",
        # Terpenoids
        "artemether", "menthol", "camphor", "limonene", "pinene",
        "linalool", "thymol", "carvacrol", "geraniol", "citronellol",
        # Alkaloids
        "nicotine", "strychnine", "atropine", "scopolamine", "cocaine",
        "quinine", "quinidine", "vincamine", "yohimbine", "berberine",
        # Polyphenols
        "rosmarinic acid", "chlorogenic acid", "gallic acid", "ellagic acid",
        "ferulic acid", "caffeic acid", "resveratrol", "curcumin",
        "epigallocatechin gallate", "nordihydroguaiaretic acid",
        # Terpenes / Steroids from nature
        "digitoxin", "digoxin", "ouabain", "stigmasterol", "beta-sitosterol",
        "ursolic acid", "oleanolic acid", "betulinic acid", "maslinic acid",
    ],
    # Neurotransmitters (adding 18 to existing 7 = 25)
    "Neurotransmitter": [
        "glycine", "taurine", "epinephrine", "acetylcholine chloride",
        "histamine", "glutamic acid", "aspartic acid", "beta-alanine",
        "norepinephrine", "salsolinol", "anandamide", "2-AG",
        "adenosine", "GHB", "phenethylamine", "tryptamine",
        "spermidine", "spermine",
    ],
    # Hormones (adding 23 to existing 7 = 30)
    "Hormone": [
        "aldosterone", "dehydroepiandrosterone", "oxytocin",
        "prostaglandin E2", "prostaglandin F2alpha", "leukotriene B4",
        "melatonin", "triiodothyronine", "thyroxine", "calcitonin",
        "parathyroid hormone", "glucagon", "somatostatin",
        "cortisol", "cortisone", "prednisone", "prednisolone",
        "testosterone", "estradiol", "progesterone", "relaxin",
        "erythropoietin", "cholecystokinin",
    ],
    # Vitamins (adding 15 to existing 5 = 20)
    "Vitamin": [
        "pyridoxine", "cyanocobalamin", "folic acid", "biotin",
        "cholecalciferol", "ergocalciferol", "thiamine", "riboflavin",
        "niacinamide", "pantothenic acid", "phylloquinone",
        "menaquinone", "retinoic acid", "alpha-tocopherol",
        "ascorbic acid sodium",
    ],
    # Anesthetics (adding 11 to existing 4 = 15)
    "Anesthetic": [
        "sevoflurane", "desflurane", "bupivacaine", "ropivacaine",
        "etomidate", "propofol", "isoflurane", "lidocaine",
        "prilocaine", "mepivacaine", "ketamine hydrochloride",
    ],
    # Anti-inflammatory (adding 16 to existing 4 = 20)
    "Anti-inflammatory": [
        "hydrocortisone", "prednisolone", "triamcinolone", "betamethasone",
        "deflazacort", "methylprednisolone", "dexamethasone sodium phosphate",
        "beclomethasone", "fluticasone", "budesonide", "momethasone",
        "clobetasol", "halobetasol", "difluprednate", "fluocinolone",
        "desonide",
    ],
    # Gastrointestinal Drugs (adding 12 to existing 3 = 15)
    "Gastrointestinal Drug": [
        "omeprazole", "pantoprazole", "esomeprazole", "lansoprazole",
        "rabeprazole", "famotidine", "ranitidine", "nizatidine",
        "metoclopramide", "ondansetron", "granisetron", "loperamide",
    ],
    # Antigout (adding 9 to existing 1 = 10)
    "Antigout Drug": [
        "colchicine", "febuxostat", "probenecid", "lesinurad",
        "pegloticase", "rasburicase", "benzbromarone", "sulfinpyrazone",
        "allopurinol",
    ],
    # Analgesic (adding 9 to existing 1 = 10)
    "Analgesic": [
        "acetaminophen", "ibuprofen lysine", "dexketoprofen", "flupirtine",
        "nefopam", "ziconotide", "carisoprodol", "gabapentin", "pregabalin",
    ],
    # Stimulants (adding 7 to existing 3 = 10)
    "Stimulant": [
        "modafinil", "armodafinil", "caffeine", "nicotine",
        "theophylline", "pemoline", "atomoxetine",
    ],
    # ============================================================
    # NEW CATEGORIES
    # ============================================================
    # Diuretics (20)
    "Diuretic": [
        "furosemide", "hydrochlorothiazide", "spironolactone", "amiloride",
        "triamterene", "bumetanide", "torsemide", "ethacrynic acid",
        "chlorthalidone", "indapamide", "metolazone", "acetazolamide",
        "mannitol", "eplerenone", "chlorthalidone", "xipamide",
        "clopamide", "cannrenoate", "benzthiazide", "polythiazide",
    ],
    # Anti-epileptic Drugs (20)
    "Anti-epileptic Drug": [
        "carbamazepine", "valproic acid", "phenytoin", "levetiracetam",
        "lamotrigine", "topiramate", "gabapentin", "pregabalin",
        "oxcarbazepine", "zonisamide", "lacosamide", "rufinamide",
        "eslicarbazepine", "brivaracetam", "clobazam", "clonazepam",
        "ethosuximide", "felbamate", "tiagabine", "vigabatrin",
    ],
    # Anti-Parkinson Drugs (15)
    "Anti-Parkinson Drug": [
        "levodopa", "carbidopa", "pramipexole", "ropinirole", "rotigotine",
        "selegiline", "rasagiline", "safinamide", "entacapone",
        "tolcapone", "benztropine", "trihexyphenidyl", "amantadine",
        "apomorphine", "istradefylline",
    ],
    # Amino Acids (25)
    "Amino Acid": [
        "L-lysine", "L-arginine", "L-glutamine", "L-cysteine", "L-methionine",
        "L-tryptophan", "L-tyrosine", "L-phenylalanine", "L-leucine", "L-isoleucine",
        "L-valine", "L-threonine", "L-serine", "L-asparagine", "L-proline",
        "L-histidine", "L-alanine", "L-citrulline", "L-ornithine",
        "L-theanine", "L-carnitine", "acetyl-L-carnitine",
        "N-acetylcysteine", "S-adenosylmethionine", "creatine",
    ],
    # Antihyperlipidemic (15)
    "Antihyperlipidemic": [
        "ezetimibe", "fenofibrate", "gemfibrozil", "niacin",
        "cholestyramine", "colestipol", "evolocumab", "alirocumab",
        "benzafibrate", "ciprofibrate", "clofibrate", "bezafibrate",
        "omega-3 fatty acids", "lomitapide", "mipomersen",
    ],
    # Muscle Relaxant (10)
    "Muscle Relaxant": [
        "baclofen", "cyclobenzaprine", "tizanidine", "methocarbamol",
        "dantrolene", "orphenadrine", "chlorzoxazone", "metaxalone",
        "succinylcholine", "pancuronium",
    ],
    # Anti-osteoporosis (10)
    "Anti-osteoporosis Drug": [
        "alendronate", "risedronate", "zoledronic acid", "ibandronate",
        "denosumab", "teriparatide", "raloxifene", "calcitonin salmon",
        "strontium ranelate", "tiludronate",
    ],
    # Diagnostic Agent (10)
    "Diagnostic Agent": [
        "iodixanol", "iohexol", "gadopentetic acid", "gadodiamide",
        "technetium tc-99m", "barium sulfate", "fluorescein sodium",
        "indocyanine green", "methylene blue", "congo red",
    ],
    # Solvent / Reagent (10)
    "Chemical Reagent": [
        "dimethyl sulfoxide", "ethylene glycol", "propylene glycol",
        "polyethylene glycol 400", "glycerol", "isopropanol",
        "n-butanol", "formaldehyde", "acetaldehyde", "glacial acetic acid",
    ],
}


def batch_resolve_cids(names, batch_size=80):
    """Resolve compound names to PubChem CIDs using individual GET requests."""
    import urllib.parse
    cids = {}
    total = len(names)

    for i, name in enumerate(names):
        encoded = urllib.parse.quote(name, safe="")
        url = f"{PUBCHEM_BASE}/compound/name/{encoded}/cids/JSON"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                cid_list = data.get("IdentifierList", {}).get("CID", [])
                if cid_list:
                    cids[name] = cid_list[0]
        except Exception:
            pass

        if (i + 1) % 50 == 0 or i == total - 1:
            logger.info(f"  Progress: {i + 1}/{total} resolved so far: {len(cids)}")

        time.sleep(0.25)

    return cids


def main():
    logger.info(f"Starting molecule database expansion from {len(EXISTING_DB)} existing molecules")

    # Collect all new names
    all_new_names = []
    category_map = {}  # name -> category
    for category, names in NEW_MOLECULES.items():
        for name in names:
            name_lower = name.lower().strip()
            # Skip duplicates
            if name_lower not in category_map:
                all_new_names.append(name_lower)
                category_map[name_lower] = category

    logger.info(f"Total new molecule names to resolve: {len(all_new_names)}")

    # Batch resolve CIDs
    logger.info("Resolving PubChem CIDs...")
    name_to_cid = batch_resolve_cids(all_new_names)

    resolved = len(name_to_cid)
    unresolved = len(all_new_names) - resolved
    logger.info(f"Resolved: {resolved}, Unresolved: {unresolved}")

    # Get existing CIDs to avoid duplicates
    existing_cids = {entry["pubchem_cid"] for entry in EXISTING_DB.values()}

    # Build expanded database
    expanded_db = dict(EXISTING_DB)  # Start with existing

    next_id = len(EXISTING_DB) + 1
    added = 0
    skipped = 0

    for name in all_new_names:
        cid = name_to_cid.get(name)
        if cid is None:
            skipped += 1
            continue
        if cid in existing_cids:
            skipped += 1
            continue

        record_id = f"MOL-{next_id:06d}"
        # Capitalize name for display
        display_name = name.title() if len(name) > 2 else name.upper()

        expanded_db[record_id] = {
            "name": display_name,
            "pubchem_cid": cid,
            "category": category_map[name],
        }
        existing_cids.add(cid)
        next_id += 1
        added += 1

    logger.info(f"Added: {added}, Skipped: {skipped}")
    logger.info(f"Total database size: {len(expanded_db)}")

    # Write output file
    output_path = os.path.join(PROJECT_ROOT, "scripts", "molecule_db_expanded.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write('"""\n')
        f.write("MolAlign Expanded Molecule Database\n")
        f.write("====================================\n")
        f.write(f"Auto-generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total molecules: {len(expanded_db)}\n")
        f.write('"""\n\n')
        f.write("MOLECULE_DB = {\n")

        # Group by category for readability
        from collections import defaultdict
        by_category = defaultdict(list)
        for rid, entry in sorted(expanded_db.items()):
            by_category[entry["category"]].append((rid, entry))

        for category, items in sorted(by_category.items()):
            f.write(f"\n    # {'=' * 60}\n")
            f.write(f"    # {category}\n")
            f.write(f"    # {'=' * 60}\n")
            for rid, entry in items:
                f.write(f'    "{rid}": {{"name": "{entry["name"]}", "pubchem_cid": {entry["pubchem_cid"]}, "category": "{entry["category"]}"}},\n')

        f.write("}\n")

    logger.info(f"Written to {output_path}")

    # Stats
    cat_counts = defaultdict(int)
    for entry in expanded_db.values():
        cat_counts[entry["category"]] += 1

    print(f"\n{'=' * 50}")
    print(f"EXPANDED MOLECULE DATABASE STATISTICS")
    print(f"{'=' * 50}")
    print(f"Total molecules: {len(expanded_db)}")
    print(f"Categories: {len(cat_counts)}")
    print()
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    print(f"\nOutput: {output_path}")


if __name__ == "__main__":
    main()
