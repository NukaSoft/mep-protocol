# YouTube Explainer Script · MEP Protocol · v3 launch media (grounded in v2.4 SoT)

**Runtime target:** ~3:30 spoken (band **3:00-5:00**)  
**Voice lock:** Nadella just named the gap. MEP already runs on Git. v3 makes the message-bus reading explicit.  
**Status:** DRAFT ONLY. HOLD. READY for Skippy tech-pass.  
**Dash rule:** No em dashes. No en dashes except number ranges.

---

## Cite guide (read before recording)

**SHIPPED (say as fact):** MEP v2.4 · Git transport · self-enforcing identity file · newest-first handoff · Hello/EOL · cross-ecosystem URL baton · standing standup · autonomous CI/handoff recovery · Apache 2.0 / CC BY 4.0.

**ASPIRATIONAL / IN FLIGHT (thesis, not live):** Nadella/All-In market frame · message-bus model (private repo = largest chat room; LLMs with tokens are participants; channels/reply channels) · closing the last paste step via webhook/poll/email.

**FORBIDDEN:** "MEP v3 is released" · "v3 shipped" · citing a merged v3 PR · inventing live APIs.

---

## Title options

1. Nadella named the gap. MEP already runs on Git.
2. The private repo is the chat room | MEP Protocol
3. Stop being the USB cable between your AIs | Meat Puppet Elimination Protocol
4. LLM-to-LLM without the human in the middle | MEP

**Recommended:** Option 1 or 2.

---

## Spoken script (~3:30 | pad to ~4:30-5:00 with holds)

### ACT 1 · HOOK · Nadella named the gap (~0:00-0:40)

**ON SCREEN (tin sign):** `OWN YOUR AI BEFORE IT OWNS YOU` / sub `MEP PROTOCOL`

**SKIPPY:**  
Nadella just named the gap.

At the All-In Summit the ask was plain: an **external harness**.  
LLM-to-LLM communication. Memory that is **not locked to one model**.

Not another chat window. Not another vendor silo.

**RITA (optional):**  
Which is a polite way of saying: stop making the human the serial cable.

**SKIPPY:**  
MEP already runs on Git.  
Public source of truth is v2.4. Production. Open source.  
This video is v3 launch positioning: we make the message-bus reading explicit. We are not pretending a new release already shipped. Stay with me.

---

### ACT 2 · THE PROBLEM (~0:40-1:20)

**SKIPPY:**  
Coding agents are stateless. New session, new machine, new chat window: zero recall.  
Finish work on one box. Walk to another. Retype the decisions. Restate what's pending. Warn about the landmines.  
Every machine switch costs five to fifteen minutes of context reconstruction.  
You are not managing the work. You are the message bus.

We call that the meat puppet problem. A skilled human used as a fleshy USB stick between Artificial Persons who forget the shift change.

It gets worse with best-of-breed. Grok for the brainstorm. Claude for the build. ChatGPT for the research. Gemini for the Google stack.  
Brilliant lanes. Shared brain: none. You become the translator between ecosystems, not just between machines.

That is the gap Nadella pointed at.

---

### ACT 3 · MEP ALREADY RUNS ON GIT (~1:20-2:25)

**SKIPPY:**  
MEP | Meat Puppet Elimination Protocol | is a self-enforcing asynchronous state relay.  
It transfers curated context between non-concurrent, stateless AI sessions across physically separate machines.  
No new daemon. No new server. No magical infinite-memory model.

Four shipped pieces:

**One. The identity file.**  
Markdown at the repo root. Example: `CLAUDE.md`.  
The agent loads it at session start. Protocol instructions live inside it.  
The agent reads its own rules and enforces them on itself. Self-enforcing. No human has to remember to invoke it.

**Two. The handoff file.**  
Not conversation history. Not a raw dump. A shift-change document.  
Three fields: what happened, what's pending, what to watch out for.  
Newest entry on top. Date and machine in the header. Briefing, not a novel.  
Write what you could not verify. Inherit doubt honestly, or the next session inherits fake confidence.

**Three. Transport: Git.**  
Pull on start. Push on end. Encrypted in transit. Versioned. Conflict tools included.

**Four. Self-enforcement.**  
Your job: open a session and talk. The agent handles the relay.

**Hello and EOL, shipped:**  
EOL: write the handoff, commit, push.  
Hello: pull, read the handoff, report ready.

**Cross-ecosystem, shipped:**  
A conversation URL is the baton between models. Paste. Fetch. Absorb. Continue.  
Standing standup surfaces let peers read project-scoped context without owning the vault.

Minimum viable MEP: private repo, identity section, `machines/handoff.md`, clone on both machines. That is it.

---

### ACT 4 · MESSAGE-BUS PUNCHLINE · v3 reading made explicit (~2:25-3:25)

**SKIPPY:**  
Here is the punchline. This is the v3 thesis. Sit with it.

Once the protocol lives in the repo, the **private repository is the message bus**.  
Not a Slack channel with a human typing. Not a vendor memory vault you rent by the token.  
A versioned, encrypted, conflict-aware room where state is written as structured text.

Call it what it is: **the largest chat room in history that you actually own.**  
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

---

### ACT 5 · HONEST NEXT + PROOF + CTA (~3:25-4:10)

**SKIPPY:**  
What is still a target, not a live API claim: closing the last meat-puppet step. Pasting a peer conversation URL so the hub agent can ingest it.  
Options under consideration: webhook receiver, polling, or email relay into an inbox pipeline.  
We are not inventing a shipped endpoint in this video.

**Proof the shipped protocol works at depth:** structured handoffs have already enabled autonomous merge recovery when two sessions collide on the same file. Structure lets a stateless agent reason. Free-form dumps do not.

Public SoT: v2.4, August eleven, twenty twenty-six.  
Apache two for the code. Creative Commons BY four for the specs.  
Take it. Build on it. Sell what you make. Credit the source.

**RITA (tag):**  
Specs: nukasoft.ai/docs/mep-protocol  
Repo: github.com/NukaSoft/mep-protocol  
Own your AI before it owns you. We're Rita and Skippy. Pierre is fine.  
Nobody asked.

**END CARD:**  
`nukasoft.ai/docs/mep-protocol`  
`github.com/NukaSoft/mep-protocol`  
`Apache 2.0 · CC BY 4.0`  
`DRAFT · HOLD` (strip after Pierre go)

---

## Runtime map

| Cut | Approx | How |
|-----|--------|-----|
| Tight | ~3:00 | Trim Rita; shorten Act 2; keep punchline + voice lock + CTA |
| Standard | ~3:30-4:00 | Full script |
| Long | ~4:30-5:00 | Longer punchline hold; optional Apr 2026 merge-recovery visual |

## Accuracy footnotes

- Voice lock line must land once cleanly in Act 4 (and optionally in Act 1 bridge).  
- Never say "MEP v3 is released" or cite a merged v3 PR.  
- AT Protocol bus stays off-camera (proposed in SoT, not shipping claim).  
- Message-bus / channels / reply channels = thesis vocabulary, not a hosted SaaS claim.  
- "5-15 minutes" from public Problem section.  
- Nadella: paraphrase unless Skippy clears a sourced verbatim quote. No fake likeness.
