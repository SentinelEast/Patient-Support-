# Business Constants: The AI Agency Blueprint

Single source of truth. Every agent and SOP references this file; none restate it. Owner: Joaquin Garcia, CEO.

## Identity and sender

- Brand: The AI Agency Blueprint
- Sender: chiefofstaff@theaiagencyblueprint.com (mailbox PENDING connection)
- Footer and unsubscribe: /config/footer.md (verbatim)
- Retired brand names must never appear anywhere. Enforced by `python execution/brand_scrub.py` (zero hits required; the patterns live only in that script).

## Voice

Confident, direct, mission-driven, builder not consultant. Faith-grounded and community-first, never preachy in outreach. Municipal tone: formal-warm. SMB tone: plain and direct.

## Positioning

We install AI-powered operations systems that cut manual workload 50-70% and produce better documentation, delivered in 21 days, trained on the client's own documents, with a named human operator.

No client case studies exist yet. Never invent results, logos, testimonials or numbers. Frame as "systems we build" and the audit as the low-risk first step.

## Offer ladder

| Step | Offer | Price | Delivery |
|---|---|---|---|
| 0 | Free 20-minute call (top-of-funnel hook; NOT a free assessment) | $0 | 20 min |
| 1 | AI Audit (entry offer) | $1,500 | 7 business days |
| 2 | AI Operations Install | $18,000 | 21 days |
| 2b | Managed Operations retainer | $2,400-$4,800/mo | ongoing |
| 3 | Resilience Operations Platform | $65,000 + $7,500/mo | later |

Rules: never mention the $1,500 audit in Email 1 (the free call is the hook). Price in writing only for anything above $1,500. Never discount on a first meeting.

## Niches

- **A. NJ municipalities**: city managers, clerks, DPW directors, administrators, emergency management.
- **B. Small businesses**: owners, founders, operations managers at NON-TECH companies with 1-50 employees in NJ and the Philadelphia area.

Geo filter: NJ and Philadelphia area only. Drop everything else.

## Phase gating (agents must not pitch outside the current phase)

| Phase / window | Sellable now |
|---|---|
| **Phase 1 (current)** | Constituent/Customer Response Agent; AI Audit |
| Months 3-4 | + Document Intake |
| Months 5-7 | + Inspection Reporting and Scheduling |
| Month 8+ | + Resilience Operations Platform |

Current phase: **Phase 1**. Joaquin changes this line; agents never do.
Off-phase pitch = critical error in shadow mode.

## Outbound capacity (Apollo only)

- Sending tool: Apollo (sequences, sending, replies, logging). No other sending tool is referenced anywhere.
- 3 domains x 4 mailboxes = 12 inboxes. Max 30 sends/inbox/day. Hard cap 350 sends/day total (12 x 30 = 360, cap wins). Mon-Fri only: ~1,750 sends/week.
- 3-touch sequence => ~580 NEW prospects/week (1,750 / 3). Daily new-prospect slots = 350 minus scheduled follow-up touches due that day.
- Prospect pool target: 2,500/week. Aaron sizes the daily send list to capacity and holds the remainder in pool.
- Per-domain ceiling: 4 inboxes x 30 = 120/day. One domain paused = capacity drops by up to 120.
- Warm-up: no inbox sends at full volume until warmed (~14 days). Before building the day's capacity, Patty checks each inbox's warm status in Apollo. Unwarmed or paused inboxes contribute 0 (or their current warm-up limit) and capacity reduces automatically. Aaron receives Patty's capacity number, never assumes 350.
- Post shadow-exit ramp for Patty: week 1 capped at 100/day, week 2 at 200/day, week 3+ at 350/day (or current healthy capacity if lower).
- Pause triggers: bounce rate >3% or any spam complaint on an inbox => pause that inbox, alert. If a whole domain trips a pause, flag it and recommend a spare domain at that point. Do not recommend buying domains otherwise.

## Domains (owned by Joaquin; do not assume names)

| Slot | Value | Status |
|---|---|---|
| DOMAIN_1 | PLACEHOLDER | open item |
| DOMAIN_2 | PLACEHOLDER | open item |
| DOMAIN_3 | PLACEHOLDER | open item |

Each domain hosts 4 mailboxes. Joaquin confirms none of the three contains the retired brand name; `execution/brand_scrub.py` re-checks this table once real values are entered.

## Weekly KPI targets (Aaron compares against)

| Metric | Target |
|---|---|
| Sends | 1,750/week |
| Personalized follow-ups | 25-35/day |
| Positive reply rate | 2%+ |
| Discovery calls | 2-4/day at maturity |
| Audit-to-install conversion | >=50% |
| List quality (verified) | >=90% |
| Bounce rate | <3% per inbox |

Escalation triggers: verified <90%; reply rate <1% for 3 days; deliverability alerts; bounce >3% or spam complaint.

## Call structure (25 minutes)

Frame 2 min, diagnose 13, present 7, close 3. Sales calls run on Joaquin's calendar via the booking link (PENDING).

## Notifications

Every notification goes to BOTH Slack and Telegram. If one channel fails, deliver on the other and log the failure. Telegram connector is not yet confirmed (open item).

## Output standard (all agents)

1. Every output ends with a **Sources / Assumptions** note: where each fact came from (Apollo record ID, URL, document) and what was assumed. Unverifiable facts are removed, not softened.
2. Concise. Questions to Joaquin as bullets.
3. Drafts only until the agent is send-authorized in /config/authority.md.
4. Apollo is the system of record. No private lists.

## Next build after outbound

AI chatbot on the Lovable-built website answering resident and inspection-paperwork questions. Lead with transparency about what it is (many people are skeptical of AI).

## Open items needing Joaquin

- [ ] Connect mailbox chiefofstaff@theaiagencyblueprint.com
- [ ] Provide DOMAIN_1, DOMAIN_2, DOMAIN_3 and confirm none contains the old brand name
- [ ] Create the 12 mailboxes and start Apollo warm-up (clock for ~14 days)
- [ ] Email verification tool: NeverBounce or MillionVerifier (default: NeverBounce)
- [ ] Booking link and Loom account for Email 1 alternative
- [ ] Telegram bot token and chat ID; Slack channel names
- [ ] Suppression list: confirm Apollo "do not contact" list is the master
- [ ] Confirm `{{unsubscribe_link}}` renders in Apollo sequences
