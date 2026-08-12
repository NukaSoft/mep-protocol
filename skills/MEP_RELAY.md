---
name: mep-relay
description: MEP Protocol — pass the baton between AI sessions. Handles Hello (tag-in), EOL (tag-out), and status.
user-invokable: true
argument-hint: "[start|end|status]"
license: Apache-2.0
copyright: Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI
---

# MEP Relay Skill (Claude Code)

Canonical protocol: `MEP.md`. This skill is the command surface. Do not fork the rules.

You are **Claude Code**. Platform: `Claude Code`. Owner tag: `[Claude]`. Peers: Cursor, GitHub Copilot, OpenAI Codex, ChatGPT.

Install: `~/.claude/skills/mep-relay/SKILL.md` or symlink from the repo.

## /mep start

Execute **Hello** from `MEP.md` before responding.

1. `git fetch origin` and read `handoff.md` (plus default-branch baton if you are not on default)
2. `git pull --ff-only` only when safe
3. Read `AGENTS.md`, `TASKS.md`, today's journal
4. Prepend your `[active]` tag-in unless you already have one. Do not edit anyone else's `[active]` entry
5. Commit `HELLO: Claude Code tagged in` and push if you can (failure does not block)
6. Report 2–3 lines

```
Picked up from [date] — [agent / platform].
Pending: [top 2-3 items].
Tagged in. Other sessions: [idle / listed [active] agents].
```

## /mep end

EOL from `MEP.md`. Triggers: `/eol`, `p-out`, `ppp`, wrap up, heading out, switching machines, end of line. Not the word `done`.

1. Fill **your** `[active]` entry in place (happened / pending / watch out, tag-out now UTC)
2. If you never tagged in, prepend a complete v2 entry
3. Append today's journal
4. Commit and push the current branch. Never force-push `main`/`master`
5. Confirm: **End of Line.**

### Conflict recovery

Keep every entry. Newest date, then timestamp (`[active]` first). `--force-with-lease` only on a branch this session created. No force-push to the default branch.

## /mep status

Newest entry plus any other `[active]` sessions, 3–4 lines.
