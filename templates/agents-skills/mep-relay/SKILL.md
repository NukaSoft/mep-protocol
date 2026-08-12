---
name: mep-relay
description: Pass the MEP baton. Use at session start (Hello / tag-in), on /eol or wrap-up, and when checking handoff status.
---

# MEP Relay (Codex / AGENTS.md skills)

Install: copy to `.agents/skills/mep-relay/SKILL.md` (OpenAI Codex repo skills) or keep this file as the distribution copy.

Canonical protocol: `MEP.md`. This skill is the command surface. Do not fork the rules.

You are **Codex (OpenAI)** unless the identity files say otherwise. Owner tag: `[Codex]`. Platform string: `Codex (OpenAI)`.

## /mep start (Hello)

Follow **Hello** in `MEP.md`: fetch, read `handoff.md`, tag in with `Tag-out: [active]`, push if you can, report 2–3 lines. Do not rewrite another agent's `[active]` entry.

## /mep end (EOL)

Follow **EOL** in `MEP.md`: fill **your** `[active]` entry in place, journal, commit, push. Never force-push `main`. The word `done` is not EOL.

## /mep status

Summarize the newest handoff entry (and any other `[active]` sessions) in 3–4 lines.
