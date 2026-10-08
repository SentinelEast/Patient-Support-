#!/usr/bin/env python3
"""Mark's ROI math (see sops/mark-sop.md). Pure arithmetic; every input is echoed with its source.

Input JSON:
{
 "hours_per_week": 15 | null,            "hours_source": "transcript 03:10",
 "hourly_cost": 28 | null,               "cost_source": "transcript 03:40",
 "loaded_multiplier": 1.0,               # PENDING in config/sales.md; 1.0 = wage only
 "replaced_share": [0.5, 0.7],           # positioning range, /config/business.md
 "options": [ {"name": "...", "one_time": 1500, "monthly": 0, "delivery": "7 business days", "price_source": "business.md"} ]
}
Usage: python execution/roi_calc.py inputs.json > roi.json     (and prints a markdown table to stderr)
Missing hours or cost => status INPUT NEEDED, no numbers (never guessed).
"""
import json
import sys

sys.dont_write_bytecode = True
WEEKS = 52


def calc(d):
    h, c = d.get("hours_per_week"), d.get("hourly_cost")
    if h is None or c is None:
        return {"status": "INPUT NEEDED", "missing": [k for k, v in (("hours_per_week", h), ("hourly_cost", c)) if v is None],
                "inputs": d, "rows": []}
    mult = d.get("loaded_multiplier", 1.0)
    rows = []
    for share in d["replaced_share"]:
        annual = h * share * c * mult * WEEKS
        monthly = annual / 12
        for o in d["options"]:
            if o["name"] == "AI Audit":  # diagnostic: replaces no hours, so no savings are claimed
                rows.append({"option": o["name"], "replaced_share": share, "hours_replaced_per_week": None,
                             "annual_savings": None, "monthly_savings": None, "one_time": o.get("one_time", 0),
                             "monthly_fee": 0, "net_monthly": None,
                             "payback_months": "n/a (diagnostic, no hours replaced)"})
                continue
            net_m = monthly - o.get("monthly", 0)
            pay = None
            if o.get("one_time", 0) > 0:
                pay = round(o["one_time"] / net_m, 1) if net_m > 0 else "no payback on labor savings alone"
            rows.append({"option": o["name"], "replaced_share": share, "hours_replaced_per_week": round(h * share, 1),
                         "annual_savings": round(annual), "monthly_savings": round(monthly),
                         "one_time": o.get("one_time", 0), "monthly_fee": o.get("monthly", 0),
                         "net_monthly": round(net_m), "payback_months": pay})
    return {"status": "OK", "inputs": d, "rows": rows}


def table(r):
    if r["status"] != "OK":
        return f"ROI: INPUT NEEDED ({', '.join(r['missing'])}). No numbers shown.\n"
    out = ["| Option | Replaced | Hrs/wk | Annual savings | Net monthly | Payback (months) |", "|---|---|---|---|---|---|"]
    money = lambda v: "n/a" if v is None else f"${v:,}"
    for x in r["rows"]:
        if x["annual_savings"] is None:
            if x["replaced_share"] == r["rows"][0]["replaced_share"]:
                out.append(f"| {x['option']} | n/a | n/a | n/a | n/a | {x['payback_months']} |")
            continue
        out.append(f"| {x['option']} | {int(x['replaced_share'] * 100)}% | {x['hours_replaced_per_week']} | {money(x['annual_savings'])} | {money(x['net_monthly'])} | {x['payback_months']} |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    res = calc(json.load(open(sys.argv[1])))
    print(json.dumps(res, indent=2))
    sys.stderr.write(table(res))
