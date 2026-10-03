# Patty dry-run: Capacity, Send Plan, Replies, Dashboard (SHADOW, 2026-10-03)

No Apollo writes, no sends. Read-only checks only. Nothing external happened.

## Step 0: Capacity check (actual)

| Domain | Inboxes | Connected | Warm | Healthy | Capacity |
|---|---|---|---|---|---|
| DOMAIN_1 (placeholder) | 4 | 0 | 0 | 0 | 0 |
| DOMAIN_2 (placeholder) | 4 | 0 | 0 | 0 | 0 |
| DOMAIN_3 (placeholder) | 4 | 0 | 0 | 0 | 0 |
| **Total** | 12 | 0 | 0 | 0 | **0** |

`capacity_tomorrow` = min(0, 350, ramp cap) = **0**. Reported to Aaron. Root cause: domains/mailboxes not yet provided (open items). Warm-up (~14 days) starts only after they are connected.

## Steps 1-2: Send plan (illustrative at capacity 350, labeled "capacity 0" in the real run)

| Check | SAMPLE-1 | SAMPLE-2 | SAMPLE-3 | SAMPLE-4 | SAMPLE-5 |
|---|---|---|---|---|---|
| Email re-verified | sim. | sim. | sim. | sim. | sim. |
| Role/generic address | no | no | no | no | no |
| Cody JSON status | PASS | PASS | PASS | PASS | PASS |
| Footer + signature match /config/footer.md | yes | yes | yes | yes | yes |
| Unsubscribe merge var present | yes (render in Apollo preview: unverified) | | | | |
| Recipient timezone / window | ET, 09:00-16:00 | ET | ET | ET | ET |

Illustrative stagger: 5 contacts across 5 distinct healthy inboxes (1 each), well under 30 per inbox and 350 total. Follow-ups: Email 2 on day 4, Email 3 on day 9 counted against that day's capacity.
In the real run these would NOT be loaded: capacity is 0 and Patty is in shadow.

## Step 3: Reply classification test (5 MOCK replies, authored for the test)

| # | Mock reply | Class | Action drafted |
|---|---|---|---|
| 1 | "Sure, I'd take a call. What days work?" | interested | Reply with three times via booking link; Slack + Telegram alert |
| 2 | "Not now, try me in January after budget adoption." | not-now | Stop sequence; Apollo task for early January |
| 3 | "Please remove me from your list." | unsubscribe | Suppress in Apollo within the hour |
| 4 | Delivery failure notice, mailbox full/unknown | bounce | Suppress; add to inbox bounce count |
| 5 | "Out until Oct 14, contact the deputy clerk." | out-of-office + referral | Pause sequence to Oct 14; draft note to deputy (after authorization) |

### Draft reply for mock #1 (needs Joaquin's approval)

> Subject: re: council minutes at Sample Township
>
> Dear Dana Reyes,
>
> Thank you. Here are three times that work for a free 20-minute call with our CEO, Joaquin Garcia:
> - {{time_option_1}}
> - {{time_option_2}}
> - {{time_option_3}}
>
> Or choose your own time here: {{booking_link}}
>
> Chief of Staff
> Office of Joaquin Garcia, CEO
>
> The AI Agency Blueprint | 80 River St., Hoboken, NJ 07030 | 856-254-6000 | www.theaiagencyblueprint.com
> Not relevant? Reply "unsubscribe" or click here to opt out: {{unsubscribe_link}}

(No price, no audit mention, per first-reply rule.)

## Step 5: Dashboard (day with 0 sends)

| Metric | Value |
|---|---|
| Sends vs capacity | 0 / 0 |
| Opens / replies / positive reply rate | n/a |
| Meetings booked | 0 |
| Bounces | 0 |
| Inbox health | no inboxes connected |
| Suppressions made | 0 (3 would be made if mock replies 3 and 4 were live) |
| Escalations | Capacity is 0: domains/mailboxes pending |

Notification test: Slack channel is reachable via connector; Telegram connector missing, so Telegram delivery is PENDING. Shadow-mode notice would read "3 drafts ready for review".

## Sources / Assumptions
- Capacity figures reflect that no mailbox exists yet, not an Apollo query (Apollo inbox listing not run).
- Replies are mock text; classification logic is shown, not accuracy-tested.
- Open items: DOMAIN_1-3, mailbox connection, booking link, Telegram, `{{unsubscribe_link}}` render check.
