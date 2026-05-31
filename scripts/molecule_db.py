"""
MolAlign 分子目标数据库
========================
覆盖 20+ 药物类别的 120 个分子
"""

MOLECULE_DB = {
    # ================================================================
    # NSAID Drugs (非甾体抗炎药)
    # ================================================================
    "MOL-000001": {"name": "Aspirin", "pubchem_cid": 2244, "category": "NSAID Drug"},
    "MOL-000002": {"name": "Ibuprofen", "pubchem_cid": 3672, "category": "NSAID Drug"},
    "MOL-000003": {"name": "Naproxen", "pubchem_cid": 1302, "category": "NSAID Drug"},
    "MOL-000004": {"name": "Diclofenac", "pubchem_cid": 3033, "category": "NSAID Drug"},
    "MOL-000005": {"name": "Celecoxib", "pubchem_cid": 2662, "category": "NSAID Drug"},
    "MOL-000006": {"name": "Indomethacin", "pubchem_cid": 3715, "category": "NSAID Drug"},

    # ================================================================
    # Antibiotics (抗生素)
    # ================================================================
    "MOL-000007": {"name": "Penicillin G", "pubchem_cid": 5904, "category": "Antibiotic"},
    "MOL-000008": {"name": "Amoxicillin", "pubchem_cid": 33613, "category": "Antibiotic"},
    "MOL-000009": {"name": "Ciprofloxacin", "pubchem_cid": 2764, "category": "Antibiotic"},
    "MOL-000010": {"name": "Doxycycline", "pubchem_cid": 54671203, "category": "Antibiotic"},
    "MOL-000011": {"name": "Azithromycin", "pubchem_cid": 447043, "category": "Antibiotic"},
    "MOL-000012": {"name": "Vancomycin", "pubchem_cid": 14969, "category": "Antibiotic"},
    "MOL-000013": {"name": "Gentamicin", "pubchem_cid": 3467, "category": "Antibiotic"},
    "MOL-000014": {"name": "Metronidazole", "pubchem_cid": 4173, "category": "Antibiotic"},

    # ================================================================
    # Antiviral Drugs (抗病毒药)
    # ================================================================
    "MOL-000015": {"name": "Ritonavir", "pubchem_cid": 3976, "category": "Antiviral Drug"},
    "MOL-000016": {"name": "Oseltamivir", "pubchem_cid": 65028, "category": "Antiviral Drug"},
    "MOL-000017": {"name": "Acyclovir", "pubchem_cid": 2022, "category": "Antiviral Drug"},
    "MOL-000018": {"name": "Remdesivir", "pubchem_cid": 121304016, "category": "Antiviral Drug"},
    "MOL-000019": {"name": "Zidovudine", "pubchem_cid": 35370, "category": "Antiviral Drug"},

    # ================================================================
    # Anticancer Drugs (抗癌药)
    # ================================================================
    "MOL-000020": {"name": "Tamoxifen", "pubchem_cid": 2733526, "category": "Anticancer Drug"},
    "MOL-000021": {"name": "Paclitaxel", "pubchem_cid": 36314, "category": "Anticancer Drug"},
    "MOL-000022": {"name": "Methotrexate", "pubchem_cid": 126941, "category": "Anticancer Drug"},
    "MOL-000023": {"name": "Doxorubicin", "pubchem_cid": 31703, "category": "Anticancer Drug"},
    "MOL-000024": {"name": "Cisplatin", "pubchem_cid": 5702198, "category": "Anticancer Drug"},
    "MOL-000025": {"name": "5-Fluorouracil", "pubchem_cid": 3385, "category": "Anticancer Drug"},
    "MOL-000026": {"name": "Imatinib", "pubchem_cid": 5291, "category": "Anticancer Drug"},
    "MOL-000027": {"name": "Cyclophosphamide", "pubchem_cid": 2907, "category": "Anticancer Drug"},

    # ================================================================
    # Targeted Therapy / Kinase Inhibitors (靶向治疗)
    # ================================================================
    "MOL-000028": {"name": "Gefitinib", "pubchem_cid": 123631, "category": "Targeted Therapy"},
    "MOL-000029": {"name": "Erlotinib", "pubchem_cid": 176870, "category": "Targeted Therapy"},
    "MOL-000030": {"name": "Sorafenib", "pubchem_cid": 216239, "category": "Targeted Therapy"},
    "MOL-000031": {"name": "Sunitinib", "pubchem_cid": 5329102, "category": "Targeted Therapy"},
    "MOL-000032": {"name": "Crizotinib", "pubchem_cid": 11626560, "category": "Targeted Therapy"},

    # ================================================================
    # Antidiabetic Drugs (抗糖尿病药)
    # ================================================================
    "MOL-000033": {"name": "Metformin", "pubchem_cid": 4091, "category": "Antidiabetic Drug"},
    "MOL-000034": {"name": "Glibenclamide", "pubchem_cid": 3488, "category": "Antidiabetic Drug"},
    "MOL-000035": {"name": "Sitagliptin", "pubchem_cid": 4369359, "category": "Antidiabetic Drug"},
    "MOL-000036": {"name": "Pioglitazone", "pubchem_cid": 4829, "category": "Antidiabetic Drug"},
    "MOL-000037": {"name": "Empagliflozin", "pubchem_cid": 11949646, "category": "Antidiabetic Drug"},

    # ================================================================
    # Antidepressants (抗抑郁药)
    # ================================================================
    "MOL-000038": {"name": "Fluoxetine", "pubchem_cid": 3386, "category": "Antidepressant"},
    "MOL-000039": {"name": "Sertraline", "pubchem_cid": 68617, "category": "Antidepressant"},
    "MOL-000040": {"name": "Paroxetine", "pubchem_cid": 43815, "category": "Antidepressant"},
    "MOL-000041": {"name": "Venlafaxine", "pubchem_cid": 5656, "category": "Antidepressant"},
    "MOL-000042": {"name": "Amitriptyline", "pubchem_cid": 2160, "category": "Antidepressant"},
    "MOL-000043": {"name": "Citalopram", "pubchem_cid": 2771, "category": "Antidepressant"},

    # ================================================================
    # Antihypertensives (降压药)
    # ================================================================
    "MOL-000044": {"name": "Lisinopril", "pubchem_cid": 5362119, "category": "Antihypertensive"},
    "MOL-000045": {"name": "Losartan", "pubchem_cid": 3961, "category": "Antihypertensive"},
    "MOL-000046": {"name": "Amlodipine", "pubchem_cid": 2162, "category": "Antihypertensive"},
    "MOL-000047": {"name": "Enalapril", "pubchem_cid": 5388962, "category": "Antihypertensive"},
    "MOL-000048": {"name": "Valsartan", "pubchem_cid": 60846, "category": "Antihypertensive"},
    "MOL-000049": {"name": "Metoprolol", "pubchem_cid": 4171, "category": "Antihypertensive"},

    # ================================================================
    # Statins (他汀类)
    # ================================================================
    "MOL-000050": {"name": "Atorvastatin", "pubchem_cid": 60823, "category": "Statin"},
    "MOL-000051": {"name": "Simvastatin", "pubchem_cid": 54454, "category": "Statin"},
    "MOL-000052": {"name": "Rosuvastatin", "pubchem_cid": 446157, "category": "Statin"},
    "MOL-000053": {"name": "Pravastatin", "pubchem_cid": 54687, "category": "Statin"},

    # ================================================================
    # Antihistamines (抗组胺药)
    # ================================================================
    "MOL-000054": {"name": "Cetirizine", "pubchem_cid": 2678, "category": "Antihistamine"},
    "MOL-000055": {"name": "Loratadine", "pubchem_cid": 3957, "category": "Antihistamine"},
    "MOL-000056": {"name": "Fexofenadine", "pubchem_cid": 3348, "category": "Antihistamine"},
    "MOL-000057": {"name": "Diphenhydramine", "pubchem_cid": 3100, "category": "Antihistamine"},

    # ================================================================
    # Opioid Analgesics (阿片类镇痛药)
    # ================================================================
    "MOL-000058": {"name": "Morphine", "pubchem_cid": 5288826, "category": "Opioid Analgesic"},
    "MOL-000059": {"name": "Codeine", "pubchem_cid": 5284371, "category": "Opioid Analgesic"},
    "MOL-000060": {"name": "Fentanyl", "pubchem_cid": 3345, "category": "Opioid Analgesic"},
    "MOL-000061": {"name": "Tramadol", "pubchem_cid": 33741, "category": "Opioid Analgesic"},

    # ================================================================
    # Bronchodilators (支气管扩张剂)
    # ================================================================
    "MOL-000062": {"name": "Salbutamol", "pubchem_cid": 2083, "category": "Bronchodilator"},
    "MOL-000063": {"name": "Salmeterol", "pubchem_cid": 5253, "category": "Bronchodilator"},
    "MOL-000064": {"name": "Montelukast", "pubchem_cid": 5281040, "category": "Bronchodilator"},

    # ================================================================
    # Anticoagulants (抗凝血药)
    # ================================================================
    "MOL-000065": {"name": "Warfarin", "pubchem_cid": 54678486, "category": "Anticoagulant"},
    "MOL-000066": {"name": "Heparin", "pubchem_cid": 772, "category": "Anticoagulant"},
    "MOL-000067": {"name": "Rivaroxaban", "pubchem_cid": 6433119, "category": "Anticoagulant"},

    # ================================================================
    # Immunosuppressants (免疫抑制剂)
    # ================================================================
    "MOL-000068": {"name": "Cyclosporine", "pubchem_cid": 5284373, "category": "Immunosuppressant"},
    "MOL-000069": {"name": "Tacrolimus", "pubchem_cid": 445643, "category": "Immunosuppressant"},
    "MOL-000070": {"name": "Mycophenolate mofetil", "pubchem_cid": 5281078, "category": "Immunosuppressant"},
    "MOL-000071": {"name": "Sirolimus", "pubchem_cid": 5284616, "category": "Immunosuppressant"},

    # ================================================================
    # Antifungal Drugs (抗真菌药)
    # ================================================================
    "MOL-000072": {"name": "Fluconazole", "pubchem_cid": 3365, "category": "Antifungal Drug"},
    "MOL-000073": {"name": "Amphotericin B", "pubchem_cid": 5280965, "category": "Antifungal Drug"},
    "MOL-000074": {"name": "Ketoconazole", "pubchem_cid": 47576, "category": "Antifungal Drug"},
    "MOL-000075": {"name": "Itraconazole", "pubchem_cid": 55183, "category": "Antifungal Drug"},

    # ================================================================
    # Antimalarial Drugs (抗疟药)
    # ================================================================
    "MOL-000076": {"name": "Chloroquine", "pubchem_cid": 2719, "category": "Antimalarial Drug"},
    "MOL-000077": {"name": "Artemisinin", "pubchem_cid": 68827, "category": "Antimalarial Drug"},
    "MOL-000078": {"name": "Quinine", "pubchem_cid": 3034034, "category": "Antimalarial Drug"},
    "MOL-000079": {"name": "Mefloquine", "pubchem_cid": 4069, "category": "Antimalarial Drug"},

    # ================================================================
    # Natural Products (天然产物)
    # ================================================================
    "MOL-000080": {"name": "Curcumin", "pubchem_cid": 969516, "category": "Natural Product"},
    "MOL-000081": {"name": "Resveratrol", "pubchem_cid": 445154, "category": "Natural Product"},
    "MOL-000082": {"name": "Quercetin", "pubchem_cid": 5280343, "category": "Natural Product"},
    "MOL-000083": {"name": "Epigallocatechin gallate", "pubchem_cid": 65064, "category": "Natural Product"},
    "MOL-000084": {"name": "Berberine", "pubchem_cid": 2353, "category": "Natural Product"},
    "MOL-000085": {"name": "Genistein", "pubchem_cid": 5280961, "category": "Natural Product"},

    # ================================================================
    # Neurotransmitters (神经递质)
    # ================================================================
    "MOL-000086": {"name": "Dopamine", "pubchem_cid": 681, "category": "Neurotransmitter"},
    "MOL-000087": {"name": "Serotonin", "pubchem_cid": 5202, "category": "Neurotransmitter"},
    "MOL-000088": {"name": "Norepinephrine", "pubchem_cid": 439260, "category": "Neurotransmitter"},
    "MOL-000089": {"name": "GABA", "pubchem_cid": 119, "category": "Neurotransmitter"},
    "MOL-000090": {"name": "Acetylcholine", "pubchem_cid": 187, "category": "Neurotransmitter"},
    "MOL-000091": {"name": "Glutamate", "pubchem_cid": 33032, "category": "Neurotransmitter"},
    "MOL-000092": {"name": "Histamine", "pubchem_cid": 774, "category": "Neurotransmitter"},

    # ================================================================
    # Hormones (激素)
    # ================================================================
    "MOL-000093": {"name": "Insulin (human)", "pubchem_cid": 16132438, "category": "Hormone"},
    "MOL-000094": {"name": "Cortisol", "pubchem_cid": 5754, "category": "Hormone"},
    "MOL-000095": {"name": "Testosterone", "pubchem_cid": 6013, "category": "Hormone"},
    "MOL-000096": {"name": "Estradiol", "pubchem_cid": 5757, "category": "Hormone"},
    "MOL-000097": {"name": "Thyroxine", "pubchem_cid": 5819, "category": "Hormone"},
    "MOL-000098": {"name": "Melatonin", "pubchem_cid": 896, "category": "Hormone"},
    "MOL-000099": {"name": "Progesterone", "pubchem_cid": 5994, "category": "Hormone"},

    # ================================================================
    # Vitamins (维生素)
    # ================================================================
    "MOL-000100": {"name": "Ascorbic acid", "pubchem_cid": 54670067, "category": "Vitamin"},
    "MOL-000101": {"name": "Retinol", "pubchem_cid": 445354, "category": "Vitamin"},
    "MOL-000102": {"name": "Tocopherol", "pubchem_cid": 14986, "category": "Vitamin"},
    "MOL-000103": {"name": "Thiamine", "pubchem_cid": 1130, "category": "Vitamin"},
    "MOL-000104": {"name": "Riboflavin", "pubchem_cid": 493570, "category": "Vitamin"},

    # ================================================================
    # Anesthetics (麻醉剂)
    # ================================================================
    "MOL-000105": {"name": "Lidocaine", "pubchem_cid": 3676, "category": "Anesthetic"},
    "MOL-000106": {"name": "Propofol", "pubchem_cid": 4943, "category": "Anesthetic"},
    "MOL-000107": {"name": "Ketamine", "pubchem_cid": 3821, "category": "Anesthetic"},
    "MOL-000108": {"name": "Isoflurane", "pubchem_cid": 3763, "category": "Anesthetic"},

    # ================================================================
    # Stimulants & CNS (中枢神经刺激剂)
    # ================================================================
    "MOL-000109": {"name": "Caffeine", "pubchem_cid": 2519, "category": "Stimulant"},
    "MOL-000110": {"name": "Methylphenidate", "pubchem_cid": 9280, "category": "Stimulant"},
    "MOL-000111": {"name": "Modafinil", "pubchem_cid": 4236, "category": "Stimulant"},

    # ================================================================
    # Anti-inflammatory (抗炎药，非 NSAID)
    # ================================================================
    "MOL-000112": {"name": "Prednisone", "pubchem_cid": 5865, "category": "Anti-inflammatory"},
    "MOL-000113": {"name": "Dexamethasone", "pubchem_cid": 5743, "category": "Anti-inflammatory"},
    "MOL-000114": {"name": "Mometasone Furoate", "pubchem_cid": 441336, "category": "Anti-inflammatory"},
    "MOL-000115": {"name": "Budesonide", "pubchem_cid": 5281004, "category": "Anti-inflammatory"},

    # ================================================================
    # Gastrointestinal Drugs (胃肠药)
    # ================================================================
    "MOL-000116": {"name": "Omeprazole", "pubchem_cid": 4594, "category": "Gastrointestinal Drug"},
    "MOL-000117": {"name": "Pantoprazole", "pubchem_cid": 4679, "category": "Gastrointestinal Drug"},
    "MOL-000118": {"name": "Ranitidine", "pubchem_cid": 3001055, "category": "Gastrointestinal Drug"},

    # ================================================================
    # Additional Important Molecules
    # ================================================================
    "MOL-000119": {"name": "Allopurinol", "pubchem_cid": 2094, "category": "Antigout Drug"},
    "MOL-000120": {"name": "Acetaminophen", "pubchem_cid": 1983, "category": "Analgesic"},
}
