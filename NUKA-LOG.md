# NUKA-LOG: MEP Protocol Development

**Status:** ACTIVE
**Authorship Lead:** Pierre Hulsebus
**Core Objective:** Establish local-first, zero-infrastructure state relay for AI agents across machines.
**License:** Apache-2.0 | Copyright 2026 Pierre Hulsebus / NukaSoft.AI

> This file is the Paper Trail of Sovereignty. By maintaining it, Pierre documents that he is the Architect and Claude is the Builder. In the 2026 legal landscape, this is the difference between owning your IP and having it declared public domain due to lack of human authorship.

---

## Log Entry 005
**Date:** 2026-04-15
**Sprint:** Public Relay Automation + Exploration Record

### Strategic Intent (Pierre)
Pierre identified that `NukaSoft/mep-protocol` was 11 days stale and looked like a graveyard to outside contributors.  Two problems: (1) no automated pipeline keeping the public repo in sync with the private working tree, and (2) a large body of exploration work | rejected transports, shelved ideas, active concepts | that existed only in session conversations and had never been committed to the record.

Pierre directed two tracks simultaneously:
1. Build a sync pipeline that keeps the public repo current on a 3-hour cadence without Pierre touching it.
2. Commit the exploration history to an `explorations/` directory so the public record reflects the actual design process, not just the final spec.

Pierre also directed that a new AP be created to own this pipeline | naming her Uhura (Lt. Nyota Uhura, ST:TOS) because the role maps exactly to a communications officer holding an open channel between the private bridge and the outside world.

### Technical Steerage
- Pierre directed Option A: auto-commit + push directly to the public repo on each sync.  No PR gate.  The public repo is a downstream mirror, not a collaborative review surface.
- Pierre set the cadence: every 3 hours.  Persistent across reboot.
- Pierre directed that sanitization be enforced at the transport layer, not at authoring time.  Any file with `visibility: private` in frontmatter never leaves the private repo.  Any block marked `<!-- private -->` is stripped before publish.  The spec author should not have to think about what is safe to write | the relay handles it.
- Pierre directed the `explorations/` directory to capture five explorations documented from session memory: S3/Redshift hosted relay (rejected), SMB/UMB file locking (rejected), Bluesky AT Proto transport (shelved), Hello Protocol (active), Google Drive shared surface (adopted as v2.1).

### Machine Execution (Claude)
- Created `scripts/mep-sync.sh` | shell script that mirrors `docs/mep-project/` to public repo root and publishes `memory/learnings/*.md` to `understandings/` with sanitization and auto-generated public INDEX.
- Created `scripts/mep-sync.service` + `scripts/mep-sync.timer` | systemd user units, 3-hour cadence, persistent.
- Created `skills/uhura/` | SKILL.md, bio.yml, README.md.  Symlinked to `~/.claude/skills/uhura`.  Registered in CLAUDE.md.
- Created `site/_crew/uhura.md` | crew page with full character context.
- Executed first live sync | commit `0475b25` on `NukaSoft/mep-protocol`.  17 files, 2689 insertions.  Nine Understandings published.  Zero private leaks.
- Installed and enabled systemd timer | confirmed active via `systemctl --user list-timers`.
- Wrote five `explorations/` files from session memory.
- Queued Rita crew-spotlight post onboarding Uhura to `content-queue/2026-04-15/` for `/review`.

### Why This Matters
MEP is a protocol about eliminating meat-puppet labor from AI session management.  Maintaining the public repo manually is exactly the kind of meat-puppet labor MEP is supposed to eliminate.  Uhura applies the protocol's own principle to the protocol's own maintenance.  The public repo is now a living relay, not a periodic manual dump.

The `explorations/` directory matters for a different reason.  A serious protocol is built through elimination.  Anyone evaluating MEP for adoption wants to know what was tried and rejected, not just what survived.  Showing the rejected paths signals rigor.  Hiding them signals that the final answer appeared from nowhere, which is not credible.

---

## Log Entry 001
**Date:** Pre-2026-03-22 (development) | Published: 2026-03-22
**Sprint:** Transport Layer Experiments & Protocol Architecture

### Strategic Intent (Pierre)
Eliminate myself as the manual context relay between AI sessions. I was re-explaining context every time I switched machines â€” Mac to Hot Rod and back. The cost was 5â€“15 minutes per switch, and it was entirely unnecessary. The goal: open a session on any machine and pick up exactly where the last one left off. Zero re-explanation. Zero meat puppet.

### Technical Steerage â€” Transport Layer Experiments
I directed empirical evaluation of multiple transport candidates before settling on Git. This was not a philosophical choice. We ran the experiments.

| Transport | Tested | Result | My Decision |
|-----------|--------|--------|-------------|
| Local SAN files | Yes | Machine-local only; broke multi-machine goal | Rejected |
| Google Doc | Yes | No version history; merge conflicts unresolvable by agent | Rejected |
| iCloud | Yes | Unstructured; unpredictable sync timing; no diff capability | Rejected |
| OneDrive | Yes | Same problems as iCloud â€” no structure, no diff | Rejected |
| Shared Git + SMB/UMB file share | Yes | Worked but failed intermittently â€” file locking (see Log 001b) | Rejected |
| **Git (GitHub)** | **Yes** | **Versioned, diffable, encrypted in transit, 2FA, audit log, conflict resolution built in** | **Selected** |

Key finding: the transport layer must support **structured diffing**. Unstructured transports fail because the agent cannot reason about merge conflicts autonomously. Git won because structure enables autonomous reasoning.

### Additional Steerage
- I named the protocol "Meat Puppet Elimination" on March 22, 2026 â€” my 62nd birthday
- I chose markdown over JSON for the baton: human-readable, diffable, autonomously mergeable
- I established the format-agnostic principle: any human-readable text two machines can exchange is a valid transport (MD, TXT, HTML, email body, Apple Reminders). Markdown is the reference implementation format because it is the best native option â€” not because the protocol requires it.
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
The file locking failure *validated* Git's design choice. Git doesn't lock files â€” it versions them and resolves conflicts post-hoc. This is the correct primitive for stateless agent handoffs where sessions don't overlap.

### Machine Execution (Claude)
- Documented the SMB/UMB file locking problem
- Confirmed no OS-level workaround available
- Validated Git as the correct transport layer

---

## Log Entry 001c
**Date:** Pre-2026-03-22
**Sprint:** Final Architecture â€” EOL Pattern

### Strategic Intent (Pierre)
After the file locking dead end, I identified the OG EOL pattern as the right model. "That's how the original guys did it" â€” end-of-session scripts that automatically commit the state and close. I directed adoption of this pattern.

### Technical Steerage
- EOL keyword triggers: automatic handoff update + commit + push to repo
- GitHub becomes the transport layer â€” not as a file share, but as a managed infrastructure service:
  - Encryption at rest: built in, zero management
  - 2FA and access control: built in
  - Audit log: built in (every commit is timestamped, attributed)
  - Conflict resolution: built in (Git merge semantics)
- My framing: "Do Nothing in Action" â€” enterprise-grade security requirements met by using infrastructure that already exists in every dev workflow

### Machine Execution (Claude)
- Implemented EOL trigger keywords in CLAUDE.md
- Built EOL sequence: update handoff.md â†’ append daily journal â†’ git commit â†’ push â†’ "End of Line."
- GitHub encryption at rest satisfies enterprise data-at-rest requirements with zero additional overhead

---

## Log Entry 002
**Date:** 2026-04-03
**Sprint:** First Autonomous CI Recovery

### Strategic Intent (Pierre)
I directed Claude to document the autonomous PR conflict resolution event as a formal protocol milestone â€” not just a git incident. I identified that the failure-recovery arc was the missing piece: the initial failure, the self-diagnosis, and the autonomous retry.

### Technical Steerage
- Pierre confirmed: the initial failure is what makes this significant. A clean resolution would be routine. A failure, self-diagnosis, and autonomous fix is the milestone.
- Pierre directed: update mep-protocol.md to include the full failure-recovery arc, not just the successful outcome

### Machine Execution (Claude)
- PR #12 (`Nagatha/dreamy-lamarr`) had a merge conflict in `machines/handoff.md`
- Main branch was 15 commits ahead (Apr 01â€“02 Hot Rod sessions)
- Initial EOL sequence failed â€” conflict blocked the push
- On retry (no human intervention): re-read handoff.md from scratch, identified the newest-first structural rule from existing entries, diagnosed the positioning error, wrote the correct resolution, rebased onto main, force-pushed
- EOL sequence completed autonomously
- Updated mep-protocol.md with First Autonomous CI Recovery milestone section

### Why This Matters
MEP was designed to eliminate the human from the context relay loop. This event proves it can close the CI feedback loop too. The handoff file's structure â€” chronological, newest-first, three named sections â€” is what made autonomous diagnosis possible. The agent could reason about "correct" without being told what correct meant.

---

## Log Entry 003
**Date:** 2026-04-03
**Sprint:** Formalization & GTM

### Strategic Intent (Pierre)
Directed formalization of MEP as a standalone publishable protocol. Two tracks:
1. `NukaSoft/mep-protocol` â€” AGPL-3.0, full sovereignty, NukaSoft brand, NUKA-LOG IP protection
2. PR to `anthropics/claude-code` â€” MIT, community contribution, designed for broad adoption

Commercial goal: if Anthropic accepts the PR, that is official validation + permanent attribution + exposure to every Claude Code user. Enterprise value proposition: GitHub as transport = enterprise-grade security (encryption at rest, 2FA, audit log) with zero management overhead.

Pierre directed: capture every use instance, every log, every PR. Build the evidence base for enterprise sales.

### Technical Steerage
- Pierre confirmed: AGPL-3.0 over MIT. Forces enterprise derivatives open.
- Pierre confirmed: Markdown as native baton format, but document format-agnostic principle explicitly
- Pierre confirmed: NUKA-LOG accuracy over template convenience. Courts care about accurate records.
- Pierre identified the commercial headline: "Do Nothing" security â€” hardest enterprise requirement, zero overhead

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
- The conflict was in `machines/handoff.md` â€” the core MEP baton file
- The worktree session (Apr 5 DNS work) wrote a new handoff entry, while main's nightly automation added content-queue files. Both modified the same file from different starting points.
- Pierre directed: document in NUKA-LOG as evidence of MEP operating under real multi-session workload

### Machine Execution (Claude)
- Worktree branch `Nagatha/brave-mahavira` diverged from main at `de18397`
- Main received `2a975da` (nightly content automation) while branch received `92f6116` (DNS session EOL)
- Initial push from worktree encountered conflict in `machines/handoff.md`
- Resolution: commit `ae0c6bd` replaced the old Apr 3 handoff with the current Apr 5 DNS session entry, preserving the newest-first ordering rule from the handoff schema
- Merge back to main completed cleanly via `git merge Nagatha/brave-mahavira`

### Observations
1. **Nightly automation is a conflict vector.** Any timer-driven commit (nightly content, captain's log) can create divergence if a worktree session is active. This is not a bug â€” it's the expected operating mode. MEP's newest-first ordering and structured sections enable clean resolution.
2. **Worktree branches are MEP's multi-session primitive.** Claude Code worktrees (`--isolation worktree`) create branches automatically. When these branches write to handoff.md, they create divergence that must be merged. The protocol handles this because the handoff schema is designed for it.
3. **Second confirmed autonomous resolution.** Entry 002 was the first. This is the second. The pattern is consistent: read the file, identify the newest entry by date, position correctly, merge.

<!-- sync:2026-09-03T03:10:04-04:00 | Uhura | 13 understandings published -->
