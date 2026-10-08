#!/usr/bin/env python3
"""Dolly's pre-handoff check on an SVG/HTML asset (sops/dolly-sop.md step 4).

Fails on: retired brand names, footer text not matching config/footer.md, result/testimonial claims,
percentages, dollar amounts above the entry offer, off-phase service names, and unapproved client names.

Usage: python execution/asset_check.py asset.svg [--client "Name"]...    (each --client = a name that is NOT approved; must be absent)
Exit 0 = PASS, 1 = FAIL.
"""
import re
import sys
from xml.sax.saxutils import escape

sys.dont_write_bytecode = True
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))
from brand_scrub import PATTERNS  # noqa: E402

CLAIMS = re.compile(r"testimonial|trusted by|case stud|guarantee|clients like|our clients|proven|award|rated|\d\s?%|\bfive[- ]star\b", re.I)
OFF_PHASE = re.compile(r"document intake|inspection|scheduling|resilience", re.I)


def check(path, banned_clients):
    raw = open(path, encoding="utf-8").read()
    visible = " ".join(re.findall(r">([^<>]+)<", raw))
    fails = []
    for p in PATTERNS:
        if p.search(raw):
            fails.append("retired brand string present")
    footer = re.findall(r"```\n(.*?)\n```", open(os.path.join(ROOT, "config", "footer.md"), encoding="utf-8").read(), re.S)[0].strip()
    if escape(footer) not in raw:
        fails.append("footer does not match config/footer.md")
    m = CLAIMS.search(visible)
    if m:
        fails.append(f"unsupported claim language: '{m.group(0)}'")
    m = OFF_PHASE.search(visible)
    if m:
        fails.append(f"off-phase service named: '{m.group(0)}'")
    for amt in re.findall(r"\$\s?([\d,]+)", visible):
        if int(amt.replace(",", "")) > 1500:
            fails.append(f"price above entry offer on an asset: ${amt}")
    for c in banned_clients:
        if c.lower() in visible.lower():
            fails.append(f"unapproved client name present: {c}")
    return fails


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    clients = [a[i + 1] for i, x in enumerate(a) if x == "--client"]
    f = check(a[0], clients)
    print("PASS" if not f else "FAIL")
    for x in f:
        print("  -", x)
    sys.exit(1 if f else 0)
