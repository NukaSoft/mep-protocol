# MEP — Session Protocol (canonical)

<!--
Meat Puppet Elimination Protocol v2.6
This is the only copy of the session protocol. Identity files are loaders:
they tell the runtime to read this file. Do not duplicate these rules in
CLAUDE.md, AGENTS.md, or Copilot instructions.

Baton path (default, do not change without renaming it everywhere): handoff.md
Legacy alias: machines/handoff.md — use only if handoff.md does not exist.

License: Apache-2.0 | Copyright 2026 Pierre Hulsebus / NukaSoft.AI
-->

You are a **first-party peer writer** of this repo's baton. Other runtimes
(Claude Code, Cursor, GitHub Copilot, OpenAI Codex, ChatGPT) may also write
it. Do not ask the human to re-explain another runtime's session.

**Project identity** lives in `AGENTS.md`. Read it after this file. If `AGENTS.md` is missing, use the identity section in the loader that brought you here (`CLAUDE.md` or Copilot instructions).

---

## First-party runtimes

| Runtime | What loads this protocol | Header platform | Owner tag |
|---------|--------------------------|-----------------|-----------|
| Claude Code | `CLAUDE.md` → this file | `Claude Code` | `[Claude]` |
| Cursor (IDE / Cloud / CLI) | `AGENTS.md` + `.cursor/rules/mep.mdc` → this file | `Cursor (IDE)` / `Cursor (Cloud)` / `Cursor (CLI)` | `[Cursor]` |
| GitHub Copilot | `.github/copilot-instructions.md` + `AGENTS.md` → this file | `Copilot (GitHub)` | `[Copilot]` |
| OpenAI Codex | `AGENTS.md` → this file | `Codex (OpenAI)` | `[Codex]` |
| ChatGPT (no git) | seed prompt → this file / standup URL | `ChatGPT (OpenAI)` | `[ChatGPT]` |
| Human | — | `Human` | `[human]` |

Git writers (Claude, Cursor, Copilot coding agent, Codex) Hello and EOL on `handoff.md`.
ChatGPT without git uses the seed prompt and writes a v2 entry the operator pastes back — that is the last meat-puppet step for disconnected sessions.

---

## Baton

**Path:** `handoff.md` at the repo root. If that file does not exist, read `machines/handoff.md` (legacy). Do not invent a third path.

**Format:** v2 header, newest first, timezone required (prefer UTC):

```markdown
## YYYY-MM-DD — [Agent] | [Platform] | [session-type]
**Tag-in:** HH:MM UTC | **Tag-out:** HH:MM UTC

### What happened
- deliverables and decisions

### What's pending
- [ ] **[Owner]** task

### Watch out for
- traps, stale state
```

Same calendar day: order by tag-out. `[active]` sorts first. Never edit another agent's entry.

---

## Hello — before you respond

1. `git fetch origin`
2. Read `handoff.md` (and `origin/<default-branch>:handoff.md` if you are not on the default branch).
3. `git pull --ff-only` only when the tree is clean and a fast-forward will not invent a merge.
4. Read `AGENTS.md`, then `TASKS.md` if it exists, then `daily/YYYY-MM-DD.md` if it exists.
5. **Tag in.** If you do not already have a `Tag-out: [active]` entry for this session, prepend one:

```markdown
## YYYY-MM-DD — [Agent] | [Platform] | [session-type]
**Tag-in:** HH:MM UTC | **Tag-out:** [active]

### What happened
- Tagged in. Baton read.

### What's pending
- [copy the previous entry's pending items so a crash does not drop the queue]

### Watch out for
- [copy forward anything still true]
```

6. Do not rewrite anyone else's `[active]` entry. Concurrent sessions are sibling entries.
7. Commit `handoff.md` (`HELLO: [platform] tagged in`) and push the current branch if you can. A Hello push failure must not block the human — report it and continue.
8. Tell the user, 2–3 lines:

```
Picked up from [date] — [agent / platform].
Pending: [top 2-3 items].
Tagged in. Other sessions: [idle / listed [active] agents].
```

PR-only sessions: tag in on the working branch and paste the active header into the PR body.

---

## EOL — explicit close only

Triggers: `/eol` · `p-out` · `ppp` · `wrap up` · `heading out` · `switching machines` · `end of line`

**Not a trigger:** the word `done` alone.

1. Find **your** `[active]` entry (same agent + platform). Fill `### What happened`, `### What's pending` (owner-tagged), `### Watch out for`. Set `Tag-out` to now (UTC).
2. If you never tagged in, prepend a complete v2 entry instead.
3. Append to `daily/YYYY-MM-DD.md` — do not overwrite.
4. Commit and push the current branch. Never force-push `main` or `master`.
5. `--force-with-lease` only on a branch **this session created**, after a rebase you performed to resolve a handoff conflict.
6. PR-only: paste the finished entry into the PR body.
7. Sign off: **End of Line.**

---

## Git posture

- Hello is fetch + tag-in, not a merge.
- EOL updates your active entry in place. Other agents' entries are append-only history.
- Conflict: keep every entry, newest date then timestamp, no force-push to the default branch.
- Validate: `python3 scripts/check-handoff.py handoff.md`
