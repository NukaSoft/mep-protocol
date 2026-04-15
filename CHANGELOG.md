# MEP Protocol — Changelog

All notable changes to the MEP Protocol are documented here.

Format: `## [version] — YYYY-MM-DD`

---

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
