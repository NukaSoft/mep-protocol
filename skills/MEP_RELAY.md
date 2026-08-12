---
name: mep-relay
description: MEP Protocol — pass the baton between AI sessions. Handles session start (load context), session end (commit state), and status check.
user-invokable: true
argument-hint: "[start|end|status]"
license: Apache-2.0
copyright: Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI
---

# MEP Relay Skill

Implements the Meat Puppet Elimination Protocol (MEP) handoff commands for Claude Code sessions. Cursor is a peer writer of the same baton — see `skills/cursor/mep-relay/SKILL.md`.

---

## /mep start

Execute at the beginning of any session.

1. `git fetch origin`
2. Read `handoff.md` (or `machines/handoff.md`) — load the baton (newest entry is current state). If this branch is not the default branch, also read the baton from `origin/<default-branch>`.
3. `git pull --ff-only` only when the working tree is clean and a fast-forward will not invent a merge.
4. Read `TASKS.md` — pick up the task queue
5. Check today's journal: `daily/YYYY-MM-DD.md`
6. If the newest entry is still `Tag-out: [active]`, report that and do not rewrite it.
7. Report to the human: what's loaded, what's pending (2–3 lines max, not a novel)

**Output format:**
```
Picked up from [date] — [agent / runtime].
Pending: [top 2-3 items].
Other runtime: [idle / tagged in / unknown].
```

---

## /mep end

Execute at the end of any session. Triggered by EOL keywords: `/eol`, `p-out`, `ppp`, or natural phrases ("wrap up", "heading out", "switching machines", "end of line").

Do not treat the word `done` alone as EOL.

1. Write the handoff entry — newest entry on top. Dual-runtime repos use the v2 header:
   - `## YYYY-MM-DD — [Agent] | Claude Code | [session-type]`
   - `**Tag-in:** HH:MM UTC | **Tag-out:** HH:MM UTC`
   - `### What happened` — concise bullet list of accomplishments
   - `### What's pending` — checkbox list of open items, scope-tagged by owner (`[Cursor]`, `[Claude]`, `[human]`)
   - `### Watch out for` — optional, only if there are traps or stale state to flag
2. Append to today's journal (`daily/YYYY-MM-DD.md`) — do not overwrite
3. Stage: `git add handoff.md daily/YYYY-MM-DD.md`
4. Commit: `git commit -m "EOL: [machine] — [one-line summary]"`
5. Push the current branch. Never force-push `main` or `master`.
6. Confirm: **"End of Line."**

### Conflict Recovery (Autonomous)

If push fails due to a merge conflict in `handoff.md`:

1. Re-read both versions of `handoff.md` (local branch + the branch you are merging)
2. Identify the structural rule from existing entries: **newest date on top, history preserved below**. Same calendar day: order by tag-out timestamp (`[active]` sorts first).
3. Keep every agent's entry. Do not edit another agent's entry to win the merge.
4. Write the resolved file, stage: `git add handoff.md`
5. If you are on a branch this session created: rebase onto the target, then `git push --force-with-lease`.
6. If you are on `main` / `master` / a shared branch: merge (no force-push), then push.
7. Complete the EOL sequence

**Do not escalate to the human** unless two entries are incomparable (missing dates, or same-day times with no timezone) and you would have to delete one of them to proceed.

---

## /mep status

Read the current `handoff.md` and summarize the last entry in 3–4 lines.

```
Last session: [date] on [agent / runtime]
Accomplished: [top 2 items]
Pending: [top 2 items]
Watch out: [if any]
```

---

## Baton Format Reference

```markdown
# Handoff Log

## YYYY-MM-DD — Agent | Runtime | session-type
**Tag-in:** HH:MM UTC | **Tag-out:** HH:MM UTC

### What happened
- Bullet list of accomplishments

### What's pending
- [ ] **[Owner]** Task description
- [ ] Another task

### Watch out for
- Optional: traps, stale state, known issues

---

## YYYY-MM-DD — Previous Agent | Runtime | session-type
...
```

---

## Installation

Drop this file into `~/.claude/skills/mep-relay/SKILL.md` or symlink from your repo.

For Cursor, install `skills/cursor/mep-relay/SKILL.md` and `templates/cursor-rules/mep.mdc`.

No dependencies. No runtime. No server. Just Git and markdown.
