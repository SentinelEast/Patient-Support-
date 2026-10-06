# Capacity Check (SHADOW, Step 0) - run 2026-10-06 (Tue), for Wed 2026-10-07

Label: **capacity 0** (inboxes now connected but not warmed; shadow mode)

## Change since 2026-10-04
All 4 .io mailboxes are NOW connected in Apollo (Gmail, active). Connection dates are 2026-10-05/06, so warm-up age is 0-1 days at most.

## Per-inbox table

| Inbox | Apollo id | Connected (created_at UTC) | Last synced | Warm-up age on 10-07 | Capacity |
|---|---|---|---|---|---|
| chiefofstaff1@...io | 6ac40b9eb6d5790014dccd80 | 2026-10-05 20:42 | 2026-10-06 15:34 | ~day 2 of 14 (if Mailwarming on) | 0 |
| chiefofstaff2@...io | 6ac4e750235df5002012c9f0 | 2026-10-06 12:19 | 2026-10-06 15:22 | ~day 1 of 14 | 0 |
| chiefofstaff3@...io | 6ac4ea5b86d68c000cd0c981 | 2026-10-06 12:32 | 2026-10-06 15:27 | ~day 1 of 14 | 0 |
| chiefofstaff4@...io | 6ac4f896d57c720010c11479 | 2026-10-06 13:33 | 2026-10-06 15:27 | ~day 1 of 14 | 0 |
| chiefofstaff@...com (PRIMARY, excluded) | 6abf9b49b26e870014ba4da2 | 2026-10-02 | 2026-10-06 15:30 | day 5 of 14 (warm-up on since 10-03) | 0 (never cold-sends) |

## Per-domain breakdown
| Domain | Connected | Warmed | Capacity |
|---|---|---|---|
| DOMAIN_1 .com (agent) | 0 | 0 | 0 |
| DOMAIN_2 .org | 0 | 0 | 0 |
| DOMAIN_3 .io | 4 of 4 | 0 of 4 | 0 |

## capacity_tomorrow
- Sum of inbox capacities = 0 warmed x 30 = 0 (4 inboxes still warming; current warm-up limits not exposed by API, so counted 0 until confirmed)
- Ramp cap: Patty is shadow, 0 external sends (/config/authority.md)
- capacity_tomorrow = min(0, 350, 0) = **0**
- Earliest full-volume date by the 14-day rule: ~2026-10-19 (inbox 1), ~2026-10-20 (inboxes 2-4), if Mailwarming is on. Joaquin may confirm earlier readiness.
- No whole domain paused; no spare-domain recommendation.

## Anomalies / flags
- Apollo endpoint still exposes no warm-up status, daily limit, bounce or spam data; cannot verify Mailwarming is ON for the 4 .io inboxes. Check in Apollo UI.
- All 4 mailboxes report `default: true` and each is tied to a different user_id, implying separate seats were created (resolves the 1-mailbox-per-user limit, to be confirmed). Per-inbox default flag matters when selecting sender for sequences: Patty must pass explicit ids.
- Primary-domain vs sender doc conflict (patty-sop Step 2 / footer.md vs business.md) from 10-04 still open.
- Telegram connector pending; no Telegram alert possible. No notifications sent other than the allowed "drafts ready" note (see below).

## Questions for Joaquin
- Is Mailwarming ON for chiefofstaff1-4@theaiagencyblueprint.io, and what is each inbox's current warm-up daily limit?
- Do you want to count inboxes at their current warm-up limit (small, e.g. 5-10/day) before day 14, or hold at 0 until you confirm?
- Were separate Apollo seats purchased (one per mailbox)?
- Still open: DOMAIN_1 spelling and purchase of the 3 domains; which sender sequences should use.

## Sources / Assumptions
- Sources: Apollo apollo_email_accounts_index (2026-10-06, read-only); /sops/patty-sop.md Step 0; /config/business.md; /config/authority.md; prior check outputs/shadow/2026-10-04/patty/capacity-check.md.
- Assumptions: warm-up start = Apollo connection date; Mailwarming on (unverified); the 14-day rule applies; warm-up limits unknown so counted 0; Wed 2026-10-07 is not a holiday.
