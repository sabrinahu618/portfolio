---
title: An AI agent that knows when to hand off
org: Nooks
summary: Taking Nooks' inbound workflow automation from beta to launch, and defining an autonomous agent built to bring in a human at the right moment.
themes: [communication]
order: 4
featured: true
years: May – Oct 2026
role: Product Manager
audience: Sales teams responding to inbound prospects, and the enterprise customers who need to trust the AI doing that work.
team: 3 engineering teams and 4 enterprise design partners
methods: [Customer interviews, Workflow observation, Co-design with customers, Prototyping]
tools: [Figma]
cover: /assets/img/nooks/plays-workflow.webp
cover_width: 818
cover_height: 750
cover_narrow: true
cover_alt: "A Nooks Plays workflow built from four connected steps: a trigger when an inbound prospect arrives, a Research Agent that looks up the prospect and account, a Draft AI Email step, and an Add to Sequence step, with an Add Step button below."
cover_caption: "An inbound Play: when a prospect shows interest, AI researches them, drafts an email, and adds them to a sequence. Image: Nooks."
highlights:
  - value: "2.6×"
    label: adoption in 6 weeks after AI-assisted building launched
  - value: "70%"
    label: fewer failed workflows
  - value: "4"
    label: enterprise design partners co-designed V1
---

{% include todo.html note="Double-check that everything here is approved to be public. It only uses what's on your resume." %}

## The problem

Nooks helps sales teams turn inbound interest into action. Its workflow product, Plays, lets a team automate everything that happens after a prospect raises their hand: research the person and their account, draft a personalized email, and add them to a sequence while their intent is still high. Plays was powerful but hard to set up, and too many workflows failed. Customers also wanted an agent that could act on its own, but only within limits they could trust.

{% include todo.html note="Check this framing: was 'hard to set up, too many failed workflows' the core problem you found in research? I inferred it from your results." %}

## Who it was for

Sales teams who want AI to take repetitive work off their plates, and the enterprise customers who need control over what an autonomous agent is allowed to do.

## Process

### Research: watching people build

I watched customers build workflows and interviewed them about where they got stuck. That research led to **AI-assisted Play building**, where AI helps people set up a workflow instead of making them start from a blank page. I took Plays from beta to general availability.

### Design: deciding the agent's limits

Then I defined a 0-to-1 **autonomous AI agent**. The most important design decisions were about its limits: when it should hand off to a human, and how each customer could set guardrails specific to their business.

{% include figure.html need="A simple diagram of the agent's decision flow: act, ask, or hand off to a human." %}

### Build: co-designing with customers

I co-designed the first version with four enterprise design partners and led execution across three engineering teams.

## Outcome

AI-assisted building drove **2.6× adoption in six weeks** and **70% fewer failed workflows**.

{% include todo.html note="Add where the autonomous agent ended up: shipped, in beta with design partners, or still in development." %}

## Reflection

{% include todo.html note="This is the strongest link to the Media Lab, so write it yourself. Suggested angle: designing a handoff is designing a relationship between a person and an AI. When should AI act, when should it ask, and when should it step back?" %}
