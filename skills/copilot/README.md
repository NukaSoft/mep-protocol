# GitHub Copilot — MEP notes

Copilot does not use Claude-style `SKILL.md` for repo chat. Injection is:

1. `.github/copilot-instructions.md` (this is the Copilot-specific loader — copy from `templates/github/copilot-instructions.md`)
2. `AGENTS.md` (Copilot coding agent reads it)
3. `MEP.md` (canonical protocol — both of the above point here)

Coding-agent PRs: Hello/EOL on the working branch and paste the newest `handoff.md` entry into the PR body so other runtimes can read it before merge.

Platform: `Copilot (GitHub)`. Owner tag: `[Copilot]`.
