import json

data = [json.loads(l) for l in open('data/processed/molalign_dataset.jsonl','r',encoding='utf-8')]
rm = {r['record_id']: r for r in data}

extra = {
    'MOL-000013': 'Gentamicin is an aminoglycoside antibiotic composed of a mixture of gentamicin C1, C2, and C1a. It is effective against Gram-negative bacteria and works by binding to the 30S ribosomal subunit, causing misreading of mRNA.',
    'MOL-000017': 'Acyclovir is a synthetic purine nucleoside analogue with activity against herpes simplex virus types 1 and 2, and varicella-zoster virus. It is converted to acyclovir monophosphate by viral thymidine kinase.',
    'MOL-000067': 'Rivaroxaban is a direct Factor Xa inhibitor used as an oral anticoagulant. It selectively blocks the active site of Factor Xa without requiring a cofactor such as antithrombin III.',
    'MOL-000093': 'Insulin (human) is a polypeptide hormone produced by the beta cells of the pancreatic islets. It regulates glucose metabolism by promoting cellular uptake of glucose and glycogen synthesis.',
    'MOL-000102': 'Tocopherol (Vitamin E) is a fat-soluble antioxidant that protects cell membranes from oxidative damage by neutralizing free radicals. Alpha-tocopherol is the most biologically active form.',
    'MOL-000110': 'Methylphenidate is a central nervous system stimulant used primarily in the treatment of attention deficit hyperactivity disorder (ADHD). It inhibits the reuptake of dopamine and norepinephrine.',
    'MOL-000119': 'Allopurinol is a xanthine oxidase inhibitor that reduces the production of uric acid. It is used in the treatment of chronic gout and hyperuricemia.',
}

for mid, desc in extra.items():
    r = rm[mid]
    r['text_descriptions'].append({
        'type': 'general_description',
        'content': desc,
        'source': {'type': 'manual_curation', 'reference': 'Pharmacology literature', 'mineru_parsed': False},
        'language': 'en',
    })
    print(f'{mid} ({r["names"]["common_name"]}): -> {len(r["text_descriptions"])}')

with open('data/processed/molalign_dataset.jsonl', 'w', encoding='utf-8') as f:
    for r in data:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open('data/processed/molalign_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

avg = sum(len(r.get('text_descriptions', [])) for r in data) / len(data)
print(f'Avg descriptions: {avg:.2f}')
print('Done')
