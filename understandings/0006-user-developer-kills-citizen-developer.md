---
number: 0006
title: "User Developer Kills Citizen Developer"
date: 2026-04-10
para: area
areas: [ai-methodology, consulting, dashboard, enterprise-it]
tags: [area:enterprise-it, paradigm-shift, mcp, user-developer, citizen-developer, semantic-layer, it-governance, power-platform-killshot]
context: "@session"
thread: [0005-dashboard-is-the-executive-surface]
phoenix: false
---

# Understanding 0006: User Developer Kills Citizen Developer

## Hook
Microsoft sold "Citizen Developer" for a decade — the fantasy that end users would learn Power Apps, Power BI, Power Automate, Copilot Studio, and assemble their own solutions. It never worked because it was still coding, just with a mouse. **User Developer** is what replaces it: the user doesn't assemble anything. They talk. The AI assembles. IT becomes the data plane and the governance layer, and the semantic layer emerges for free from the MCP surface. No middleware. No BI team ticket. No Citizen Developer bootcamp. Just the question, answered.

## The Quote That Crystallized It

> "I mean that IS a paradigm shift. No IT needed.... And IT would Love this model. Screw the Citizen Developer crowd, this is User Developer. I ask, it happens. IT becomes Governance and Guard rails. Data layer creates security, yes. But also creates an incidental Semantic Layer that we can leverage in an executive question about the Data.
>
> An MCP connection to Dynamics.
> An MCP connection to mcp.learn.microsoft.com.
> An MCP connection to Fabric Database running every data slice needed by users.
>
> Literally no layer between.... 'Hey what is the next quarter's run rate on part #21434 and what will the shortages in that supply do to my sales orders in Q3.'
>
> And a sweet graph and a visual report on my iPad in like two minutes.
>
> No meeting, no RFP, no making-a-pizza-for-everyone model. Or a Power BI that is so complex that the one number you actually watch is buried on page seven.
>
> Power BI is based on a business model of 2001. It was a bought tech anyway."
>
> — Pierre Hulsebus, 2026-04-10

## The Citizen Developer Failure

The Citizen Developer pitch, unvarnished: *"Give your business users low-code tools. They'll build the apps IT doesn't have time for. Everyone wins."* In reality:

- **Power Apps** required users to learn a new IDE, data sources, formula language (effectively Excel-JS), and lifecycle management. Most users bounced off it within a week. The ones who stuck with it became shadow-IT — building unmaintainable apps on top of Dataverse that IT then had to govern anyway.
- **Power BI** required users to learn DAX, semantic models, relationships, and Power Query M. DAX alone is harder than SQL for the average user. The "citizen" never showed up. BI teams kept owning it.
- **Power Automate** was the closest thing to a real win, and even it required users to understand triggers, connectors, loops, error handling, and approval routing.
- **Copilot Studio** was supposed to fix this with natural language. But Copilot Studio still makes the user define topics, entities, actions, knowledge sources, channels — it's low-code bot authoring with AI hints, not "talk and it happens."

The common thread: the user was still the developer. The tools were friendlier, but the user still had to think like a developer — data modeling, state management, error handling, deployment. "Citizen Developer" was always a euphemism for "part-time developer without the training." It created a permanent training tax, a governance sprawl, and a class of shadow-IT artifacts IT eventually had to absorb.

IT hated Citizen Developer. Users hated Citizen Developer. The only people who loved it were the vendors selling seats.

## The User Developer Model

User Developer inverts the roles:

| Layer | Citizen Developer model | User Developer model |
|---|---|---|
| **User** | Learns low-code tools, builds apps, owns app lifecycle | Talks. Asks questions. Reads answers. |
| **AI** | Suggests formulas, autocompletes, offers templates | Owns reasoning, query composition, data joins, formatting, publishing |
| **IT** | Gatekeeper of tools, licenses, tenants, governance nightmares | Operates the data plane: MCP servers, schemas, access control, audit |
| **Data** | Semantic models hand-built in Power BI, maintained by BI team | Semantic layer emerges from MCP tool descriptions and examples |
| **Output** | A Power App, a Power BI report, a Power Automate flow | An answer. Optionally published to the composable front-end as a card. |
| **Failure mode** | User gives up, shadow IT, governance sprawl | User asks, IT denies at the data layer if required, audit log catches it |

The user doesn't build. The user asks. The AI goes and actually does the thing — query the warehouse, pull the Dynamics record, cross-reference the documentation, compute the answer, format it as a report, publish it to the dashboard. The user is the *specifier*, not the *builder*. That's the inversion.

## IT Would Actually Love This

The single most important insight in this paradigm: **IT would love this**, and Citizen Developer was secretly an IT nightmare.

Under Citizen Developer, IT was the reluctant parent cleaning up shadow apps, governing rogue flows, revoking access from departed employees who left Power Apps scattered across five environments, and fielding "my app broke" tickets for things they never built. IT got all the responsibility and none of the authorship.

Under User Developer, IT reclaims its actual job:

1. **Deploy and operate MCP servers** for every authoritative data source — Dynamics, Fabric, SharePoint, D365 F&O, the ERP, the ticketing system, the HR database. One MCP server per source, each with clearly defined tools, schemas, and access scopes.
2. **Govern access at the data plane** — who can query what, with what filters, with what audit trail. The MCP server is the chokepoint. Every AI call goes through it. Every call is logged. No shadow.
3. **Own the semantic layer** — but it emerges naturally from the work they were already doing. To expose a tool over MCP, you have to describe it: what the table means, what the columns are, what a "sales order" is in this company's language, what "Q3" means in this company's fiscal calendar. The MCP tool descriptions ARE the semantic layer. IT doesn't build it as a separate deliverable — it falls out of the MCP work.
4. **Enforce guard rails** — rate limits, query cost caps, row-level security, PII redaction. All at the MCP layer, enforced once, inherited by every AI that connects.

IT goes from "reluctant platform team for a pile of low-code junk" to "operator of the data plane that powers every answer in the company." Same people, better job, clearer scope, less on-call pain, more strategic leverage. IT would fight for this model if they saw it clearly.

## The Incidental Semantic Layer

This is the quiet genius of the MCP approach.

A traditional enterprise semantic layer (Power BI semantic models, AtScale, Looker LookML, dbt metric layers) is an expensive, explicit deliverable. Someone has to sit down and model the business: what's a customer, what's revenue, what's "active" versus "closed won," how do the tables join, what are the blessed KPIs. It's a project. It costs six figures. It drifts the moment someone changes a source table.

MCP tool definitions require the same information, for a different reason. To expose a tool that an LLM can call, you have to write a tool schema — what the tool does, what the arguments are, what the return looks like, what the fields mean, what the enum values represent, what business concepts they map to. That's a semantic model, written as a side effect of making the tool callable. It's not an extra deliverable. It's the work.

And because LLMs are better at using MCP tools when the descriptions are rich, there's a natural forcing function for IT to keep those descriptions accurate and complete. The tool descriptions ARE the semantic layer, and the "is it good enough?" test is "can the AI get the right answer with these tools?" — which is a way sharper feedback loop than "does the DAX model validate?"

**The semantic layer stops being a project and becomes a property.** It exists because the MCP layer exists. IT can audit it, version it, enforce it, but they don't have to build it as a separate track of work. The two things collapse into one.

## The Example, Unpacked

> "Hey what is the next quarter's run rate on part #21434 and what will the shortages in that supply do to my sales orders in Q3."

Decompose this question. It needs:

1. **Current run rate on part #21434** — query to D365 F&O or the manufacturing warehouse (supply side)
2. **Forecasted run rate for next quarter** — query to Fabric or the planning system (demand side)
3. **Open sales orders with part #21434 as a BOM line for Q3** — join across D365 CE (sales orders) and D365 F&O (BOM explosions)
4. **Methodology check** — "what's the right way to calculate 'shortage impact on sales orders'?" — query to mcp.learn.microsoft.com for Microsoft's official D365 supply planning docs, or to an internal methodology library
5. **Synthesis** — compose a short answer with the numbers, the risk, and the recommendation

Under Citizen Developer, this question is a six-week project:
- Data engineer builds a Power BI dataset joining supply and demand
- BI analyst builds a report with filters for Part #
- Business analyst interprets the numbers
- User files a ticket, waits, reads the report, asks a follow-up, ticket goes back
- Repeat until Q3 is over

Under User Developer, this is one voice command and a 30-second LLM turn:
- Agent receives the question
- Calls `dynamics.query_supply(part="21434", horizon="next_quarter")`
- Calls `fabric.query_demand(part="21434", period="Q3")`
- Calls `dynamics.query_sales_orders(bom_includes="21434", period="Q3")`
- Calls `mcp_learn.search(topic="D365 FO supply shortage impact methodology")`
- Synthesizes the answer, formats it, publishes the card to the dashboard
- Pierre sees it

No Power BI. No BI team ticket. No Citizen Developer bootcamp. No "let me circle back with the team." The question is answered because the data plane is addressable and the AI can reason across it.

## Why Copilot-in-D365 Isn't This

Microsoft's pitch for Copilot in Dynamics 365 is "AI in your CRM." That's useful, but it's architecturally limited in a way the MCP model isn't: **Copilot lives inside a single app context.** Copilot in D365 CE can see CE data. Copilot in D365 F&O can see F&O data. Copilot in Power BI can see the semantic model it's embedded in. None of them can reach across the app boundary without Dual Write, a custom connector, or the tenant's overworked integration team.

An MCP-native agent with connections to D365 CE, D365 F&O, Fabric, and Microsoft Learn can answer the cross-domain question in one turn. It doesn't care which app owns which table — it calls the MCP tool, gets the data, moves on. The model collapses the app silos that Microsoft's own architecture created.

That's not a small difference. That's the difference between "AI that helps you operate the app you're in" and "AI that actually answers your business question." The first is a feature. The second is a paradigm.

## What IT Does Not Do Anymore

Equally important: things IT stops having to do under User Developer.

- **Build Power BI reports on request.** No more "please build me a report showing X." The AI composes the query live. IT only maintains the MCP tools and access policy.
- **Maintain a zoo of Power Apps.** No more governance sprawl. If a workflow is worth keeping, it becomes a dashboard card fed by a scheduled agent call, not a Power App someone has to own.
- **Write DAX for end users.** No more "can you help me with this DAX measure." The AI writes the query against the MCP data source directly, in whatever query language the source speaks.
- **Curate a central semantic model as a project.** The MCP tool descriptions are the semantic model. It's a property, not a deliverable.

What IT keeps doing — and does better:

- Access control, audit, data classification, retention policy
- MCP server deployment and uptime
- Schema governance and change management
- Security at the data plane
- Network isolation (see Understanding 0005 — the box in the office with enterprise VPN)

It's a strictly better job. Less thankless maintenance, more strategic authorship of the data plane.

## Impact

- **Kills:** "Citizen Developer" as a go-to-market positioning. Power Apps as an end-user tool. Power BI as the default BI layer. The BI team as a bottleneck. Copilot Studio's entire reason to exist. Six-figure semantic-model consulting engagements.
- **Enables:** Voice-native executive queries that cross app boundaries. IT as the data-plane operator instead of the reluctant app landlord. Single-tenant enterprise deployments where the whole stack lives behind one VPN. A real answer to "what does AI actually change about my IT department."
- **Method:** MCP servers as the data plane + LLM agent as the reasoning layer + composable front-end (see 0005) as the publishing destination. Three layers, no middleware between them.
- **Proof needed:** A working prototype with at least two MCP connections (Dynamics + Fabric, or Dynamics + Microsoft Learn) answering a cross-domain executive question in one turn, with the answer published to the dashboard. Candidates: Nutanix engagement, AMD Montreal, Powered Wild's own data.
- **Sales implication:** This is the real Alithya pitch. Not "we'll build you Power Apps." It's "we'll stand up your MCP data plane, install the AI layer, deploy the composable front-end, and your exec team starts asking questions that used to take six weeks and get answers in thirty seconds. IT keeps the authority. Users get the outcomes. Nobody has to learn DAX."

## Two Minutes, Not Six Weeks

The time-to-insight argument is the one executives actually feel. Under the Citizen Developer / Power BI / BI-team-ticket regime, the path from question to answer is roughly:

1. Executive has a question
2. Question gets batched into a BI team intake form
3. Data engineer models the source tables (days)
4. BI analyst builds the visual and runs it past the executive (days)
5. Executive asks a follow-up; back to step 3
6. Six weeks later, the first version of the answer exists
7. By the time it arrives, the business has moved; the answer is already stale

Under User Developer + MCP + composable front-end:

1. Executive has a question
2. Executive talks the question into Skippy
3. Agent composes queries across the MCP data plane in one turn
4. A sweet graph + a visual report + a one-paragraph summary lands as a card on the dashboard
5. Executive reads it on the iPad two minutes later

That's not "a faster version of the old workflow." That's a completely different order of magnitude. Orders of magnitude changes don't just speed things up — they change what's *possible*. When the cost of asking a question drops from six weeks to two minutes, executives stop batching questions. They stop saving them up for quarterly reviews. They ask as they think. The decision loop tightens from quarterly to real-time.

**Unit economics:** One Power BI report costs a BI analyst's time (days to weeks), plus the data engineer who builds the source model (days), plus Power BI Premium capacity, plus the ongoing maintenance drag every time a source schema changes. Call it $5K–$50K per net-new report when you fully load it. One MCP-served agent answer costs a few cents of LLM inference plus a trivial query cost at the MCP data plane. Call it $0.05. That's a **100,000× cost delta** on a per-answer basis, before you even count the time-value of the decision being available same-day instead of six weeks later.

And the agent answer is not worse. It is often *better*, because it can cross app boundaries Power BI couldn't reach — CE sales orders joined to F&O BOM explosions joined to Fabric forecasts joined to the Microsoft Learn methodology for how the calculation should actually be done. Power BI could never reach across those sources without a Dual Write project and a semantic model refactor. The agent does it in one turn.

## The Pizza-For-Everyone Problem

Pierre's phrase, and it's the sharpest critique of enterprise BI dashboards ever put in six words.

Traditional enterprise dashboards are built as **one pizza for the whole team**. The BI team tries to anticipate every possible slicer, filter, drill-down, and view so that a hundred different users with a hundred different questions can all find what they need in the same artifact. The result is always a monstrosity: forty visuals on one page, seventeen slicers in the top nav, six bookmarks down the side, three "view" toggles, four drill-through pages, and the one KPI the executive actually cares about is on page seven behind a filter nobody sets correctly. The dashboard is simultaneously too busy and too shallow — too many elements fighting for attention, none of them personalized to the reader.

This failure is structural, not a skills gap. The BI team is doing their job correctly given the constraints. Every additional dashboard costs weeks to build and maintain, so they're forced to serve the maximum number of users per dashboard they ship. "Pizza for everyone" is an economic consequence of the build cost, not a design choice.

The composable front-end model destroys the economic constraint. Every question gets its own card. Every card is cheap to produce because the agent composes it live against the MCP data plane and publishes it via `publish-report.sh` or `publish-pdf.sh`. There is no "one dashboard to rule them all." There are N cards, each answering one specific question for one specific reader, each fresh because the underlying query runs on demand.

The executive's "one number I watch" is the *only thing* on its card. No burial. No page seven. No slicer to set correctly. The card exists because the executive asked for it, and it disappears (or gets archived) when the executive stops caring.

This is why BI dashboards failed at the executive level in a way nobody wanted to admit: they were designed for the median user, and **the median executive does not exist**. Every CEO, every CFO, every COO, every VP of Sales has a different "one number I watch" — and their number changes week to week depending on what fire they're fighting. Serving them with one shared Power BI workspace was always going to fail. Giving each of them their own auto-generated, voice-driven, continuously-refreshed set of personal cards is what they actually needed the whole time. The composable front-end finally makes it affordable to build that.

No meeting. No RFP. No making a pizza for everyone. No Power BI so complex that the one number you watch is buried on page seven.

## Power BI Is 2001 Tech

The historical-provenance argument is the kill shot.

Power BI's lineage, in order:

- **ProClarity** — founded 1995, acquired by Microsoft in 2006. The OLAP analytics layer that became the heart of Microsoft PerformancePoint Server. A pre-cloud, cube-based, Analysis-Services-era product designed for a world where "the data" meant "a pre-aggregated Kimball-style cube that the BI team hand-built for you."
- **Dundas Data Visualization** — visualization controls acquired piecemeal by Microsoft and others. Charting from the same era.
- **PerformancePoint Server 2007** — Microsoft's first attempt to glue ProClarity, Dundas, and Excel Services into an executive dashboard product. The mental model: a BI analyst authors a scorecard, executives consume it.
- **Power Pivot** (2010) — an in-memory tabular engine (VertiPaq) embedded in Excel. Replaced the Analysis Services cube with a column-store model, but kept the same "analyst builds, consumer reads" assumption.
- **Power View + Power Query + Power Map** (2012–2013) — Excel add-ins that became the authoring surface.
- **Power BI** (GA 2014, current rebrand 2015) — a web surface wrapped around Power Pivot (VertiPaq) + Power Query (M) + Power View (visuals) + some ProClarity/Dundas DNA for enterprise cred.

Every foundational assumption in this stack predates the transformer architecture (2017), predates cloud-scale warehouses at commodity prices (Snowflake GA was late 2014), predates MCP (November 2024), and predates the current LLM generation. The mental model is fixed at **"a BI analyst builds a semantic model, a consumer reads the report."** That assumption came from ProClarity in 2001 and has never been revisited at the foundation.

It is also **bought technology, stitched together from acquisitions**. Power BI was never designed as a coherent product. It is the DNA of ProClarity wearing Dundas clothes running on a Power Pivot engine with a Power Query ETL layer and a Power View front-end, all rewrapped for the browser in 2014 and continuously patched since. When a product is stitched together from five acquisitions across fifteen years, its internals will never be as clean as something built from scratch for the current primitives. The seams show up as complexity, inconsistency, performance edges, and the permanent need for a BI team to translate business questions into DAX measures that navigate the Frankenstein semantic model.

It was always going to lose to something built from scratch for the current primitives: **LLM reasoning + MCP tool calling + composable front-end**. That something doesn't need a pre-built semantic model because the LLM reasons over the MCP tool descriptions. It doesn't need DAX because the query runs in the source system's native language. It doesn't need a BI analyst because the user talks.

Microsoft's own Fabric pitch quietly acknowledges this. Fabric is the attempt to unify the warehouse layer (OneLake) so that the next generation of tools — including MCP servers and AI agents — can plug into it without carrying Power BI's legacy forward. Fabric is positioned as the data plane. Power BI is positioned as "one of the workloads" on top of Fabric. Read between the lines: Microsoft is quietly conceding that Power BI is the legacy consumer layer, and Fabric is the future infrastructure. Fabric is the data plane this milestone predicts IT will own. **Power BI is the surface Fabric will bury.**

**Strategic implication:** Don't fight Power BI. Don't sell against it head-on. Watch it age out. The business model is 2001. The acquisition provenance means its internals will never be refactored. The customers that matter — the ones making buying decisions in 2027 and 2028 — will be on User Developer by the time their Power BI Premium renewal cycles come around, because their competitors will be getting two-minute answers on their iPads and they will be getting six-week reports on their laptops. The migration will happen because the economics of asking questions changed, not because anyone marketed against Power BI.

The Alithya practice positioning: let the Power BI business stay on the P&L while it drifts down. Invest the new dollars in MCP-native data plane work. Package it as "User Developer Enablement." When a customer calls us to build their next Power BI report, upsell them to the MCP + agent + composable front-end model for a quarter of the cost and two hundred times the speed. The ones who say yes become the reference architectures. The ones who say no renew Power BI for another three years and come back when their competitors start eating them alive.

## Related

- `0005-dashboard-is-the-executive-surface.md` — the publishing layer this insight sits on top of
- `memory/projects/project_do_nothing_company.md` — the commercial framing
- `memory/projects/project_mep_origin_story.md` — the consulting methodology this plugs into (MEP as the engagement shell, MCP as the data plane)
- `skills/d365/` (Garrus) — the D365 knowledge side of the stack
- `CLAUDE.md` — Dynamics/CE/F&O/MCP Service glossary entries already point this direction

## Open Questions

1. Who's the first customer to see this model demonstrated live? AMD Montreal (Ismail already thinks in MCP terms) or Nutanix (Evans/Olivia need the executive-query pitch)?
2. Where does Microsoft land on this? Do they embrace MCP-native access to Dynamics and Fabric (the Jaive/MCP Service team is pushing this direction) or do they try to lock it behind Copilot Studio? The answer shapes the next 18 months of the D365 FS practice.
3. How does this interact with Fabric's own "OneLake" pitch? Fabric is arguably the right data plane for the MCP layer to sit on — it already unifies the warehouses. The stack might be Fabric + MCP on top of Fabric + agent + dashboard.
4. What's the minimum viable MCP server for a D365 CE/F&O connection that a mid-market customer could deploy behind their VPN in a week? That's the prototype to build.
