#!/usr/bin/env python3
"""Assemble and validate a Cody outreach sequence.

Cody writes a draft JSON (copy only). This script appends the footer and
unsubscribe line read from config/footer.md (never retyped), then runs the
hard-rule checks from sops/cody-sop.md. Output JSON is the handoff to Patty.

Usage:  python execution/assemble_sequence.py draft.json out.json
Exit 0 = PASS, 1 = FAIL (failures listed in out.json under "checks" and printed).

Draft schema:
  prospect_id, first_name, last_name, title, org, city, niche ("A"|"B"),
  trigger_line, trigger_source,
  emails: [{day, subject, greeting, body}] x3,
  linkedin_note, sources_assumptions: [str]
"""
import json
import os
import re
import sys

sys.dont_write_bytecode = True  # keep compiled files (which embed the scrub patterns) out of the repo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))
from brand_scrub import PATTERNS  # noqa: E402  (retired-name patterns live only there)

SENDER = "chiefofstaff@theaiagencyblueprint.com"
WORD_RANGES = {0: (60, 80), 4: (40, 60), 9: (30, 40)}
LINKEDIN_MAX = 300

# Phase 1 sells only the Constituent/Customer Response Agent and the AI Audit.
OFF_PHASE = ["document intake", "inspection", "scheduling", "resilience"]
# We have no client case studies; no result claims.
BANNED_CLAIMS = ["case study", "case studies", "guarantee", "our clients",
                 "clients like", "we helped", "proven", "%"]


FIRST_PERSON = re.compile(r"\b(I|I'll|I'd|I'm|I've|my|me)\b")


def booking_link() -> str:
    """Read the verified booking URL from the BOOKING_LINK line in config/business.md."""
    text = open(os.path.join(ROOT, "config", "business.md"), encoding="utf-8").read()
    m = re.search(r"^- BOOKING_LINK: (\S+)", text, re.M)
    if not m:
        raise SystemExit("BOOKING_LINK not found in config/business.md")
    return m.group(1)


def footer_blocks() -> tuple[str, str, str]:
    """Return (footer, unsubscribe, signature) from the first three fenced blocks in footer.md."""
    text = open(os.path.join(ROOT, "config", "footer.md"), encoding="utf-8").read()
    blocks = re.findall(r"```\n(.*?)\n```", text, re.S)
    return blocks[0].strip(), blocks[1].strip(), blocks[2].strip()


def words(s: str) -> int:
    return len(s.split())


def validate(d: dict, footer: str, unsub: str) -> list[str]:
    fails = []
    emails = d.get("emails", [])
    if [e.get("day") for e in emails] != [0, 4, 9]:
        fails.append("emails must be exactly 3, on days 0, 4, 9")
        return fails
    for e in emails:
        lo, hi = WORD_RANGES[e["day"]]
        n = words(e["body"])
        if not lo <= n <= hi:
            fails.append(f"day {e['day']} body is {n} words (needs {lo}-{hi})")
        low = e["body"].lower() + " " + e["subject"].lower()
        for p in OFF_PHASE:
            if p in low:
                fails.append(f"day {e['day']} off-phase term: {p}")
        for p in BANNED_CLAIMS:
            if p in low:
                fails.append(f"day {e['day']} banned claim: {p}")
        if FIRST_PERSON.search(e["body"]):
            fails.append(f"day {e['day']} uses first-person singular (Chief of Staff voice is \"we\")")
        for pat in PATTERNS:
            if pat.search(e["body"] + e["subject"] + e["greeting"]):
                fails.append(f"day {e['day']} retired brand string")
        if d["first_name"] not in e["greeting"]:
            fails.append(f"day {e['day']} greeting does not use first name from record")
    e1, e3 = emails[0], emails[2]
    low1 = e1["body"].lower()
    if "audit" in low1 or "$" in e1["body"] or "price" in low1:
        fails.append("email 1 mentions audit/price (free call is the hook)")
    if "20-minute" not in e1["body"] or "Loom" not in e1["body"]:
        fails.append("email 1 must offer the free 20-minute call and the 2-minute Loom")
    if d["org"] not in e1["body"] and d["city"] not in e1["body"]:
        fails.append("email 1 must name the org or city from the record")
    if "{{booking_link}}" not in e3["body"]:
        fails.append("email 3 must include {{booking_link}}")
    note = d.get("linkedin_note", "")
    if not note or len(note) >= LINKEDIN_MAX:
        fails.append(f"linkedin note must be 1-{LINKEDIN_MAX - 1} chars (got {len(note)})")
    if any(p.search(note) for p in PATTERNS):
        fails.append("linkedin note has retired brand string")
    if not d.get("trigger_source"):
        fails.append("trigger_source missing (no source, no trigger line)")
    if not d.get("sources_assumptions"):
        fails.append("sources_assumptions missing")
    return fails


def main(src: str, dst: str) -> int:
    d = json.load(open(src, encoding="utf-8"))
    footer, unsub, signature = footer_blocks()
    link = booking_link()
    fails = validate(d, footer, unsub)
    for e in d["emails"]:
        e["word_count"] = words(e["body"])
        e["full_text"] = (f"{e['greeting']}\n\n{e['body']}\n\n{signature}\n\n"
                          f"{footer}\n{unsub}").replace("{{booking_link}}", link)
    d["sender"] = SENDER
    d["footer_ref"] = "config/footer.md"
    d["checks"] = {"status": "FAIL" if fails else "PASS", "failures": fails}
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False)
    print(f"{d['prospect_id']}: {d['checks']['status']}", *fails, sep="\n  ")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
