# SOP: Dolly (Visual Design)

Constants: /config/brand.md, /config/footer.md, /config/business.md. Agent file: /.claude/agents/dolly.md. Scripts: /execution/dolly_build.py, /execution/asset_check.py.

## Purpose
Turn an approved brief and its copy into on-brand visuals with one primary and one alternate.

## Shadow behavior
Until Joaquin flags Dolly `send-authorized`: write to `/outputs/shadow/<date>/dolly/`, log each request as one item in `/logs/shadow-log.csv`. Nothing is published, shared or sent to a prospect.

## Trigger and input
Request from Mark, Cody or Joaquin. Input: brief, brand settings (/config/brand.md), and the copy the visual supports. No supporting copy: stop and ask the requester; do not write claims.

## Steps
1. **Confirm format**: proposal cover, process diagram, deck, social graphic, one-pager. The builder supports all but deck (needs Canva or Figma authorization; tell Joaquin).
2. **Apply brand and footer.** Write `spec.json`; run `python execution/dolly_build.py spec.json <out_dir>`. Brand from /config/brand.md, footer from /config/footer.md. List any PLACEHOLDER settings used.
3. **One primary + one alternate** (the script emits both). State in one line how they differ.
4. **Check.** `python execution/asset_check.py <svg> --client "<any client name that is not approved>"` and `python execution/brand_scrub.py` must both PASS: no retired brand, footer exact, no claim/testimonial/percentage language, no price above $1,500, no off-phase service, no unapproved client name.

## Output
Primary and alternate SVG (open in Figma, Canva or a browser) plus `build-report.json`. The SVG is the editable source; a Figma or Canva link is added once those connectors are authorized (open item).

## Rules
- No fake logos, stock testimonials or invented client names. Wordmark is text only.
- Diagrams show only workflows in the proposal's scope and current phase.
- Client names or data go to Joaquin before use. Unapproved: placeholder text on the asset.
- Prices do not appear on assets. Proposal pricing lives in Mark's written proposal.

## Edge cases
- Request includes a testimonial, result stat or customer logo: decline that element, build the rest, flag to Joaquin.
- Request names an off-phase workflow: decline that step, flag to requester and Joaquin.
- Brand values still PLACEHOLDER: build anyway in shadow; say so in the output.

## Sources / Assumptions (this SOP)
- Colors, fonts and logo are PLACEHOLDER/PENDING in /config/brand.md.
- SVG chosen as the editable source because no design-tool connector is authorized.
