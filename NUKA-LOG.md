# NUKA-LOG: MEP Protocol Development

**Status:** ACTIVE
**Authorship Lead:** Pierre Hulsebus
**Core Objective:** Establish local-first, zero-infrastructure state relay for AI agents across machines.
**License:** AGPL-3.0-or-later

> This file is the Paper Trail of Sovereignty. By maintaining it, Pierre documents that he is the Architect and Claude is the Builder. In the 2026 legal landscape, this is the difference between owning your IP and having it declared public domain due to lack of human authorship.

---

## Log Entry 001
**Date:** Pre-2026-03-22 (development) | Published: 2026-03-22
**Sprint:** Transport Layer Experiments & Protocol Architecture

### Strategic Intent (Pierre)
Eliminate myself as the manual context relay between AI sessions. I was re-explaining context every time I switched machines — Mac to Hot Rod and back. The cost was 5–15 minutes per switch, and it was entirely unnecessary. The goal: open a session on any machine and pick up exactly where the last one left off. Zero re-explanation. Zero meat puppet.

### Technical Steerage — Transport Layer Experiments
I directed empirical evaluation of multiple transport candidates before settling on Git. This was not a philosophical choice. We ran the experiments.

| Transport | Tested | Result | My Decision |
|-----------|--------|--------|-------------|
| Local SAN files | Yes | Machine-local only; broke multi-machine goal | Rejected |
| Google Doc | Yes | No version history; merge conflicts unresolvable by agent | Rejected |
| iCloud | Yes | Unstructured; unpredictable sync timing; no diff capability | Rejected |
| OneDrive | Yes | Same problems as iCloud — no structure, no diff | Rejected |
| Shared Git + SMB/UMB file share | Yes | Worked but failed intermittently — file locking (see Log 001b) | Rejected |
| **Git (GitHub)** | **Yes** | **Versioned, diffable, encrypted in transit, 2FA, audit log, conflict resolution built in** | **Selected** |

Key finding: the transport layer must support **structured diffing**. Unstructured transports fail because the agent cannot reason about merge conflicts autonomously. Git won because structure enables autonomous reasoning.

### Additional Steerage
- I named the protocol "Meat Puppet Elimination" on March 22, 2026 — my 62nd birthday
- I chose markdown over JSON for the baton: human-readable, diffable, autonomously mergeable
- I established the format-agnostic principle: any human-readable text two machines can exchange is a valid transport (MD, TXT, HTML, email body, Apple Reminders). Markdown is the reference implementation format because it is the best native option — not because the protocol requires it.
- I directed the EOL keyword system: `/eol`, `p-out`, `ppp` trigger automatic commit and push

### Machine Execution (Claude)
- Drafted initial session protocol in CLAUDE.md
- Implemented handoff.md schema (three sections: what happened, pending, watch out)
- Established EOL trigger keywords and shutdown sequence
- Drafted first version of mep-protocol.md documentation

---

## Log Entry 001b
**Date:** Pre-2026-03-22
**Sprint:** File Locking Dead End

### Strategic Intent (Pierre)
After initial Git latency concerns, I directed exploration of shared file systems as a potentially lower-latency transport alternative.

### Technical Steerage
- Tested shared Git repo + SMB/UMB file share hybrid
- Worked under normal conditions but failed intermittently under concurrent agent access
- Filed a PR with Claude on the SMB vs UMB file locking problem
- Discovery: no workaround exists. File locking at the OS level is non-deterministic under concurrent AI agent access. This is a known unsolved problem in distributed systems.
- My decision: abandon shared file system entirely. Return to Git as sole transport.

### Key Insight
The file locking failure *validated* Git's design choice. Git doesn't lock files — it versions them and resolves conflicts post-hoc. This is the correct primitive for stateless agent handoffs where sessions don't overlap.

### Machine Execution (Claude)
- Documented the SMB/UMB file locking problem
- Confirmed no OS-level workaround available
- Validated Git as the correct transport layer

---

## Log Entry 001c
**Date:** Pre-2026-03-22
**Sprint:** Final Architecture — EOL Pattern

### Strategic Intent (Pierre)
After the file locking dead end, I identified the OG EOL pattern as the right model. "That's how the original guys did it" — end-of-session scripts that automatically commit the state and close. I directed adoption of this pattern.

### Technical Steerage
- EOL keyword triggers: automatic handoff update + commit + push to repo
- GitHub becomes the transport layer — not as a file share, but as a managed infrastructure service:
  - Encryption at rest: built in, zero management
  - 2FA and access control: built in
  - Audit log: built in (every commit is timestamped, attributed)
  - Conflict resolution: built in (Git merge semantics)
- My framing: "Do Nothing in Action" — enterprise-grade security requirements met by using infrastructure that already exists in every dev workflow

### Machine Execution (Claude)
- Implemented EOL trigger keywords in CLAUDE.md
- Built EOL sequence: update handoff.md → append daily journal → git commit → push → "End of Line."
- GitHub encryption at rest satisfies enterprise data-at-rest requirements with zero additional overhead

---

## Log Entry 002
**Date:** 2026-04-03
**Sprint:** First Autonomous CI Recovery

### Strategic Intent (Pierre)
I directed Claude to document the autonomous PR conflict resolution event as a formal protocol milestone — not just a git incident. I identified that the failure-recovery arc was the missing piece: the initial failure, the self-diagnosis, and the autonomous retry.

### Technical Steerage
- Pierre confirmed: the initial failure is what makes this significant. A clean resolution would be routine. A failure, self-diagnosis, and autonomous fix is the milestone.
- Pierre directed: update mep-protocol.md to include the full failure-recovery arc, not just the successful outcome

### Machine Execution (Claude)
- PR #12 (`Nagatha/dreamy-lamarr`) had a merge conflict in `machines/handoff.md`
- Main branch was 15 commits ahead (Apr 01–02 Hot Rod sessions)
- Initial EOL sequence failed — conflict blocked the push
- On retry (no human intervention): re-read handoff.md from scratch, identified the newest-first structural rule from existing entries, diagnosed the positioning error, wrote the correct resolution, rebased onto main, force-pushed
- EOL sequence completed autonomously
- Updated mep-protocol.md with First Autonomous CI Recovery milestone section

### Why This Matters
MEP was designed to eliminate the human from the context relay loop. This event proves it can close the CI feedback loop too. The handoff file's structure — chronological, newest-first, three named sections — is what made autonomous diagnosis possible. The agent could reason about "correct" without being told what correct meant.

---

## Log Entry 003
**Date:** 2026-04-03
**Sprint:** Formalization & GTM

### Strategic Intent (Pierre)
Directed formalization of MEP as a standalone publishable protocol. Two tracks:
1. `NukaSoft/mep-protocol` — AGPL-3.0, full sovereignty, NukaSoft brand, NUKA-LOG IP protection
2. PR to `anthropics/claude-code` — MIT, community contribution, designed for broad adoption

Commercial goal: if Anthropic accepts the PR, that is official validation + permanent attribution + exposure to every Claude Code user. Enterprise value proposition: GitHub as transport = enterprise-grade security (encryption at rest, 2FA, audit log) with zero management overhead.

Pierre directed: capture every use instance, every log, every PR. Build the evidence base for enterprise sales.

### Technical Steerage
- Pierre confirmed: AGPL-3.0 over MIT. Forces enterprise derivatives open.
- Pierre confirmed: Markdown as native baton format, but document format-agnostic principle explicitly
- Pierre confirmed: NUKA-LOG accuracy over template convenience. Courts care about accurate records.
- Pierre identified the commercial headline: "Do Nothing" security — hardest enterprise requirement, zero overhead

### Machine Execution (Claude)
- Created `NukaSoft/mep-protocol` GitHub repo
- Built complete repo structure: spec/, templates/, skills/, examples/
- Wrote NUKA-LOG.md (this file) with accurate 4-entry history
- Wrote LICENSE (AGPL-3.0 + NukaSoft header)
- Wrote formal spec, handoff schema, MEP_RELAY skill, templates, README, CONTRIBUTING
- Opened PR against anthropics/claude-code
- Wired Piper to monitor PR status

---

## Log Entry 004
**Date:** 2026-04-05
**Sprint:** Worktree Conflict Resolution & Multi-Session Divergence

### Strategic Intent (Pierre)
Identified a handoff conflict that occurred when a Mac worktree session (DNS infrastructure, `Nagatha/brave-mahavira`) diverged from main while nightly content automation committed to main (`2a975da`). Pierre directed documentation of the conflict resolution pattern as a MEP protocol data point.

### Technical Steerage
- Pierre identified this as a variant of the Entry 002 pattern: worktree branches create divergence by design, and MEP must handle the merge cleanly
- The conflict was in `machines/handoff.md` — the core MEP baton file
- The worktree session (Apr 5 DNS work) wrote a new handoff entry, while main's nightly automation added content-queue files. Both modified the same file from different starting points.
- Pierre directed: document in NUKA-LOG as evidence of MEP operating under real multi-session workload

### Machine Execution (Claude)
- Worktree branch `Nagatha/brave-mahavira` diverged from main at `de18397`
- Main received `2a975da` (nightly content automation) while branch received `92f6116` (DNS session EOL)
- Initial push from worktree encountered conflict in `machines/handoff.md`
- Resolution: commit `ae0c6bd` replaced the old Apr 3 handoff with the current Apr 5 DNS session entry, preserving the newest-first ordering rule from the handoff schema
- Merge back to main completed cleanly via `git merge Nagatha/brave-mahavira`

### Observations
1. **Nightly automation is a conflict vector.** Any timer-driven commit (nightly content, captain's log) can create divergence if a worktree session is active. This is not a bug — it's the expected operating mode. MEP's newest-first ordering and structured sections enable clean resolution.
2. **Worktree branches are MEP's multi-session primitive.** Claude Code worktrees (`--isolation worktree`) create branches automatically. When these branches write to handoff.md, they create divergence that must be merged. The protocol handles this because the handoff schema is designed for it.
3. **Second confirmed autonomous resolution.** Entry 002 was the first. This is the second. The pattern is consistent: read the file, identify the newest entry by date, position correctly, merge.
