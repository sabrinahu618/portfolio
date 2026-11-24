---
title: About
permalink: /about/
kicker: About
heading: I'm curious about what happens when people and technology meet.
lede: I'm Sabrina. I like asking questions, making things, and figuring out how they might make someone's life a little better.
description: Sabrina Hu's story across education, research, and building technology, and the questions she wants to explore next.
body_class: about
---

<figure class="about__photo">
  <img src="{{ '/assets/img/about/candid.webp' | relative_url }}" alt="Sabrina sitting at an outdoor table in a park on a sunny spring day, smiling at the camera." width="720" height="864" loading="lazy">
</figure>

I've explored this through computer science, education, research, and product development. Lately, I've been thinking a lot about AI: not just what we can build with it, but how it might change the way we learn, think, and connect with one another.

## It started with a bottle cap

My first invention was a solar-powered water purifier I built in high school to help my community during Florida's hurricanes. I spent a year designing, building, testing, failing, and trying again. I loved the process of taking an idea that existed only in my head and figuring out how to make it work in the real world.

That project, [Solar Cap]({{ '/work/solar-cap/' | relative_url }}), eventually followed me to MIT, where it grew into a team effort across D-Lab and the Urban Risk Lab. It was my first experience seeing how engineering, design, and an understanding of people's needs could come together to address a real problem.

## How do people learn?

At MIT, I studied **Media Studies and Computer Science** (Course 21E). I was interested in both how technology works and how people make sense of it. I didn't want to choose between understanding people and building for them.

I got to explore that intersection in the classroom, too. I tutored students in MIT's intro Python courses and designed a two-week web development course for 24 students at [Haileybury]({{ '/work/haileybury/' | relative_url }}) in the UK. None of them had coded before, and by the end, every student had built and launched a website.

At [iCivics]({{ '/work/icivics/' | relative_url }}), I approached learning from a research perspective, interviewing educators and other stakeholders to understand why PDF-based classroom readings created barriers for some students.

These experiences made me curious about more than how we teach technical skills. I started thinking about how the tools we build shape what people are able to understand, explore, and create for themselves.

## How do we stay connected?

I've also spent time exploring the role technology plays in bringing people together.

At the [MIT Digital Humanities Lab]({{ '/work/digital-humanities-lab/' | relative_url }}), I interviewed 16 Ukrainian scientists living in exile across 15 countries. I learned about the challenges of maintaining research collaborations and a sense of community while displaced. Those conversations helped inform a platform that eventually served 224 researchers.

At [NOMO]({{ '/work/nomo/' | relative_url }}), I explored a different side of connection: our relationship with social media. I surveyed 109 students about their social media habits, attention, and wellbeing. I became interested in a question that still sticks with me: how might we design technology that helps people connect without demanding more and more of their attention?

## What happens when AI becomes part of the interaction?

After graduating, I joined the tech industry as a product manager. At [Samsara]({{ '/work/samsara/' | relative_url }}), I led the development of a messaging platform used by around 800,000 drivers and built an evaluation framework for an AI assistant. At [Nooks]({{ '/work/nooks/' | relative_url }}), I worked on AI-powered workflows and helped define an autonomous agent, including when it should act independently and when it should hand control back to a person.

Working on these products gave me a different perspective on the questions I'd been exploring in school and research. I became fascinated by the boundary between human and machine capabilities. When should an AI take initiative? When should it ask for help? How do we design systems that make people more capable rather than more dependent?

I don't think these questions have straightforward answers, and that's part of what makes them exciting to me.

## Questions I'm exploring

I'm particularly interested in a few directions:

- **AI that helps us learn, rather than learns for us.** What would it look like to build AI tutors and companions that know when to guide, when to challenge, and when to step back? I'm interested in systems that help people develop their own understanding and capabilities rather than simply providing answers.
- **Measuring AI's impact on people.** We've gotten increasingly good at evaluating whether AI systems produce accurate answers. But how do we evaluate whether they actually help people? I'd love to explore ways to measure their effects on learning, confidence, independence, and relationships.
- **Technology that brings people together.** From researchers living in exile to students navigating social media, my projects have repeatedly brought me back to questions of connection and community. I'm curious about what new forms of connection become possible as our interactions with technology change.

I'm still figuring out where these questions will lead me. I'd love to keep experimenting, working across disciplines, and building things that help us better understand ourselves and one another.

## A little timeline

<ol class="timeline">
{%- for t in site.data.timeline %}
  <li><span class="timeline__when">{{ t.when }}</span><span class="timeline__what">{{ t.what }}</span><span class="timeline__note">{{ t.note }}</span></li>
{%- endfor %}
</ol>

## Beyond the work

Outside of work, you can usually find me looking for a good scoop of honey lavender ice cream, strumming my ukulele, trying a new matcha spot, or going down an internet rabbit hole. I also enjoy a good hike and occasionally catch myself dramatically staring off into space.

I'm currently based in {{ site.data.profile.location }}.

{% include contact-links.html %}
