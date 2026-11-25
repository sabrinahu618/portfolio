---
title: Keeping 800,000 drivers connected
org: Samsara
summary: Rebuilding how drivers, dispatchers, and fleet admins talk to each other, and learning in beta that a platform is only as good as what customers can actually set up.
themes: [communication]
order: 2
featured: true
years: Aug 2025 – May 2026
role: Associate Product Manager
audience: Truck drivers on the road, and the dispatchers, safety managers, and admins who coordinate with them.
team: 4 engineers, plus design, mobile, platform, and go-to-market partners
methods: [Customer calls, App review analysis, Usage data analysis, Prototyping, Beta rollout, LLM evaluation]
tools: [Figma, Figma Make, Databricks, SQL, Mixpanel]
cover: /assets/img/samsara/inbox-thread.webp
cover_width: 1600
cover_height: 873
cover_alt: "The Samsara dashboard's Messages view. A list of conversations on the left includes Safety Team Updates, Admins, Northeast Region (with a severe weather warning), and All Drivers (a reminder to verify logs). The open Safety Team Updates channel shows mentions, replies, a thumbs-up reaction, a Proof of Delivery PDF, and a photo of a loading dock."
cover_caption: "The new messaging experience in the Samsara dashboard: channels for teams, regions, and all drivers, with replies, reactions, files, and photos. Demo data."
highlights:
  - value: "800K"
    label: monthly active drivers on the platform
  - value: "~50"
    label: more customers enabled in the two weeks after the onboarding fix
  - value: "$300K+"
    label: in annual recurring revenue unlocked by integrations
---

## The problem

Samsara's existing messaging was built around a single pattern: one driver, chatting with all of their admins, in text only. That isn't how fleets actually communicate. Dispatchers need to reach a whole region before a storm. Safety teams need to send announcements no one can reply-all to. Drivers need to share photos and files, like proof of delivery, and sometimes need to message hands-free.

So customers worked around it, coordinating across text, email, Slack, WhatsApp, Teams, and phone calls. Communication between drivers, dispatchers, and admins was fragmented across all of those tools.

## Who it was for

Drivers who need a quick, safe way to reach their team while working, and the dispatchers, safety managers, and admins on the other end of the conversation.

## Process

### Research: listening to fleets and drivers

I led **15 customer calls** with fleets to understand how they really used messaging, from roadside-inspection blitzes to weekly safety tips and company announcements. The same priorities kept coming up: rich media, acknowledgment that a message was read, in-cab audio, and keeping message history for 6 to 12 months.

To hear from drivers directly, I wrote a biweekly Driver App feedback report, analyzing **6,500 app reviews** to surface the most common pain points alongside real driver quotes. I also used usage data to find the fleets that relied on messaging most heavily, and recruited them as early beta customers.

### Design and build: from one chat to a platform

I owned the 0-to-1 messaging and calling platform with a team of four engineers. To get leadership aligned on a new direction quickly, I prototyped the experience in Figma Make, so people could click through it instead of reading a spec. The platform added:

- **Channels and group conversations**, for teams, regions, and the whole fleet
- **Membership and permission controls**, including read-only channels for announcements
- **Rich media**: photos, videos, and files
- **Voice and hands-free messaging** for drivers on the road
- **Messaging APIs** (contracts, routing, and identity) so partners could build on top of it

{% include figure.html src="/assets/img/samsara/compose.webp" alt="A Compose a message dialog over the Messages view, with a recipient menu offering three options: Driver, Tag, and User." width="1600" height="872" caption="Composing a message: send to one driver, everyone with a tag such as a region or team, or another user." %}

{% include figure-pair.html src1="/assets/img/samsara/driver-thread.webp" alt1="The Driver App in dark mode showing the Safety Team Updates channel, with messages from teammates, an @mention, and the driver's reply, Hello team, marked as read." src2="/assets/img/samsara/driver-attach.webp" alt2="The Driver App's attachment menu with four options: Take a photo, Take a video, Photo library, and Files." width="701" height="928" caption="The driver's side in the Driver App: reply in a channel, or share a photo, video, or file from the road." %}

### What went wrong in beta

We enabled the first beta for about 15 to 20 customers, and it didn't go the way we hoped. The platform could do far more than the old chat, but that was the problem: the new interface and all of its configuration options overwhelmed customers, and some asked us to roll back.

The capability was there. What was missing was a way in. So I gave customers a better starting point in two ways. I added **self-serve defaults to onboarding**, and I led onboarding sessions that walked fleets through the new messaging experience and gathered their feedback. Every fleet now starts with sensible default channels, like a company-wide announcements channel and a direct line from each driver to their admins, so drivers know immediately who to message and admins can adjust from a working setup instead of a blank one.

After that change, we enabled **about 50 more customers in the following two weeks**.

### Deciding when an AI assistant is good enough

Samsara's AI Driver Assistant answers questions for drivers on the road. A wrong or confusing answer there has real consequences, and "it looks fine in the demo" isn't a standard.

I built an LLM evaluation framework for the assistant: quality rubrics that defined what a good answer looks like for a driver, and automated regression tests to catch it when a change made the answers worse. It moved the team from anecdotes toward measuring quality systematically.

{% include todo.html note="Optional: give one example of a rubric dimension (for example, safe to read while driving, or accurate to fleet policy)." %}

## Outcome

The beta grew from its first 15 to 20 customers, with about 50 more enabled in the two weeks after onboarding defaults shipped. With that foundation in place, the new messaging platform launched at Samsara's annual conference, in front of more than 5,000 attendees. The messaging API unlocked more than **$300K in annual recurring revenue** from integrations.

## Reflection

More capability made the product harder to adopt. The new platform could do far more than the old chat, but every new option was one more decision a busy fleet admin had to make before their drivers could send a single message. Adding features wouldn't have fixed that. A better starting point did: defaults that worked out of the box, and onboarding sessions that showed customers how the platform fit the way their fleet already communicated.

I learned the same lesson again at Nooks, from a different side. Whether it's a messaging platform or an AI workflow builder, the setup is part of the product. Defaults are design decisions about how people should communicate, and getting them right matters as much as anything you build on top.
