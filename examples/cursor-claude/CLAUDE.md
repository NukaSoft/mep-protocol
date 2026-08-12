# My Project — AI Session Protocol (MEP)

<!--
Dual-runtime example. Keep this Session Protocol identical to AGENTS.md.
Baton path: handoff.md
-->

## Session Protocol (MANDATORY)

This repo is worked by Cursor and Claude Code as peers. The baton is one file. Do not ask the human to re-explain the other runtime's session.

### Hello — BEFORE responding to the user

1. `git fetch origin`
2. Read `handoff.md`. If this session is not on the default branch, also read the baton from `origin/<default-branch>`.
3. `git pull --ff-only` when it is safe. Do not create merge commits as a side effect of Hello.
4. If the newest entry is still tagged **Tag-out: [active]**, do not rewrite that entry.
5. Briefly tell the user what you picked up (2–3 lines max).

### EOL — session end

Triggers: `/eol`, `p-out`, `ppp`, `wrap up`, `heading out`, `switching machines`, `end of line`.

Do not treat the word `done` alone as EOL.

1. Prepend a v2 handoff entry: `## YYYY-MM-DD — [Agent] | Claude Code | code` plus tag-in/tag-out with timezone (prefer UTC).
2. Three sections: what happened / what's pending / watch out for. Owner-tag pending items `[Cursor]`, `[Claude]`, or `[human]`.
3. Commit and push the current branch. Never force-push `main` or `master`.
4. Sign off: "End of Line."

### Conflict recovery

Keep every entry. Newest date on top. Same-day entries order by tag-out timestamp. No force-push to the default branch.

---

## Project Identity

[Replace with your project identity.]

### Runtimes on this repo

| Runtime | Identity file | Writes the baton |
|---------|---------------|------------------|
| Cursor | `AGENTS.md` + `.cursor/rules/mep.mdc` | Yes |
| Claude Code | `CLAUDE.md` | Yes |
