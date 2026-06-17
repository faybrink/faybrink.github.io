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

---

## BUILDER RESOURCE COLLECTION — Only You Can Get These

*These items must be collected in person or by contacting each builder directly.
The builders.html page has "Coming Soon" placeholders ready to be replaced with real PDFs.*

### 🔴 Priority 1 — Clay Residential / Marvida (You're Already On-Site)
You have direct access. Pull all of the following from your OSC or sales desk:

- [ ] **Current Incentive Sheet** — Rate buy-down %, closing cost $, appliance/design credit. Updated monthly — pull the latest version.
- [ ] **Available Floor Plan PDFs** — One PDF per plan (Hillcrest, Magnolia, etc.). Ask for the full current lineup.
- [ ] **Standard Features & Spec Sheet** — What is standard vs. upgrade in each series. Ask: "Can I get the features list that shows standard vs. upgrade?" They have it.
- [ ] **Community Site Map with Available Lots** — Phase map showing sold, under contract, and available lots with lot premiums noted.
- [ ] **HOA Documents** — CC&Rs, fee schedule, Marvida master HOA and Land Tejas HOA info.
- [ ] **Preferred Lender Rate Special** — Current rate if using their preferred lender. Get the number so buyers can compare.
- [ ] **Warranty Summary** — Builder's 1-2-10 warranty overview PDF.
- [ ] **Completion Timeline / Build Schedule** — How long from contract to close on available specs vs. to-be-built.

**Where to go:** Walk to the Clay Residential sales office on-site at Marvida (Fry Rd & West Rd, Cypress).

---

### 🟡 Priority 2 — Bridgeland Model Home Row (7 Builders in One Trip)
**Address:** Bridgeland Creek Pkwy & Mason Rd area, Cypress 77433 — look for the model home village signage off Bridgeland Lake Dr.
**Best time:** Weekday morning (less crowded, sales agents have more time).

From EACH builder's model home, collect:
- [ ] Current incentive flyer (ask: "Do you have today's incentive sheet?")
- [ ] Floor plan brochure / plan book
- [ ] Standard features list (ask: "What's included in the base price vs. design center?")
- [ ] HOA fee information for this community section
- [ ] Preferred lender current rate special and any builder credit for using them

**Builders to hit in Bridgeland:**
- [ ] David Weekley
- [ ] Lennar / Village Builders
- [ ] Perry Homes
- [ ] Westin Homes
- [ ] Newmark Homes
- [ ] Taylor Morrison
- [ ] Toll Brothers (Parkland Village — separate model location, ask for directions at the village)

---

### 🟡 Priority 3 — Cross Creek Ranch, Fulshear (6 Builders)
**Address:** FM 1093 & Cross Creek Bend Ln, Fulshear 77441

Same collection as Bridgeland for each builder present:
- [ ] Perry Homes
- [ ] Taylor Morrison
- [ ] Westin Homes
- [ ] Chesmar Homes
- [ ] David Weekley
- [ ] Newmark Homes

---

### 🟡 Priority 4 — Harvest Green, Richmond (Fort Bend ISD Focus)
**Address:** Harlem Rd & W Airport Blvd, Richmond 77406

- [ ] David Weekley
- [ ] Perry Homes
- [ ] Lennar / Village Builders
- [ ] Taylor Morrison
- [ ] Meritage Homes
- [ ] Westin Homes

Also: Ask for the Harvest Green master developer info (Fort Bend ISD zoning confirmation letter/map is useful for buyers).

---

### 🟢 Priority 5 — Online Collection (No Drive Required)

These can be pulled from builder websites or by emailing their OSC:

| Builder | What to Request | How |
|---------|----------------|-----|
| D.R. Horton | Current Houston incentives PDF | drhorton.com → Houston → Request Info |
| KB Home | Built-to-Order options guide | kbhome.com → Book appointment online |
| Meritage | Energy features comparison vs. standard | meritagehomes.com → Contact |
| Pulte | Del Webb at Sweetgrass amenities guide | delwebb.com → Contact |
| Perry Homes | Digital floor plan catalog | perryhomes.com → Floor Plans section |
| CastleRock | Standard features comparison | castlerocktx.com → Contact |

---

### 💡 What to ASK at Every Model Home

Script for the sales agent:
> "I'm a REALTOR who represents buyers considering this community. I'd love to get your current incentive sheet, a floor plan brochure, and your standard features list so I can share them with buyers I'm working with. Do you have a packet you give to agents?"

Most builder sales offices have a **Realtor/Agent packet** ready to hand out — it often includes more detail than the consumer-facing materials. Always identify yourself as a REALTOR first.

---

### 🏗️ Future Resource Ideas for builders.html

These would add significant value once you have the source material:

- **Design Center Upgrade Price Lists** — What specific upgrades cost at each builder's design center. Extremely rare to share publicly but builders sometimes provide to registered agents. Ask directly.
- **Builder Warranty Comparison Chart** — Side-by-side of 1-yr, 2-yr, 10-yr warranty terms across 5-6 builders.
- **Preferred Lender vs. Outside Lender Comparison** — A real example showing rate, closing cost, and monthly payment comparison. Would be your most-shared resource on this page.
- **HOA Fee Comparison by Community** — What the monthly HOA + master fees total across Bridgeland, Cross Creek Ranch, Marvida, Harvest Green, etc.
- **Custom Home Refinishing Guide** — A guide for buyers who want to customize a production home after close (paint, flooring, fixtures) — what to do yourself, what to hire out, what affects warranty.
- **"What the Inspection Found" Series** — Anonymized real examples of new construction inspection findings. You would need homeowner permission but this content is gold.


---

## DESIGNATION MARKS — Low Priority / Not SEO-Immediate

*Skip until higher-priority items are done. These are trust signals for human visitors, not search engines.*

- [ ] Download CLHMS mark (logo) from Institute for Luxury Home Marketing → add to `wealth-strategy.html` and `river-oaks-rice-village.html`
- [ ] Download CNHP mark from NAHB → add to `builders.html` and `new-construction.html`
- [ ] Download Divorce Specialist mark → add to `divorce-real-estate.html`

Note: Use the compact designation logo/mark only — not full certificate scans. Certificate scans go on LinkedIn and listing presentations, not web pages.


---

## DISCLAIMER SYSTEM — Auto-Protecting Future Content

Two files at `/home/claude/` handle all legal disclaimers going forward.
**Never build a new post or page without using these.**

### Files

| File | Purpose |
|------|---------|
| `/home/claude/disclaimers.py` | Library of 9 category-specific disclaimer blocks |
| `/home/claude/post_template.py` | Master blog post factory — auto-injects disclaimers |

### How to use in a new build session

```python
from post_template import make_post
from disclaimers import get_disclaimer

# Blog post — disclaimers auto-selected from data_cat + title keywords
html = make_post(
    filename   = 'blog-new-article.html',
    title      = 'Title Here',
    meta_desc  = 'SEO description',
    keywords   = 'kw1, kw2',
    category   = 'Display Category',
    data_cat   = 'taxes',           # drives auto-disclaimer selection
    pub_date   = 'June 17, 2026',
    body_html  = article_body,
    tags       = ['Tag1', 'Tag2'],
    byline     = 'Fay Brink',       # or 'Fay Brink, Divorce Specialist'
    fair_housing = False,           # set True for neighborhood content
)
```

### Disclaimer categories available

| Key | Triggers for | Warns about |
|-----|-------------|-------------|
| `universal` | All posts | General: not professional advice |
| `taxes` | tax, homestead, capital gains, widow | CPA required, deadline urgency |
| `divorce` | divorce, marital | Licensed Texas attorney required |
| `estate` | legacy, medicaid, trust, lady bird | Licensed Texas estate attorney required |
| `senior` | senior, elder | Legal + medical + financial team required |
| `wealth` | wealth, heloc, velocity, 1031, cost segregation | CPA + financial advisor required |
| `flood` | flood, insurance | Licensed insurance professional required |
| `inspection` | inspect, pier and beam, foundation | Licensed inspector + engineer required |
| `credit` | credit, mortgage qualification | Licensed mortgage professional required |
| `relocation` | school, district | Verify zoning directly with district |
| `fair_housing` | Any neighborhood characterization | Fair Housing Act notice |

### Auto-detection
`make_post()` scans the article title for keywords and auto-adds the right disclaimers.
"Houston Property Tax Guide" automatically adds `universal` + `taxes`.
"Heights Home Inspection" automatically adds `universal` + `inspection`.
You do not need to manually specify categories if the title contains the keywords.

### For service pages (not blog posts)
Use `get_disclaimer()` directly and insert the returned HTML into the page template
near the relevant content sections.

### Notes
- TREC-required disclosure links (Information About Brokerage Services + Consumer Protection Notice) are in the standard footer on every page — already covered.
- Fair Housing notice is OFF by default. Turn it ON for area guide pages, neighborhood characterization content, or anything that describes who lives somewhere.
- Disclaimers are styled to match site branding and are visually distinct but not alarmist.
- The disclaimer system does NOT replace your obligation to disclose known material defects in an actual transaction. That is a transaction-level obligation, not a content-level one.

