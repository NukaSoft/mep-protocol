# MEP Protocol — Changelog

All notable changes to the MEP Protocol are documented here.

Format: `## [version] — YYYY-MM-DD`

---

## 2.6 | 2026-08-12

**First-party runtimes. Canonical `MEP.md`. Hello tag-in.**

v2.5 put the session protocol in every identity file and called Cursor a peer. Five loaders will drift. v2.6 puts Hello, EOL, and git posture in one file. Copilot, Codex, and ChatGPT join as first-party participants.

### Added
- `templates/MEP.md` — the only copy of the session protocol
- Thin loaders: `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/mep.mdc`, `.github/copilot-instructions.md`
- Codex skill: `templates/agents-skills/mep-relay/SKILL.md` → `.agents/skills/`
- ChatGPT seed: `templates/openai/SEED_PROMPT.md`
- `examples/first-party/` — Claude, Cursor, Copilot, Codex, ChatGPT
- Hello **writes** `Tag-out: [active]` and pushes if it can; EOL fills that entry in place
- Default baton path: `handoff.md` (legacy alias `machines/handoff.md`)
- `.github/workflows/mep-handoff.yml` — `python3 scripts/check-handoff.py --ci`
- Handoff schema 1.2 (Hello stubs, in-place EOL)

### Changed
- Identity files no longer contain the protocol. They point at `MEP.md`.
- Component 10 renamed/expanded from Cursor+Claude to first-party runtimes
- `examples/cursor-claude/` is a pointer at `examples/first-party/`

### Design Decisions
- GitHub Copilot = Microsoft's first-party coding agent. M365 Copilot is a standup reader (no git).
- OpenAI splits: Codex is a git writer (`AGENTS.md`). ChatGPT without git uses the seed prompt and one paste.
- Grok and Gemini stay spokes until they ship a git-writing coding agent. Then add a loader, do not fork `MEP.md`.

---

## 2.5 | 2026-08-12

**Component 10: Dual-Runtime Peers (Cursor + Claude).**

Claude Code loads `CLAUDE.md`. Cursor does not. A repo that both tools write, with only `CLAUDE.md`, is running MEP on one side of the pair. Cursor is a peer writer (git access), not a spoke (conversation URL).

### Added
- `templates/AGENTS.md` — identity file Cursor and other AGENTS.md loaders actually load
- `templates/cursor-rules/mep.mdc` — always-on Cursor rule so Hello/EOL is injected, not hoped for
- `skills/cursor/mep-relay/SKILL.md` — Cursor port of `/mep start|end|status`
- `examples/cursor-claude/` — worked dual-runtime example
- `scripts/check-handoff.py` — conformance checker (newest-first, required sections, same-day timestamps)
- Spec Component 10 and handoff schema 1.1 (timestamp tie-breaker)

### Changed
- Identity files and skills: Hello is `git fetch` + read baton, not a blind `git pull`
- Conflict recovery: never force-push `main`/`master`; `--force-with-lease` only on a branch this session created
- EOL: the word `done` is not a trigger (false positives in coding sessions)
- Dual-runtime entries use v2 headers with timezones; prefer UTC
- `templates/shared-handoff.md` is a blank template; the filled NukaSoft standup moved to `examples/shared-surface/`
- README version badge tracks the spec (2.5). Leftover AGPL "network service" sentence removed after the 2.4 relicense

### Design Decisions
- Two identity files, one baton. Drift between `CLAUDE.md` and `AGENTS.md` Session Protocol sections is a protocol bug.
- Cursor Cloud PR workflows still write the baton; if they cannot land it on default, they paste the newest entry into the PR body.
- Same-day ordering is load-bearing now that two runtimes routinely share a calendar day.

---

## 2.4 | 2026-08-11

### Relicensed to full open source

AGPL-3.0 replaced by a two license split by artifact type.

- **Code, templates, skills, examples:** Apache License 2.0
- **Specification documents (`spec/`, `LEXICON.md`):** CC BY 4.0

**Why.** AGPL defeated the goal. The templates exist to be copied into other
people's repositories, and under AGPL that arguably relicensed their work, so
the on-ramp to the protocol was a legal hazard. AGPL also permanently blocked
upstream adoption, since permissively licensed projects cannot take it. And its
one real protection, the network service loophole, does not apply to a document
protocol whose transport is git.

A specification is only worth writing if anyone can implement it. Implementing
MEP now requires no permission and imposes no obligation. Attribution is
required only when copying or adapting the documents themselves.

Sole copyright holder, so no contributor consent was required. Verified against
both the private history and the public repository before relicensing.

## [MEEP-ReadOnly-v1] — 2026-04-29

**Read-only peer-agent context surface.**

### Added
- **`spec/meep-readonly-v1.md`** | New sibling spec defining a small, public-but-unlinked Markdown page that external peer agents (Grok, ChatGPT, Gemini) fetch on session start. Unidirectional, agent-scoped, pull-on-demand. Sized to act as effective system-prompt context without blowing token budget.
- **First instance:** Hastings (Leo) at `nukasoft.ai/leo`. Page owner: Rita. Source scaffolded at `site/_pages/leo.md`.
- **Required sections** | Stable Fundamentals, Current Strategic Priorities, Open Questions, Recent Decisions, Active Workstream State, Sync Notes, Changelog.
- **Token budget** | Soft cap ~1,500 words / ~2,000 tokens per page.

### Design Decisions
- **Not a Standing Standup.** The standup (v2.1) is bidirectional and project-scoped. MEEP-ReadOnly-v1 is unidirectional and agent-scoped. Different problem, different primitive.
- **No time-based pruning in v1.** A 48-hour prune was considered and rejected: peer agents that check in weekly would silently lose history they never read. Manual curation by the page owner instead. v2 path is last-read telemetry.
- **No scheduled rebuild timer in v1.** External peer agents do not need 10-minute freshness; the timer adds operational overhead with little signal value. Triggers are manual + a light EOL hook that queues drafts but does not auto-publish.
- **Security via obscurity + content discipline.** `noindex,nofollow`, `robots.txt` disallow, no sitemap entry. Content rule: if a competitor reading this would be a problem, it does not go on the page. Auth tokens are v2 backlog.
- **URL shortener / redirector deferred to v2.** Direct `nukasoft.ai/{agent-name}` is the v1 primitive; an aka.ms-style redirector to an off-repo canonical surface is the expected next step.

---

## [2.2] — 2026-04-15

**Public Relay Automation + Exploration Archive**

### Added
- **`explorations/` directory** | Five documented explorations capturing the design process behind the spec.  What was tried, what was rejected, what is active.  The proof of work.
  - `s3-redshift-hosted-relay.md` | Rejected.  Correct SaaS architecture, wrong for a zero-infrastructure protocol.
  - `smb-umb-file-locking.md` | Rejected.  Non-deterministic file locking validated Git as the only viable transport.
  - `bluesky-atproto-transport.md` | Shelved.  Technically sound for real-time multi-agent coordination.  Revisit when concurrent sessions are a first-class requirement.
  - `hello-protocol.md` | Active.  Formalizing the session startup event as a lifecycle primitive.  Draft spec included.
  - `google-drive-shared-surface.md` | Active (shipped as v2.1 Component 9).  Cross-ecosystem shared handoff via Drive MCP.
- **Uhura | MEP Public Relay AP** | The AP responsible for keeping this public repo in sync with the private working tree.  Named for Lt. Nyota Uhura (ST:TOS, 1966 to 1969).  Skills: `skills/uhura/`.  Cadence: every 3 hours via systemd timer.
- **`understandings/` directory** | Nine inaugural Understandings published from Pierre's private knowledge store.  Aha moments captured in the moment they clicked.  Published via Uhura on every sync.
- **Automated sync pipeline** | `mep-sync.sh` + systemd timer.  The public repo is now a downstream mirror of the private working tree, not a periodic manual dump.  Sanitization enforced at the transport layer.

### Design Decisions
- **Sanitization at transport, not at authoring time.**  Authors mark private content in frontmatter or with `<!-- private -->` blocks.  Uhura enforces the boundary.  Authors should not have to think about what is safe to write.
- **No PR gate on the public mirror.**  The public repo is downstream.  Collaborative review happens in the private repo.  Public surfaces Uhura's curated output.
- **Explorations are first-class documentation.**  A protocol built through elimination should show the eliminated paths.  Hiding dead ends makes the final answer look like it arrived from nowhere.

---

## [2.1] — 2026-04-13

**Outbound Baton + Unified Handoff Schema**

### Added
- **Component 9: Outbound Baton** — Shared handoff file on Google Drive.  All agents (Claude, Grok, ChatGPT, Gemini) read AND append to the same file.  Same handoff schema as v1 — not a new format.
- **Multi-agent tag-in/tag-out** in handoff schema — extended header: `## DATE — Agent | Platform | session-type` + `**Tag-in:** TIME | **Tag-out:** TIME`.  Backward-compatible with v1 headers.
- **Shared surface protocol** — any agent reads on start, appends on end.  One file, many agents, same rules.
- Static context header (who Pierre is, active projects, crew, voice rules) + rolling handoff entries.
- Platform-specific setup for Grok (upload), ChatGPT (project knowledge file), Gemini (native Drive read).
- Complete loop diagram: publish → read → contribute → ingest → update → publish.

### Standing Standup Reframing
- **The shared handoff surface is a "Standing Standup"** — a persistent standup meeting with history and pointers that agents walk into, read, work, and append to.
- **Project-scoped, not universe-scoped.**  Each project gets its own standup.  Eliminates the "Unimind" problem — no master document trying to contain everything.
- Standup contains: project scope, artifacts inventory, pointers (public URLs), party line (active agents), and a standup log (tag-in/tag-out entries).
- Not a briefing doc.  It is a live meeting that never ends.

### Design Decisions
- **One template, not many.**  The handoff schema is the SAME format for machine-to-machine, LLM-to-LLM, and shared surfaces.  Only the header extends.
- Google Drive as shared surface transport.  Claude has MCP write access; other agents need Pierre to copy entries back (until API access available).
- The file is a projection of the repo.  Sanitized of private details.
- Append-only entries prevent conflict.  No agent modifies another's entries.  Newest on top.
- **Standing Standup is always project-scoped.**  Agents only see context for the project they are working on.

---

## [2.0] — 2026-04-13

**Project-Centric Cross-Ecosystem Routing**

### Added
- **MEP v2 design spec** — all cross-ecosystem work converges on Claude projects/skills as the canonical home.  Grok, ChatGPT, Gemini are spokes; Claude is the hub; the repo is the durable layer.
- **Peer projects model** — each skill/project can declare linked sessions on other platforms.  When a peer session produces insights, they route into the skill and enrich it permanently.
- **Project context accumulation** — cross-ecosystem conversations don't just transfer context once; they grow the project.  Every Grok brainstorm, every ChatGPT research session makes the skill smarter for every future session.
- **Routing rules** — 5-step ingestion: identify project → archive conversation → extract insights → route to project → surface in handoff.
- **3-phase implementation plan** — manual archive (now) → auto-routing (next) → bi-directional sync (future).
- **Commercial angle** — MEP v2 as convergence layer for knowledge workers using multiple AI tools.

### Design Decisions
- Claude is the hub, not because of vendor loyalty, but because it has code execution + repo access + durable memory.  The hub must be the LLM that can ACT on insights, not just discuss them.
- Conversations are project contributions, not events.  Archive them, route them, enrich the skill.
- The skill doesn't care which LLM generated the insight.  It cares that the insight exists.

---

## [1.1] — 2026-04-13

**Cross-Ecosystem Context Transfer + Seed Prompt**

### Added
- **Component 7: Cross-Ecosystem Context Transfer** — conversation URLs from Grok, ChatGPT, Gemini, or any LLM become the baton for cross-provider context relay.  Operator pastes URL, receiving agent reads full conversation, continues without re-explanation.  Best-of-breed AI routing without context tax.
- **Component 8: Seed Prompt** — self-contained text block for bootstrapping disconnected sessions (Cowork mode, Claude Desktop, any session without repo access).  One paste, zero questions.  "DO NOT ASK ME ANY QUESTIONS" is a valid protocol instruction.
- Combined flow diagram: Grok (brainstorm) → Claude Mac (cowork) → Claude Hot Rod (code) → Claude Mac (next day).  Context follows the operator across LLMs AND machines.

### Design Decisions
- Conversation URL is transport-agnostic — works regardless of source platform
- Seed prompts are read-and-execute, not read-and-plan
- Cross-ecosystem transfer is ephemeral (platform-hosted); recommend archiving fetched conversations to `memory/conversations/` for permanence
- "Low meat puppet friction" adopted as design standard for all context handoff patterns

### Production Milestones
- **Grok → Claude architecture transfer** (Apr 13): 3-hour Grok session on GBrain/GStack patterns transferred to Claude via URL.  Claude produced 172-line journal, Captain's Log PDF, and forward objectives.  Zero re-explanation.
- **Skool cowork seed prompt** (Apr 13): New Claude Desktop session bootstrapped with paste-and-go seed prompt.  No clarifying questions.  Immediate productive work.

---

## [1.0.1] — 2026-04-03

**Milestone: First Autonomous CI Recovery**

### Proven
- MEP closes the CI feedback loop, not just the context relay loop
- Agent autonomously resolved a merge conflict in `handoff.md` (PR #12) after initial EOL failure
- No human intervention. Failure self-diagnosed. Fix self-applied. Session completed.

### Added to Spec
- Conflict recovery procedure documented in `skills/MEP_RELAY.md`
- Conformance test: autonomous merge test added to `spec/handoff-schema.md`
- Key insight recorded: structured state files (not free-form) enable autonomous reasoning

### Formalization
- `NukaSoft/mep-protocol` standalone repo created
- AGPL-3.0 license applied
- `NUKA-LOG.md` authorship audit trail established
- Formal BNF grammar for handoff file schema
- `MEP_RELAY.md` skill for Claude Code
- PR opened to `anthropics/claude-code` examples

## [1.0] — 2026-03-22

**Initial release.**

### Added
- Session protocol: identity file (`CLAUDE.md`) with mandatory start/end sequences
- Handoff file schema: three-section structure (what happened / pending / watch out for), newest-first ordering
- EOL trigger keywords: `/eol`, `p-out`, `ppp`, and natural language phrases
- Git as reference transport layer — encryption at rest, 2FA, conflict resolution built in
- Self-enforcement mechanism: agent reads own protocol from identity file

### Design Decisions
- Markdown chosen as reference baton format: diffable, autonomously mergeable, no tooling required
- Format-agnostic by design: any structured human-readable text is a valid baton
- No new infrastructure: Git, markdown, SSH — all pre-existing in any dev workflow

### Validated Transports
- Git (GitHub/GitLab): conformant ✅
- SMB/UMB file shares: rejected — non-deterministic file locking ❌
- iCloud, OneDrive, Google Docs: rejected — no structured diff support ❌

---
