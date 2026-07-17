#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
chmod 755 permissions/scripts/run.sh permissions/scripts/report.py projects/beta/src/*.sh projects/alpha/src/main.py
chmod 600 permissions/private/passwords.txt
chmod 640 permissions/private/notes.txt
chmod 666 temp/public.tmp 2>/dev/null || true
ln -sfn missing-target mixed/broken_link
ln -sfn app.log data/current_app.log
ln -sfn alpha projects/latest
touch -d '2023-11-07 12:00:00' projects/archive/old_report.txt
touch -d '2024-05-25 12:00:00' projects/archive/legacy.py
touch -d '2025-12-06 12:00:00' logs/2025/december/old.log
touch -d '2026-01-10 12:00:00' logs/2026/january/server1.log
touch -d '2026-01-11 12:00:00' logs/2026/january/server2.log
touch -d '2025-12-26 12:00:00' temp/cache/cache_1.tmp
touch -d '2026-01-05 12:00:00' temp/cache/cache_2.tmp
touch -d '2026-01-12 12:00:00' temp/cache/cache_3.tmp
printf 'Metadata and permissions restored.
'
