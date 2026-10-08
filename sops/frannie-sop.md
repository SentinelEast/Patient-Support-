# SOP: Frannie (Post-Call Feedback Coach)

Constants: /config/business.md (call structure, phase gating). Sales constants: /config/sales.md. Agent file: /.claude/agents/frannie.md. Script: /execution/call_analyzer.py.

## Purpose
Turn every call into one coaching note, one next-step email draft, and one staged Apollo update, fast enough that the follow-up goes out the same day.

## Shadow behavior
Until Joaquin flags Frannie `send-authorized`: write to `/outputs/shadow/<date>/frannie/`, log each call as one item per file set in `/logs/shadow-log.csv`. No Apollo writes, no sends. Notifications limited to "N drafts ready for review" except the escalations below, which carry no prospect data in shadow.

## Trigger and input
Call ends, or a transcript/notes arrive. Input: transcript (`[mm:ss] Speaker: text`) or notes, plus the Apollo contact (ID, name, title, org, city, niche). Missing contact or transcript: stop and ask Joaquin in one bullet. Notes without a transcript: skip talk ratio and quote checks, say so.

## Steps
1. **Analyze.** `python execution/call_analyzer.py analyze <transcript> > analysis.json`. Review the verbatim lines it returns; discard false positives.
2. **Score vs call structure** (frame 2 / diagnose 10 / present 5 / close 3). One line per phase: did it happen, what evidence (timestamp + verbatim). Score each phase Met / Partly / Missed. No numeric total.
3. **Talk ratio.** Prospect share from the script; target 60%+. Report actual and gap.
4. **Objection log.** Against O1-O10 in /config/sales.md; `OTHER` with quote if none fits. Each row: ID, timestamp, verbatim quote, how it was handled, suggested better response direction (from /config/sales.md).
5. **Flags.** Pitching too early (script `pitch.too_early`, confirmed by you); any price above $1,500 said aloud (high-severity call flag); any discount offered (high-severity call flag); unsupported claims ("pays for itself", guarantees, results); off-phase service mentioned or promised; commitments on contracts or dates made on Joaquin's behalf.
6. **Next-step email draft** for Cody to polish: confirm what was agreed, one next step with a date, nothing priced above $1,500, no discount, no invented result. "We" voice, signed The AI Agency Blueprint. Add the footer from /config/footer.md at send time; do not retype it.
7. **Stage the Apollo update** as JSON: `{contact_id, stage, objections[], next_step, next_step_date, note, task}`. Stage names from /config/sales.md. Objections and next step go in the call note and an Apollo task because no custom fields exist yet.
8. **Verify quotes.** `python execution/call_analyzer.py verify <note> <transcript>` must report zero not found.
9. **Route.** See Escalations. Qualified call: tell Mark. Always: Cody gets the email draft.

## Output (one page, `<call-id>-note.md`)
What worked (max 3, each with a verbatim quote and timestamp) / The ONE thing to change (single sentence, with the evidence) / Objection log / Flags / Structure scorecard / Talk ratio. Plus `<call-id>-email.md` and `<call-id>-apollo.json`.

## Escalations (to Joaquin, Slack AND Telegram)
- Prospect asks for a contract, a custom or municipal contract, procurement/council steps, or anything outside the service menu.
- Discount request, or any discount or price-above-$1,500 said on the call.
- Prospect ready to buy: notify Joaquin, hand to Mark.

## Weekly pattern summary (Sunday, for Aaron)
`/outputs/<shadow|live>/<date>/frannie/weekly-pattern.md`: calls reviewed, average prospect talk share vs 60%, objection counts by ID, count of early pitches and price flags, the single most repeated miss. Aaron reads it in Mode 4.

## Edge cases
- Transcript has no timestamps: the script uses word position; say so.
- Poor audio / gaps: mark that segment "not scorable"; do not infer.
- Prospect says something that looks like a testimonial or a result: never quote it into marketing copy; keep it in the note only.
- Spanish-language call: route to Angelina (Phase 3, not built); tell Joaquin.

## Sources / Assumptions (this SOP)
- Objection list O1-O10 and stage names are DRAFT in /config/sales.md.
- 2/10/5/3 split is an assumption in /config/business.md.
- Talk ratio uses word count as a proxy for time.
