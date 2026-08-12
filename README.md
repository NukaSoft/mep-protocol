# MEP Protocol

**Meat Puppet Elimination Protocol** — a self-enforcing asynchronous state relay for AI sessions across machines.

[![Code: Apache 2.0](https://img.shields.io/badge/Code-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![MEP Version](https://img.shields.io/badge/MEP-v2.6-green.svg)](spec/mep-protocol.md)
[![Status: Production](https://img.shields.io/badge/Status-Production%20Proven-brightgreen.svg)](spec/mep-protocol.md#milestone-first-autonomous-ci-recovery)

---

## The Problem

AI agents are stateless. Every session starts from zero. When you work across machines, **you become the message bus** — re-explaining context, re-establishing decisions, re-describing work in progress. Every machine switch costs 5–15 minutes of reconstruction.

You are the meat puppet.

## The Solution

MEP eliminates you from the relay loop:

| Component | What It Does |
|-----------|-------------|
| **Canonical protocol** (`MEP.md`) | The only copy of Hello, EOL, and git posture. Identity files are loaders. |
| **Identity loaders** | `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/mep.mdc` |
| **Handoff File** (`handoff.md`) | Shared baton. Newest-first. Hello writes `[active]`. |
| **Transport Layer** (Git) | Versioned, encrypted, conflict-resolution built in. Enterprise-grade security. Zero management. |
| **Self-Enforcement** | No human action required. The agent reads, follows, and executes the protocol on itself. |

Your only job: open a session and start talking. The agent handles the rest.

---

## Quick Start

**Minimum viable MEP in 5 steps:**

```bash
# 1. Create a private repo
gh repo create my-project --private

# 2. Clone it
git clone https://github.com/you/my-project && cd my-project

# 3. Copy the canonical protocol and the baton
cp path/to/mep-protocol/templates/MEP.md .
cp path/to/mep-protocol/templates/handoff.md handoff.md
cp path/to/mep-protocol/templates/CLAUDE.md .
cp path/to/mep-protocol/templates/AGENTS.md .

# 4. Edit AGENTS.md with your project identity
# 5. Push and start a session
git add . && git commit -m "MEP: initialize" && git push
```

That's it for Claude Code + any `AGENTS.md` loader (Cursor, Codex, Copilot coding agent).

### First-party (Claude, Cursor, Copilot, Codex, ChatGPT)

Copy the full loader set so every git runtime Hello/EOLs the same baton:

```bash
cp path/to/mep-protocol/templates/MEP.md .
cp path/to/mep-protocol/templates/AGENTS.md .
cp path/to/mep-protocol/templates/CLAUDE.md .
cp path/to/mep-protocol/templates/handoff.md handoff.md
mkdir -p .cursor/rules .cursor/skills/mep-relay .github .agents/skills/mep-relay
cp path/to/mep-protocol/templates/cursor-rules/mep.mdc .cursor/rules/mep.mdc
cp path/to/mep-protocol/skills/cursor/mep-relay/SKILL.md .cursor/skills/mep-relay/SKILL.md
cp path/to/mep-protocol/templates/github/copilot-instructions.md .github/copilot-instructions.md
cp path/to/mep-protocol/templates/agents-skills/mep-relay/SKILL.md .agents/skills/mep-relay/SKILL.md
```

ChatGPT without git: paste `templates/openai/SEED_PROMPT.md`.

Worked example: [`examples/first-party/`](examples/first-party/). Spec: [Component 10](spec/mep-protocol.md#component-10-first-party-runtimes).

Validate: `python3 scripts/check-handoff.py --ci`

---

## Why Git as the Transport Layer

We tested five alternatives before Git:

| Transport | Problem |
|-----------|---------|
| Local SAN files | Machine-local — breaks multi-machine goal |
| Google Docs | No version history, merge conflicts unresolvable by agent |
| iCloud | Unstructured, unpredictable sync timing |
| OneDrive | Same as iCloud |
| SMB/UMB file share | File locking is non-deterministic under concurrent agent access — no workaround |

Git won because **structure enables autonomous reasoning**. When a conflict occurs, the agent can reason about the correct resolution from the file's structure — newest-first entries with named sections — without human instruction.

GitHub as transport also means: encryption at rest, 2FA, access control, and full audit log. All built in. Zero additional management. Enterprise security requirements met for free.

---

## Production Milestone

**April 3, 2026 — First Autonomous CI Recovery**

PR #12 opened with a merge conflict in `handoff.md`. Main branch was 15 commits ahead. The initial EOL sequence failed.

Without human intervention, the session:
1. Re-read `handoff.md` to understand the conflict
2. Identified the structural rule (newest-first) from existing entries
3. Diagnosed the positioning error
4. Wrote the correct resolution
5. Rebased onto main, force-pushed
6. Completed the EOL sequence

Pierre did nothing. MEP closed the CI feedback loop autonomously.

---

## Lexicon

New to the terminology? The **[MEP Lexicon](LEXICON.md)** defines every term — from [Meat Puppet](LEXICON.md#meat-puppet) to [Tour Sheet](LEXICON.md#tour-sheet) to [Do Nothing Security](LEXICON.md#do-nothing-security). Start there if this is your first read.

---

## Repository Structure

```
mep-protocol/
├── LICENSE                    Apache-2.0 (code, templates, skills)
├── LICENSE-DOCS               CC BY 4.0 (spec/, LEXICON.md)
├── README.md                  This file
├── LEXICON.md                 Protocol terminology and lineage
├── NUKA-LOG.md                Human authorship audit trail
├── CHANGELOG.md               Protocol version history
├── CONTRIBUTING.md            How to propose changes
├── spec/
│   ├── mep-protocol.md        Full protocol specification
│   ├── handoff-schema.md      BNF grammar + conformance tests
│   └── meep-readonly-v1.md    Read-only peer-agent context surface (sibling spec)
├── templates/
│   ├── MEP.md                 Canonical session protocol (the only copy)
│   ├── CLAUDE.md              Claude Code loader → MEP.md
│   ├── AGENTS.md              Project identity + loader (Cursor, Codex, Copilot)
│   ├── cursor-rules/mep.mdc   Always-on Cursor rule → MEP.md
│   ├── github/copilot-instructions.md
│   ├── agents-skills/mep-relay/  Codex skill
│   ├── openai/SEED_PROMPT.md  ChatGPT without git
│   ├── handoff.md             Blank baton (default path: repo root)
│   ├── shared-handoff.md      Blank Standing Standup template
│   └── NUKA-LOG.md            Blank authorship log template
├── skills/
│   ├── MEP_RELAY.md           Claude Code skill
│   ├── cursor/mep-relay/      Cursor skill
│   ├── copilot/               GitHub Copilot notes
│   └── openai/                Codex / ChatGPT notes
├── scripts/
│   └── check-handoff.py       Handoff conformance checker (`--ci`)
├── .github/workflows/         Checker CI
├── tests/handoff/             Checker fixtures
└── examples/
    ├── minimal/               Claude-only (MEP.md + CLAUDE.md)
    ├── first-party/           Claude, Cursor, Copilot, Codex, ChatGPT
    ├── cursor-claude/         Pointer at first-party
    └── shared-surface/        Filled Standing Standup example
```

---

## Format Agnosticism

The baton (handoff file) must be human-readable text. Markdown is the reference format — it is diffable, autonomously mergeable, and natively supported by Git. But any structured text format two machines can exchange works: TXT, HTML, structured email body.

The key requirement is **structure**. Unstructured text cannot be autonomously merged.

---

## License

Open source, two licenses by artifact type.

- **Code, templates, skills, examples:** Apache License 2.0.  See `LICENSE`.
- **Specification documents (`spec/`, `LEXICON.md`):** CC BY 4.0.  See `LICENSE-DOCS`.

Copyright 2026 Pierre Hulsebus / NukaSoft.AI.

Implementing MEP requires no permission and imposes no obligation.  Attribution is required when you copy or adapt the documents themselves.  A protocol is only worth writing if people can build on it.

Use it. Build on it. Eliminate your own meat puppet.

---

*First implemented by Pierre Hulsebus & Skippy the Magnificent, NukaSoft.AI*
*[nukasoft.ai](https://nukasoft.ai)*
