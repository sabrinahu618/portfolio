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
team: Solo in high school; at MIT, I led a team of mechanical and electrical engineers across D-Lab and the Urban Risk Lab.
methods: [Engineering design, Prototyping, Water-quality testing, Benchmarking, Partnerships]
tools: [Arduino, Custom PCB, Resin 3D printing, UVC LEDs, Colilert, Petrifilm, Quanti-Tray]
cover: /assets/img/solar-cap/cover.webp
cover_width: 1600
cover_height: 888
cover_alt: Close-up of the Solar Cap prototype, a black cylindrical cap with a USB cable plugged into its side, sitting on a clear water bottle.
highlights:
  - value: "99.46%"
    label: of pathogens eliminated in 4 minutes, in early tests on spring water
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

People in the hours and days after a disaster, when there's no clean water, no power, and no time to learn a complicated device. That meant it had to work with one button, run on sunlight, and use materials people would already have on hand. The same design also serves anyone far from safe water: people in rural areas, hikers, and travelers. Today's alternatives each fall short somewhere: boiling isn't always possible, pathogens can grow resistant to chlorine, and bottled water is expensive and wasteful.

{% include todo.html note="Add a sentence about what you saw in your own community during hurricanes, or who you talked to. A specific moment makes the 'who' real." %}

## Part 1 · The first prototype, in high school

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

## Part 2 · Taking it further at MIT

At MIT, Solar Cap became Solar Capital, and a one-person science project became a team effort. Through MIT D-Lab, I led a team of mechanical and electrical engineers, secured the MIT ESG-PKG Social Impact Fellowship and more than $10,000 in MIT funding, and started working through what it would take to put the cap in people's hands.

### Rebuilding it as a product

We split the work. An electrical engineer designed a custom circuit board to connect the UVC LED, battery, and solar panel and run the timer, replacing the Arduino. A mechanical engineer designed a 3D-printed case. Another teammate and I ran the water testing. I led the product as a whole: pulling the design together, co-running the tests and analyzing the results, and figuring out the path to public use.

{% include figure.html src="/assets/img/solar-cap/mit-pcb.webp" alt="Annotated diagram of the custom circuit board, with wires running to the UVC LED, a solar panel, a lithium-polymer battery, status LEDs, a power switch, and micro-USB and USB-A ports for charging." width="1600" height="1235" caption="The custom circuit board connects the UVC LED, solar panel, and battery, and adds status lights and USB ports for charging a phone." %}

The case went through two versions. The second added ridges along the bottom so the cap could grip containers of different sizes, and enlarged the ports to account for 3D-printer error.

{% include figure-pair.html src1="/assets/img/solar-cap/mit-case-v1.webp" alt1="The first 3D-printed case: a light gray resin cylinder with a lid, a round opening on top for the solar panel, and cutouts on the side for ports and switches." src2="/assets/img/solar-cap/mit-case-v2.webp" alt2="The second 3D-printed case: a dark gray cylinder on a desk, with a round opening on top and small port openings on the side." width="540" height="540" caption="Two iterations of the 3D-printed case. The second version grips containers of different sizes." %}

### Testing against a harder standard

In high school, I had tested spring water. At MIT, we tested water from the Charles River, a much tougher challenge, using standard lab methods: Colilert tubes for E. coli and Petrifilm plates to count bacterial colonies. We also benchmarked against a commercial UVC water bottle.

The first rounds were messy. In one test, treated and untreated water looked the same, likely because the LED wasn't powerful enough. In another, after several days of rain, every sample had too many colonies to count. By the third and fourth tests, Solar Cap was clearly reducing bacteria, and longer exposure worked better:

{% include solar-cap-results.html %}

{% include figure.html src="/assets/img/solar-cap/mit-petrifilm.webp" alt="Eight Petrifilm plates in two rows, each labeled by sample, showing red circles where bacteria were cultured." width="1400" height="1050" caption="Petrifilm plates from one round of testing." %}

Then we ran the most rigorous test, a Quanti-Tray that estimates how many bacteria are present. Every well came back positive for E. coli: for our cap, and for the commercial bottle too. **Neither could make Charles River water safe to drink.** It was disappointing, and it was the most useful result of the project. A single UVC LED isn't enough for heavily contaminated water.

### What we'd change

- **Filter first.** Use a pre-filter to remove most contaminants, with UVC as the final disinfection step.
- **More light.** Try three LEDs instead of one, and test other wavelengths (265 and 278 nm) at different water depths. If LEDs still fall short, look at UVC lamps.
- **Plan for hardware delays.** The wrong circuit boards arrived first, the replacements needed pre-soldering we couldn't do ourselves, and the final boards shipped from overseas and arrived the day before the semester ended.

Bringing the cap to the public raised its own questions. I researched the testing standards and regulatory steps needed for public use, and learned from MIT's Technology Licensing Office that MIT couldn't patent the cap, since it didn't own it. Working with a manufacturer would mean an NDA instead, which the BU Law Clinic's free legal services could help with. I also built a relationship with the CLEO Institute, a Florida climate nonprofit.

### Where it ended up

I transitioned the product to the **Bosai Plus** disaster-relief marketplace.

{% include video.html id="Ddm0hCcHDqw" title="Solar Cap: what the project became" caption="A video I made about what Solar Cap eventually became." %}

{% include todo.html note="Tell me what the video shows and what moving to Bosai Plus meant in practice (listed for sale, piloted, or licensed?), and I'll write this section properly. Also: what did the Urban Risk Lab contribute?" %}

## Outcome

- **In high school:** a working, self-contained prototype that purified spring water in minutes and charged a phone, for about **$44** in parts.
- **At MIT:** a team-built second version with a custom circuit board and 3D-printed case, and honest lab results that showed exactly what the next version needs.
- **Recognition:** Regeneron ISEF 2020 finalist, Spellman HV Clean Tech Top 10 worldwide, MIT IDEAS Social Innovation Challenge finalist, MIT ESG-PKG Social Impact Fellowship, and the USAID Science Champion Award, among others.

## Reflection

{% include todo.html note="Draft in your own words. Suggested angle: what this taught you about designing for people in crisis, and how you'd involve those people earlier now that you've done user research professionally." %}

Solar Cap taught me to love iterating, failing on the bench and trying again. At MIT it taught me something harder: a result that works in one setting can fail in another, and an honest test is worth more than a good demo. Looking back, I also designed it mostly from the lab outward. Today I'd start with the people who would use it.
