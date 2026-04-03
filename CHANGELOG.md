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
