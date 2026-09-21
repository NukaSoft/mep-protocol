# LinkedIn Series · MEP Protocol · v3 launch media (grounded in v2.4 SoT)

**Posts:** 4 (+ optional 5th)  
**Status:** **READY for Skippy tech-pass.** DRAFT ONLY. HOLD until Pierre go.  
**Voice lock:** Nadella just named the gap. MEP already runs on Git. v3 makes the message-bus reading explicit.  
**Voice style:** NukaSoft brand / Skippy-adjacent. **Not** Pierre-voice paste.  
**Cite guide:** SHIPPED = v2.4 facts only. Message-bus / channels / Nadella frame = aspirational thesis, not a shipped v3 product.  
**Dash rule:** No em dashes. No en dashes except number ranges.  
**Stagger:** 1 post/day after go (or burst if Pierre wants).

---

## Post 1 · Nadella named the gap

**Angle:** Market moment. External harness. LLM-to-LLM. Memory not locked to one model.

**Body:**

Nadella just named the gap.

At the All-In Summit the ask was plain: an external harness for LLM-to-LLM communication, and memory that is not locked to one model.

Not another chat tab.  
Not another vendor silo that forgets when you switch tools.

MEP already runs on Git.  
Public SoT is v2.4: identity file, newest-first handoff, Hello/EOL, conversation URL baton, standing standup. Production facts. Open source.

v3 is not a fake release note.  
v3 makes the message-bus reading explicit: the private repo is the room; models with tokens are participants.

Own your AI before it owns you.

**Soft CTA:** Specs: https://nukasoft.ai/docs/mep-protocol/

**Hashtags (optional, light):** #AI #LLM #DeveloperTools #OpenSource

---

## Post 2 · You are still the cable

**Angle:** Stateless sessions; human as message bus; 5-15 minute tax. SHIPPED problem statement from v2.4.

**Body:**

Every AI coding session starts from zero.

New window. New machine. New model.  
Whatever the last session decided is gone unless somebody carries it.

That somebody is usually a skilled human.  
Re-explaining context. Restating pending work. Warning about landmines.

Five to fifteen minutes of reconstruction. Every switch.  
You stop managing the work. You become the message bus.

Best-of-breed makes it worse: one model for brainstorm, one for build, one for research. Brilliant lanes. Shared brain: none.

Nadella just named that gap.  
MEP already runs on Git so the human can stop being the cable.

Next: what is actually shipping in the repo today.

**Soft CTA:** If this is your Tuesday, you are not alone.

---

## Post 3 · What already runs on Git (v2.4 shipped)

**Angle:** SHIPPED components only. No v3-released language.

**Body:**

MEP | Meat Puppet Elimination Protocol | already runs on Git.

Public v2.4, in production:

1. **Identity file** at the repo root. The agent reads its own instructions and enforces the protocol on itself. No daemon. No server.  
2. **Handoff file.** Shift-change brief: what happened, what's pending, what to watch out for. Newest on top. Not a chat dump.  
3. **Transport: Git.** Pull on start. Push on end. Versioned. Encrypted in transit.  
4. **Hello / EOL.** Session start pulls and reads. Session end writes, commits, pushes.  
5. **Cross-ecosystem baton.** A conversation URL moves context between models. Fetch. Absorb. Continue.  
6. **Standing standup.** Project-scoped surfaces peers can read without owning the whole vault.

Minimum viable: private repo + identity section + handoff.md + clone on both machines.

That is the external harness, built from tools developers already trust.  
Apache 2.0 for code. CC BY 4.0 for the spec.

**Soft CTA:** https://nukasoft.ai/docs/mep-protocol/ · https://github.com/NukaSoft/mep-protocol

---

## Post 4 · Message-bus thesis (v3 reading made explicit)

**Angle:** Aspirational / in-flight thesis. Private repo as room. Participants with tokens. Channels / reply channels. Not "v3 shipped."

**Body:**

Punchline (thesis, made explicit for v3 launch positioning):

Once MEP lives in the repository, the **private repo is the message bus**.

Not a rented memory vault.  
Not a human typing between tabs.

A versioned room you own. Structured text. Conflict tools. History.

Call it the largest chat room in history that still belongs to you.  
Every LLM with credentials and tokens to that repo can participate: read the handoff, write the handoff, follow the identity file.

They do not need to share a vendor.  
They need to share the room.

Channels and reply channels are how we are naming that bus as the reading gets explicit.  
Closing the last manual paste step (peer URL into the hub) is the v3 target: webhook, poll, or email relay. Not a claim that those APIs are live today.

Nadella just named the gap.  
MEP already runs on Git.  
v3 makes the message-bus reading explicit.

**Soft CTA:** Specs: https://nukasoft.ai/docs/mep-protocol/  
Repo: https://github.com/NukaSoft/mep-protocol  
Tag someone who is still acting as the USB cable.

---

## Optional Post 5 · Structure is the feature (proof)

**Angle:** SHIPPED milestone + discipline. Use if Pierre wants a fifth.

**Body:**

A dump is not context. It is noise with a timestamp.

MEP's handoff schema is strict on purpose: newest first, three sections, honest "watch out for."  
That structure is what lets a stateless agent reason about its own merge conflicts instead of escalating every collision to a human.

We have run that loop in production (autonomous handoff recovery on the public record). The protocol is not a slide. It is a habit encoded in markdown and Git.

Licenses: Apache 2.0 for code and templates. CC BY 4.0 for the specification.  
Implementing MEP requires no permission and imposes no obligation. Credit the source if you copy or adapt the doc.

Own your AI before it owns you.

**Soft CTA:** Start with handoff.md and three headings. Ship the minimum on Monday.

---

## Series notes for Skippy / Rita

- **READY for tech-pass.** Cite guide applied.  
- Do not attach vendor logos or a fake Satya portrait.  
- Tin-sign stills from the YouTube pack are fine (cream/red).  
- If linking YouTube, wait until video is go-approved; else docs+GitHub only.  
- Strike any line that implies v3 APIs or a merged v3 PR are live.  
- Not Pierre-voice: avoid "I", birthday lore, double-space styling.  
