# Contributing to MEP Protocol

MEP is a protocol specification, not a software library. Contributions are proposals to change how the protocol works — they carry more weight than a typical code PR.

---

## What Can Be Contributed

| Type | Examples | Process |
|------|----------|---------|
| **Bug reports** | Handoff schema edge case, conformance test failure | Open an issue |
| **Transport profiles** | Conformance evaluation for a new transport | PR to `spec/handoff-schema.md` |
| **Skill ports** | MEP_RELAY for Cursor, Copilot, Gemini CLI | PR to `skills/` |
| **Example implementations** | Working MEP setup for a specific tech stack | PR to `examples/` |
| **Protocol changes** | Changes to required fields, ordering rules, EOL behavior | RFC process (see below) |

---

## Protocol Changes — RFC Process

MEP is a versioned protocol. Changes to core behavior (handoff schema, ordering rules, EOL sequence, conflict recovery) require an RFC:

1. Open an issue titled `RFC: [your proposal]`
2. Describe the problem, proposed change, and backward compatibility impact
3. Discuss for at least 7 days
4. If accepted, PR the spec changes with a CHANGELOG entry
5. Version bump follows semver: breaking changes = major, additions = minor, fixes = patch

**The ordering rule (newest-first) is load-bearing.** The autonomous conflict resolution capability depends on it. Any proposal to change it must demonstrate that autonomous merge remains possible under the new scheme.

---

## Authorship & IP

MEP is open source under two licenses: Apache 2.0 for code, templates, skills, and examples; CC BY 4.0 for the specification documents. By contributing, you agree your contribution is licensed under whichever of the two applies to the file you touched.

You may build on MEP, ship it, and sell it, with no obligation to open your changes. Implementing the protocol requires no permission at all. If you copy or adapt the spec documents themselves, credit the source.

---

## Code of Conduct

Be direct. Be accurate. If something doesn't work, say so with evidence. If you disagree, say why. We are building infrastructure for AI agents — correctness matters more than politeness.
