---
status: rejected
date: 2026-03
proposed_by: Pierre
outcome: Non-deterministic file locking under concurrent agent access. No OS-level workaround. Killed at the design stage and validated by empirical failure.
---

# Exploration: SMB/UMB File Shares as Transport Layer

## The Idea

Use a shared file system (SMB for Windows/Mac, UMB for Linux) as the baton transport instead of Git.  The appeal: lower latency, simpler tooling, no commit overhead.  The baton is just a file.  Any machine that can mount the share can read and write it.

Pierre had a NAS (Synology) already on the network.  Hot Rod and the Mac could both mount it.  The infrastructure was sitting there.

## What We Tested

We ran the shared Git repo + SMB/UMB hybrid pattern for a period before settling on Git-only.

The setup: baton file lived on the NAS share.  Both machines mounted it via SMB.  Agents read and wrote directly.  No commits, no push, just file I/O.

## What We Found

**It mostly worked.**  Under normal single-agent serial access | one session ends, one begins | the pattern was reliable.  Fast reads, no merge overhead.

**It failed intermittently under concurrent access.**

The failure mode: two processes attempting to write the baton file at the same time.  In a fully manual workflow, this barely happens.  But MEP includes timer-driven automation | nightly content jobs, the captain's log, the sync scripts.  These create concurrent write windows.

When concurrency hit, behavior was non-deterministic:
- SMB file locking is advisory, not mandatory, on most Linux implementations.  Agents that did not explicitly call `flock()` before writing could collide.
- Even with explicit locking, lock acquisition failure behavior depends on the SMB server implementation and the mount options.  Synology's SMB server does not guarantee POSIX lock semantics over the network.
- The result: partial writes, corrupted baton content, silent failures where the write appeared to succeed but the file was in an inconsistent state.

Pierre filed a PR against Claude on the SMB vs UMB file locking problem.  The finding: no OS-level workaround exists.  File locking at the network boundary is a known unsolved problem in distributed systems.  NFS has the same issue.  Windows SMB oplocks add another layer of complexity.

## Decision

Rejected.  No workaround.

The failure is architectural, not implementational.  You cannot fix non-deterministic network file locking by being more careful.  The transport model is wrong.

**The failure validated Git's design choice.**  Git does not use file locking.  It versions files and resolves conflicts post-hoc.  This is the correct primitive for stateless agent handoffs where you cannot guarantee that sessions do not overlap.  Git's conflict resolution semantics are deterministic | the protocol can reason about them.  SMB locking semantics are not.

## Key Insight

The MEP requirement is not "fast writes."  It is "reliable state handoff under conditions where write timing is non-deterministic."  That is a different requirement, and it points to a different architecture.

Git was the answer not because it is fast but because its consistency model is correct.  Two concurrent commits produce a detectable, resolvable conflict.  Two concurrent SMB writes produce silent corruption.

Silence is worse than noise.

## See Also

- `NUKA-LOG.md` | Log Entry 001b | original field notes from this failure
- `spec/mep-protocol.md` | Validated Transports section | formal rejection recorded
