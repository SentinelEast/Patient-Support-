# Capacity Check (SHADOW, Step 0) - run 2026-10-04 (Sun), for Mon 2026-10-05

Label: **capacity 0** (dry run; no sending inboxes exist yet)

## Per-domain table

| Domain | Mailboxes expected | Connected in Apollo | Warm-up | Health (bounce/spam) | Capacity |
|---|---|---|---|---|---|
| DOMAIN_1 theaiagentagencyblueprint.com | 4 | 0 | n/a | n/a | 0 |
| DOMAIN_2 theaiagencyblueprint.org | 4 | 0 | n/a | n/a | 0 |
| DOMAIN_3 theaiagencyblueprint.io | 4 | 0 | n/a | n/a | 0 |
| Excluded: PRIMARY theaiagencyblueprint.com (chiefofstaff@) | 1 | 1 (Gmail, active, default) | Mailwarming enabled 2026-10-03 (day 1 of ~14) | not exposed by endpoint | 0 (never used for cold sends) |

## capacity_tomorrow
- Sum of sending-inbox capacity = 0 inboxes x 30 = 0
- Ramp cap: Patty is shadow, 0 external sends (/config/authority.md)
- capacity_tomorrow = min(0, 350, ramp cap) = **0**
- Per-domain breakdown: 0 / 0 / 0. No whole-domain pause triggered (domains simply not live); no spare-domain recommendation.

## Anomalies / flags
- Apollo email_accounts endpoint returns only id, email, type, active, default, created_at, last_synced_at. It does NOT expose warm-up status, daily limit, bounce rate or spam complaints. Those cannot be verified via the API; check the Apollo UI (Mailwarming settings). The SOP assumption on field names is not borne out.
- Doc conflict: patty-sop.md Step 2 and footer.md name chiefofstaff@theaiagencyblueprint.com (primary domain) as the sender, while business.md says the primary domain is never used for cold sends and sending inboxes are on DOMAIN_1-3. Joaquin to resolve.
- Apollo limits on the primary mailbox per business.md (50/day, 6/hour) not re-verifiable via API.
- DOMAIN_1 spelling ("agent") and purchase status of all 3 domains still unconfirmed.
- Telegram connector pending; no notifications sent per instructions.

## Questions for Joaquin
- Confirm the three domains are purchased and DOMAIN_1 spelling is intended.
- Which sender should sequences use: primary chiefofstaff@ or the DOMAIN_1-3 inboxes?
- ETA for creating the 12 mailboxes (warm-up ~14 days from creation).

## Sources / Assumptions
- Sources: Apollo apollo_email_accounts_index (2026-10-04, account id 6abf9b49b26e870014ba4da2); /sops/patty-sop.md Step 0; /config/business.md; /config/authority.md.
- Assumptions: absence from Apollo = not connected; primary mailbox contributes 0 per instruction; next business day Mon 2026-10-05 has no holiday impact; no sequence data checked (campaign search not needed at capacity 0).
