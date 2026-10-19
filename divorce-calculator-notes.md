# Divorce Home Calculator: What's in This Upload

## New page
**divorce-home-calculator.html**: the keep / buy out / sell calculator.

- **Step 1, The Equity:** the buyout value (ideally from an independent appraisal), a separate likely sale price if the home were listed and marketed (it matches the buyout value until changed), mortgage, HELOC, departing spouse's share (any %, since Texas splits "just and right," not automatically 50/50), selling costs, and the part of the buyout paid with other assets (such as a retirement offset). An optional checkbox deducts selling costs from the buyout.
- **Step 2, Can One Income Carry It?:** the keeping spouse's income, support they receive, debts, rate, term, tax rate, insurance, HOA, and refinance closing costs.
- **Results:** total equity, buyout amount, new loan, and payment. Two color-coded checks:
  - **Loan size:** under 80% is a standard Texas cash-out; 80–95% usually needs an owelty lien; over 95% is unlikely.
  - **Debt-to-income:** 43% or lower looks workable; up to 50% is possible but tight; over 50% is unlikely. This check also shows the income that would bring the ratio to 43%.
- **Keep vs. Sell, Side by Side** for both spouses. A note says which path nets the departing spouse more on the numbers entered, and why, without assuming either one wins. A caution line follows: either path can be worked against a spouse (lowball buyout value, or an underpriced, poorly marketed, or stalled sale), with a link to the stalling-spouse post.
- **Print or Save as PDF** creates a clean one-page summary for the client to bring to their attorney.
- Nothing is saved or sent unless the visitor submits the form.

## Pages updated (links only, no rewrites)
- **divorce-hub.html:** "Free Tool" callout card above the eleven guides
- **divorce-real-estate.html:** "Run the numbers yourself →" link in the Buyout Analysis card
- **blog-divorce-keep-house-spouse-buyout-refinance-texas.html**, **blog-owelty-lien-divorce-refinance-buyout.html**, **blog-can-you-keep-house-after-divorce-texas.html:** one sentence before the closing call-to-action
- **calculators.html:** added to the "Jump to a Calculator" list
- **sitemap.xml:** new page added

## Attorney tracking links
Give each firm its own link:
`https://faybrink.github.io/divorce-home-calculator.html?ref=smithlaw`

Use lowercase letters, numbers, and dashes only. The tag stays with the visitor for that browsing session.

These Google Analytics events fire with the `ref` tag attached:

| Event | When it fires |
|---|---|
| `divorce_calc_view` | Page opened |
| `divorce_calc_used` | Visitor changed a number |
| `divorce_calc_print` | Visitor printed or saved the summary |
| `divorce_calc_send_click` | Visitor clicked "Email Me This Summary" |

**One-time GA setup:** To see the firm tags in GA reports, register `ref` as a custom dimension:
1. Go to Admin → Custom definitions → Create custom dimension.
2. Set the dimension name to `ref`, the scope to Event, and the event parameter to `ref`.

Tags only show in reports from the day you create the dimension forward.

## Still to do: the form
Until the form exists, the contact section shows your phone number and email.

Once the form exists, open divorce-home-calculator.html, find this line near the bottom, and paste the form ID between the quotes:

`var DC_JOTFORM_ID = '';`

The form loads already filled in with the visitor's numbers and their firm tag in hidden fields named:
`ref`, `home_value`, `mortgage_balance`, `selling_costs`, `total_equity`, `split_pct`, `buyout_amount`, `refi_result`, `net_if_keep`, `net_if_sell`, `source_page`

## Test after pushing
1. Open `divorce-home-calculator.html?ref=test` on your phone.
2. Change a few numbers, then tap **Print or Save as PDF**.
3. In GA, open Reports → Realtime and confirm the `divorce_calc_` events appear.
