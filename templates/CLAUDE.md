# [Project Name] — AI Session Protocol (MEP)

<!--
MEP Protocol Template — Meat Puppet Elimination Protocol v1.0
Drop this into your repo root as CLAUDE.md.
Replace bracketed placeholders with your project details.
License: AGPL-3.0 — Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI
-->

## ⚡ Session Protocol (MANDATORY)

### On Session Start — BEFORE responding to the user:
1. Run `git pull` — fetch the latest baton
2. Read `handoff.md` — session context from previous work
3. Read `TASKS.md` — current task queue (if exists)
4. Check for today's journal: `daily/YYYY-MM-DD.md` (if exists)
5. Briefly tell the user what you picked up (2–3 lines max)

### On Session End — triggered by ANY of these keywords:
> **`/eol`** · **`done`** · **`wrap up`** · **`heading out`** · **`switching machines`**

When triggered, execute the shutdown sequence:
1. Update `handoff.md` — newest entry on top, three sections: what happened / what's pending / watch out for
2. Append to today's journal (`daily/YYYY-MM-DD.md`) — do not overwrite
3. `git add handoff.md daily/` → `git commit` → `git push`
4. Sign off: "End of Line."

### Why This Exists
Each AI session is stateless. The handoff file carries context between sessions. Git is the transport layer — it provides encryption at rest, 2FA, audit log, and conflict resolution with zero additional infrastructure.

---

## Project Identity

[Replace this section with your project's identity: name, purpose, key people, key terms, active work. This is what the AI reads to understand who it's working with and what matters.]

---

## Preferences

[Replace with your working style preferences: tone, output format, what to avoid, what to emphasize.]
