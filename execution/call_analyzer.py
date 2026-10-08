#!/usr/bin/env python3
"""Frannie's deterministic call checks (see sops/frannie-sop.md).

Counts and pattern matches only. Frannie makes the judgment calls; this script
supplies the numbers and the verbatim lines so nothing is quoted from memory.

Transcript format, one turn per line:   [mm:ss] Speaker: text      (timestamp optional)
Speakers whose name starts with --us (default "Joaquin") are our side; all others are the prospect.

Usage:
  python execution/call_analyzer.py analyze  transcript.txt [--us Joaquin] > analysis.json
  python execution/call_analyzer.py verify   note.md transcript.txt        # every quote must exist verbatim
Exit 0 = ok, 1 = verify found a quote not in the transcript.
"""
import json
import re
import sys

sys.dont_write_bytecode = True

ENTRY_PRICE = 1500          # AI Audit, /config/business.md. Anything above is written-only.
TARGET_PROSPECT_SHARE = 0.60
DIAGNOSE_END_SEC = 12 * 60  # frame 2 + diagnose 10 (call structure, /config/business.md)
CALL_SEC = 20 * 60

LINE = re.compile(r"^\s*(?:\[(\d+):(\d{2})\]\s*)?([A-Za-z][\w .'-]*?):\s*(.+)$")

# Pitch = we describe what we would build/install or the offer itself.
PITCH = re.compile(r"\b(we (can|will|would|could) (build|install|set up|put in)|we build|we install|"
                   r"the audit|an audit|ai audit|the install|operations install|retainer|managed operations|"
                   r"our (system|agent|audit|install))\b|\$", re.I)
DISCOUNT = re.compile(r"\b(discount|knock (some|something)? ?off|% off|percent off|cheaper|special price|"
                      r"throw in|waive|match (their|that) price)\b", re.I)
ESCALATE = {
    "contract": re.compile(r"\b(contract|agreement|MSA|terms and conditions|indemnif|insurance certificate)\b", re.I),
    "municipal/procurement": re.compile(r"\b(procurement|resolution|RFP|bid threshold|council (has|must|needs|will)|"
                                        r"governing body|purchasing)\b", re.I),
    "discount_request": re.compile(r"\b(discount|better price|lower the price|can you do \$?[\d,]+k?\b|cheaper)\b", re.I),
}
OFF_PHASE = re.compile(r"\b(document intake|inspection|scheduling|resilience|dispatch|route planning)\b", re.I)
READY = re.compile(r"\b(where do i sign|what do i (need to )?sign|send (me )?(the|a) (contract|agreement|proposal|invoice)|"
                   r"let'?s do it|how do we (start|get started)|i'?m in\b|ready to (start|move|go|buy|sign)|"
                   r"when can (you|we) start)\b", re.I)
OBJ = {
    "O1": r"\b(too expensive|expensive|no budget|can'?t afford|budget is|price)\b",
    "O2": r"\b(not (right )?now|next quarter|next year|bad timing|budget cycle|after the (holidays|season|budget))\b",
    "O3": r"\b(don'?t trust|makes? mistakes|hallucinat|skeptic|not sure (ai|it) (works|is ready)|wrong answers?)\b",
    "O4": r"\b(privacy|security|confidential|sensitive data|data (is|stays)|where does the data)\b",
    "O5": r"\b(run it by|check with|need (to )?(approval|approve)|my (partner|board|boss)|council (has|must|needs)|sign[- ]?off)\b",
    "O6": r"\b(already have|we use [A-Z]|do it in[- ]house|our current (tool|system|vendor))\b",
    "O7": r"\b(my (staff|team|people) (will|would)|replace (my|our) (staff|people|team)|take (their|our) jobs?|lose (their|her|his) job)\b",
    "O8": r"\b(think (about|it over)|get back to you|sleep on it)\b",
    "O9": r"\b(procurement|RFP|legal (has|needs|will)|attorney|solicitor|formal contract)\b",
    "O10": r"\b(tried (automation|ai|a chatbot|something)|didn'?t work|burned (us|me)|bad experience)\b",
}
OBJ = {k: re.compile(v, re.I) for k, v in OBJ.items()}

WORD_NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
            "ten": 10, "twelve": 12, "fifteen": 15, "eighteen": 18, "twenty": 20, "twenty-five": 25,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty-five": 65}


def parse(path, us):
    turns = []
    for raw in open(path, encoding="utf-8"):
        m = LINE.match(raw)
        if not m:
            continue
        mm, ss, who, text = m.groups()
        sec = int(mm) * 60 + int(ss) if mm is not None else None
        turns.append({"sec": sec, "who": who.strip(), "ours": who.strip().lower().startswith(us.lower()),
                      "text": text.strip()})
    return turns


def stamp(t):
    return None if t["sec"] is None else f"{t['sec'] // 60:02d}:{t['sec'] % 60:02d}"


def amounts(text):
    """Dollar amounts in a line, spoken or written, as ints."""
    out = []
    for m in re.finditer(r"\$\s?([\d,]+(?:\.\d+)?)\s?(k|K|thousand)?", text):
        v = float(m.group(1).replace(",", ""))
        out.append(int(v * 1000) if m.group(2) else int(v))
    for m in re.finditer(r"\b([\w-]+) thousand( dollars)?", text, re.I):
        n = WORD_NUM.get(m.group(1).lower())
        if n:
            out.append(n * 1000)
    for m in re.finditer(r"\b([\d,]{4,}) dollars", text, re.I):
        out.append(int(m.group(1).replace(",", "")))
    return sorted(set(out))


def analyze(path, us):
    turns = parse(path, us)
    ours = sum(len(t["text"].split()) for t in turns if t["ours"])
    theirs = sum(len(t["text"].split()) for t in turns if not t["ours"])
    total = max(ours + theirs, 1)
    timed = [t for t in turns if t["sec"] is not None]
    res = {
        "turns": len(turns),
        "duration": stamp(timed[-1]) if timed else None,
        "talk_ratio": {"prospect_pct": round(100 * theirs / total, 1), "ours_pct": round(100 * ours / total, 1),
                       "basis": "word count (proxy for talk time)",
                       "meets_target": theirs / total >= TARGET_PROSPECT_SHARE},
    }

    # First pitch, and whether it came before the diagnose window closed.
    first = next((i for i, t in enumerate(turns) if t["ours"] and PITCH.search(t["text"])), None)
    if first is None:
        res["pitch"] = {"first_pitch": None, "too_early": False}
    else:
        t = turns[first]
        words_before = sum(len(x["text"].split()) for x in turns[:first])
        frac = words_before / total
        if t["sec"] is not None:
            early = t["sec"] < DIAGNOSE_END_SEC
            basis = f"timestamp {stamp(t)} vs diagnose end 12:00"
        else:
            early = frac < DIAGNOSE_END_SEC / CALL_SEC
            basis = f"{round(100 * frac)}% of words vs 60% diagnose end"
        res["pitch"] = {"first_pitch": {"at": stamp(t), "line": t["text"]}, "too_early": early, "basis": basis,
                        "note": "heuristic; Frannie confirms against the full transcript"}

    # Prices we said aloud.
    priced = []
    for t in turns:
        if t["ours"]:
            for a in amounts(t["text"]):
                priced.append({"at": stamp(t), "amount": a, "above_entry_offer": a > ENTRY_PRICE, "line": t["text"]})
    res["our_price_mentions"] = priced
    res["price_violation"] = any(p["above_entry_offer"] for p in priced)
    res["prospect_price_mentions"] = [{"at": stamp(t), "amounts": amounts(t["text"]), "line": t["text"]}
                                      for t in turns if not t["ours"] and amounts(t["text"])]
    res["our_discount_language"] = [{"at": stamp(t), "line": t["text"]} for t in turns
                                    if t["ours"] and DISCOUNT.search(t["text"])]

    # Objection candidates (prospect lines), verbatim.
    objs = []
    for t in turns:
        if t["ours"]:
            continue
        for oid, rx in OBJ.items():
            if rx.search(t["text"]):
                objs.append({"id": oid, "at": stamp(t), "line": t["text"]})
    res["objection_candidates"] = objs

    esc = []
    for t in turns:
        if t["ours"]:
            continue
        for name, rx in ESCALATE.items():
            if rx.search(t["text"]):
                esc.append({"trigger": name, "at": stamp(t), "line": t["text"]})
    res["escalation_candidates"] = esc
    res["off_phase_mentions"] = [{"who": t["who"], "at": stamp(t), "line": t["text"]}
                                 for t in turns if OFF_PHASE.search(t["text"])]
    res["ready_to_buy_cues"] = [{"at": stamp(t), "line": t["text"]} for t in turns
                                if not t["ours"] and READY.search(t["text"])]
    return res


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s$%]", "", s.lower())).strip()


def verify(note_path, transcript_path):
    transcript = norm(" ".join(t["text"] for t in parse(transcript_path, "\0")))
    note = open(note_path, encoding="utf-8").read()
    quotes = re.findall(r"[\"“]([^\"”\n]{12,}?)[\"”]", note)
    bad = [q for q in quotes if norm(q) not in transcript]
    print(f"quotes checked: {len(quotes)}; not found verbatim: {len(bad)}")
    for q in bad:
        print(f"  NOT IN TRANSCRIPT: {q}")
    return 1 if bad else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "analyze":
        us = a[a.index("--us") + 1] if "--us" in a else "Joaquin"
        print(json.dumps(analyze(a[1], us), indent=2))
    elif len(a) == 3 and a[0] == "verify":
        sys.exit(verify(a[1], a[2]))
    else:
        print(__doc__)
        sys.exit(2)
