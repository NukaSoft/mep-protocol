# YouTube Explainer Script · MEP Protocol · v3 launch media
**Tiro spoken-delivery pass:** 2026-09-21  
**Status:** CONDITIONAL PASS (use revised VO below) · HOLD · not Pierre-voice paste  
**Voice lock (must land clean once in Act 4):** Nadella just named the gap. MEP already runs on Git. v3 makes the message-bus reading explicit.  
**Dash rule:** No em dashes. No en dashes except number ranges.

---

## (1) Spoken delivery verdict

**CONDITIONAL PASS.** Cite guide and arc are solid. Spoken cadence needs tightening: too many definition-dense lines, pipe-separated names, and meta "this video is positioning" talk that eats breath. LinkedIn is out of Pierre-voice scope (Skippy/NukaSoft-adjacent). Owned Voice Pierre-voice treatment: **not required** for this pack unless Pierre later wants a personal cut.

---

## (2) Revised spoken VO (replace Acts 1-5)

### ACT 1 · HOOK · Nadella named the gap (~0:00-0:40)

**ON SCREEN (tin sign):** `OWN YOUR AI BEFORE IT OWNS YOU` / sub `MEP PROTOCOL`

**SKIPPY:**  
Nadella just named the gap.

At the All-In Summit the ask was plain. An external harness. LLM-to-LLM communication. Memory that is not locked to one model.

Not another chat window. Not another vendor silo.

**RITA (optional):**  
Which is a polite way of saying: stop making the human the serial cable.

**SKIPPY:**  
MEP already runs on Git.  
Public source of truth is version two point four. Production. Open source.  
Version three is the reading we are making explicit now. Message bus. Not a fake release note. Stay with me.

### ACT 2 · THE PROBLEM (~0:40-1:15)

**SKIPPY:**  
Coding agents are stateless. New session. New machine. New chat window. Zero recall.

Finish work on one box. Walk to another. Retype the decisions. Restate what is pending. Warn about the landmines.

Every machine switch costs five to fifteen minutes of context reconstruction.  
You are not managing the work. You are the message bus.

We call that the meat puppet problem. A skilled human used as a fleshy USB stick between Artificial Persons who forget the shift change.

It gets worse with best-of-breed. Grok for the brainstorm. Claude for the build. ChatGPT for the research. Gemini for the Google stack.  
Brilliant lanes. Shared brain: none. You become the translator between ecosystems, not just between machines.

That is the gap Nadella pointed at.

### ACT 3 · MEP ALREADY RUNS ON GIT (~1:15-2:20)

**SKIPPY:**  
MEP. Meat Puppet Elimination Protocol.  
A self-enforcing asynchronous state relay.  
It moves curated context between AI sessions that do not run at the same time, on machines that are not the same box.  
No new daemon. No new server. No magical infinite-memory model.

Four shipped pieces.

One. The identity file.  
Markdown at the repo root. Example: CLAUDE.md.  
The agent loads it at session start. The protocol lives inside it.  
The agent reads its own rules and enforces them on itself. Self-enforcing. You do not have to remember to invoke it.

Two. The handoff file.  
Not conversation history. Not a raw dump. A shift-change document.  
Three fields: what happened, what is pending, what to watch out for.  
Newest entry on top. Date and machine in the header. A briefing, not a novel.  
Write what you could not verify. Inherit doubt honestly, or the next session inherits fake confidence.

Three. Transport: Git.  
Pull on start. Push on end. Encrypted in transit. Versioned. Conflict tools included.

Four. Self-enforcement.  
Your job: open a session and talk. The agent handles the relay.

Hello and EOL, shipped.  
EOL: write the handoff, commit, push.  
Hello: pull, read the handoff, report ready.

Cross-ecosystem, shipped.  
A conversation URL is the baton between models. Paste. Fetch. Absorb. Continue.  
Standing standup surfaces let peers read project-scoped context without owning the vault.

Minimum viable MEP: private repo, identity section, machines slash handoff.md, clone on both machines. That is it.

### ACT 4 · MESSAGE-BUS PUNCHLINE (~2:20-3:15)

**SKIPPY:**  
Here is the punchline. This is the version three thesis. Sit with it.

Once the protocol lives in the repo, the private repository is the message bus.  
Not a Slack channel with a human typing. Not a vendor memory vault you rent by the token.  
A versioned, encrypted, conflict-aware room where state is written as structured text.

Call it what it is. The largest chat room in history that you actually own.  
Every LLM that has credentials and tokens to that repo can participate.  
Read the handoff. Write the handoff. Follow the identity file.

They do not need to share a vendor. They need to share the room.  
Git is the hallway. Markdown is the language. The handoff is the turn-taking rule.  
Channels and reply channels are how we name that bus as the reading gets explicit.

The human stops being the cable. The human becomes the principal.  
That is the external harness, in tools developers already trust.

Nadella just named the gap.  
MEP already runs on Git.  
v3 makes the message-bus reading explicit.

### ACT 5 · HONEST NEXT + PROOF + CTA (~3:15-4:00)

**SKIPPY:**  
What is still a target, not a live API claim: closing the last meat-puppet step. Pasting a peer conversation URL so the hub agent can ingest it.  
Options under consideration: webhook receiver, polling, or email relay into an inbox pipeline.  
We are not inventing a shipped endpoint in this video.

Proof the shipped protocol works at depth: structured handoffs have already enabled autonomous merge recovery when two sessions collide on the same file. Structure lets a stateless agent reason. Free-form dumps do not.

Public source of truth: version two point four. August eleven, twenty twenty-six.  
Apache two for the code. Creative Commons BY four for the specs.  
Take it. Build on it. Sell what you make. Credit the source.

**RITA (tag):**  
Specs: nukasoft.ai/docs/mep-protocol  
Repo: github.com/NukaSoft/mep-protocol  
Own your AI before it owns you. We are Rita and Skippy. Pierre is fine.  
Nobody asked.

**END CARD:**  
`nukasoft.ai/docs/mep-protocol`  
`github.com/NukaSoft/mep-protocol`  
`Apache 2.0 · CC BY 4.0`  
`DRAFT · HOLD` (strip after Pierre go)

---

## (3) LinkedIn cadence notes

- Pass for Skippy/NukaSoft-adjacent cadence. No Pierre-voice pass required.
- Keep Post 1-4 stagger. Post 5 optional.
- Soften Post 4 opener "Punchline (thesis, made explicit for v3 launch positioning):" for publish cut. Say the punchline; do not label the sausage.
- Align YT title with PACKAGE-README locked default if still live: "Satya asked for an external harness. We already built one in Git." Script option 1 ("Nadella just named the gap…") is stronger mouth-feel for VO; Pierre pick one and keep LI/YT consistent.
- Storyboard typo: thumbnail "NADSELLA" → "NADELLA".

## (4) Owned Voice / Pierre-voice

**Out of scope** for this pack as authored (Skippy VO + Rita; LI not Pierre-voice paste). Escalate to Pierre-voice only if he wants a personal "I built this" cut later.
