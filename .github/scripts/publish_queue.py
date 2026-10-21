#!/usr/bin/env python3
"""Publish queued blog posts whose date has arrived.

Queued posts live in _queue/YYYY-MM-DD/. Because the folder name starts with
an underscore, GitHub Pages (Jekyll) never serves it, so nothing in it is on
the website until this script copies it into place.

Each dated folder holds only the files that change that day. Files are merged
into the live site with a three-way merge, so edits made on the live site
since the post was queued are kept. If an edit collides with the queued
change, nothing is published and the workflow run fails, so a person can look.

_queue/published.txt lists every date already published.
"""
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
QUEUE = ROOT / "_queue"
BASE = QUEUE / "_base"
LOG = QUEUE / "published.txt"
TZ = ZoneInfo("America/Chicago")
GO_LIVE_HOUR = 6  # posts go live on or after 6 AM Central

now = datetime.now(TZ)
today = os.environ.get("PUBLISH_TODAY") or now.date().isoformat()
manual = os.environ.get("FORCE_RUN") == "true"

def output(name, value):
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a") as fh:
            fh.write(f"{name}={value}\n")
    print(f"{name}={value}")

if not manual and not os.environ.get("PUBLISH_TODAY") and now.hour < GO_LIVE_HOUR:
    print(f"It's {now:%H:%M} Central, before {GO_LIVE_HOUR} AM. Nothing to do yet.")
    output("count", 0)
    output("html_count", 0)
    sys.exit(0)

published = set()
if LOG.exists():
    published = {l.strip() for l in LOG.read_text().splitlines() if l.strip()}

dates = sorted(p.name for p in QUEUE.iterdir()
               if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name))
due = [d for d in dates if d <= today and d not in published]
print(f"Today (Central): {today}. Due: {', '.join(due) or 'none'}")

def find_base(rel, date):
    for earlier in reversed([d for d in dates if d < date]):
        cand = QUEUE / earlier / rel
        if cand.exists():
            return cand
    cand = BASE / rel
    return cand if cand.exists() else None

changed = []
conflicts = []
for date in due:
    folder = QUEUE / date
    for new in sorted(p for p in folder.rglob("*") if p.is_file()):
        rel = new.relative_to(folder)
        live = ROOT / rel
        before = live.read_bytes() if live.exists() else None
        base = find_base(rel, date)
        if before is None:
            live.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(new, live)
        elif base is None:
            if before != new.read_bytes():
                conflicts.append(f"{date}: {rel} already exists on the site with different content")
                continue
        else:
            res = subprocess.run(["git", "merge-file", "-p", "-L", "live site", "-L", "queued from",
                                  "-L", f"queued {date}", str(live), str(base), str(new)],
                                 capture_output=True)
            if res.returncode != 0:
                conflicts.append(f"{date}: {rel} was edited on the site in a way that collides with the queued change")
                continue
            live.write_bytes(res.stdout)
        if live.read_bytes() != before and str(rel) not in changed:
            changed.append(str(rel))
    published.add(date)

if conflicts:
    print("::error::Nothing was published. Fix these, then run the workflow again:")
    for c in conflicts:
        print(f"::error::{c}")
    sys.exit(1)

if due:
    LOG.write_text("\n".join(sorted(published)) + "\n")

html = [c.replace(os.sep, "/") for c in changed if c.endswith(".html")]
output("count", len(due))
output("dates", " ".join(due))
output("html_count", len(html))
output("html", " ".join(html))
for c in changed:
    print(f"updated: {c}")
