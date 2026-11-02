---
title: Designing AI that knows when to hand off
org: Samsara & Nooks
summary: A messaging platform for 800,000 drivers, a framework for judging an AI assistant's answers, and an autonomous agent built to bring in a human at the right moment.
themes: [communication]
order: 3
featured: true
years: 2025–2026
role: Product manager
audience: Truck drivers and the fleet teams who support them (Samsara), and sales teams automating their work with AI (Nooks).
team: Engineering, design, and enterprise customers; at Nooks, 3 engineering teams and 4 design partners.
methods: [Customer interviews, Workflow observation, Prototyping, LLM evaluation, Co-design with customers]
tools: [Figma, Figma Make, LLM evaluation rubrics, Automated regression tests]
cover_need: A diagram works well here if screenshots are confidential, for example the agent's 'hand off to a human' flow sketched simply. I can draw it from your notes.
highlights:
  - value: "800K"
    label: monthly active drivers on the messaging platform
  - value: "2.6×"
    label: adoption in 6 weeks after AI-assisted building launched
  - value: "70%"
    label: fewer failed workflows
---

Over a year and a half as a product manager, I worked on three problems that all came down to one question: **how should AI and people communicate?**

{% include todo.html note="Double-check that everything here is approved to be public. It only uses what's on your resume." %}

## 1. A messaging platform for 800,000 drivers · Samsara

### The problem

Drivers spend their days on the road, away from the dispatchers and fleet teams they depend on.

{% include todo.html note="One or two sentences on what was broken before (for example, personal phones or scattered tools) and why it mattered for safety or the job." %}

### Process

I led the 0-to-1 development of a messaging and calling platform for 800,000 monthly active drivers. To get leadership aligned on a new direction quickly, I prototyped the experience in Figma Make, so people could click through it instead of reading a spec. I also designed the communications API layer underneath it (contracts, routing, and identity) so partners could build on top of it.

### Outcome

The platform launched at Samsara's annual conference, in front of more than 5,000 attendees. The API layer unlocked more than **$300K in annual recurring revenue** from integrations.

## 2. Deciding when an AI assistant is good enough · Samsara

### The problem

Samsara's AI Driver Assistant answers questions for drivers on the road. A wrong or confusing answer there has real consequences, and "it looks fine in the demo" isn't a standard.

### Process

I built an LLM evaluation framework for the assistant: quality rubrics that defined what a good answer looks like for a driver, and automated regression tests to catch it when a change made the answers worse.

{% include todo.html note="Give one example of a rubric dimension (for example, safe to read while driving, or accurate to fleet policy), and how the framework changed a launch decision." %}

## 3. An autonomous agent with a human in the loop · Nooks

### The problem

Nooks helps sales teams automate their work. Its workflow product, Plays, was powerful but hard to set up, and too many workflows failed. Customers also wanted an agent that could act on its own, but only within limits they could trust.

{% include todo.html note="Check this problem framing; I inferred it from your results." %}

### Process

I watched customers build workflows and interviewed them about where they got stuck. That research led to **AI-assisted Play building**, where AI helps people set up a workflow instead of making them start from a blank page. I took Plays from beta to general availability.

Then I defined a 0-to-1 **autonomous AI agent**. The most important design decisions were about its limits: when it should hand off to a human, and how each customer could set guardrails specific to their business. I co-designed the first version with four enterprise design partners and led execution across three engineering teams.

{% include figure.html need="A simple diagram of the agent's decision flow: act, ask, or hand off to a human. Sketch it on paper and I'll redraw it." %}

### Outcome

AI-assisted building drove **2.6× adoption in six weeks** and **70% fewer failed workflows**.

## Reflection

{% include todo.html note="This is the strongest link to the Media Lab, so write it yourself. Suggested angle: evaluation and handoff are the same problem from two sides, knowing what AI does to the people who rely on it. What would you study if you could measure effects on people rather than answer quality?" %}
