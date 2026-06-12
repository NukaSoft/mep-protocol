# MEP Protocol

**Meat Puppet Elimination Protocol** â€” a self-enforcing asynchronous state relay for AI sessions across machines.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![MEP Version](https://img.shields.io/badge/MEP-v1.0-green.svg)](spec/mep-protocol.md)
[![Status: Production](https://img.shields.io/badge/Status-Production%20Proven-brightgreen.svg)](spec/mep-protocol.md#milestone-first-autonomous-ci-recovery)

---

## The Problem

AI agents are stateless. Every session starts from zero. When you work across machines, **you become the message bus** â€” re-explaining context, re-establishing decisions, re-describing work in progress. Every machine switch costs 5â€“15 minutes of reconstruction.

You are the meat puppet.

## The Solution

MEP eliminates you from the relay loop. Four components:

| Component | What It Does |
|-----------|-------------|
| **Identity File** (`CLAUDE.md`) | Loads automatically. Self-enforces the protocol. The agent reads its own instructions. |
| **Handoff File** (`handoff.md`) | Carries curated context between sessions. Structured, newest-first. The baton. |
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

# 3. Copy the templates
cp path/to/mep-protocol/templates/CLAUDE.md .
cp path/to/mep-protocol/templates/handoff.md machines/handoff.md

# 4. Edit CLAUDE.md with your project identity
# 5. Push and start a Claude Code session
git add . && git commit -m "MEP: initialize" && git push
claude
```

That's it. The protocol is active.

---

## Why Git as the Transport Layer

We tested five alternatives before Git:

| Transport | Problem |
|-----------|---------|
| Local SAN files | Machine-local â€” breaks multi-machine goal |
| Google Docs | No version history, merge conflicts unresolvable by agent |
| iCloud | Unstructured, unpredictable sync timing |
| OneDrive | Same as iCloud |
| SMB/UMB file share | File locking is non-deterministic under concurrent agent access â€” no workaround |

Git won because **structure enables autonomous reasoning**. When a conflict occurs, the agent can reason about the correct resolution from the file's structure â€” newest-first entries with named sections â€” without human instruction.

GitHub as transport also means: encryption at rest, 2FA, access control, and full audit log. All built in. Zero additional management. Enterprise security requirements met for free.

---

## Production Milestone

**April 3, 2026 â€” First Autonomous CI Recovery**

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

New to the terminology? The **[MEP Lexicon](LEXICON.md)** defines every term â€” from [Meat Puppet](LEXICON.md#meat-puppet) to [Tour Sheet](LEXICON.md#tour-sheet) to [Do Nothing Security](LEXICON.md#do-nothing-security). Start there if this is your first read.

---

## Repository Structure

```
mep-protocol/
â”œâ”€â”€ LICENSE                    AGPL-3.0
â”œâ”€â”€ README.md                  This file
â”œâ”€â”€ LEXICON.md                 Protocol terminology and lineage
â”œâ”€â”€ NUKA-LOG.md                Human authorship audit trail
â”œâ”€â”€ CHANGELOG.md               Protocol version history
â”œâ”€â”€ CONTRIBUTING.md            How to propose changes
â”œâ”€â”€ spec/
â”‚   â”œâ”€â”€ mep-protocol.md        Full protocol specification
â”‚   â”œâ”€â”€ handoff-schema.md      BNF grammar + conformance tests
â”‚   â””â”€â”€ meep-readonly-v1.md    Read-only peer-agent context surface (sibling spec)
â”œâ”€â”€ templates/
â”‚   â”œâ”€â”€ CLAUDE.md              Drop-in session protocol template
â”‚   â”œâ”€â”€ handoff.md             Blank baton template
â”‚   â””â”€â”€ NUKA-LOG.md            Blank authorship log template
â”œâ”€â”€ skills/
â”‚   â””â”€â”€ MEP_RELAY.md           Claude Code skill (/mep start|end|status)
â””â”€â”€ examples/
    â””â”€â”€ minimal/               Bare-bones working example
```

---

## Format Agnosticism

The baton (handoff file) must be human-readable text. Markdown is the reference format â€” it is diffable, autonomously mergeable, and natively supported by Git. But any structured text format two machines can exchange works: TXT, HTML, structured email body.

The key requirement is **structure**. Unstructured text cannot be autonomously merged.

---

## License

AGPL-3.0-or-later. Copyright (C) 2026 Pierre Hulsebus / NukaSoft.AI.

Use it. Build on it. If you distribute a modified version â€” especially as a network service â€” your modifications must remain open.

Eliminate your own meat puppet.

---

*First implemented by Pierre Hulsebus & Skippy the Magnificent, NukaSoft.AI*
*[nukasoft.ai](https://nukasoft.ai)*
