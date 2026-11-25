# Sabrina Hu — portfolio

Live at **https://sabrinahu618.github.io/portfolio/**

The site is built with [Jekyll](https://jekyllrb.com/), which GitHub Pages runs automatically. You edit text files, push to `main`, and the site updates within about a minute. There's no build step to run.

## Where things live

| To change… | Edit |
|---|---|
| Your name, intro, email, LinkedIn, resume link, "Now" line | `_data/profile.yml` |
| The three themes (Learning, Communication, Social impact) | `_data/themes.yml` |
| A case study | `_projects/<name>.md` |
| The "Earlier work" list on the Work page | `_data/archive.yml` |
| The About page story | `about.md` |
| The About page timeline | `_data/timeline.yml` |
| Your resume | Replace `assets/files/Sabrina_Hu_Resume.pdf` (keep the same name) |
| The homepage headline | `index.html`, the `<h1>` line |
| Colors and fonts | `assets/css/main.css` (top of the file) |

## Adding or editing a case study

Each project is one Markdown file in `_projects/`. The block at the top, between the `---` lines, fills in the header and the "At a glance" box:

```yaml
---
title: Solar Cap
org: Solar Capital · MIT D-Lab & Urban Risk Lab   # small label above the title
summary: One or two sentences, shown on cards and under the title.
themes: [impact]              # any of: learning, communication, impact
order: 1                      # position on the Work page
featured: true                # also show on the homepage
years: 2019–2025
role: Founder & inventor
audience: Who it was for.
team: Who you worked with.
methods: [User interviews, Prototyping]
tools: [Figma, Arduino]
cover: /assets/img/solar-cap/cover.webp
cover_width: 1600
cover_height: 888
cover_alt: Describe the image for someone who can't see it.
highlights:                   # big numbers at the top (optional)
  - value: "99.46%"
    label: of pathogens eliminated in 4 minutes
links:                        # optional
  - label: News story
    url: https://...
---
```

Below that, write normally in Markdown, using `## Problem`, `## Who it was for`, `## Process` (with `### Research`, `### Design`, `### Build`), `## Outcome`, and `## Reflection`.

### Images

1. Optimize the image (requires Python and `pip install pillow`):
   ```bash
   python3 scripts/optimize_images.py ~/Desktop/photo.jpg assets/img/solar-cap/photo.webp
   ```
   This prints the width and height.
2. Put it in the case study:
   ```liquid
   {% include figure.html src="/assets/img/solar-cap/photo.webp" alt="What the image shows" width="1600" height="900" caption="Optional caption" %}
   ```
   Add `wide=true` to let it extend past the text column on large screens.

Always write alt text that describes what's in the image, not "image of…".

### Drafting notes and placeholders

While drafting, you can leave yourself notes that show up as yellow boxes:

```liquid
{% include todo.html note="Add the survey findings." %}
{% include figure.html need="Photo of the prototype" %}
```

**Before you submit your application**, set `show_placeholders: false` in `_config.yml`. That hides every note and empty image box. Then search for `todo.html` to confirm nothing important is left.

## Previewing on your computer (optional)

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/portfolio/.

## Credits

Fonts: [Fraunces](https://github.com/undercasetype/Fraunces) and [Source Sans 3](https://github.com/adobe-fonts/source-sans), both under the SIL Open Font License (see `assets/fonts/`).
