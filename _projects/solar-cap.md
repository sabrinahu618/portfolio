---
title: Solar Cap
org: Solar Capital · MIT D-Lab & Urban Risk Lab
summary: A solar-powered UVC cap that turns any drink can into a water purifier and phone charger, taken from a high-school science fair to a disaster-relief marketplace.
themes: [impact]
order: 1
featured: true
years: 2019–2025
role: Founder & inventor
audience: Families who lose safe tap water and power after hurricanes and other disasters, starting with my own community in Florida.
team: Solo in high school; at MIT, I led 4 mechanical and electrical engineers.
methods: [Engineering design, Prototyping, Lab testing, Field research]
tools: [Arduino, Soldering, UVC LEDs, Solar charging circuits]
cover: /assets/img/solar-cap/cover.webp
cover_width: 1600
cover_height: 888
cover_alt: Close-up of the Solar Cap prototype, a black cylindrical cap with a USB cable plugged into its side, sitting on a clear water bottle.
highlights:
  - value: "99.46%"
    label: of pathogens eliminated after 4 minutes of UVC exposure
  - value: "$10K+"
    label: in MIT funding for the next version
  - value: "Top 10"
    label: worldwide, Spellman HV Clean Tech competition
links:
  - label: WCTV news story
    url: https://www.wctv.tv/2020/08/09/rickards-high-senior-changes-world-through-a-bottle-cap/
  - label: Tallahassee Democrat
    url: https://www.tallahassee.com/story/life/2020/04/22/rickards-high-school-student-invents-solar-powered-water-bottle-phone-charger/5099253002/
  - label: Capital Outlook
    url: https://capitaloutlook.com/site/rickards-rising-senior-makes-a-splash-with-water-purifier-invention/
---

## The problem

More than a billion people lack access to safe drinking water. After a natural disaster, it gets worse for everyone: tap water and electricity are often the first things to fail. The usual answer, bottled water, creates its own problem, since billions of plastic bottles are bought every year and more than half end up in oceans or landfills.

I wanted something that could **clean water and charge a phone** without the grid, and that was small and simple enough for anyone to use.

## Who it was for

People in the hours and days after a disaster, when there's no clean water, no power, and no time to learn a complicated device. That meant it had to work with one button, run on sunlight, and use materials people would already have on hand.

{% include todo.html note="Add a sentence about what you saw in your own community during hurricanes, or who you talked to. A specific moment makes the 'who' real." %}

## Process

### Research: why UVC

UVC light kills pathogens by damaging their DNA (it forms thymine dimers, so the cells can't replicate). A small UVC LED at 278 nm, placed inside a cap, could sterilize water without chemicals or filters wearing out. From there I set five engineering goals:

- **Solar-powered**, so it works when the power is out
- **Battery storage**, so it works after dark
- **Automatic shut-off**, so the light turns off once the water is safe
- **Device charging**, because a phone is a lifeline in an emergency
- **Fits a drink can**, because cans are everywhere

### Build: making the power reliable

The hardest part was power. My first circuit drew straight from the solar panel, but the panel wasn't stable enough, and the Arduino kept rapidly switching on and off as it drew more current than was available. Charging a separate power bank would have been cheaper, but it meant carrying a second device. I chose a solar charger feeding a LiPo battery, with a boost module powering the Arduino. That made the cap self-contained: leave it in the sun, and it stores energy for later.

{% include figure.html src="/assets/img/solar-cap/circuit.webp" alt="Diagram of the Arduino circuit next to photos of the front and back of the soldered circuit board and the solar module plugged in." width="1600" height="395" caption="The control board turns the UVC LED on with one button press and off automatically after a programmed time." wide=true %}

### Design: a happy accident with soda cans

The circuit was long enough that it pushed the LED off-center in the cap. Then I noticed that the opening of a drink can is off-center too. The cap fit perfectly on top of a standard aluminum can, so anyone with an empty soda can now had a water bottle.

{% include figure.html src="/assets/img/solar-cap/prototype.webp" alt="Six photos of the prototype: the water bottle, the solar module on top of the cap, the inside of the cap, the cap charging a phone, the cap on an aluminum can, and the purple glow of the UVC LED from the bottom." width="1400" height="1013" caption="The prototype: solar module on top, UVC LED inside, and a USB port for charging a phone." %}

### Test: does it actually work?

I collected water from Wakulla Springs and split it into five identical aluminum cans, exposing each to the UVC LED for one more minute than the last. Then I plated samples and counted bacterial colonies. **By minute four, the LED had eliminated 99.46% of pathogens.**

{% include figure.html src="/assets/img/solar-cap/plate-test.webp" alt="Grid of petri dishes from the test next to a line graph showing bacterial colonies dropping sharply from the 0-minute group to near zero by the 4-minute group." width="1600" height="730" caption="Bacterial colonies fall to near zero as UVC exposure time increases." wide=true %}

### Taking it further at MIT

At MIT, Solar Cap became Solar Capital. I led a team of four mechanical and electrical engineers across MIT D-Lab and the Urban Risk Lab, secured more than $10,000 in MIT funding, and moved the product toward people who could actually use it.

{% include todo.html note="This is the most important part for reviewers. What did D-Lab and Urban Risk Lab change about the design? Did you talk to disaster-relief organizations or users? What changed between the high-school prototype and the MIT version (cost, materials, form)?" %}

{% include figure.html need="A photo of the MIT-era prototype or the team at D-Lab or Urban Risk Lab." %}

## Outcome

- A working, self-contained prototype that purifies water in minutes and charges devices, for about **$44** in parts, with a clear path to lower cost at volume.
- Transitioned to the **Bosai Plus** disaster-relief marketplace.
- **Regeneron ISEF 2020 finalist**, **Spellman HV Clean Tech Top 10 worldwide**, **MIT IDEAS Social Innovation Challenge finalist**, and USAID Science Champion Award, among others.

{% include todo.html note="Add one line on what 'transitioned to Bosai Plus' means in practice: is it listed, piloted, or licensed?" %}

## Reflection

{% include todo.html note="Draft in your own words. Suggested angle: what this taught you about designing for people in crisis, and how you'd involve those people earlier now that you've done user research professionally." %}

Solar Cap taught me to love iterating, failing on the bench and trying again. Looking back, I designed it mostly from the lab outward. Today I'd start with the people who would use it.
