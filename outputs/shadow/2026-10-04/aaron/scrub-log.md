# Scrub log 2026-10-04 (SHADOW, Modes 1-2)

Pulled: 31 people from 2 free Apollo people searches (15 niche A, 16 shown niche B; 237 and 4,980 total matches). Shortlisted 10 (5 A, 5 B), one per org.

| Step | Result |
|---|---|
| 1. Verify email | NOT DONE. No credit spend authorized; Apollo free search returns only a has_email flag, no address. All 10 = "not verified (no credit spend authorized)". Verified rate = 0/10 = 0%, below the 90% target. This is an expected consequence of no-spend, not a list-quality failure, but it blocks any send list. |
| 2. Dedupe | Partial. One apollo_contacts_search (keyword) on the shortlisted orgs returned 0 saved contacts. Keyword search is a weak check. Suppression (do-not-contact) list not accessible from this run: not checked. |
| 3. Role/generic addresses | Not checkable (no addresses). Municipal clerk inboxes are a known risk once revealed. |
| 4. Geo/niche | All 10 filtered to NJ at person and org level. No Philadelphia-area results pulled. Org city and employee count are hidden in free results, so the 1-50 size limit for niche B is UNVERIFIED. Possible niche B misfits: none excluded on evidence, but Titanium Plumbing (org revenue $35.9M) and Pruzansky Plumbing were left out as likely over 50 staff. |
| 5. Verified rate | 0/10 (see step 1). Escalation threshold technically tripped; flagged here, not posted (no posts allowed). |

Other notes
- Last names are obfuscated in free search; names are partial. Full names need paid enrichment.
- apollo_organizations_job_postings states a cost of 1 credit per request, so it was NOT called. No job-posting triggers were retrieved.
- Candidate bench not used (has_email=true): Hopewell, Manville, Montgomery, Bernards, Hardyston. Excluded for no email flag: Hamilton Twp, Mansfield Twp, Sayreville DPW.
- Credit usage: none observed in any response (no mcp_credits block).

## Sources / Assumptions
- Sources: Apollo people search (two calls), Apollo company search (3 lookups: Delanco, Sea Bright, Titanium), Apollo contacts search (1 call), run 2026-10-04.
- Assumed: title match implies decision-maker fit; generic pain scored 10 with no trigger line; fiscal-year type unknown, neutral timing 8. SMB size unverified.
