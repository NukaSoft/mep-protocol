# [Project Name] — AI Session Protocol (MEP)

<!--
MEP Protocol Template — Meat Puppet Elimination Protocol v2.5
Drop this into your repo root as AGENTS.md.
Cursor, Codex, and other AGENTS.md loaders read this automatically.
If this repo also uses Claude Code, copy templates/CLAUDE.md as well and keep
the Session Protocol sections identical.

Baton path (name it once, use it everywhere): handoff.md
Multi-machine layout may use machines/handoff.md instead — if you change the
path, change it in CLAUDE.md and .cursor/rules/mep.mdc too.

License: Apache-2.0 | Copyright 2026 Pierre Hulsebus / NukaSoft.AI
-->

## Session Protocol (MANDATORY)

This repo may be worked by more than one runtime (Cursor and Claude Code are
peers). The baton is one file. Do not ask the human to re-explain the other
runtime's session.

### Hello — BEFORE responding to the user

1. `git fetch origin`
2. Read the baton (`handoff.md`, or `machines/handoff.md` if that is the path this repo uses). If this session is not on the default branch, also read the baton from `origin/<default-branch>` so you see what the other runtime last landed.
3. Fast-forward only when it is safe: `git pull --ff-only`. Do not create merge commits as a side effect of Hello.
4. Read `TASKS.md` if it exists.
5. Check today's journal: `daily/YYYY-MM-DD.md` if it exists.
6. If the newest entry is still tagged **Tag-out: [active]**, another session may be live. Do not rewrite that entry.
7. Briefly tell the user what you picked up (2–3 lines max).

**Hello output:**
```
Picked up from [date] — [agent / runtime].
Pending: [top 2-3 items].
Other runtime: [idle / tagged in / unknown].
```

### EOL — session end

Trigger on explicit close, not on ordinary task completion:

> **`/eol`** · **`p-out`** · **`ppp`** · **`wrap up`** · **`heading out`** · **`switching machines`** · **`end of line`**

Do **not** treat the word `done` alone as EOL. Coding sessions say "done" constantly. That trigger is a false-positive in dual-runtime repos.

When triggered:

1. Write a new handoff entry at the top. Use the v2 header when more than one runtime writes this repo:
   `## YYYY-MM-DD — [Agent] | [Runtime] | [session-type]`
   plus `**Tag-in:** HH:MM TZ | **Tag-out:** HH:MM TZ`
   Timezones are required. Prefer UTC. Same-day entries order by tag-out (or tag-in if still `[active]`), newest first.
2. Three sections: `### What happened` / `### What's pending` / `### Watch out for`
3. Scope-tag pending items by owner: `[Cursor]`, `[Claude]`, `[human]`, or a named agent.
4. Append to today's journal (`daily/YYYY-MM-DD.md`) — do not overwrite.
5. Commit on the current branch. Push the current branch.
6. Sign off: "End of Line."

### Git posture (dual-runtime)

- Never `git push --force` to `main` or `master`.
- `git push --force-with-lease` is allowed only on a branch **this session created**, after a rebase you performed to resolve a handoff conflict.
- Do not edit another agent's handoff entry. Append yours. Preserve history below.
- If this session cannot land the baton on the default branch (PR-only workflow), write the entry on the working branch **and** paste the newest entry into the PR body so the other runtime can read it before merge.
- If push conflicts on `handoff.md`: fetch, merge both entries newest-first (date, then timestamp), commit the resolution, push without forcing the default branch.

### Why This Exists

Each AI session is stateless. The handoff file carries context between sessions and between runtimes. Git is the transport layer. The human is not the message bus.

---

## Project Identity

[Replace this section with your project's identity: name, purpose, key people, key terms, active work.]

### Runtimes on this repo

| Runtime | Identity file | Writes the baton |
|---------|---------------|------------------|
| Cursor (IDE / Cloud Agent / CLI) | `AGENTS.md` + `.cursor/rules/mep.mdc` | Yes |
| Claude Code | `CLAUDE.md` | Yes |

---

## Preferences

[Replace with your working style preferences: tone, output format, what to avoid, what to emphasize.]
