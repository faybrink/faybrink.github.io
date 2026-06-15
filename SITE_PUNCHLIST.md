# Fay Brink Site — Development Punchlist
*Last updated: June 15, 2026*

---

## Area Pages — Remaining to Build


### Priority 0 — Corporate Relocation Hub (High Priority)
- **File:** `relocation.html` — currently a placeholder; rebuild as a full dedicated hub
- **Target audience:** Corporate HR/recruiting teams, relocation coordinators, transferees from Energy Corridor companies (Shell, ConocoPhillips, BP, TechnipFMC), TMC institutions, and national companies relocating to Houston
- **Why Priority 0:** The Energy Corridor is Houston's #1 buyer-intent search corridor. Corporate relo packages = motivated, pre-qualified, timeline-driven buyers. One relo referral relationship with an HR department can yield multiple transactions per year.
- **Fay's angle:** Has had relocation instruction (not certified), has worked relo-timeline transactions, understands the corporate package structure, and covers all key Employment corridors — Energy Corridor, TMC, Woodlands/Exxon, Greenspoint
- **Content priorities:**
  - Lead with the employer ecosystem: Shell, ConocoPhillips, BP America, TechnipFMC, Waste Management, MD Anderson, UT Health, Houston Methodist, ExxonMobil (Woodlands), Amazon (Greenspoint area)
  - Speak directly to HR/recruiting language: "Helping your people land well in Houston"
  - Highlight speed and process: relocation timelines are compressed; being ready is the service
  - Cover all four major relo corridors: Energy Corridor (I-10 west), TMC/South Loop, The Woodlands/I-45 N, Greenspoint/IAH corridor
  - Add employer-facing content: "For Relocation Coordinators" section with how referral relationships work
  - FAQ targeting recruiter/HR queries: "What neighborhoods are closest to Shell campus?", "How fast can we close?", "Do you work with relo packages?"
  - Schema: Organization + FAQPage schema with relo-specific questions
- **SEO targets:** "Houston corporate relocation realtor," "Energy Corridor relocation housing," "Houston relocation specialist," "Shell ConocoPhillips employee housing Houston"
- **Tone:** Professional but not stiff — the voice that makes an HR director feel confident handing your name to a VP who just accepted an offer
- **Notes:** Fay has instruction in relocation (without formal certification) — acknowledge expertise without overclaiming credential. "I have worked relocation transactions and have formal training in the process" is accurate and sufficient.

### Priority 1 — Aldine
- **File:** `aldine.html`
- **Coverage:** Northeast Harris County along I-45 and I-69 north of the city
- **School District:** Aldine ISD
- **Character:** More affordable, working-class community; diverse demographics; proximity to Bush Airport
- **Fay's angle:** Serves buyers who are priced out of Spring/Woodlands but want north-side location and airport access
- **Notes:** Important to cover honestly — not a luxury market, but a real one with real buyers. Strong value story for first-time buyers and investors.
- **Map center:** ~30.00, -95.37 | zoom 12

### Priority 2 — Jersey Village
- **File:** `jersey-village.html`
- **Coverage:** Northwest Harris County, chartered city near Beltway 8 / Hwy 290
- **School District:** Jersey Village ISD (very small K-12 district, a significant selling point)
- **Character:** Independent city with its own services, between Cypress and northwest Houston; middle-class suburban feel; underexposed relative to neighboring Cypress
- **Fay's angle:** Adjacent to Fay's home corridor (Cypress/Paddock Bend); knows the area personally; good for buyers who want small-district schools without The Woodlands prices
- **Notes:** Jersey Village ISD is a genuine hidden gem — smaller than any major district, high accountability ratings, community-oriented. Lead with that.
- **Map center:** ~29.885, -95.561 | zoom 13

### Priority 3 — Sugar Land / Missouri City
- **File:** `sugar-land-missouri-city.html`
- **Coverage:** Fort Bend County, southwest metro along Hwy 59/69
- **School District:** Fort Bend ISD (one of the strongest in the state)
- **Character:** Established planned communities (First Colony, Riverstone, Telfair), highly diverse demographics, strong academic performance
- **Notes:** Natural complement to Fulshear (both Fort Bend County). High search volume from relocating families who've heard of Fort Bend ISD.

### Priority 4 — Pearland / Friendswood
- **File:** `pearland-friendswood.html`
- **Coverage:** South of Houston along Hwy 288 and I-45, Brazoria County
- **School Districts:** Pearland ISD, Friendswood ISD
- **Character:** One of the fastest-growing corridors in the metro; Friendswood has a small-town character similar to Tomball; proximity to Johnson Space Center employment
- **Notes:** High demand from aerospace/NASA employees; Friendswood ISD is excellent and often overlooked.

### Priority 5 — Conroe / Montgomery County
- **File:** `conroe-montgomery.html`
- **Coverage:** North of The Woodlands, Montgomery County along I-45
- **School District:** Conroe ISD
- **Character:** Rapidly growing exurban corridor; more affordable than The Woodlands; lake country (Lake Conroe); serious upside in the right neighborhoods
- **Notes:** Natural extension of The Woodlands page northward. Growing relocation traffic from people who looked at The Woodlands and found the prices have moved.

---

## Service / Content Pages — To Build or Improve

- [ ] **`contact.html`** — Add embedded HiHello widget (currently just a link)
- [ ] **`blog.html`** — Add 3-4 new blog posts on inner-loop topics (Heights inspection reality, River Oaks buying timeline, Medical Center relocation guide)
- [ ] **`new-construction.html`** — Flesh out from placeholder; strong SEO opportunity given Fay's CNHP credential
- [ ] **`relocation.html`** — Currently minimal; expand to full relocation guide with corporate relocation section (TMC, Energy Corridor employers)
- [ ] **`wealth-strategy.html`** — Expand content; target investment buyer queries
- [ ] **`resources.html`** — Add actual resource links/downloads

---

## Technical — To Do

- [ ] **Favicon** — Circle logo mark as 32px/180px favicon (was discussed, not yet implemented)
- [ ] **`sitemap.xml`** — Update whenever new pages are added (current: 36 URLs as of June 15)
- [ ] **`robots.txt`** — Verify sitemap reference is correct
- [ ] **Social icons** — Currently only on `index.html`; consider adding footer social bar to `contact.html` and `reviews.html`
- [ ] **Google Business Profile** — Add real Google review link to `reviews.html` and `contact.html` (current placeholder has empty `placeid=`)
- [ ] **Areas.html** — Add Aldine, Jersey Village, Sugar Land, Pearland cards once pages are built
- [ ] **Index.html** — Services nav dropdown on mobile (currently flat on mobile)
- [ ] **OG images** — Open Graph image tags have no actual image URL; add a hosted image for social sharing previews

---

## Photo / Visual — To Do

- [ ] Consider replacing the existing headshot in the index `hero-intro` circle with one of the new photos
- [ ] Review contact page photo (IMG_7189) sizing on mobile — may need CSS adjustment
- [ ] Brand banners (Wide_Nike_banner.jpg, Tall_Nike_Banner.png) — determine which pages use which version

---

## Notes

- All pages currently use **self-contained base64 images** (no external hosting required for GitHub Pages)
- Blog post pages use a separate `article-wrap` layout — different from the page-hero layout used on area and service pages
- The `build_page.py` builder at `/home/claude/build_page.py` is the template for new area pages — always run the 3 map fixes after building (tile layer reference, events, pin commas)
