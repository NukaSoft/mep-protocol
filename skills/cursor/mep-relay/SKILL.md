---
name: mep-relay
description: Pass the MEP baton between Cursor and Claude sessions. Use at session start, on /eol or wrap-up, and when checking handoff status.
---

# MEP Relay (Cursor)

Implements the Meat Puppet Elimination Protocol for Cursor IDE, Cloud Agent, and CLI sessions. Claude Code is a peer writer of the same `handoff.md`. Commands match the Claude skill so either runtime can pick up the baton.

Install: copy this file to `.cursor/skills/mep-relay/SKILL.md` in the project (or symlink from this repo).

Also install the always-on rule: `templates/cursor-rules/mep.mdc` → `.cursor/rules/mep.mdc`.

---

## /mep start

Execute at the beginning of any session.

1. `git fetch origin`
2. Read `handoff.md` (or `machines/handoff.md`). If this branch is not the default branch, also read the baton from `origin/<default-branch>`.
3. `git pull --ff-only` only when the working tree is clean and a fast-forward will not invent a merge.
4. Read `TASKS.md` if it exists.
5. Check today's journal: `daily/YYYY-MM-DD.md`
6. If the newest entry is still `Tag-out: [active]`, report that and do not rewrite it.
7. Report to the human (2–3 lines max).

**Output format:**
```
Picked up from [date] — [agent / runtime].
Pending: [top 2-3 items].
Other runtime: [idle / tagged in / unknown].
```

---

## /mep end

Execute at explicit session end. Triggers: `/eol`, `p-out`, `ppp`, "wrap up", "heading out", "switching machines", "end of line".

Do not treat the word `done` alone as EOL.

1. Write the handoff entry — newest entry on top, v2 header:
   - `## YYYY-MM-DD — [Agent] | Cursor ([IDE|Cloud|CLI]) | [session-type]`
   - `**Tag-in:** HH:MM UTC | **Tag-out:** HH:MM UTC`
   - `### What happened` — concise bullet list of accomplishments
   - `### What's pending` — checkbox list, owner-tagged (`[Cursor]`, `[Claude]`, `[human]`)
   - `### Watch out for` — optional
2. Append to today's journal (`daily/YYYY-MM-DD.md`) — do not overwrite
3. Stage: `git add handoff.md daily/YYYY-MM-DD.md`
4. Commit: `git commit -m "EOL: Cursor — [one-line summary]"`
5. Push the **current branch**. Never force-push `main` or `master`.
6. If this session is PR-only, paste the newest handoff entry into the PR body so Claude can read it before merge.
7. Confirm: **"End of Line."**

### Conflict Recovery (Autonomous)

If push fails due to a merge conflict in `handoff.md`:

1. Re-read both versions (this branch + the branch you are merging).
2. Keep **every** entry. Newest date on top. Same calendar day: order by tag-out timestamp (timezone-aware; `[active]` sorts first).
3. Do not edit another agent's entry to "win" the merge.
4. Stage the resolved file: `git add handoff.md`
5. If you are on a branch this session created: rebase onto the target, then `git push --force-with-lease`.
6. If you are on `main` / `master` / a shared branch: merge (no force-push), then push.
7. Complete the EOL sequence.

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

## YYYY-MM-DD — Cursor | Cursor (Cloud) | code
**Tag-in:** 19:56 UTC | **Tag-out:** 20:40 UTC

### What happened
- Bullet list of accomplishments

### What's pending
- [ ] **[Claude]** Task the other runtime should pick up
- [ ] **[Cursor]** Task that stays on this runtime

### Watch out for
- Optional: traps, stale state, known issues

---

## YYYY-MM-DD — Skippy | Claude Code (Hot Rod) | code
**Tag-in:** 15:10 UTC | **Tag-out:** 17:00 UTC
...
```

---

## Installation

```bash
mkdir -p .cursor/skills/mep-relay .cursor/rules
cp path/to/mep-protocol/skills/cursor/mep-relay/SKILL.md .cursor/skills/mep-relay/SKILL.md
cp path/to/mep-protocol/templates/cursor-rules/mep.mdc .cursor/rules/mep.mdc
cp path/to/mep-protocol/templates/AGENTS.md AGENTS.md
```

No dependencies. No runtime. No server. Just Git and markdown.
