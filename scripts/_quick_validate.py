"""Quick inline validation for molalign_dataset.json"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ds_path = os.path.join(BASE, 'data', 'processed', 'molalign_dataset.json')
ds = json.load(open(ds_path, 'r', encoding='utf-8'))

total = len(ds)
print(f"Total records: {total}")

# Required fields
required = ['record_id', 'molecule_id', 'smiles', 'names', 'modalities', 'properties', 'text_descriptions', 'entity_relations']
missing = []
for i, r in enumerate(ds):
    for f in required:
        if f not in r:
            missing.append((i, f))
if missing:
    print(f"MISSING FIELDS: {missing[:10]}")
else:
    print("[OK] All required fields present")

# Modalities
has_2d = sum(1 for r in ds if r.get('modalities', {}).get('structure_2d'))
has_3d = sum(1 for r in ds if r.get('modalities', {}).get('structure_3d'))
has_paper = sum(1 for r in ds if r.get('modalities', {}).get('structure_paper'))
print(f"[OK] structure_2d: {has_2d}")
print(f"[OK] structure_3d: {has_3d}")
print(f"[OK] structure_paper: {has_paper}")

# SMILES
empty_smiles = sum(1 for r in ds if not r.get('smiles'))
print(f"[{'OK' if empty_smiles == 0 else 'FAIL'}] Empty SMILES: {empty_smiles}")

# Duplicate IDs
ids = [r['record_id'] for r in ds]
dup = len(ids) - len(set(ids))
print(f"[{'OK' if dup == 0 else 'FAIL'}] Duplicate record_ids: {dup}")

# File existence
proc = os.path.join(BASE, 'data', 'processed')
missing_2d = 0
missing_3d = 0
for r in ds:
    m = r.get('modalities', {})
    s2d = m.get('structure_2d')
    if s2d and s2d.get('rdkit_generated'):
        p = os.path.join(proc, s2d['rdkit_generated'])
        if not os.path.exists(p):
            missing_2d += 1
    s3d = m.get('structure_3d')
    if s3d and s3d.get('sdf_path'):
        p = os.path.join(proc, s3d['sdf_path'])
        if not os.path.exists(p):
            missing_3d += 1
print(f"[{'OK' if missing_2d == 0 else 'FAIL'}] Missing 2D images: {missing_2d}")
print(f"[{'OK' if missing_3d == 0 else 'FAIL'}] Missing 3D SDFs: {missing_3d}")

# File counts on disk
png_dir = os.path.join(proc, 'images', '2d')
sdf_dir = os.path.join(proc, 'models', '3d')
pngs = len([f for f in os.listdir(png_dir) if f.endswith('.png')]) if os.path.isdir(png_dir) else 0
sdfs = len([f for f in os.listdir(sdf_dir) if f.endswith('.sdf')]) if os.path.isdir(sdf_dir) else 0
print(f"[INFO] 2D PNG files on disk: {pngs}")
print(f"[INFO] 3D SDF files on disk: {sdfs}")

ok = (not missing and dup == 0 and empty_smiles == 0
      and missing_2d == 0 and missing_3d == 0)
print(f"\n{'=== VALIDATION PASSED ===' if ok else '=== VALIDATION FAILED ==='}")
sys.exit(0 if ok else 1)
