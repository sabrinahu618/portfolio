---
title: Automation that's easy to build, and safe to trust
org: Nooks
summary: Turning a confusing, low-adoption workflow product into an AI-assisted experience sales teams could actually use, then defining an autonomous inbound agent that knows when to bring in a human.
themes: [communication]
order: 4
featured: true
years: May – Oct 2026
role: Product Manager
audience: Sales teams who wanted to automate repetitive prospecting work but struggled to set up automations themselves.
team: Engineering, design, and customers; the inbound agent spanned 3 engineering teams and 4 enterprise design partners.
methods: [Customer interviews, Sales rep observation, Funnel analysis, Co-design with design partners, Customer enablement]
tools: [Figma, Salesforce]
cover: /assets/img/nooks/plays-editor.webp
cover_width: 1600
cover_height: 913
cover_alt: "The Nooks Plays editor for a draft workflow called Competitor renewal. A palette on the left lists steps to add: Trigger, AI actions (Agent, AI Prospecting, AI Email), and Condition. On the right, the workflow starts with a trigger that fires when an account's Competitor Renewal signal is triggered, followed by an AI Prospecting step set to find up to 20 prospects per account across 7 personas."
cover_caption: "The Plays editor: teams build a workflow from triggers, AI actions, and conditions. Here, a Competitor Renewal signal on an account kicks off AI prospecting. Image: Nooks."
highlights:
  - value: "2.6×"
    label: Plays adoption in six weeks
  - value: "70%"
    label: fewer workflow failures
---

{% include todo.html note="Before publishing: confirm the metric definitions (what counts as adoption, what counts as a failure, and the baseline and time window for each), and that everything on this page is approved to be public. Also check the end date: your resume says October, your notes say September." %}

I owned two connected initiatives at Nooks. The first made an existing automation product, **Plays**, something customers could actually use. The second extended it into **autonomous inbound automation**: AI agents that qualify, research, contact, and route new leads, and know when to hand off to a person. They share a product and a question (how much should people have to do, and how much should AI do on their behalf?), but their outcomes are separate, so I've kept them apart below.

## Part 1 · Plays: making automation easy to build

### What Plays was

Plays sat between a company's CRM and its sales outreach. Instead of a rep manually researching every new prospect, writing an email, and enrolling them in a sequence, a team could set up a workflow that did it automatically. A typical Play for inbound follow-up:

1. **Trigger:** a lead in Salesforce becomes a marketing-qualified lead.
2. **Research:** AI gathers context about the person and their company.
3. **Personalization:** AI drafts an individualized email.
4. **Execution:** the email is sent and the prospect is enrolled in a sequence.
5. **Follow-up:** the prospect moves into calls, emails, texts, and LinkedIn outreach.

### The problem: automation that asked for too much work

When I joined, Plays was in beta. The idea was compelling, but customers were confused by it and adoption was low. Through customer interviews and watching sales reps do their actual work, I found that the problem wasn't demand. Customers wanted automation. **Setting up the automation was itself the hard, manual task.** A product built to eliminate busywork was asking people to do a lot of it before they saw any benefit.

That showed up in a few ways:

- **Getting started:** customers struggled to understand how to create and configure a Play.
- **Complexity:** building one meant understanding the workflow logic underneath it.
- **Reliability:** workflows failed, which undermined trust in letting automation act on their behalf.
- **Legibility:** when the AI did something unexpected, users had no easy way to see why or to tell it that it was wrong.

{% include todo.html note="Add one or two specific findings from discovery: how many customers or reps you talked to, and a moment or anonymized quote that changed your thinking." %}

### What we changed

I shifted the strategy from asking customers to configure every step themselves to letting AI help them build. I think about it in three parts:

- **Generation:** **AI-assisted Play building**, including a natural-language Plays Assistant. Users describe the sales process they want to automate in their own words (for example, which leads to target, how to research them, what kind of outreach to send, and which sequence to add them to), and the assistant turns that intent into a workflow.
- **Transparency:** showing users what the AI is doing and why, so automation isn't a black box. This shipped in GA.
- **Correction:** a way for users to reject an AI decision and explain what was wrong, so the system could be corrected rather than abandoned. We explored this, but it didn't ship in GA.

{% include figure.html src="/assets/img/nooks/plays-assistant.webp" alt="The Create Play screen with the Build with assistant tab selected. A text box asks 'What should this play automate?' with the example 'when an account books a meeting, alert the AE in Slack and pause my outbound to it.' Below are one-click starting points: Inbound, Closed Lost, and Job Change." width="1197" height="609" caption="Building with the assistant: describe what a Play should automate in plain language, or start from a one-click template. Image: Nooks." %}

I also scoped Slack alerts to make automation visible where reps already work. A Play can now message the assigned rep or a channel directly, including outputs from earlier steps such as an agent's response, so nobody has to keep checking the product to know what ran.

{% include figure.html src="/assets/img/nooks/slack-alert.webp" alt="The Plays editor with a workflow of Draft AI Email, then Add to Sequence (assigned round robin to an Inbound Lead - Demo Request sequence), then a Slack Alert step. A side panel configures the Slack Alert to send to the user assigned in the Add to Sequence step, with a message box that can include variables from earlier steps." width="1600" height="1072" caption="A Slack Alert step tells the assigned rep the moment a Play acts, using details from earlier steps. Image: Nooks." %}

### Diagnosing failures

To bring failures down, I first sorted them by cause, because each kind needs a different fix:

- **Configuration:** triggers, conditions, or actions set up incorrectly.
- **User error:** customers building workflows incorrectly because the builder was confusing.
- **AI:** incorrect outputs, malformed data, or not following instructions.
- **Integration:** Salesforce or other third-party API failures.
- **Execution:** steps timing out, failing to run, or completing out of order.
- **Product bugs:** platform defects unrelated to how a customer set things up.

The first two are design problems. A builder that's easy to misconfigure will be misconfigured, and AI-assisted building and a clearer editor go straight at them. The rest needed engineering, so I prioritized them with the team and closed the workflow gaps behind them.

{% include todo.html note="Which causes were most common, and which fixes moved the 70%? If only some of these six actually came up, keep just those; a shorter, specific list is more convincing than a complete one." %}

### Helping customers adopt it

I also worked on adoption outside the product itself, through onboarding documentation, a customer webinar, and walkthroughs on customer calls. A new kind of tool only gets adopted if people understand how it fits into the way they already work.

### Outcome

Plays went from beta to general availability. In the six weeks after AI-assisted building launched, **adoption grew 2.6×** and **workflow failures fell 70%**.

{% include todo.html note="If the definitions check out, add customer activation (about 11 to 120 customers with Play activity) and live Plays (about 50). Keep each metric clearly labeled; they measure different things." %}

## Part 2 · Autonomous inbound: from automation to agents

### The opportunity

Companies spend heavily to generate inbound interest, but turning an inbound lead into a real sales conversation is often slow, fragmented, and manual. Analyzing the inbound funnel and speed-to-lead showed where leads were falling through the cracks. It also pointed to an ambitious goal: **double the meetings booked from the same volume of leads.**

### Designing the agent

I defined a 0-to-1 autonomous inbound experience and scoped it across three engineering teams. The agent covers the full path from a new lead to a booked meeting:

1. **Scoring:** decide which leads to prioritize.
2. **Research:** gather context on the lead and their company.
3. **Outreach:** write personalized messages.
4. **Routing:** send the lead to the right sales rep.
5. **Scheduling:** help book the meeting.
6. **CRM updates:** keep records accurate.
7. **Human escalation:** bring in a person when the agent shouldn't act on its own.

The most important design work was on the limits. Each customer could set guardrails specific to their business, and escalating to a human was a deliberate part of the design, not a fallback. I recruited four enterprise design partners and co-designed the first version with them.

The agent built directly on Plays. An event triggers a Play, and the prospect is added to a sequence for an SDR to work. The sequence runs automatically until the prospect replies, which takes them out of it. When the reply is an email, the agent can respond on its own, unless sensitive information is involved. Then it escalates to a person.

{% include nooks-agent-flow.html %}

{% include todo.html note="Where did this end up: shipped, in beta with design partners, or still in development? And can you name the design partners publicly? (Check with Nooks before listing Toast, Deel, ServiceTitan, or Vanta.)" %}

## Reflection

{% include todo.html note="Rewrite this in your own voice. It's the strongest link to the Media Lab." %}

Both projects taught me the same lesson from opposite directions. AI only helps when it genuinely reduces the effort a person has to put in. A powerful tool that takes hard work to set up goes unused. And people only hand work to an agent they can understand and correct. Transparency, correction, and knowing when to hand off aren't features added at the end; they're what makes people willing to trust automation at all. I want to keep studying that line: when AI should act, when it should ask, and when it should step back.
