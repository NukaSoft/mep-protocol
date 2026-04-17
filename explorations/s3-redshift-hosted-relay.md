---
status: rejected
date: 2026-04
proposed_by: Pierre
outcome: Correct architecture for multi-tenant SaaS, wrong architecture for a protocol that should run on infrastructure you already have.
---

# Exploration: S3 + Redshift Hosted Relay

## The Idea

Replace Git as the baton transport with a managed cloud store.  The sketch:

- **S3** | baton files land here as objects.  Versioned bucket.  Each session commit = one `PUT`.  Reads are cheap, writes are cheap, retention is configurable.
- **Redshift** | structured query surface on top of the baton history.  Query "show me every unresolved blocker from the last 30 days across all projects" in SQL.  Turn the handoff history into a data warehouse.
- **Public query endpoint** | expose a read-only API surface so external consumers (dashboards, other agents, enterprise integrations) can pull structured baton data without touching the raw store.

The appeal: this is the SaaS version of MEP.  Pierre could sell access to the query layer.  Enterprise buyers could point their BI tools at it.  The protocol becomes a product.

## What We Tested

We did not run a full implementation.  We scoped the architecture and killed it at the design stage.

Specific concerns surfaced:

**1. Infrastructure overhead defeats the Do Nothing principle.**
MEP's core value proposition is zero new infrastructure.  Git + markdown + SSH exists in every dev workflow.  S3 + Redshift is a real AWS footprint: IAM roles, VPC config, Redshift cluster sizing, cost management, backup retention, security groups.  You have traded "open a session and work" for "maintain a cloud data stack."  That is the opposite of Do Nothing.

**2. Latency is worse, not better.**
Git round-trips on a push/pull are milliseconds on a local LAN.  S3 `PUT` latency is real.  Redshift query cold start on a small cluster is seconds.  For a protocol whose primary job is session startup, you do not want to add query latency to the hot path.

**3. Baton structure does not benefit from columnar storage.**
Redshift is optimized for aggregate analytical queries over wide tables.  The MEP baton is a small, deeply structured document that you read sequentially, not a table you scan for aggregates.  The data model is wrong for the store.  You would spend more engineering time normalizing baton content into rows than you would gain from SQL access.

**4. Multi-tenant SaaS is a different product.**
If the goal is "sell query access to handoff history," that is a legitimate product idea.  But it is MEP-as-a-Service, not MEP-as-a-protocol.  The protocol should remain infrastructure-agnostic.  A hosted product can be built on top of the protocol later without changing the spec.

## Decision

Rejected for the reference implementation.  The Git transport wins because it requires no new infrastructure, has better latency on the hot path, and matches the baton's document structure natively.

**What survives from this exploration:**
- The "query surface on handoff history" idea is still interesting for a future MEP-as-a-Service product.
- The structured frontmatter in the baton format (date, agent, session-type) was partly driven by this exploration | it makes a future columnar migration tractable if someone wants to build that product.
- The public query endpoint idea maps cleanly to the public repo model we actually ship | the public Git repo IS the query surface, just via `git log` and `grep` instead of SQL.

## See Also

- `NUKA-LOG.md` Log Entry 001 | Transport Layer Experiments | original rejection of shared file systems
- `spec/mep-protocol.md` | Validated Transports section
