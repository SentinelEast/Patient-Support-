#!/usr/bin/env python3
"""Brand scrub: fail if any retired brand string appears anywhere in the repo.

The retired names are assembled from fragments so this file itself never
contains them (otherwise the scrub would flag its own source).

Usage:  python execution/brand_scrub.py [root]
Exit 0 = zero hits. Exit 1 = hits found (printed as path:line:text).
"""
import os
import re
import sys

# Fragments joined at runtime; do not write the full strings in this file.
PATTERNS = [
    re.compile("sent" + "inel", re.I),                # covers the full name and the short form
    re.compile(r"\bS\.E\.T\b", re.I),                 # initials
    re.compile("guard" + "ian" + r"[-\s]?" + "484", re.I),
]
SKIP_DIRS = {".git", ".tmp", "node_modules"}


def scan(root: str) -> list[str]:
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = os.path.join(dirpath, name)
            # File names count too.
            if any(p.search(name) for p in PATTERNS):
                hits.append(f"{path}: (file name)")
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    for n, line in enumerate(fh, 1):
                        if any(p.search(line) for p in PATTERNS):
                            hits.append(f"{path}:{n}:{line.strip()[:120]}")
            except OSError:
                continue
    return hits


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    found = scan(root)
    if found:
        print(f"BRAND SCRUB FAILED: {len(found)} hit(s)")
        print("\n".join(found))
        sys.exit(1)
    print("BRAND SCRUB PASSED: 0 hits")
