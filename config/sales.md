# Sales Constants (Phase 2 agents: Frannie, Mark, Dolly)

Companion to /config/business.md. Prices, delivery times, offer ladder, phase gating, call structure and footer live THERE and are not restated here. This file holds only what Phase 2 needs beyond them. Owner: Joaquin Garcia, CEO. Only Joaquin edits.

Status key: **SET** = decided by Joaquin. **DRAFT** = starter written by Claude, Joaquin to approve or replace. **PENDING** = no value exists; agents must print the placeholder, never guess.

> The 12-month plan is not in the repo. Everything below marked DRAFT or PENDING should be reconciled with it.

## Service menu for proposals (SET by reference)

Source: Offer ladder + Phase gating in /config/business.md. Current phase = Phase 1, so proposals may include only:
- AI Audit (entry offer)
- AI Operations Install, scoped to the Constituent/Customer Response Agent (ASSUMPTION: the Install is the vehicle for the Phase 1 agent; Joaquin to confirm)
- Managed Operations retainer (ASSUMPTION: sellable in Phase 1 as an add-on to the Install; Joaquin to confirm)

Not in a proposal: Document Intake, Inspection Reporting and Scheduling, Resilience Operations Platform (off-phase). Anything the prospect asks for outside this list = "outside the service menu" = escalate to Joaquin.

## Price disclosure rules (SET)

- Entry offer = AI Audit, $1,500 (business.md). It may be said aloud.
- Anything above $1,500 is quoted in writing only, in an approved proposal. Never aloud, never in a first reply.
- No discounts on a first meeting. Offer reduced scope instead (e.g. Audit first, then Install).

## Escalate to Joaquin immediately (SET)

1. Prospect asks for a contract (any contract).
2. Custom or municipal contract, procurement process, council resolution, RFP, or insurance/indemnity terms.
3. Anything outside the service menu above.
4. Prospect is ready to buy (Frannie notifies Joaquin and hands to Mark).
5. Request for a discount or custom pricing (answer: no discount, offer reduced scope; tell Joaquin).

## Call stages (Apollo) (DRAFT)

Frannie uses exactly these stage names so Apollo stays clean. Verify against Apollo before first live write.

`Discovery Held` > `Qualified - Proposal Needed` > `Proposal Sent` > `Closed Won` | `Closed Lost` | `Nurture`

Apollo facts checked 2026-10-08 (read-only): the only custom contact field is `Qualify Contact` (picklist: Qualified / Disqualified, read-only via API). There are NO custom fields for objections, next step or next-step date. Until Joaquin creates them (open item), Frannie stages the update as: stage, a call note (objections + summary), and an Apollo task (next step + due date).

## Standard objections list (DRAFT)

Frannie logs against these IDs; anything else is logged as `OTHER` with the verbatim quote. Response direction is guidance, not a script. No numbers.

| ID | Objection | Response direction |
|---|---|---|
| O1 | Price / no budget | Do not discount. Offer reduced scope: start with the Audit. Price above $1,500 follows in writing. |
| O2 | Bad timing / next quarter / budget cycle | Ask what changes by then; propose the Audit as a low-risk first step; set a dated follow-up. |
| O3 | Don't trust AI / it makes mistakes | Be transparent about what it is. Trained on their own documents, named human operator, human review. No result claims. |
| O4 | Data privacy / security | Say what data the system touches in the agreed scope; specifics go in writing; escalate legal/security questionnaires to Joaquin. |
| O5 | Need someone else to approve (partner, board, council) | Ask who and what they need; offer a written summary they can forward; propose a joint follow-up. |
| O6 | We already have a tool or do it in-house | Ask what it does not cover; position as replacing admin hours, not their core tool. |
| O7 | Staff will push back / fear of replacement | Frame as removing repetitive work; involve the staff who own the workflow in the Audit. |
| O8 | Need to think about it | Ask what specifically; agree a next step with a date. |
| O9 | Procurement / contract / legal requirements | ESCALATE to Joaquin. No commitments. |
| O10 | Tried automation before and it failed | Ask what failed; the Audit scopes the workflow before any build. |

## Proposal terms (Mark reads these; never invented)

| Term | Value | Status |
|---|---|---|
| Follow-up cadence after proposal sent | Day 3, day 7, day 13 | SET (brief 2026-10-08) |
| Proposal expiry | PENDING (days from send) | PENDING Joaquin |
| Deposit | PENDING (amount or %, due when) | PENDING Joaquin |
| Payment schedule / balance due | PENDING | PENDING Joaquin |
| Delivery timeline per service | Audit 7 business days; Install 21 days; retainer ongoing (business.md) | SET |
| Start-date rule (kickoff after deposit) | PENDING | PENDING Joaquin |

A proposal with any PENDING term prints `[PENDING: <term>, Joaquin]` in that spot and cannot leave shadow until filled.

## ROI inputs (Mark)

| Input | Rule | Status |
|---|---|---|
| Hours currently spent on the pain workflow | Must come from the prospect (transcript/notes). If absent: "INPUT NEEDED", no number. | SET |
| Hourly cost | Use the wage the prospect states. If they give none: "INPUT NEEDED". | SET |
| Loaded-cost multiplier (taxes, benefits) | Default 1.0 (wage only, conservative) until Joaquin sets a factor. | PENDING Joaquin |
| Share of hours replaced | Show BOTH 50% and 70%, the positioning range in business.md. State it is a target range, not a guarantee, and that no client results exist yet. | SET |
| Weeks per year | 52 | SET |
| Payback (months) | Price / monthly net savings. If net savings <= 0: "no payback on labor savings alone". | SET |

## Option construction (Mark) (DRAFT)

Three options, all from business.md prices:
- **Below target**: AI Audit ($1,500, 7 business days). Reduced scope; the low-risk first step. (Whether the Audit fee is credited toward an Install is PENDING Joaquin. Mark does not promise a credit.)
- **At target**: AI Operations Install ($18,000, 21 days), Constituent/Customer Response Agent.
- **Above target**: Install + Managed Operations retainer, starting at the low end of the retainer range ($2,400/mo). Which tier ($2,400-$4,800/mo) applies to which scope is PENDING Joaquin.

Target = the Install. If Joaquin sets a different target, change this line.

## Shadow log for Phase 2

Same format as Phase 1: `date,agent,item,approved,edits,error_severity` in /logs/shadow-log.csv. Each agent's 10-business-day clock starts at its first logged shadow item after Joaquin flags it in /config/authority.md.
