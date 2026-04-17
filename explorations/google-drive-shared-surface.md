---
status: active
date: 2026-04-13
proposed_by: Pierre
outcome: Adopted as MEP v2.1 Component 9 (Outbound Baton). Operationally live.
---

# Exploration: Google Drive as Cross-Ecosystem Shared Surface

## The Idea

The original MEP baton travels via Git | private repo, Hot Rod as the source of truth, Mac clones and pulls.  This works perfectly for Claude-to-Claude handoffs on machines Pierre controls.

But Pierre uses multiple AI platforms.  Grok for brainstorming.  ChatGPT for certain research tasks.  Gemini for Drive-native work.  The Git baton is invisible to all of them | they cannot clone a private repo.

The proposal: a parallel surface on Google Drive.  A single shared handoff file that any agent | Claude, Grok, ChatGPT, Gemini | can read and append to.  Same handoff schema.  Sanitized of private details.  Live.

## What "Cross-Ecosystem" Means in Practice

The problem Pierre was solving is concrete:

1. He does a 3-hour brainstorm with Grok on a new architecture.
2. He wants Claude to pick up that context and act on it.
3. Grok cannot push to GitHub.  Claude cannot read Grok's conversation history natively.

Without this, Pierre re-explains 3 hours of work to Claude.  That is the meat puppet problem showing up in a cross-ecosystem context.

The solution: Grok appends its session summary to the shared Drive file.  Claude reads the Drive file at session start.  No re-explanation.

## How It Works (v2.1 Implementation)

**File location:** Google Drive, shared with Claude via Google Drive MCP.

**Format:** Same MEP handoff schema, extended header:

```
## 2026-04-13 — Grok | xAI | brainstorm
**Tag-in:** 10:00 | **Tag-out:** 13:00

### What Happened
...

### Pending
...

### Watch Out For
...
```

**Write access by platform:**
- Claude | Drive MCP.  Writes natively.
- Grok | Pierre copies the session summary manually (Grok has no Drive write access yet).
- ChatGPT | Pierre uploads a text block to the project knowledge file.
- Gemini | native Drive read/write.

The manual copy step for Grok and ChatGPT is an acknowledged limitation.  It is still better than re-explaining from scratch | Pierre copies once, every future agent reads the record.

**Sanitization rule:** the Drive file is not the private baton.  It is a projection.  No client names, no credentials, no `visibility: private` content.  Pierre reviews before the copy step.

## What We Found

**What works:**
- Claude + Drive MCP is seamless.  Reads and writes in session with no friction.
- The shared format means any agent that reads the file gets immediately useful context.
- "Standing Standup" framing makes the pattern intuitive | it is a persistent meeting room with a whiteboard.  You walk in, you read the board, you add your notes, you leave.

**What does not work yet:**
- Grok and ChatGPT require manual copy from Pierre.  This is not zero meat puppet | it is reduced meat puppet.  Acceptable for now.
- There is no conflict resolution on Drive.  If two agents write simultaneously, the last writer wins.  Append-only discipline solves this in practice (never edit another agent's entry), but there is no enforcement mechanism.
- The Drive file is not the source of truth.  It is a projection.  The private Git repo is still the source of truth.  Agents that only have Drive access have a sanitized, potentially delayed view.

**Design principle confirmed:**
The format-agnostic principle holds.  The same handoff schema that works in `machines/handoff.md` (Git, markdown) works in a Google Doc.  The schema is the protocol.  The transport is interchangeable.

## Decision

Adopted.  Shipped as MEP v2.1 Component 9 (Outbound Baton).

The manual copy limitation is a known gap, not a blocker.  As Grok and ChatGPT add Drive write access or API hooks, the manual step goes away.  The protocol is ready for that upgrade without a schema change.

## See Also

- `CHANGELOG.md` | v2.1 | Outbound Baton + Standing Standup
- `spec/mep-protocol.md` | Component 9
- `explorations/bluesky-atproto-transport.md` | real-time alternative considered and shelved
