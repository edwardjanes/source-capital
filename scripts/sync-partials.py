#!/usr/bin/env python3
"""
Sync shared nav/footer/analytics markup into every built page.

How it works: each page contains <!-- NAV_START --> ... <!-- NAV_END -->,
<!-- FOOTER_START --> ... <!-- FOOTER_END -->, and
<!-- ANALYTICS_START --> ... <!-- ANALYTICS_END --> marker comments. This
script replaces everything between each pair of markers with the current
content of _partials/nav.html / _partials/footer.html / _partials/analytics.html,
so there is exactly one place to edit each, and every page picks it up on the
next run. Pages are plain static HTML (no build step, no Jekyll), so this
runs by hand whenever a partial changes or a new page is added.

Usage: python3 scripts/sync-partials.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "_partials"
SKIP_DIRS = {"legacy", "_partials", "scripts", ".git", "core-story"}

def read(path):
    return path.read_text(encoding="utf-8")

def sync_block(content, partial_content, start_marker, end_marker):
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    if not pattern.search(content):
        return content, False
    replacement = partial_content.strip()
    new_content = pattern.sub(replacement, content, count=1)
    return new_content, True

def main():
    nav_partial = read(PARTIALS / "nav.html")
    footer_partial = read(PARTIALS / "footer.html")
    analytics_partial = read(PARTIALS / "analytics.html")

    changed_files = []
    for html_file in ROOT.rglob("*.html"):
        rel = html_file.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        original = read(html_file)
        content = original
        content, nav_hit = sync_block(content, nav_partial, "<!-- NAV_START -->", "<!-- NAV_END -->")
        content, footer_hit = sync_block(content, footer_partial, "<!-- FOOTER_START -->", "<!-- FOOTER_END -->")
        content, analytics_hit = sync_block(content, analytics_partial, "<!-- ANALYTICS_START -->", "<!-- ANALYTICS_END -->")
        if content != original:
            html_file.write_text(content, encoding="utf-8")
            changed_files.append(str(rel))

    if changed_files:
        print("Synced partials into:")
        for f in changed_files:
            print(f"  - {f}")
    else:
        print("No files needed syncing (no marker matches found, or all already up to date).")

if __name__ == "__main__":
    main()
