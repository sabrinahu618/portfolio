---
title: Keeping 800,000 drivers connected
org: Samsara
summary: Leading a 0-to-1 messaging and calling platform for 800,000 drivers, and building the framework that decides when an AI assistant's answers are good enough to ship.
themes: [communication]
order: 3
featured: true
years: Aug 2025 – May 2026
role: Associate Product Manager
audience: Truck drivers on the road and the dispatchers and fleet teams who support them.
team: Engineering, design, and partner teams
methods: [Prototyping, LLM evaluation, API design]
tools: [Figma, Figma Make, LLM evaluation rubrics, Automated regression tests]
cover: /assets/img/samsara/inbox-thread.webp
cover_width: 1600
cover_height: 873
cover_alt: "The Samsara dashboard's Messages view. A list of conversations on the left includes Safety Team Updates, Admins, Northeast Region (with a severe weather warning), and All Drivers (a reminder to verify logs). The open Safety Team Updates channel shows mentions, replies, a thumbs-up reaction, a Proof of Delivery PDF, and a photo of a loading dock."
cover_caption: "The new messaging experience in the Samsara dashboard: channels for teams, regions, and all drivers, with replies, reactions, files, and photos. Demo data."
highlights:
  - value: "800K"
    label: monthly active drivers on the platform
  - value: "5,000+"
    label: attendees at the launch, Samsara's annual conference
  - value: "$300K+"
    label: in annual recurring revenue unlocked by integrations
---

{% include todo.html note="Double-check that everything here is approved to be public. It only uses what's on your resume." %}

## The problem

Drivers spend their days on the road, away from the dispatchers and fleet teams they depend on.

{% include todo.html note="One or two sentences on what was broken before (for example, personal phones or scattered tools) and why it mattered for safety or the job." %}

## Who it was for

Drivers who need a quick, safe way to reach their team while working, and the fleet teams on the other end of the conversation.

## Process

### A messaging platform, from zero to launch

I led the 0-to-1 development of a messaging and calling platform for 800,000 monthly active drivers. To get leadership aligned on a new direction quickly, I prototyped the experience in Figma Make, so people could click through it instead of reading a spec.

I also designed the communications API layer underneath it (contracts, routing, and identity) so partners could build on top of it.

{% include figure.html src="/assets/img/samsara/compose.webp" alt="A Compose a message dialog over the Messages view, with a recipient menu offering three options: Driver, Tag, and User." width="1600" height="872" caption="Composing a message: send to one driver, everyone with a tag such as a region or team, or another user." %}

{% include figure-pair.html src1="/assets/img/samsara/driver-thread.webp" alt1="The Driver App in dark mode showing the Safety Team Updates channel, with messages from teammates, an @mention, and the driver's reply, Hello team, marked as read." src2="/assets/img/samsara/driver-attach.webp" alt2="The Driver App's attachment menu with four options: Take a photo, Take a video, Photo library, and Files." width="701" height="928" caption="The driver's side in the Driver App: reply in a channel, or share a photo, video, or file from the road." %}

{% include figure.html need="A Figma Make prototype screen, if you can share one, to show how you aligned leadership." %}

### Deciding when an AI assistant is good enough

Samsara's AI Driver Assistant answers questions for drivers on the road. A wrong or confusing answer there has real consequences, and "it looks fine in the demo" isn't a standard.

I built an LLM evaluation framework for the assistant: quality rubrics that defined what a good answer looks like for a driver, and automated regression tests to catch it when a change made the answers worse.

{% include todo.html note="Give one example of a rubric dimension (for example, safe to read while driving, or accurate to fleet policy), and how the framework changed a launch decision." %}

## Outcome

The platform launched at Samsara's annual conference, in front of more than 5,000 attendees. The API layer unlocked more than **$300K in annual recurring revenue** from integrations.

## Reflection

{% include todo.html note="Write this yourself. Suggested angle: an evaluation rubric encodes a judgment about what's good for the person on the other end. What would it mean to evaluate AI by its effect on people, not just the quality of its answers?" %}
