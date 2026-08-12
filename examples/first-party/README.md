# First-party MEP example

Minimum setup for a repo that **Claude Code, Cursor, GitHub Copilot, and OpenAI Codex** all write. ChatGPT without git uses the seed prompt.

```
examples/first-party/
├── MEP.md                              Canonical session protocol
├── AGENTS.md                           Project identity + loader (Cursor, Codex, Copilot agent)
├── CLAUDE.md                           Claude Code loader
├── handoff.md                          Shared baton (default path)
├── .cursor/rules/mep.mdc               Cursor always-on rule
├── .github/copilot-instructions.md     GitHub Copilot loader
├── .agents/skills/mep-relay/SKILL.md   Codex skill
└── SEED_PROMPT.md                      ChatGPT (no git)
```

Copy into a project root:

```bash
cp examples/first-party/MEP.md examples/first-party/AGENTS.md examples/first-party/CLAUDE.md examples/first-party/handoff.md .
mkdir -p .cursor/rules .github .agents/skills/mep-relay .cursor/skills/mep-relay
cp examples/first-party/.cursor/rules/mep.mdc .cursor/rules/mep.mdc
cp examples/first-party/.github/copilot-instructions.md .github/copilot-instructions.md
cp examples/first-party/.agents/skills/mep-relay/SKILL.md .agents/skills/mep-relay/SKILL.md
cp path/to/mep-protocol/skills/cursor/mep-relay/SKILL.md .cursor/skills/mep-relay/SKILL.md
# ChatGPT sessions without git: paste SEED_PROMPT.md
```

Edit `AGENTS.md` project identity. Do not fork the protocol into the loaders — change `MEP.md` once.

`examples/cursor-claude/` is a pointer at this example. Use this one.
