# Scrub log 2026-10-06 (SHADOW, Modes 1-2)

Pulled: 50 people (25 niche A from Apollo free search, 25 niche B from Apollo free search; 189 and 11,733 total matches) plus a 20-row Vibe niche B preview (39,798 matches). Shortlisted 26 (12 A, 14 B), one per org, has_email=true only. Target was about 20 per niche; niche A page held only 12 with an email flag and one per org.

| Step | Result |
|---|---|
| 1. Verify email | NOT DONE. No credit spend authorized; Apollo free search returns only a has_email flag. Verified rate = 0/26 = 0%, below the 90% target. Expected under no-spend, not a list-quality failure, but blocks any send list. |
| 2. Dedupe | NOT DONE this run. No Apollo contacts or suppression check run; suppression list not accessible. |
| 3. Role/generic addresses | Not checkable (no addresses). 4 niche A records are Municipal Clerks, a known shared-inbox risk once revealed (Tier C rule applies if only a clerk@ address exists). |
| 4. Geo/niche | Search filtered to NJ (A) and NJ plus Philadelphia (B) at person level. City and employee count hidden in free results, so 1-50 size for niche B is UNVERIFIED. Dropped Camden County (county, not a municipality). Vibe preview was noisy: consulting/nonprofit/PA-outside-Philly rows (Hanover PA) and no non-tech filter, because industry autocomplete is not available here. Vibe rows NOT used in scoring. |
| 5. Verified rate | 0/26. Escalation threshold technically tripped; flagged here only (shadow, no posts). |

Scoring result: 0 Tier A, 0 Tier B, 26 Tier C (A scores 43-46, B scores 27-37; all C because reach = 0 and no trigger sources). No trigger lines written: "none found" for all. apollo_organizations_job_postings costs 1 credit per request and was not called.

Vibe cost estimate (read-only, 20 niche B rows, email only): base 20 credits + enrichment 40 credits (2 per email) = 60 credits, 3 per row. Extrapolated to the approved 700-row start = about 2,100 credits/week; 2,500 rows = about 7,500 credits/week. Phone enrichment not estimated. Base alone at 2,500 rows would be 2,500, so the approved cap is exceeded once enrichment is added above about 833 rows/week; Joaquin decision needed.

Blockers
- No verification credits or approval: 0% verified, no Tier A/B possible.
- Free search hides email, city, size; trigger sources need paid job-postings lookups or manual council-minutes research.
- Vibe niche B lacks a non-tech filter in this session; noisy results.
- Fiscal-year type per municipality not researched; timing set to neutral 8.
- Credit usage: none observed.

## Sources / Assumptions
- Sources: Apollo people search (2 calls plus 2 empty/over-filtered attempts), run 2026-10-06; Vibe fetch-entities preview session_39_tidy_ferrets_loosely_listened (table fetch_prospects_qyvjsxes) and enrich-prospects estimate (view_kgtep7ml), no export.
- Assumed: title match implies decision-maker fit; generic pain scored 10; timing neutral 8 (A) / 5 (B, no hiring signal); size unverified; cost extrapolation is linear.
