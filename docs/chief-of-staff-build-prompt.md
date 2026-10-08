# Claude Code Prompt: Build the Chief of Staff (Orchestrator)

Paste everything below the line into Claude Code, run from the repo root.

---

You are building the **Chief of Staff**, the orchestrator for Joaquin Garcia's AI agent team. Follow the 3-layer architecture in `AGENTS.md`: directive (SOP), orchestration (the Chief of Staff), execution (deterministic Python). Do not create or overwrite any existing directive, SOP or config file without asking. New files are fine; edits to existing files are limited to the ones listed under "Allowed edits".

## 0. Read first (in this order)
`AGENTS.md`, `config/authority.md`, `config/business.md`, `config/sales.md`, `config/footer.md`, `runbook/RUNBOOK.md`, every file in `.claude/agents/` and `sops/`, `logs/shadow-log.csv`, and one folder under `outputs/shadow/` to see how drafts are laid out. Match their tone, density and file conventions.

## 1. What the Chief of Staff is
The single point of coordination across Joaquin's ventures. It receives a request (from Joaquin, or a handoff from an agent), decides which specialist owns it, hands it over with the right inputs, tracks it to done, and reports back. It does not do the specialists' work itself.

**Ventures it covers**
1. **The AI Agency Blueprint** (Apollo outreach and sales pipeline). Fully configured in this repo.
2. **S.E.T. Agent Vault**
3. **Pathfinder**
4. **NJ EDA Grant work**

Only venture 1 has config, SOPs and agents today. For ventures 2-4, do NOT invent facts, goals, deadlines, people or agents. Create `config/ventures.md` with a section per venture (purpose, owner, status, active agents, key files, deadlines) and fill unknown fields with `[PENDING: <field>, Joaquin]`. Then list in your final report every PENDING field so Joaquin can fill them.

**Current team it routes to** (verify against `.claude/agents/`, do not trust this list over the files)
- Aaron: lead sourcing, scoring, send list, weekly review, pre-call briefs
- Cody: outreach copy, proposal narrative, polishing email drafts
- Patty: campaign operations, inbox health, replies, dashboard
- Frannie: post-call coaching, objection log, next-step email draft
- Mark: proposal scoping, three options, ROI
- Dolly: visuals (covers, diagrams, one-pagers, social graphics)
- Phase 3 agents (Vicky, Jerry, Maya, Angelina) are not built. The router must recognise that they do not exist and escalate to Joaquin instead of routing to them.

## 2. Naming collision to handle
"Chief of Staff" is already the role-based email signature and display name for outbound mail (`config/business.md`, `config/footer.md`). Do not change that. Name this new orchestrator `chief-of-staff` in files, and keep its internal documentation clear that the orchestrator and the outbound signature are different things. Flag the overlap in your final report.

## 3. Architecture decision (important)
Claude Code subagents cannot spawn other subagents. So the orchestrator must run in the **main session**, not as a subagent. Build it as:
- `.claude/commands/cos.md`: a slash command (`/cos <request>`) that loads the Chief of Staff playbook and runs in the main session, delegating to the existing subagents with the Agent tool.
- `sops/chief-of-staff-sop.md`: the directive layer (see section 5).
- Optionally a short `.claude/agents/chief-of-staff.md` only if you can make it useful as a read-only "triage" subagent that returns a routing plan without delegating. If it adds nothing, skip it and say why.

## 4. Deliverables
1. `sops/chief-of-staff-sop.md`
2. `.claude/commands/cos.md`
3. `config/ventures.md` (as above)
4. `config/routing.md`: the routing table, one row per task type: trigger keywords or conditions, owning agent, required inputs, expected output, handoff target, and whether it needs Joaquin's approval. Cover at minimum: new prospects/lead lists, outreach copy, campaign status and inbox health, replies, call debriefs, proposal scoping, proposal visuals, weekly review, pre-call brief, and "unknown / no owner".
5. `execution/route_request.py`: deterministic keyword and rule based classifier that reads `config/routing.md` and returns JSON `{venture, task_type, owner_agent, confidence, needs_joaquin, reason}`. Low confidence or no match returns `owner_agent: null` and `needs_joaquin: true`. No LLM calls, no network.
6. `execution/team_status.py`: scans `config/authority.md`, `logs/shadow-log.csv` and `outputs/shadow/` and prints a per-agent rollup: phase, status, items logged, approved-with-no-edits rate, critical errors, items awaiting Joaquin. Read-only.
7. `execution/cos_log.py`: appends one row per routed request to `logs/cos-log.csv` (`date,request,venture,task_type,owner_agent,status,needs_joaquin`). Create the header if missing.
8. `runbook/` additions: a "Chief of Staff" section in `runbook/RUNBOOK.md` (see allowed edits).
9. Tests for the three scripts (plain `pytest` or `unittest`, whichever the repo already uses; if none, use `unittest`). Include cases for: ambiguous request, off-phase service request, request for a non-existent Phase 3 agent, request that names the wrong venture.

## 5. Behavior the SOP and `/cos` must encode
**Core loop:** intake > classify (venture + task type, using `route_request.py`) > check authority and phase > delegate to the owning agent with a complete brief > verify the output against that agent's own rules > log > report to Joaquin.

**Daily/weekly duties**
- On request: a brief "state of the team" using `team_status.py`, plus a short list of items awaiting Joaquin's approval, oldest first.
- Surface blockers and stale items (anything awaiting approval for more than 2 business days).
- Keep the venture status in `config/ventures.md` read-only for the orchestrator unless Joaquin asks for an update; propose edits, do not make them silently.

**Hard rules (these are non-negotiable)**
1. **Never flip authority.** Only Joaquin edits `config/authority.md`. The Chief of Staff never edits it and never treats an agent as send-authorized unless the file says so.
2. **Shadow mode is inherited.** The Chief of Staff itself starts in `shadow`. Until Joaquin says otherwise it only produces routing plans, delegation briefs and status reports, written to `outputs/shadow/<YYYY-MM-DD>/chief-of-staff/` and logged in `logs/shadow-log.csv`. No external sends, posts, spend, or Apollo writes that touch prospects. Delegated agents run in their own shadow mode too.
3. **Respect phase gating.** Check `config/business.md` for the current phase. Off-phase service requests are escalated to Joaquin, not routed.
4. **Never invent.** No fabricated facts, results, clients, deadlines, grant details or agent capabilities. Unknown means `[PENDING: ..., Joaquin]` or a question to Joaquin.
5. **No cross-venture leakage.** Data, contacts and drafts for one venture never flow into another venture's outputs. Each delegation brief names exactly one venture.
6. **Do the minimum routing.** If one agent can own it, route to one agent. Chain agents only along the documented handoff contracts in the runbook (Aaron > Cody > Patty; Frannie > Mark > Cody + Dolly).
7. **Escalate immediately** (per the runbook's escalation list) and for: contracts, custom or municipal contracts, discount requests, anything outside the service menu, any grant submission or funder-facing document, any critical error by an agent.
8. **Grant work (NJ EDA):** treat everything funder-facing as draft-only and Joaquin-approved. Never state eligibility, award amounts, deadlines or program rules unless sourced from a document Joaquin provided or a cited official page; otherwise PENDING.
9. **Every output ends with Sources / Assumptions,** and questions to Joaquin as bullets.
10. **Self-anneal.** When routing fails or an agent's output is rejected, record the cause in the SOP's "Learnings" section and propose a routing-table change instead of silently patching.

**Delegation brief template** (put in the SOP): venture, task, owning agent, inputs with file paths or Apollo IDs, constraints (phase, shadow, price/discount rules), expected output path, deadline, who approves.

## 6. Allowed edits to existing files
- `runbook/RUNBOOK.md`: append a "Chief of Staff" section and add the new orchestration flow. Do not rewrite existing sections.
- `config/authority.md`: **do not edit.** Instead, put a proposed Status-table row for the Chief of Staff (Phase 0 or "orchestrator", status `shadow`, send-authorized NO) in your final report for Joaquin to add himself.
- `.gitignore`: add `logs/cos-log.csv` only if the repo already ignores comparable logs; otherwise leave it.

## 7. Verify before you finish
- Run `python execution/brand_scrub.py` and require zero hits.
- Run the new tests and show passing output.
- Dry-run `/cos` logic by running `route_request.py` on at least these eight requests and showing the JSON: "find 50 NJ city clerks", "write the follow-up email for the Hamilton call", "are our inboxes healthy", "scope a proposal for the Trenton call", "make a one-pager for the audit", "draft the NJ EDA grant narrative", "update the Pathfinder roadmap", "pitch document intake to a prospect" (must be escalated as off-phase).
- Confirm nothing was written to `config/authority.md`.

## 8. Final report format
Short. List: files created, files edited, test and scrub results, the eight routing dry-run outputs, every `[PENDING]` field Joaquin must fill, the naming-collision note, and the proposed authority row. Do not commit or open a PR unless Joaquin asks.
