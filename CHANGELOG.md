# MEP Protocol — Changelog

All notable changes to the MEP Protocol are documented here.

Format: `## [version] — YYYY-MM-DD`

---

## 2.4 | 2026-08-11

### Relicensed to full open source

AGPL-3.0 replaced by a two license split by artifact type.

- **Code, templates, skills, examples:** Apache License 2.0
- **Specification documents (`spec/`, `LEXICON.md`):** CC BY 4.0

**Why.** AGPL defeated the goal. The templates exist to be copied into other
people's repositories, and under AGPL that arguably relicensed their work, so
the on-ramp to the protocol was a legal hazard. AGPL also permanently blocked
upstream adoption, since permissively licensed projects cannot take it. And its
one real protection, the network service loophole, does not apply to a document
protocol whose transport is git.

A specification is only worth writing if anyone can implement it. Implementing
MEP now requires no permission and imposes no obligation. Attribution is
required only when copying or adapting the documents themselves.

Sole copyright holder, so no contributor consent was required. Verified against
both the private history and the public repository before relicensing.

## [MEEP-ReadOnly-v1] — 2026-04-29

**Read-only peer-agent context surface.**

### Added
- **`spec/meep-readonly-v1.md`** | New sibling spec defining a small, public-but-unlinked Markdown page that external peer agents (Grok, ChatGPT, Gemini) fetch on session start. Unidirectional, agent-scoped, pull-on-demand. Sized to act as effective system-prompt context without blowing token budget.
- **First instance:** Hastings (Leo) at `nukasoft.ai/leo`. Page owner: Rita. Source scaffolded at `site/_pages/leo.md`.
- **Required sections** | Stable Fundamentals, Current Strategic Priorities, Open Questions, Recent Decisions, Active Workstream State, Sync Notes, Changelog.
- **Token budget** | Soft cap ~1,500 words / ~2,000 tokens per page.

### Design Decisions
- **Not a Standing Standup.** The standup (v2.1) is bidirectional and project-scoped. MEEP-ReadOnly-v1 is unidirectional and agent-scoped. Different problem, different primitive.
- **No time-based pruning in v1.** A 48-hour prune was considered and rejected: peer agents that check in weekly would silently lose history they never read. Manual curation by the page owner instead. v2 path is last-read telemetry.
- **No scheduled rebuild timer in v1.** External peer agents do not need 10-minute freshness; the timer adds operational overhead with little signal value. Triggers are manual + a light EOL hook that queues drafts but does not auto-publish.
- **Security via obscurity + content discipline.** `noindex,nofollow`, `robots.txt` disallow, no sitemap entry. Content rule: if a competitor reading this would be a problem, it does not go on the page. Auth tokens are v2 backlog.
- **URL shortener / redirector deferred to v2.** Direct `nukasoft.ai/{agent-name}` is the v1 primitive; an aka.ms-style redirector to an off-repo canonical surface is the expected next step.

---

## [2.2] — 2026-04-15

**Public Relay Automation + Exploration Archive**

### Added
- **`explorations/` directory** | Five documented explorations capturing the design process behind the spec.  What was tried, what was rejected, what is active.  The proof of work.
  - `s3-redshift-hosted-relay.md` | Rejected.  Correct SaaS architecture, wrong for a zero-infrastructure protocol.
  - `smb-umb-file-locking.md` | Rejected.  Non-deterministic file locking validated Git as the only viable transport.
  - `bluesky-atproto-transport.md` | Shelved.  Technically sound for real-time multi-agent coordination.  Revisit when concurrent sessions are a first-class requirement.
  - `hello-protocol.md` | Active.  Formalizing the session startup event as a lifecycle primitive.  Draft spec included.
  - `google-drive-shared-surface.md` | Active (shipped as v2.1 Component 9).  Cross-ecosystem shared handoff via Drive MCP.
- **Uhura | MEP Public Relay AP** | The AP responsible for keeping this public repo in sync with the private working tree.  Named for Lt. Nyota Uhura (ST:TOS, 1966 to 1969).  Skills: `skills/uhura/`.  Cadence: every 3 hours via systemd timer.
- **`understandings/` directory** | Nine inaugural Understandings published from Pierre's private knowledge store.  Aha moments captured in the moment they clicked.  Published via Uhura on every sync.
- **Automated sync pipeline** | `mep-sync.sh` + systemd timer.  The public repo is now a downstream mirror of the private working tree, not a periodic manual dump.  Sanitization enforced at the transport layer.

### Design Decisions
