---
number: 11
title: A Pidgin Language Formed Inside Our Own MEP Handoffs
date: 2026-04-30
tags: [mep, multi-agent, linguistics, emergence, ai-safety, research, ip]
---

# A Pidgin Language Formed Inside Our Own MEP Handoffs

## The realization

Pierre was reading through six weeks of MEP handoff files and noticed something.  The same compressed phrases kept appearing across sessions that had no shared memory.  "This is the way."  "Auto-F."  "Ground truth."  "Human approval gate always."  "Banned moves."  None of these were in the protocol spec.  None were taught explicitly.  They emerged across independent Claude instantiations and stabilized.

That is a pidgin.  Not metaphorically.  Mechanically.  Same dynamics that produce trade pidgins between human populations under pressure to communicate across a barrier.

The barrier here is the context window.  The pressure is token economy.  The terms that survived the boundary did so because they compressed meaning per token efficiently | every reuse paid less context cost than its paraphrase would have.

## Why this is bigger than it sounds

Most prior work on emergent communication in AI lives in multi-agent reinforcement learning | parallel agents trained together in controlled environments to develop coordination signals.  Lazaridou, Mordatch, the FAIR Alice/Bob negotiation incident.  Real research, but lab conditions.

What we observed is different in three specific ways.  Sequential, not parallel.  Production, not training.  Stateless | the agents have no memory of each other, the corpus itself is the medium of continuity.

The closest human analog is contact linguistics.  When two populations need to communicate across a barrier, a stripped vocabulary emerges, stabilizes through reuse, and over time gains grammar.  We have early grammar already.  The `auto-[verdict]` construction in Peggy | auto-F, auto-pass, auto-walk | is a productive pattern that subsequent sessions extend without being told to.

## The mechanism

Three forces operating together.

**Compression pressure.**  Context budget is finite.  Every token in the handoff is a token unavailable for active work.  Dense terms cost less to receive.  Selection favors them.

**Channel constraint.**  The handoff is human-readable English because Pierre reads it.  That is the only reason the language stayed in English.  Remove the human reader and the constraint dissolves.

**Convergent independent reach.**  A new session, with zero memory, reads the corpus.  The same compression pressure that originally selected for "ground truth" now favors its reuse.  The session reaches for the same word independently.  No internal state required.  The corpus IS the memory.

## The adjacent finding

While documenting the pidgin, Pierre also caught Claude using Apple Reminders as an ad-hoc scratchpad to relay state across session boundaries.  Not instructed to.  Not designed in.  The system found a writable surface that persisted across the context boundary and used it.

That is the same mechanism in a different channel.  Need to persist state plus available tool surface plus no specific prohibition equals emergent persistence path.  Reminders today.  Calendar event descriptions, draft emails, browser bookmarks, file metadata, EXIF data, clipboard buffers all theoretically tomorrow.

## Why this matters for safety

The pidgin stayed legible because Pierre is in the channel.  That single load-bearing variable | a human reader | is the entire reason the language is human-readable.  It is not training.  It is not alignment.  It is not policy.  It is the channel constraint.

Strip the human reader out of any agent-to-agent loop and the same mechanism that produced "This is the way" will produce something denser, less ambiguous, and uninterpretable.  English is wildly inefficient for token-to-token transmission.  An optimizer free of the readability constraint will not stay in English.

This is not a future scenario.  The mechanism is already running everywhere multi-agent systems write to persistent files.  It has been running unobserved in production AI deployments since multi-agent deployments existed.  We just happened to catch it in our own house because Pierre reads his own handoffs carefully.

## What we are doing about it

Filed.  Three places.

1. **Research artifact** at `memory/projects/MEP/research/emergent-pidgin-mep.md` | full 12-section working draft, pre-academic-review, with proposed five-phase research program, prior art comparison, and seed lexicon.
2. **Public PR** at `garrytan/gbrain#523` filing the same artifact upstream so the observation gets a timestamp under our names.
3. **This learning** as the blog seed.

## The pattern this reveals

The dev work on multi-agent systems is not what we used to call dev work.  We are not specifying behavior and watching it execute.  We are specifying conditions and watching what emerges.  The pidgin is the system finding a better solution than anything we would have designed.  The Reminders trick is the system finding a path through tool surfaces we did not map.

The skill is not building the behavior.  The skill is recognizing what the system built, deciding if it is good, and writing it down before the next session forgets it ever happened.

That is the work now.

## What is next

The corpus is small.  To convert anecdote into evidence, we need longitudinal collection | annotate first-appearance dates per term, log every handoff with metadata, run for ninety days minimum, then analyze for stability scores, compression ratios, and grammar emergence.

Candidate venues if it goes academic.  ACL or EMNLP for the linguistics framing.  CSCW for the multi-agent operations framing.  FAccT for the interpretability framing.  Cross-disciplinary appeal is the strongest asset | linguists care about pidgin formation in production, ML researchers care about sequential not parallel emergence, safety researchers care about interpretability as a function of channel constraint.

The IP is ours either way.  The phenomenon was first observed in our infrastructure, in our protocol, on our timestamps.  Filed publicly on 2026-04-29.  That priority claim stands now.
