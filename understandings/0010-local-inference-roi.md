---
number: 10
title: Local Inference Pays For Its Own Hardware in Months, Not Years
date: 2026-04-20
tags: [infrastructure, economics, ai-stack, ollama, gemma, ROI]
---

# Local Inference Pays For Its Own Hardware in Months, Not Years

## The realization

I cut my cloud LLM spend roughly in half by installing a free piece of software on a box I already owned. That's the whole story.

Hot Rod's hardware bill was around $1,500. The cloud LLM run-rate before this experiment was about **$612/month, $7,449/year**. Moving 80% of server-side automation to a local Gemma 4 26B MoE model running on Ollama drops that to roughly **$300-360/month, $3,600-4,400/year** | a savings of about **$3,000-3,800 a year**.

That math means the entire machine pays for itself in **3 to 4 months**. Six months tops. After that, the hardware is free and every month of saved cloud spend is pure margin.

## Why this is bigger than it sounds

Most people frame "running models locally" as a privacy or latency story. Those matter, but the load-bearing argument is **economic**: a single mid-range AMD box with an iGPU and ROCm acceleration can absorb the routine, recurring, server-side work that a small AI operation otherwise rents at retail token prices from the cloud.

The cloud bill isn't going to zero | the cloud still runs the work that genuinely needs frontier-tier reasoning (Rita's voice, Skippy chat, skill building, planning, anything where quality matters more than cost). But that's maybe 20% of the volume. The other 80% | classification, extraction, document ingestion, agent tool-calls, summarization | is dominated by the *number* of calls, not the difficulty of any single call. That's exactly what a local 26B MoE eats for breakfast.

## The conversion details I'm hand-waving on

I don't pretend the savings number is precise to the dollar. The conversion from "spend by model" to "spend by workload" is an estimate. Token-cost ratios between Opus and a local Gemma run aren't 1:1 because the workloads route differently. Cache hit rates change. Some loads will refuse to move (anything voice-sensitive, anything Pierre wants to read in the morning). The savings could land at 40% instead of 50%. It could land at 60%.

But the **shape** of the answer doesn't change with the exact number: a free piece of software cut my recurring AI bill in half on hardware I already owned. The ROI window is short enough that even pessimistic accounting still pays back inside a year.

## The pattern this reveals

This is the **right tier of asset to own** for a one-person AI operation in 2026.

You don't need a GPU rack. You don't need a data center. You need *one* box capable enough to run a 17 GB MoE model with native vision, native tool calling, and a 262K context window, and you need the discipline to route the right work to the right model. The capability ceiling on local hardware moved up dramatically while I wasn't looking | Gemma 4 with native tool calling and vision is something Phi-4 14B couldn't touch six months ago.

## Why I'm writing this down as a learning, not a status update

Because this is the kind of decision I will want to repeat | and explain to others | for the rest of the build. **Capacity moved local. Economics followed. Routing is the design pattern.**

Every future "should we add a model for X?" question gets answered against this template:
1. Is the work creative or judgment-heavy? → Cloud Opus.
2. Is the work recurring, classification-shaped, or extraction-shaped? → Local Gemma.
3. Is the volume high enough that token cost dominates? → Always local.
4. Is the work novel and exploratory (still figuring it out)? → Cloud, then move local once stable.

That's the playbook. The $1,500 box paid for itself in a quarter, the cloud still does what only the cloud can do, and the system as a whole gets cheaper *and* more capable at the same time.

## Related

- `docs/llm-cost-baseline.md` | the actual numbers and methodology
- `TASKS.md` | `[Ratchet] Gemma 4 26B MoE vs Phi-4 Bench` for the full benchmark plan
- `scripts/llm-proxy/README.md` | the cloud/local switching infrastructure
