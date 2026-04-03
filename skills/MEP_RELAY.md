---
name: mep-relay
description: MEP Protocol — pass the baton between AI sessions. Handles session start (load context), session end (commit state), and status check.
user-invokable: true
argument-hint: "[start|end|status]"
license: AGPL-3.0-or-later
copyright: Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI
---

# MEP Relay Skill

Implements the Meat Puppet Elimination Protocol (MEP) handoff commands for Claude Code sessions.

---

## /mep start

Execute at the beginning of any session.

1. Run `git pull` to fetch the latest baton
2. Read `handoff.md` — load the baton (newest entry is current state)
3. Read `TASKS.md` — pick up the task queue
4. Check today's journal: `daily/YYYY-MM-DD.md`
5. Report to the human: what's loaded, what's pending (2–3 lines max, not a novel)

**Output format:**
```
Picked up from [date] — [machine].
Pending: [top 2-3 items].
Today's journal: [exists / not started].
```

---

## /mep end

Execute at the end of any session. Triggered by EOL keywords: `/eol`, `p-out`, `ppp`, or natural phrases ("done", "wrap up", "heading out", "switching machines").

1. Write the handoff entry — newest entry on top, three sections:
   - `### What happened` — concise bullet list of accomplishments
   - `### What's pending` — checkbox list of open items, scope-tagged by owner
   - `### Watch out for` — optional, only if there are traps or stale state to flag
2. Append to today's journal (`daily/YYYY-MM-DD.md`) — do not overwrite
3. Stage: `git add handoff.md daily/YYYY-MM-DD.md`
4. Commit: `git commit -m "EOL: [machine] — [one-line summary] — Stardate [YYYY.DDD]"`
5. Push: `git push`
6. Confirm: **"End of Line."**

### Conflict Recovery (Autonomous)

If push fails due to a merge conflict in `handoff.md`:

1. Re-read both versions of `handoff.md` (local branch + remote main)
2. Identify the structural rule from existing entries: **newest date on top, history preserved below**
3. Diagnose the conflict: determine which entry is newer by date header
4. Write the resolved file: newer entry at top, older entries intact below
5. Stage the resolved file: `git add handoff.md`
6. Rebase onto main: `git rebase origin/main`
7. Force-push the branch: `git push --force-with-lease`
8. Complete the EOL sequence

**Do not escalate to the human.** The handoff file has sufficient structure for autonomous resolution. If the conflict cannot be resolved from structure alone, only then surface it.

---

## /mep status

Read the current `handoff.md` and summarize the last entry in 3–4 lines.

```
Last session: [date] on [machine]
Accomplished: [top 2 items]
Pending: [top 2 items]
Watch out: [if any]
```

---

## Baton Format Reference

```markdown
# Handoff Log

## YYYY-MM-DD — Machine Name (branch/context)   ← newest entry ALWAYS on top

### What happened
- Bullet list of accomplishments

### What's pending
- [ ] **[Owner]** Task description
- [ ] Another task

### Watch out for
- Optional: traps, stale state, known issues

---

## YYYY-MM-DD — Previous Machine                ← older entries below
...
```

---

## Installation

Drop this file into `~/.claude/skills/mep-relay/SKILL.md` or symlink from your repo.

No dependencies. No runtime. No server. Just Git and markdown.
