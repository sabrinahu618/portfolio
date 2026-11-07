---
title: About
permalink: /about/
kicker: About
heading: I design for the people on the other side of the screen.
lede: I'm Sabrina, a designer, researcher, and educator building human-centered technology for learning, communication, and social impact.
description: Sabrina Hu's story across education, design, and AI for social impact.
body_class: about
---

<figure class="about__photo">
  <img src="{{ '/assets/img/about/candid.webp' | relative_url }}" alt="Sabrina sitting at an outdoor table in a park on a sunny spring day, smiling at the camera." width="720" height="864" loading="lazy">
</figure>

## It started with a bottle cap

My love for technology and problem-solving took off with my first invention: a solar-powered cap that purifies water with UVC light, built to help my community in Florida during hurricanes. I spent that year designing, building, testing, failing, and trying again, and I became enamored with turning an idea into something that helps someone. That project, [Solar Cap]({{ '/work/solar-cap/' | relative_url }}), followed me to MIT, where it grew into a team effort across D-Lab and the Urban Risk Lab.

## Learning how people learn

At MIT I studied **Media Studies and Computer Science** (Course 21E), because I didn't want to choose between understanding people and building for them. Classes like *Learning, Media & Technology* and *Imagination, Computation & Expression* sat next to *Artificial Intelligence* and *Human-Centered Design*, and the overlap became my home.

Teaching made it concrete. I tutored about 500 beginners in MIT's intro Python courses. At [Haileybury]({{ '/work/haileybury/' | relative_url }}) in the UK, I designed and taught a two-week web development course for 24 students who had never coded, and every one of them launched a website. I also studied learning from the research side at iCivics, interviewing stakeholders about why PDF-based classroom readings shut some students out.

## Designing for connection

My research keeps coming back to how people stay connected. At the [MIT Digital Humanities Lab]({{ '/work/digital-humanities-lab/' | relative_url }}), I interviewed 16 Ukrainian scientists living in exile across 15 countries, then helped build a platform that served 224 of them. At [NOMO]({{ '/work/nomo/' | relative_url }}), I surveyed more than 110 students about their relationship with social media, which raised questions about attention and wellbeing I'm still thinking about.

## Shipping AI that people can trust

After graduating, I became a product manager. At [Samsara]({{ '/work/samsara/' | relative_url }}) I led a messaging platform for 800,000 drivers and built the framework we used to judge whether an AI assistant's answers were good enough to ship. At [Nooks]({{ '/work/nooks/' | relative_url }}) I defined an autonomous AI agent, including when it should step back and hand off to a person. That work taught me that the hardest questions in AI aren't about the model. They're about the people on the other side of it.

## What I want to explore next

{% include todo.html note="This section is my draft of the questions your work points toward. Rewrite it in your own voice; faculty will read it closely." %}

- **When should AI step back?** Good teachers know when to let a student struggle. I want to design AI tutors and companions that build people's own abilities instead of replacing them.
- **How do we measure what AI does to us?** I've built rubrics for whether an AI's answers are good. I want to evaluate AI by its effect on the people using it: their learning, confidence, and relationships.
- **How can technology hold communities together?** From exiled scientists to drivers on the road, I've seen how much depends on the right channel at the right moment.

## A timeline

<ol class="timeline">
{%- for t in site.data.timeline %}
  <li><span class="timeline__when">{{ t.when }}</span><span class="timeline__what">{{ t.what }}</span><span class="timeline__note">{{ t.note }}</span></li>
{%- endfor %}
</ol>

## Beyond the work

You can spot me in the wild eating honey lavender ice cream, strumming my ukulele, sipping hot matcha, or dramatically staring off into space. I'm based in {{ site.data.profile.location }}.

{% include contact-links.html %}
