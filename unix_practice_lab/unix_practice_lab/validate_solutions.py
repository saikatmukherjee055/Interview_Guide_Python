#!/usr/bin/env python3
"""Run every solution command from exercise_index.json and report failures."""
from pathlib import Path
import json
import subprocess
import sys
import shutil

root = Path(__file__).resolve().parent
index = json.loads((root / 'exercise_index.json').read_text(encoding='utf-8'))

# Restore metadata/permissions before validation.
reset = subprocess.run(['bash', str(root / 'reset_metadata.sh')], cwd=root)
if reset.returncode != 0:
    sys.exit(reset.returncode)

workspace = root / 'workspace'
workspace.mkdir(exist_ok=True)
for path in workspace.iterdir():
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()

failures = []
for item in index:
    result = subprocess.run(
        ['bash', '-lc', item['cmd']],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        failures.append((item['n'], item['title'], result.returncode, result.stderr.strip()))

if failures:
    print(f'{len(failures)} command(s) failed:')
    for number, title, code, error in failures:
        print(f'  {number}. {title} — exit {code}: {error}')
    sys.exit(1)

print(f'PASS: all {len(index)} solution commands executed successfully.')
