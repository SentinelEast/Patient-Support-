# Aaron dry-run: Scrub, Score, Send List (SHADOW, 2026-10-03)

All 5 prospects are SYNTHETIC. No Apollo, Vibe Prospecting or verifier calls were made; no credits spent.

## Mode 2: Scrub log (7 pulled, 5 kept)

| Record | Result | Rule |
|---|---|---|
| SAMPLE-1 to SAMPLE-5 | kept | verified (simulated), named person, in niche, in geo |
| SAMPLE-X1, info@ address at a township | removed | role/generic address |
| SAMPLE-X2, hardware store in Albany, NY | removed | outside NJ/Philadelphia area |

Verified rate: 7/7 simulated (no real verifier run), so the 90% escalation is not tested here.

## Scores
See `scored-prospects.csv`. Tier mix: 3 x A, 2 x B, 0 x C. Rubric and weights from /sops/aaron-sop.md (fit 30, pain 30, reach 20, timing 20). Municipal timing scores high for early October (calendar-year budget build, assumption).

## Mode 3: Daily send list for next business day (Mon 2026-10-05)

- **Actual:** `capacity_tomorrow` from Patty = **0** (inboxes not yet connected or warmed). Per SOP, no list is produced.
- **Illustrative (if healthy capacity were 350, 0 follow-ups due):**
  - slots = 350 - 0 = 350
  - eligible Tier A/B in pool = 5
  - filled = 5 (A first: SAMPLE-1, 2, 3; then B: 4, 5); pool remaining = 0
  - never exceeds slots: PASS
  - note: pool is far below the 2,500/week target in this dry run because it is 5 samples; sourcing throughput is untested.

## Weekly review (Mode 4)
Not exercised: no week of metrics exists. Will be exercised the first Sunday after live data.

## Sources / Assumptions
- Prospects, orgs, emails and trigger signals are fictional; scores show the rubric working, not market data.
- Municipal fiscal year assumed calendar-year; Joaquin to verify.
- Questions for Joaquin:
  - Confirm the title list for niche A and the SMB industry list for niche B.
  - Approve a Vibe Prospecting credit budget per week before the first live sourcing run.
