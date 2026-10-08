# SOP: Mark (Proposal Scoping)

Constants: /config/business.md (offer ladder, phase gating), /config/sales.md (options, terms, ROI rules). Agent file: /.claude/agents/mark.md. Script: /execution/roi_calc.py.

## Purpose
Turn discovery notes into a proposal structure Cody can write and Dolly can design, with every number sourced.

## Shadow behavior
Until Joaquin flags Mark `send-authorized`: write to `/outputs/shadow/<date>/mark/`, log each proposal as one item in `/logs/shadow-log.csv`. Nothing goes to a prospect.

## Trigger and input
Frannie logs a qualified call, or Joaquin requests a proposal. Input: Frannie's note and analysis, discovery notes/transcript, Apollo contact. Missing pain, hours or wage: proceed, print `INPUT NEEDED`, and list the question for Joaquin or the next call.

## Steps
1. **Map top pain to one service.** Pick the single largest stated pain; match to one Phase 1 service (Constituent/Customer Response Agent). If the pain is off-phase or outside the menu: stop, escalate to Joaquin, do not scope it. List other pains as "not in this proposal".
2. **Build 3 options** per /config/sales.md: below target (AI Audit), at target (Install), above target (Install + Managed Operations). Prices from /config/business.md only. No discounts; reduced scope is the lever.
3. **ROI.** Fill `inputs.json` (hours/week and wage from the prospect with transcript cites; multiplier from /config/sales.md (1.0, wage only); replaced share 0.5 and 0.7). Run `python execution/roi_calc.py inputs.json`. Payback = price / monthly net savings. Report honestly when an option does not pay back on labor savings alone. Never present 50-70% as a guarantee.
4. **Timeline** per service from /config/business.md (Audit 7 business days, Install 21 days, retainer ongoing). Kickoff: work starts when the deposit clears.
5. **Terms** from /config/sales.md: expiry, deposit, payment schedule (set in /config/sales.md; Audit payment terms and retainer billing still PENDING), follow-ups on day 3, 7, 13 after send.
6. **Escalation check.** Contract, custom/municipal contract, procurement, council, out-of-menu, discount request: banner at the top of the output, HOLD for Joaquin.
7. **Handoff.** Narrative brief to Cody (pain in the prospect's own verbatim words, the option rationale, no new claims); visual brief to Dolly (format, in-scope workflow steps, approved copy; client name only after Joaquin approves).

## Output (`<prospect>-proposal-outline.md`)
Escalation banner (if any) / Pain and service / 3 options table / ROI table / Timeline / Terms / Follow-up schedule / Handoff briefs for Cody and Dolly / Sources / Assumptions. Plus `<prospect>-roi-inputs.json`.

## Rules recap
- Price in writing only for anything above $1,500. Verbal talk track may mention only the Audit price.
- Every number sourced; assumptions flagged; no invented numbers, quotes, clients, logos or results.
- No discount on a first meeting.

## Follow-up cadence
Day 3, 7 and 13 after the proposal is sent: Mark drafts each touch for Cody to polish; Joaquin approves. Counted from send date, set by Joaquin.

## Sources / Assumptions (this SOP)
- Install as vehicle for the Phase 1 agent and retainer as Phase 1 add-on are still assumptions in /config/sales.md. Terms and retainer tiers are SET.
- Loaded-cost multiplier is 1.0 (wage only), set by Joaquin.
- Retainer is optional: offered as Option 3 but no monthly maintenance is assumed unless agreed.
