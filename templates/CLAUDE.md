# [Project Name] â€” AI Session Protocol (MEP)

<!--
MEP Protocol Template â€” Meat Puppet Elimination Protocol v1.0
Drop this into your repo root as CLAUDE.md.
Replace bracketed placeholders with your project details.
License: Apache-2.0 | Copyright 2026 Pierre Hulsebus / NukaSoft.AI
-->

## âš¡ Session Protocol (MANDATORY)

### On Session Start â€” BEFORE responding to the user:
1. Run `git pull` â€” fetch the latest baton
2. Read `handoff.md` â€” session context from previous work
3. Read `TASKS.md` â€” current task queue (if exists)
4. Check for today's journal: `daily/YYYY-MM-DD.md` (if exists)
5. Briefly tell the user what you picked up (2â€“3 lines max)

### On Session End â€” triggered by ANY of these keywords:
> **`/eol`** Â· **`done`** Â· **`wrap up`** Â· **`heading out`** Â· **`switching machines`**

When triggered, execute the shutdown sequence:
1. Update `handoff.md` â€” newest entry on top, three sections: what happened / what's pending / watch out for
2. Append to today's journal (`daily/YYYY-MM-DD.md`) â€” do not overwrite
3. `git add handoff.md daily/` â†’ `git commit` â†’ `git push`
4. Sign off: "End of Line."

### Why This Exists
Each AI session is stateless. The handoff file carries context between sessions. Git is the transport layer â€” it provides encryption at rest, 2FA, audit log, and conflict resolution with zero additional infrastructure.

---

## Project Identity

[Replace this section with your project's identity: name, purpose, key people, key terms, active work. This is what the AI reads to understand who it's working with and what matters.]

---

## Preferences

[Replace with your working style preferences: tone, output format, what to avoid, what to emphasize.]
