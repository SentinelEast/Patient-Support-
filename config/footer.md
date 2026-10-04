# Email Footer (verbatim, every outbound template)

Agents read this file at send time. Never retype or paraphrase the footer. If the text below ever differs from an email draft, the draft is wrong.

## Footer (plain text)

```
The AI Agency Blueprint | 80 River St., Hoboken, NJ 07030 | 856-254-6000 | www.theaiagencyblueprint.com
```

## Unsubscribe line (CAN-SPAM, required directly under the footer)

```
Not relevant? Reply "unsubscribe" or click here to opt out: {{unsubscribe_link}}
```

`{{unsubscribe_link}}` is Apollo's merge variable. Patty confirms it renders in the Apollo sequence preview before any send (open item if it does not).

## Signature (Chief of Staff, above the footer on every email)

```
Chief of Staff
Office of Joaquin Garcia, CEO
```

No personal name is invented for the Chief of Staff. Emails are written in the first-person plural ("we"); Joaquin is named as "our CEO" where the call is offered. Replies from prospects reach the Chief of Staff mailbox, and Joaquin approves any reply that books or commits him.

## Sender

- From: one of the 12 sending inboxes (chiefofstaff1-4 on each sending domain, display name "Chief of Staff, The AI Agency Blueprint"), assigned by Patty.
- Replies: NO Reply-To override (changed 2026-10-04). Replies must land in the sending inbox so Apollo detects and logs them; a Reply-To on another mailbox would hide replies from Apollo, the system of record. The primary-domain mailbox is connected in Apollo with Mailwarming on (2026-10-03) but is never used for cold sends.
- Sending inboxes themselves are on DOMAIN_1 to DOMAIN_3 (see /config/business.md). Footer text is identical on every inbox.

## Checks (Patty runs before loading any sequence)

1. Footer string matches the block above character for character.
2. Unsubscribe line present.
3. Signature block matches the block above (no individual's name).
4. No retired-brand strings (run `python execution/brand_scrub.py`).
