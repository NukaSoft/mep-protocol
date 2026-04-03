# MEP Handoff Schema — Formal Specification

**Version:** 1.0
**Date:** 2026-03-22
**License:** AGPL-3.0-or-later — Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI

---

## Overview

The handoff file (baton) is the core state artifact of the MEP Protocol. It is a structured markdown document that carries curated context between AI sessions. This document defines the formal grammar, field semantics, and conformance requirements.

---

## BNF Grammar

```
handoff-file    ::= file-header newline entry+

file-header     ::= "# Handoff Log" newline description-line

entry           ::= date-header newline section-happened newline section-pending newline section-watchout?

date-header     ::= "## " ISO-DATE " — " machine-context

ISO-DATE        ::= YYYY "-" MM "-" DD

machine-context ::= machine-name (" (" branch-or-context ")")?

section-happened  ::= "### What happened" newline bullet+
section-pending   ::= "### What's pending" newline (task-item | bullet)+
section-watchout  ::= "### Watch out for" newline bullet+

task-item       ::= "- [ ] " text newline
bullet          ::= "- " text newline

newline         ::= "\n"
```

---

## Ordering Rule

**Entries MUST be ordered newest-first.** The most recent entry appears at the top of the file. This is not a convention — it is a protocol requirement. The autonomous conflict resolution capability of MEP depends on this ordering being machine-parseable.

```
## 2026-04-03 — Hot Rod (main)        ← newest, read first
...

## 2026-04-02 — Hot Rod (main)        ← previous
...

## 2026-04-01 — Mac (Nagatha/worktree) ← oldest in window
...
```

---

## Field Semantics

### `### What happened`
**Required.** A concise record of actions taken this session. Bullet list. Not prose. Focus on deliverables and decisions — not process.

Good:
```
- Built `/iterate` skill — 7-stage loop, Run Sheet template, symlinked
- Resolved merge conflict in handoff.md — PR #12 rebased and pushed
```

Bad:
```
- I started the session and read the handoff file
- Then I thought about what to do
```

### `### What's pending`
**Required.** Tasks and open items for the next session. Use checkbox format for actionable items. Scope-tag tasks by owner if multiple agents or humans are involved.

```
- [ ] **[Pierre]** Post Reddit drafts — 5 posts ready
- [ ] **[Skippy]** Wire Piper PR monitor
- [ ] Fix Pip-Boy frame consistency
```

### `### Watch out for`
**Optional.** Traps, blockers, stale state, known issues. Things the next session should check before assuming a clean environment.

```
- `~/.leo/` still exists as backup — can delete once confirmed
- Google Tasks MCP auth broken — needs `node auth.js`
```

---

## Transport Layer Requirements

The handoff file must be exchanged via a transport that satisfies:

1. **Structured diff support** — The transport must allow the receiving agent to compare versions and identify which entry is newer. Git satisfies this natively.
2. **Conflict resolution** — The transport must support merging divergent versions without data loss. Git satisfies this via rebase/merge semantics.
3. **Encryption in transit** — Required for enterprise deployments. Git over SSH or HTTPS satisfies this.
4. **No mandatory locking** — The transport must not use file locking. SMB/UMB file shares fail this requirement due to non-deterministic lock behavior under concurrent AI agent access.

### Conformant Transports
| Transport | Diff | Conflict Resolution | Encryption | No Lock | Conformant |
|-----------|------|--------------------|---------|---------|----|
| Git (GitHub/GitLab) | ✅ | ✅ | ✅ | ✅ | **YES** |
| Git (self-hosted) | ✅ | ✅ | ✅ (SSH) | ✅ | **YES** |
| SFTP + manual merge | ✅ | Manual | ✅ | ✅ | Partial |
| SMB/UMB file share | ❌ | ❌ | Optional | ❌ | **NO** |
| iCloud Drive | ❌ | ❌ | ✅ | ❌ | **NO** |
| OneDrive | ❌ | ❌ | ✅ | ❌ | **NO** |
| Google Docs | ❌ | ❌ | ✅ | ❌ | **NO** |

---

## Format Agnosticism

The handoff file MUST be human-readable text. Markdown is the reference implementation format and is strongly recommended. However, the protocol does not require Markdown specifically. Any format that satisfies:

- Human-readable (plaintext)
- Structured (sections are machine-identifiable)
- Diffable (line-based)

...is a valid baton format. TXT with consistent headers, HTML with `<section>` tags, or structured email bodies have all been validated as transport-compatible formats in MEP's development history.

The key requirement is structure. Unstructured text cannot be autonomously merged.

---

## Conformance Test

A conformant handoff file passes all of the following checks:

1. File is valid UTF-8 plaintext
2. First entry's date is the most recent date in the file
3. Every entry contains at minimum `### What happened` and `### What's pending` sections
4. No entry is missing a `## YYYY-MM-DD` date header
5. Task items under `### What's pending` use `- [ ]` checkbox format

A conformant MEP implementation passes the autonomous merge test:

> Given two divergent versions of a handoff file (branch A and branch B), the agent can resolve the merge correctly — placing the newer entry on top — without human instruction, using only the structure of the existing entries as a guide.

This was first demonstrated on April 3, 2026 (PR #12).
