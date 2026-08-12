# My Project — AI Session Protocol (MEP)

## ⚡ Session Protocol (MANDATORY)

### On Session Start — BEFORE responding to the user:
1. `git fetch origin` then `git pull --ff-only` when it is safe
2. Read `handoff.md` — load context from last session
3. Briefly tell the user what's pending (2–3 lines)

### On Session End — triggered by: `/eol`, `p-out`, `ppp`, `wrap up`, `heading out`
1. Update `handoff.md` — newest entry on top, three sections: what happened / pending / watch out
2. `git add handoff.md && git commit -m "EOL: [summary]" && git push`
3. Say: "End of Line."

### Conflict Recovery (if push fails)
Re-read both versions of `handoff.md`. Newest date goes on top. Same-day entries order by timestamp. Resolve and push. Never force-push `main`.
