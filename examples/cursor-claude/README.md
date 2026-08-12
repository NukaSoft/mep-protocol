# Cursor + Claude dual-runtime example

Minimum MEP setup for a repo that both **Cursor** (IDE, Cloud Agent, or CLI) and **Claude Code** write.

Both runtimes load their own identity file. Both read and write the same baton. The human does not relay.

```
examples/cursor-claude/
├── AGENTS.md                 Cursor / AGENTS.md loaders
├── CLAUDE.md                 Claude Code
├── handoff.md                Shared baton
└── .cursor/
    └── rules/mep.mdc         Always-on Cursor rule
```

Copy these four files to a project root (plus the Cursor skill if you want `/mep` commands):

```bash
cp examples/cursor-claude/AGENTS.md examples/cursor-claude/CLAUDE.md examples/cursor-claude/handoff.md .
mkdir -p .cursor/rules .cursor/skills/mep-relay
cp examples/cursor-claude/.cursor/rules/mep.mdc .cursor/rules/mep.mdc
cp path/to/mep-protocol/skills/cursor/mep-relay/SKILL.md .cursor/skills/mep-relay/SKILL.md
```

Then edit the Project Identity sections. Keep the Session Protocol blocks in `AGENTS.md` and `CLAUDE.md` identical.

See spec Component 10 in `spec/mep-protocol.md` for git posture, same-day ordering, and why `done` is not an EOL trigger.
