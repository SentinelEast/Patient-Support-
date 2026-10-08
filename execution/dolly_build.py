#!/usr/bin/env python3
"""Dolly's asset builder: spec JSON in, primary + alternate SVG out (editable source).

SVG opens in Figma, Canva, Illustrator and any browser, so the SVG itself is the editable source.
Brand settings come from config/brand.md (PLACEHOLDER values are flagged in the output),
the footer from config/footer.md. Nothing is retyped here.

Spec JSON:
{ "format": "proposal_cover|process_diagram|one_pager|social_graphic",
  "title": "...", "subtitle": "...", "date": "YYYY-MM-DD",
  "client_name": "..." (optional), "client_name_approved": false,
  "steps": ["..."]            # process_diagram: workflow steps, in scope only
  "bullets": ["..."]          # one_pager / social_graphic body lines (copy supplied by Cody/Mark)
}
Usage: python execution/dolly_build.py spec.json out_dir     -> out_dir/<format>-primary.svg, -alternate.svg, build-report.json
"""
import json
import os
import re
import sys
from xml.sax.saxutils import escape

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMATS = {"proposal_cover": (1200, 1600), "process_diagram": (1600, 900), "one_pager": (1275, 1650),
           "social_graphic": (1080, 1080)}


def brand():
    text = open(os.path.join(ROOT, "config", "brand.md"), encoding="utf-8").read()
    def val(name):
        m = re.search(rf"^\| {name} \| (.+?) \| (.+?) \|$", text, re.M)
        return (m.group(1).strip(), "PLACEHOLDER" in m.group(2)) if m else (None, True)
    out = {k: val(k) for k in ("Primary color", "Accent color", "Heading font", "Body font")}
    return {k: v[0].split()[0].rstrip(",") if k.endswith("color") else v[0] for k, v in out.items()}, \
           [k for k, v in out.items() if v[1]]


def footer():
    text = open(os.path.join(ROOT, "config", "footer.md"), encoding="utf-8").read()
    return re.findall(r"```\n(.*?)\n```", text, re.S)[0].strip()


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    return lines + ([cur] if cur else [])


def text(x, y, s, size, fill, font, weight="normal", anchor="start", wrap_at=None, lead=1.3):
    lines = wrap(s, wrap_at) if wrap_at else [s]
    tspans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else int(size * lead)}">{escape(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{tspans}</text>'


def build(spec, variant, b):
    fmt = spec["format"]
    w, h = FORMATS[fmt]
    dark = variant == "alternate"
    bg, fg = ("#FFFFFF", "#1A1A1A") if not dark else (b["Primary color"], "#FFFFFF")
    band = b["Primary color"] if not dark else b["Accent color"]
    bandfg = "#FFFFFF" if not dark else "#1A1A1A"
    hf, bf = b["Heading font"], b["Body font"]
    el = [f'<rect width="{w}" height="{h}" fill="{bg}"/>', f'<rect width="{w}" height="{int(h * 0.04)}" fill="{band}"/>']
    # Wordmark: text only, never a logo.
    el.append(text(60, 110, "The AI Agency Blueprint", 34, fg, hf, "bold"))
    client = spec.get("client_name")
    if client and not spec.get("client_name_approved"):
        client_line = "Prepared for: [client name pending Joaquin approval]"
    elif client:
        client_line = f"Prepared for: {client}"
    else:
        client_line = None
    if fmt == "proposal_cover":
        el.append(text(60, 520, spec["title"], 76, fg, hf, "bold", wrap_at=22, lead=1.15))
        el.append(text(60, 800, spec.get("subtitle", ""), 34, fg, bf, wrap_at=44))
        if client_line:
            el.append(text(60, 1000, client_line, 30, fg, bf))
        el.append(text(60, 1060, spec.get("date", ""), 28, fg, bf))
        el.append(f'<rect x="60" y="1150" width="220" height="8" fill="{band}"/>')
    elif fmt == "process_diagram":
        el.append(text(60, 200, spec["title"], 52, fg, hf, "bold"))
        steps = spec["steps"]
        n = len(steps)
        bw = (w - 120 - (n - 1) * 40) // n
        for i, s in enumerate(steps):
            x = 60 + i * (bw + 40)
            el.append(f'<rect x="{x}" y="320" width="{bw}" height="300" rx="14" fill="{band}"/>')
            el.append(text(x + 24, 380, f"{i + 1}", 44, bandfg, hf, "bold"))
            el.append(text(x + 24, 450, s, 26, bandfg, bf, wrap_at=max(10, bw // 15)))
            if i < n - 1:
                el.append(f'<polygon points="{x + bw + 6},470 {x + bw + 34},470 {x + bw + 20},490" fill="{fg}" transform="rotate(-90 {x + bw + 20} 480)"/>')
        el.append(text(60, 720, spec.get("subtitle", ""), 26, fg, bf, wrap_at=100))
    elif fmt == "one_pager":
        el.append(text(60, 240, spec["title"], 56, fg, hf, "bold", wrap_at=34, lead=1.15))
        y = 460
        for bl in spec.get("bullets", []):
            el.append(f'<circle cx="75" cy="{y - 9}" r="7" fill="{band}"/>')
            lines = len(wrap(bl, 62))
            el.append(text(100, y, bl, 28, fg, bf, wrap_at=62))
            y += 50 + (lines - 1) * 36
        if client_line:
            el.append(text(60, y + 40, client_line, 26, fg, bf))
    elif fmt == "social_graphic":
        el.append(text(60, 400, spec["title"], 72, fg, hf, "bold", wrap_at=24, lead=1.15))
        y = 760
        for bl in spec.get("bullets", [])[:3]:
            el.append(text(60, y, bl, 32, fg, bf, wrap_at=48))
            y += 90
    fy = h - 60
    el.append(f'<rect x="0" y="{fy - 50}" width="{w}" height="110" fill="{band}"/>')
    el.append(text(w // 2, fy + 8, footer(), 20 if w < 1300 else 22, bandfg, bf, anchor="middle"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            + "".join(el) + "</svg>")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    spec = json.load(open(sys.argv[1]))
    if spec["format"] not in FORMATS:
        sys.exit(f"Format '{spec['format']}' not supported by the builder (deck: build in Canva/Figma once authorized).")
    b, placeholder = brand()
    os.makedirs(sys.argv[2], exist_ok=True)
    files = []
    for v in ("primary", "alternate"):
        p = os.path.join(sys.argv[2], f"{spec['format']}-{v}.svg")
        open(p, "w", encoding="utf-8").write(build(spec, v, b))
        files.append(p)
    rep = {"files": files, "placeholder_brand_settings": placeholder, "footer_source": "config/footer.md",
           "client_name_used": bool(spec.get("client_name_approved"))}
    json.dump(rep, open(os.path.join(sys.argv[2], f"{spec['format']}-build-report.json"), "w"), indent=2)
    print(json.dumps(rep, indent=2))
