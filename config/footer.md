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

## Sender

- From: chiefofstaff@theaiagencyblueprint.com (mailbox connection PENDING, see /config/business.md open items)
- Sending inboxes themselves are on DOMAIN_1 to DOMAIN_3 (placeholders, owned by Joaquin). Footer text is identical on every inbox.

## Checks (Patty runs before loading any sequence)

1. Footer string matches the block above character for character.
2. Unsubscribe line present.
3. No retired-brand strings (run `python execution/brand_scrub.py`).
