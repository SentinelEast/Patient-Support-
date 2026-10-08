# Dolly dry run (SYNTHETIC SAMPLE, SHADOW, nothing shared)
Date 2026-10-08. Each request produced a primary and an alternate SVG (the editable source; opens in Figma, Canva or a browser) plus a PNG preview of one variant. All six SVGs pass `asset_check.py`.

| # | Requester | Format | Files | Differences (primary vs alternate) | Check |
|---|---|---|---|---|---|
| R1 | Mark (S1) | Proposal cover | r1/proposal_cover-primary.svg, -alternate.svg | White page, navy bands vs navy page, gold bands | PASS |
| R2 | Mark (S3) | Process diagram | r2/process_diagram-primary.svg, -alternate.svg | Same layout, light vs dark | PASS |
| R3 | Joaquin | Social graphic | r3/social_graphic-primary.svg, -alternate.svg | Light vs dark | PASS |

## Rule tests
- R1: client name supplied but not approved. The asset shows "Prepared for: [client name pending Joaquin approval]"; the check confirms "Reyes Property Management" is absent from the file.
- R2: requester asked for a "crew scheduling" step. Declined: off-phase and not in the proposal scope. Only the four in-scope steps are drawn.
- R3: brief asked for a testimonial and a "trusted by" logo strip. Declined: none exist. Headline and bullets only. Negative control: an edited copy with "Trusted by 50 clients, 90% faster" FAILS the check, as it should.
- No prices appear on any asset. Footer is read from /config/footer.md at build time and matches exactly (the check compares it character for character).

## Brand settings used
Primary #1F3A5F, accent #C9A227, Georgia/Arial: all PLACEHOLDER in /config/brand.md. Wordmark is plain text; there is no logo file.

## Sources / Assumptions
- Copy: R1/R2 from Mark's outlines (S1, S3); R3 from Cody-style lines supplied in the request. "Delivered in 21 days" is from /config/business.md. "Trained on your own documents" and "named human operator" are from /config/business.md positioning.
- Assumption: SVG is acceptable as the editable source until a Figma or Canva connector is authorized (Canva needs authorization; Figma not set up for brand files).
- Editable source link: PENDING, see open items.
