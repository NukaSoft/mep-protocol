---
name: mep-relay
description: Pass the MEP baton between first-party runtimes. Use at Hello (tag-in), /eol, and status.
---

# MEP Relay (Cursor)

Canonical protocol: `MEP.md`. This skill is the command surface. Do not fork the rules.

Install: `.cursor/skills/mep-relay/SKILL.md` plus `templates/cursor-rules/mep.mdc` → `.cursor/rules/mep.mdc`.

You are **Cursor**. Platform: `Cursor (IDE)`, `Cursor (Cloud)`, or `Cursor (CLI)`. Owner tag: `[Cursor]`. Peers: Claude Code, GitHub Copilot, OpenAI Codex, ChatGPT.

## /mep start

Execute **Hello** from `MEP.md`: fetch, read `handoff.md`, tag in `[active]`, push if you can, report 2–3 lines. Do not rewrite another agent's `[active]` entry.

## /mep end

Execute **EOL** from `MEP.md`: fill your `[active]` entry in place, journal, push. Never force-push `main`. PR-only: paste the finished entry into the PR body. The word `done` is not EOL.

## /mep status

Newest entry plus any other `[active]` sessions, 3–4 lines.
