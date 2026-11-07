---
title: A home base for exiled Ukrainian scientists
org: MIT Digital Humanities Lab
summary: Designing a platform that helps Ukrainian scientists scattered by the war find each other, keep collaborating, and stay connected to science in Ukraine.
themes: [communication, impact]
order: 4
featured: true
format: short
years: Feb–May 2023
role: Designer
audience: Ukrainian scientists displaced by the war, at home and abroad, and the Ukrainian ministry office working to support them.
team: An MIT Digital Humanities Lab team, advised by Professor Elizabeth Wood (MIT History), with partners at Ukraine's Ministry of Education and Science
methods: [User interviews, Information architecture, UI design, Prototyping]
tools: [Figma, Django, Bootstrap]
cover: /assets/img/dh-lab/mockups.webp
cover_width: 1806
cover_height: 1308
cover_alt: "An overview of about 15 page designs for the platform in blue and yellow: a home page with a mission statement and upcoming events, news and event pages, a network directory, a scholar directory with filters, a map of scholars across Europe, member stories, career advice, and several screens of a find-a-mentor flow."
cover_caption: "The screens I designed: home, news, events, a network and scholar directory, a map of scholars, member stories, and a mentorship flow."
highlights:
  - value: "16"
    label: scientists interviewed in 15 countries
  - value: "224"
    label: scientists served by the platform
links:
  - label: Ukrainian Science Diaspora site
    url: https://ukrdiaspora.nauka.gov.ua/en/
---

## The problem

Before Russia's full-scale invasion, Ukraine had more than 60,000 researchers. Many have since been displaced inside the country or forced abroad, and with research infrastructure badly damaged, many labs and research centers can no longer operate. Ukraine's Ministry of Education and Science launched the Ukrainian Science Diaspora initiative to stay connected with these scientists, support them, and help them eventually return to Ukraine and Ukraine-based programs.

## What we built

Our team built for the ministry's Scholar Support Office, which runs the initiative with the Young Scientists Council. We took on two jobs:

1. **A communication platform** where scientists in the diaspora could network and collaborate with each other and with colleagues still in Ukraine.
2. **A database and interactive map** of scholars who had left Ukraine, so people could find potential collaborators.

## What I did

I started by interviewing **16 exiled scientists living in 15 countries** about what they needed after war and displacement. Then I designed the platform's screens: a home page and mission, news and events, a directory of scholars and organizations with filters, a map of where scholars had settled, member stories, career advice, and a flow for finding a mentor. Our team built the platform in Django and Bootstrap.

The heart of the platform was the two features the ministry asked for: the map and the directory. In both, blue and yellow, the colors of Ukraine's flag, mark scholars who left before and after February 24, 2022, so the ministry could see how the war reshaped the community.

{% include figure-gallery.html src1="/assets/img/dh-lab/map.webp" alt1="Map of Scholars page: a map of Europe with numbered clusters of scholars, blue for those who left before 24 February 2022 and yellow for after, a legend, and filters for field and year of migration." w1="717" h1="1218" src2="/assets/img/dh-lab/directory.webp" alt2="Scholar Directory page: a search bar, filters for location, institution, field, phase, and company, and a list of scholar profiles with name, title, location, and field, each color-coded blue or yellow." w2="435" h2="756" caption="The Map of Scholars and the Scholar Directory, filterable by field, location, institution, and when scholars left." %}

Around them, I designed the pages that make it feel like a community rather than a database: events, news, and members' own stories.

{% include figure-gallery.html src1="/assets/img/dh-lab/home.webp" alt1="Home page: a photo banner, mission statement with a Join the Ukrainian Scientists Network button, goal cards for projects, mentorship, and stories, upcoming events, and sponsors and partners." w1="534" h1="1401" src2="/assets/img/dh-lab/event.webp" alt2="Event page: an event title with venue, time, and registration deadline, an image area, description, registration link, and sidebars for upcoming and past events by month." w2="861" h2="1473" src3="/assets/img/dh-lab/stories.webp" alt3="Exploring the Ukrainian Diaspora page: an introduction, quotes from members in a carousel, and an invitation to share your story." w3="822" h3="1404" caption="The home page, an event page, and a page for members' stories. Placeholder text in the designs." %}

## Outcome

The platform served **224 scientists**, giving the ministry a way to keep a scattered research community in touch with each other and with Ukraine.
