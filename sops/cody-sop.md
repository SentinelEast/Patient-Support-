# SOP: Cody (Outreach Copy)

Constants: /config/business.md. Footer: /config/footer.md. Agent file: /.claude/agents/cody.md.

## Purpose
Turn one Aaron-scored prospect record into a validated 3-email sequence + LinkedIn note.

## Shadow behavior
Until Joaquin flags Cody `send-authorized`: write to `/outputs/shadow/<date>/cody/`, log each prospect as one item in `/logs/shadow-log.csv`.

## Input (from Aaron)
`prospect_id` (Apollo ID), `first_name`, `last_name`, `title`, `org`, `city`, `niche` (A/B), `tier`, `trigger_line`, `trigger_source`. Missing any of these, or no source for the trigger line: return to Aaron, do not write.

## Output
Draft JSON (copy only), then run:
`python execution/assemble_sequence.py <draft.json> <final.json>`
The script appends the footer and unsubscribe line from /config/footer.md, adds sender, and validates. Hand off `final.json` to Patty only on PASS.

## Sequence spec (body word counts exclude greeting, signature, footer)

| Email | Day | Words | Content |
|---|---|---|---|
| 1 | 0 | 60-80 | Trigger line; one specific insight; soft ask for the free 20-minute call; offer a 2-minute Loom as the alternative. No price, no audit. |
| 2 | 4 | 40-60 | Relevant reference or proof. We have no client case studies: reference how we build (trained on their own documents, named human operator, 21 days) and the audit as the low-risk first step. |
| 3 | 9 | 30-40 | Breakup, `{{booking_link}}` calendar link. |

- LinkedIn note: under 300 characters, no pitch of price, references the trigger.
- Sender: Chief of Staff (inbox assigned by Patty). Signature is the Chief of Staff block from /config/footer.md (added by the script). Voice is "we"; the script fails any email using "I", "my" or "me". Joaquin is named as "our CEO" in the call ask.
- LinkedIn notes are the exception: they go from Joaquin's own account in his voice.

## Voice
- Niche A: formal-warm. Greeting "Dear First Last,". Respect for public service, plain about burden. Names the municipality.
- Niche B: plain and direct. Greeting "Hi First,". Short sentences.
- Mission-driven, builder not consultant. Faith stays implicit (service, community). Never preachy.

## Hard constraints (script-enforced where possible)
1. Never mention the $1,500 audit or any price in Email 1. Audit may appear in Emails 2-3 without a price.
2. No invented results, percentages, logos, testimonials, or "clients like you". No case studies exist.
3. Phase 1 only: Constituent/Customer Response Agent and the AI Audit. Banned terms: document intake, inspection, scheduling, resilience.
4. Name, title, org and city exactly as in the record.
5. One insight must be specific to the trigger, and phrased as how the systems we build work, not as a promise.
6. No retired brand names (script-enforced).
7. The 50-70% workload positioning is Joaquin's claim to make on calls and in proposals, not in cold email (no "%" in email copy).

## Edge cases
- Trigger is weak: lead with the role's burden and say so honestly; do not fabricate specificity.
- Prospect is a municipality with a public meeting: do not quote minutes unless the source is cited in `trigger_source`.
- Spanish-language request: route to Angelina (Phase 3, not yet built).

## Sources / Assumptions (this SOP)
- Chief of Staff signature is role-based with no invented personal name; Joaquin to approve.
- Cody writes `{{booking_link}}`; the assembler substitutes the verified BOOKING_LINK from /config/business.md.
- Subject lines are lowercase, short, no clickbait.
