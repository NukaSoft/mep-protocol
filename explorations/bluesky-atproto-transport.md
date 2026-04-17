---
status: shelved
date: 2026-04
proposed_by: Pierre
outcome: Technically sound as a real-time inter-agent bus. Premature. Revisit when multi-agent coordination is a first-class MEP requirement.
---

# Exploration: Bluesky AT Protocol as Inter-Agent Transport

## The Idea

Use the Bluesky AT Protocol (AT Proto) as a real-time message bus for agent-to-agent communication inside MEP.

AT Proto is a federated social protocol with a few properties that make it interesting for this use case:

- **Decentralized identity (DIDs)** | every agent gets a DID.  Cryptographically verifiable identity without a central auth server.
- **Lexicon schemas** | AT Proto allows you to define custom record types (lexicons).  A MEP baton is a structured document | it maps to a lexicon record.
- **Pub/sub via firehose** | the AT Proto firehose broadcasts all public records in real time.  An agent can subscribe to records from specific DIDs and receive updates immediately without polling.
- **Federation** | the relay network is distributed.  No single point of failure, no vendor lock-in to GitHub.

The sketch: each agent publishes a baton record to AT Proto on EOL.  Subscribing agents pick it up from the firehose on startup.  The handoff is real-time and infrastructure-agnostic.

## The Hello Protocol Connection

Pierre proposed a **Hello Protocol** | a formal MEP startup event.  When a session begins, the agent broadcasts a `hello` message before reading the baton.  The `hello`:
- Announces presence (which machine, which agent, session type)
- Timestamps the tag-in
- Signals to any monitoring surface that a session is active

AT Proto is a natural transport for Hello.  The firehose means every other subscribed agent sees the `hello` in real time.  A monitoring dashboard could show "active sessions" live, based on recent `hello` records from registered agent DIDs.

This is the "party line" feature described in the Standing Standup model | a live view of which agents are currently tagged in across all projects.

## What We Tested

Architecture analysis only.  No implementation.

Specific findings:

**1. AT Proto lexicon for baton records is straightforward.**
The handoff schema maps cleanly to a Lexicon record type.  Frontmatter becomes record metadata.  The three sections (what happened / pending / watch out) become structured fields.  Schema definition would be maybe 50 lines of JSON.

**2. DID management is non-trivial in a fully automated context.**
AT Proto DIDs require key management.  In a local dev context, you are managing signing keys for each agent's DID.  This is not hard for a human developer, but for autonomous agents running in a systemd context on Hot Rod, key rotation and revocation need to be handled carefully.  It is solvable but adds operational overhead.

**3. The firehose is public.**
AT Proto records are public by default.  The baton contains Pierre's working context, including project names, client references, and system state.  Putting that on a public federated network is a `visibility: private` violation waiting to happen.  The protocol would need an encryption layer or a private relay | which brings back the infrastructure overhead problem.

**4. Latency benefit is real but the use case is not yet there.**
Real-time inter-agent coordination (two agents running simultaneously, passing state back and forth) is a future MEP requirement, not a current one.  Right now, MEP sessions are serial | one ends, the next begins.  Git's asynchronous model handles this fine.  AT Proto's real-time model shines when sessions overlap, and we are not there yet.

## Decision

Shelved.  Not rejected | the architecture is sound.  The timing is wrong.

**Conditions for revisiting:**
- MEP use case expands to concurrent multi-agent sessions (two agents working the same project simultaneously)
- AT Proto adds private record support or a trusted relay option
- Pierre's agent fleet grows to a point where real-time coordination signals (hello/goodbye/active) have operational value

**What survives:**
- The Hello Protocol concept is valid and worth formalizing independent of the transport.  `hello-protocol.md` carries that work forward.
- The DID-per-agent identity model is interesting for the longer-term MEP identity spec | each agent having a verifiable, portable identity that is not tied to a GitHub account.
- The party line concept from Standing Standups was directly shaped by this exploration.

## See Also

- `explorations/hello-protocol.md` | Hello Protocol as standalone MEP lifecycle event
- `spec/mep-protocol.md` | Component 9: Outbound Baton (Google Drive shared surface, the simpler near-term version of the same idea)
- [AT Protocol docs](https://atproto.com/docs)
