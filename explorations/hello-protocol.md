---
status: active
date: 2026-04
proposed_by: Pierre
outcome: Adopted as a MEP lifecycle concept. Formal spec pending. Transport TBD.
---

# Exploration: Hello Protocol

## The Idea

Formalize the session startup moment as a first-class MEP lifecycle event.

Right now, MEP has a rich end-of-session ritual (EOL: update handoff, commit, push, "End of Line.") but the start of session is implicit.  The agent reads the baton and begins working.  There is no announcement, no tag-in signal, no acknowledgment that a new session has started and who is holding the ball.

The Hello Protocol proposes to fix this.  On session startup, before reading the baton, the agent broadcasts a `hello` event:

```
HELLO
agent: Skippy
machine: Hot Rod
session_type: code
timestamp: 2026-04-15T16:00:00-04:00
project: skippy-brain
handoff_read: machines/handoff.md
```

This is the tag-in.  It is symmetric with the tag-out at EOL.

## Why It Matters

### The Standing Standup party line

In the Standing Standup model (MEP v2.1), each project has a persistent context surface that agents walk into, read, and contribute to.  The party line | the "who is tagged in right now" field | is the one thing that requires a real-time signal.  Git commits are the record.  But "is anyone currently in session?" requires a heartbeat, not a history log.

Hello provides that heartbeat.

### Operational visibility

Pierre wants to know, at a glance: "is there an active session right now, and if so, which agent and which project?"  The dashboard (`/brief`) currently has no live session indicator.  Hello events feed that indicator.

### Audit trail completeness

NUKA-LOG tracks authorship decisions.  But the handoff history only shows EOL moments | it does not show how many sessions happened, how long they ran, or which agent handled which work period.  Hello+EOL pairs make the session log complete:

```
[start] 2026-04-15 16:00 | Skippy | Hot Rod | code
[end]   2026-04-15 18:30 | Skippy | Hot Rod | code | 2.5h
```

That is a real operating record.

## Transport Options

The Hello event is transport-agnostic.  The transport decision depends on what the signal needs to do:

| Transport | Use when | Notes |
|-----------|----------|-------|
| Append to `machines/handoff.md` | Local session record only | Simplest.  No new infrastructure.  Drift-visible in git log. |
| Append to Standing Standup shared surface | Cross-agent party line (Google Drive) | MEP v2.1 model.  Works with Drive MCP. |
| AT Proto firehose | Real-time multi-agent coordination | Shelved until concurrent sessions are a reality | See `bluesky-atproto-transport.md`. |
| Radar (internal message bus) | Notification to Pierre via Telegram | Already wired. Low-friction path. |

**Current recommendation:** append to `machines/handoff.md` for the local record, and optionally ping Radar with a session-start notification if Pierre wants a Telegram tap-on-shoulder when a session begins.

## Formal Spec (Draft)

```
hello_event:
  version: "1.0"
  type: "mep.hello"
  agent: <string>           # canonical agent name (Skippy, Chloe, etc.)
  machine: <string>         # machine hostname
  session_type: <enum>      # code | cowork | chat | autonomous
  timestamp: <ISO 8601>
  project: <string>         # primary repo / project name
  handoff_read: <path>      # path to the baton file read on startup
  prior_session_end: <ISO 8601 | null>   # when the last session closed (if known)
```

The goodbye (EOL) event mirrors this with `type: "mep.goodbye"` and adds `duration_minutes`.

## Current Status

The concept is adopted.  No formal implementation yet.  The CLAUDE.md session protocol should be updated to include a Hello step in the startup sequence.

The lowest-friction first implementation is a one-line addition to the session startup sequence: "Log hello to handoff.md."  It costs nothing, produces a clean tag-in record, and requires no new infrastructure.

## Next Steps

1. Add Hello to `spec/mep-protocol.md` as Component 10
2. Add Hello step to the mandatory startup sequence in `templates/CLAUDE.md`
3. Decide transport for the live party-line signal (Radar/Telegram is the quick win)
4. Revisit AT Proto when concurrent sessions become the operating mode

## See Also

- `explorations/bluesky-atproto-transport.md` | AT Proto as the real-time transport for Hello
- `spec/mep-protocol.md` | Component 9: Outbound Baton / Standing Standup | party line field
- `CHANGELOG.md` | v2.1 | Standing Standup Reframing
