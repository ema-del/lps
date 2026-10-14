# LPCR page review: College Zoom (David Reynaldo)

Date: 2026-10-14. Page reviewed: https://go.collegezoom.com/access (opt-in for "OLead - CZ - Free Training - US - 30+").
Screenshots: oct14/college-zoom-desktop.png, oct14/college-zoom-mobile.png (plus -full versions).

## Verdict
LPCR fell from about 20% (late Aug to mid Sep) to 5-7% the week the new ads launched on Sep 14. The two new ads (Dear Letter and White Notes App, 83% of spend) promise "the free training" and "the key" / "personalized answer key", but the page never says "free", never names the training, and ends in a "Submit" button under a money question. The older Twitter ad, whose words the page matches best, still converts at 20%.

Also broken: the Meta pixel on the page has curly quotes, so it never loads. Meta shows 48 landing page views against 59 leads.

## LPCR numbers (client sheet)
Source: "(CZ) - Business Reporting B2C" (fileId 15BB-dlXY_g-0Xl8A9UYv0X88BVs0I7TOFTRzOJC49QU, most recently modified copy, 2026-10-12). Tabs Jul, Aug, Sep, Oct (daily rows) and Dash (monthly). Columns: E "Link Clicks", H "Lead", I "Pre-Qualified Leads". LPCR = H / E.
The sheet is filled only through Oct 11 (Oct 12 and 13 are blank), so the windows below are the latest 7 and 3 logged days.

| Window | Clicks | Leads | LPCR | CPL |
|---|---|---|---|---|
| Last 7 logged days (Oct 5-11) | 437 | 50 | **11.4%** | $24.08 |
| Last 3 logged days (Oct 9-11) | 204 | 25 | **12.3%** | $20.89 |
| Best month 2026: Aug | 1,166 | 154 | **13.2%** | $19.95 |
| Jul / Sep / Oct MTD | 1,015 / 2,126 / 745 | 58 / 203 / 65 | 5.7% / 9.5% / 8.7% | |

Weekly LPCR and what changed (sheet comments in column A):

| Week | Clicks | Leads | LPCR | Sheet comment |
|---|---|---|---|---|
| Aug 17-23 | 239 | 23 | 9.6% | |
| Aug 24-30 | 240 | 47 | 19.6% | Aug 25 "launched video ad", Aug 28 "added prequalifier" |
| Aug 31-Sep 6 | 235 | 55 | **23.4%** (best week) | |
| Sep 7-13 | 296 | 55 | 18.6% | budget raised Sep 7, 10, 11 |
| Sep 14-20 | 823 | 60 | 7.3% | Sep 14 "new ads launched" |
| Sep 21-27 | 603 | 34 | 5.6% | |
| Sep 28-Oct 4 | 515 | 24 | 4.7% | |
| Oct 5-11 | 437 | 50 | 11.4% | |

- **When it dropped: Sep 14.** That day clicks tripled (58 to 178) and CPC halved ($3.10 to $1.41), but leads stayed flat. The two ads launched that day are the two now spending most (creative names are dated 2026-09-14).
- Adding the pre-qualifier on Aug 28 did not hurt. LPCR went up after it.

## Live ads (Meta, last 7 days = Oct 7-13, ACTIVE only)

| Ad | Spend | Share | Link clicks | LPVs | Leads (Meta) | Load rate | LPCR (leads/clicks) |
|---|---|---|---|---|---|---|---|
| PP1 - Dear Letter | $633.88 | 52.7% | 231 | 24 | 30 | 10.4%* | 13.0% |
| PP1 - White Notes App | $369.91 | 30.8% | 172 | 14 | 16 | 8.1%* | 9.3% |
| Paint Point 1 - Twitter Color | $198.04 | 16.5% | 65 | 10 | 13 | 15.4%* | **20.0%** |
| **Total** | $1,201.83 | | 468 (423 unique) | 48 | 59 | 10.3%* | 12.6% (13.9% on unique) |

*Load rate is not real. LPVs are lower than leads, which is impossible if the page view event fired. See Fix first #1.

- Meta trend tool: cost per result is rising on all 3 ads (White Notes +95.7%, Twitter +63.2%, Dear Letter +12.3%). White Notes conversion rate is down 58.9%.
- Meta benchmark: the campaign's cost per result is 57% below (better than) peer median. The cost per lead is fine. The page conversion rate is the problem.
- Meta leads (59 for Oct 7-13) vs sheet leads (41 for Oct 7-11, about 8 a day in both): no undercount, so lead tracking is OK (likely through Conversions API).

## Fix first (not tests)
1. **Meta pixel is broken on the opt-in page.** The head tracking code uses curly quotes: `fbq(‘init’, ‘988221430355964’); fbq(‘track’, ‘PageView’);` and `t.src=v ... (window, document,‘script’, ‘https://connect.facebook.net/en_US/fbevents.js’)`. That is a JavaScript syntax error, so fbevents.js never loads. In two Playwright loads, desktop and mobile, there were zero requests to facebook.com/tr or fbevents.js. Re-paste the pixel with straight quotes (' ') and check with Meta Pixel Helper. Until then, load rate cannot be judged, and Meta only gets server events.
2. **Proof number mismatch inside the same ad.** Primary text: "17 years. 2,900+ students. 96.5% success rate to a student's top 3 self-chosen college." Dear Letter image: "17 years ... 2,200 families, a 96.5% top-3-choice rate." Confirm the right number with David before it goes on the page. Neither number is in the client profile. The profile only confirms "I've been doing it for 17 years."
3. **Check the UTM hidden fields.** On the first desktop load they filled ("meta", "paid_social", "pcw_freetraining", "pp1dearletter"). On two later loads (desktop and mobile) they were empty after 8 seconds. Do a test submit from a phone with the ad URL and check that the GHL contact gets utm_content. Without it, you cannot count booked calls per ad.
4. **Check where Lead fires.** The form's Facebook pixel setting looks empty. Per playbook, with a pre-qualifier, Lead should fire on the training page. Right now Meta counts every opt-in, including disqualified ones.
5. **Page speed.** Desktop took 6.5s to "load" on the first run and 11.8s on the second. Mobile took 4.1-4.7s. Worth a look once the pixel is fixed and real load rate shows.
6. Phone field defaults to United States +1. Correct for a US campaign. No test data in fields. Privacy and Terms links are in place. All OK.

## Ad-to-page match

| Item | Ad (quoted) | Page (quoted) | Match? |
|---|---|---|---|
| Call-out | "If your teen is in 9th to 12th grade, targeting UCLA, USC, or better" / Twitter image "(for parents of 9th to 12th graders targeting top 50 colleges only)" | "PARENTS OF 9TH-12TH GRADERS ONLY" | Partial. The page drops the "targeting UCLA, USC, or better" filter. |
| Pain / hook | Headline "Is Your Teen Actually Competitive for Their Top College? Most Parents Don't Know Until It's Too Late." / Dear Letter "you're quietly terrified it still won't be enough" | "The Hidden Score That Gets Your Teen Into Their Top-3 College" | Partial. The "hidden score" idea matches. The fear in the ad does not appear. |
| Offer name | "Free Training: How Elite Colleges Actually Score Your Teen", "Watch the Free Training", Dear Letter "Watch the free training and I'll hand you the key", Notes "Get your personalized answer key below" | "Training access in just 30 sec!" and button "Submit" | **No.** The word "free" is not on the page. The training's name is not on the page. "Key" / "answer key" is not on the page. |
| Proof | "A parent who runs a $10 million admissions consulting company hired us for their own kid..." and "17 years. 2,900+ students. 96.5% success rate..." | 12 review cards and "5.0 · 46 reviews" (Google), "5.0 · 94 reviews" (Yelp), all below the form | Partial. Reviews are good but sit below Submit. None of the ad's numbers or its "$10 million company" story are on the page. |
| Guarantee | None in ads | None on page | OK. The profile only has a draft guarantee ("Maybe this?"), so leave it out. |
| Numbers | 2,900+ students (text) vs 2,200 families (image) | none | Flag (Fix first #2). |

## Page vs playbook
- Headline: playbook says "Headline = the offer ... and it must be the same on every page." The page headline is a promise ("Gets Your Teen Into Their Top-3 College") and never names the free training the ad sold.
- Button: playbook form spec is button "Access". The page says "Submit".
- Pre-qualifier: playbook says "not for competitive ones like college consulting" and "B2C: never mention money ('It is a complete drop off moment'). Use workarounds, e.g. 'Do you need scholarship help?'". The current question starts with scholarships, then the answers say "financial aid", "cost reduction", "Cost is a consideration" and "cost isn't an issue". That is money, 4 times. Since LPCR rose after it was added, test the wording instead of removing it. CPL is $21-24, which is between the playbook's "$10-20, you SHOULD" and "$45-50, don't".
- Form: 3 fields + 1 radio question + required consent checkbox. Short enough.
- Squeeze page elements: logo yes, call-out yes, headline yes, **no subheadline**, video yes (a captioned talking-head video sits where the VSL preview GIF should be), short form yes, reviews block yes (below the form).
- Mobile (390x844): the first screen shows the logo, call-out, headline and the top of the video. The first form field starts at 655px. "Submit" is at 1,525px, about 1.8 screens down. The video sits above the form on phones.
- Desktop: the form starts at the fold. There is an empty white block on the left above the video.

## 5 A/B tests (biggest expected lift first)

**T1. Headline + subheadline (offer match)**
- Change: "The Hidden Score That Gets Your Teen Into Their Top-3 College"
- To: "Free Training: How Elite Colleges Actually Score Your Teen". Subheadline: "See the internal scoring system elite colleges use to grade your kid, and find out exactly which gaps are standing between your teen and an acceptance."
- Why: all 3 ads name this exact training ("Free Training: How Elite Colleges Actually Score Your Teen"). The subheadline is lines 2 and 3 of the Twitter ad image, the ad that converts at 20%. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad."

**T2. Form header + button (one name for the freebie)**
- Change: "Training access in just 30 sec!" and button "Submit"
- To: "Get the free training (takes 20 minutes)" and button "Watch the Free Training"
- Why: the ads end with "👇 Watch the Free Training" and the Twitter image says "(free - takes 20 minutes, could change everything)". The button should say what they get. Playbook button is "Access", and "Submit" names nothing.

**T3. Pre-qualifier wording (no money words)**
- Change: "Will earning scholarships be a key factor in where your child ultimately enrolls?" with answers "Yes - we'll need significant financial aid" / "Yes - but I'm not sure we'll qualify for aid, so any cost reduction helps" / "Cost is a consideration, but not the biggest one" / "No - cost isn't an issue"
- To: "Do you need scholarship help?" with answers "Yes - we'll need significant scholarship help" / "Some help would be nice" / "No"
- Why: the playbook's B2C rule is "never mention money" and gives "Do you need scholarship help?" as the workaround. Keep the same disqualify logic on the first answer. Judge this test on pre-qualified leads per click and booked calls, not only LPCR. Profile: qualified families earn $200k-250k+.

**T4. Call-out + proof above the form**
- Change: "PARENTS OF 9TH-12TH GRADERS ONLY" (and nothing between the headline and the form)
- To: "FOR PARENTS OF 9TH-12TH GRADERS TARGETING UCLA, USC, OR BETTER", and directly above the form: "A parent who runs a $10 million admissions consulting company hired us for their own kid. So did former admissions readers at our largest competitors."
- Why: the call-out is the ad's first line, word for word. The proof is the ad's second paragraph, and right now the page shows no proof above "Submit". Optionally add "17 years. 2,900+ students. 96.5% success rate to a student's top 3 self-chosen college." once Fix first #2 is answered. Leave it out until then.

**T5. Mobile order (form first)**
- Change: phone order of logo, call-out, headline, video, "Training access in just 30 sec!", form (first field at 655px, button at 1,525px)
- To: logo, call-out, headline, form, then the video below the form (or a 10-second VSL preview GIF in its place)
- Why: most clicks come from Instagram and Facebook feeds on phones, and the form is not fully visible on the first screen. Playbook squeeze page uses a "VSL preview GIF", a short clip, before a "short form".

Leave out: any guarantee (the profile only has a draft, "Maybe this?"). Also leave out the Duke/Stanford and "flipped 2 rejections from USC" stories. They are in the intake form, but not in the ads or on the page, and David hasn't approved them for public use.

## How to run them
- Traffic: about 440-470 link clicks a week (437 in the sheet for Oct 5-11, 468 in Meta for Oct 7-13), about 65 a day.
- At about 150 visitors per version (300 per test, 50/50 split), each round needs about 5 days. Use 7 days to cover a full week.
- Five single tests in a row would take about 5 weeks, so bundle:
  - Round 1 (week 1): **T1 + T2 together** (same idea: name the free training on the headline, form header and button). Clarity labels T1-A / T1-B.
  - Round 2 (week 2): **T4 + T5 together** (what sits above the form, and form position on mobile). Labels T2-A / T2-B.
  - Round 3 (weeks 3-4): **T3 alone**, because it changes lead quality. Run it 10-14 days and judge on pre-qualified leads and booked calls. Labels T3-A / T3-B.
- Clarity is already on the page (project xg3eqqx7ms). Tag each version with `clarity("set", "test", "T1-A")` and so on.
- Fix the pixel (Fix first #1) before Round 1, so landing page views are real during the tests. Count visitors by link clicks until then.

## Questions for Ema / David
1. Did anything on the page change on or near Sep 14, besides the new ads? When was the current Meta pixel code pasted into head tracking?
2. Which is right: "2,900+ students" (primary text) or "2,200 families" (Dear Letter image)?
3. The White Notes ad says "Get your personalized answer key below". The page offers a training. Is the training meant to be the "answer key"? This ad has the lowest LPCR (9.3%).
4. Which pre-qualifier answers disqualify, and where do they redirect? Is the Lead event on the form or on the training page?
5. The playbook says parents respond better to a "free roadmap / one-pager" than a 10-15 minute training. Is that worth a later test, after these 5?

---

## Appendix: Facts pulled

### LPCR
- Sheet: "(CZ) - Business Reporting B2C", fileId 15BB-dlXY_g-0Xl8A9UYv0X88BVs0I7TOFTRzOJC49QU (modified 2026-10-12T20:01, shared with me). A second copy with the same name (15PHZw6ci2y5XLa0iWsQqoZC0MUc59lYIz9ggKBDLOGs, modified 2026-10-11) was not used.
- Tabs used: Dash, Jul, Aug, Sep, Oct. Columns: A date, B Adspend (USD), E Link Clicks, H Lead, I Pre-Qualified Leads, J Qualified Lead. Threaded comments in column A were read for the change log.
- 7d (Oct 5-11): 50 / 437 = 11.4%. 3d (Oct 9-11): 25 / 204 = 12.3%. Best month Aug: 154 / 1,166 = 13.2%. Best week Aug 31-Sep 6: 55 / 235 = 23.4%. Drop: Sep 14 ("new ads launched").
- Pre-qualified rate Oct 5-11: 42 / 50 = 84%. Qualified leads Oct MTD: 2 of 65 (sheet Dash).
- Sheet comment log: Jul 22 "changed button to book a call", Aug 6 "launched new ads", Aug 25 "launched video ad", Aug 28 "added prequalifier", Sep 7 "increased budget", Sep 10 "budget to 140", Sep 11 "budget to 170$", Sep 14 "new ads launched".

### Ad copy (all 3 ads share it)
- Headline (title): "Is Your Teen Actually Competitive for Their Top College? Most Parents Don't Know Until It's Too Late."
- Link description (from preview): "Many of my peers' college consultants charged them 2x or 3x the price of College Zoom while not investing into them half as much..." (the same Katelyn L. review that is on the page).
- Primary text, key lines:
  - "If your teen is in 9th to 12th grade, targeting UCLA, USC, or better, and you feel overwhelmed by conflicting admissions advice - this is for you."
  - "A parent who runs a $10 million admissions consulting company hired us for their own kid. So did an investor in a global rival. So did former admissions readers at our largest competitors."
  - "That's what the Free Training: How Elite Colleges Actually Score Your Teen walks through."
  - "🎥 Step 1: Watch the Free Training / 📞 Step 2: Book your Free College Strategy Call - a direct conversation with David."
  - "17 years. 2,900+ students. 96.5% success rate to a student's top 3 self-chosen college."
  - "👇 Watch the Free Training and book your Free College Strategy Call."
- CTA: Learn More. URL: go.collegezoom.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=pcw_freetraining&utm_content=pp1dearletter.
- Creative images (downloaded and viewed, 1080x1350 each):
  - Dear Letter: "Dear Parent, If your teen has great grades and a real shot at a top UC, USC, or an Ivy - but you're quietly terrified it still won't be enough - there's a key almost no one has seen. ... I've spent 17 years reverse-engineering it into a personalized answer key: 2,200 families, a 96.5% top-3-choice rate. This is for parents ready to invest in doing college right - not the cheapest shortcut. Watch the free training and I'll hand you the key."
  - White Notes App: "There's a scoring rubric elite colleges use ... and almost no one's seen it. Targeting a top UC, USC, or an Ivy? ... I've spent 17 years collecting admissions office rubrics to create personalized answer keys for students. This is for parents ready to invest in doing it right - not the cheapest option. Get your personalized answer key below 👇"
  - Twitter Color: "How to Get Your 4.0 Teen Into a Top School When "Good Enough" Keeps Getting Rejected. 1 - Watch our Free Training: How Elite Colleges Actually Score Your Teen (free - takes 20 minutes, could change everything) 2 - See the internal scoring system elite colleges use to grade your kid 3 - Find out exactly which gaps are standing between your teen and an acceptance. Watch the training today 👇 (for parents of 9th to 12th graders targeting top 50 colleges only)"

### Page copy (go.collegezoom.com/access)
- Title "College Zoom". Call-out "PARENTS OF 9TH-12TH GRADERS ONLY". Headline "The Hidden Score That Gets Your Teen Into Their Top-3 College". Form header "Training access in just 30 sec!"
- Fields: First Name * (text), Phone * (tel, US +1 flag), Email *, radio "Will earning scholarships be a key factor in where your child ultimately enrolls? *" (4 options quoted above), consent checkbox "I consent to receive emails and SMS messages regarding my submission and related updates." (required, unticked), 4 hidden UTM fields, button "Submit".
- Below the form: "GOOGLE REVIEWS ★★★★★ 5.0 · 46 reviews", "YELP REVIEWS ★★★★★ 5.0 · 94 reviews", 12 review cards (e.g. Gaurav K. "Both my children are now attending Cornell University for Computer Science."; Katelyn L. "USC WBB - Half-Tuition Scholarship"), "Showing verified reviews from 140 total - 46 Google · 94 Yelp · All 5-star ratings".
- Tracking in the page: Clarity (xg3eqqx7ms) and a Meta pixel (988221430355964) with curly quotes, so it does not run.
- Page height: 1,967px on desktop, 2,364px on mobile.

### Profile facts (Client Profile: David Reynaldo (CollegeZoom))
- Offer: admissions consulting. Entry product is the College-Specific Gap Analysis ($450, or $530 for 75 min), then hourly ($350/hr) or packages. 3 draft one-sentence offers (college planning 9-11, applications, transfers).
- Guarantee: **none confirmed.** Only a draft ("Maybe this? ... We guarantee an offer of admission to a Top [50/100] University, or we will [Refund X% / Work for free next cycle]"), and David is uneasy about guarantees. Not used.
- Proof in profile: 17 years; last year 79 package + 28 hourly college app clients; "we just flipped 2 rejections from USC into acceptances"; Duke ED release to Stanford. The ad numbers (2,900+ / 2,200 / 96.5%) are not in the profile. They come from the live ad only.
- ICP: parents (students under 18), high-achieving but "boring" teens, mostly 11th then 10th grade, LA and Bay Area, 30-40% East Coast. Often STEM, pre-med, business.
- Qualified lead: household income $200k+ (often $250k+). Interviewed big firms and found them impersonal. Often a second or third child, after a bad experience with another consultant. Converts 2x when the student joins the call.

### Could NOT get
- Sheet rows for Oct 12-13 (not logged yet), so 7d/3d use Oct 5-11 / Oct 9-11.
- Real load rate: the broken pixel makes Meta's landing page views unusable.
- GHL funnel stats (page views to opt-ins), the pre-qualifier redirect logic, and the form's Lead event setting. No HighLevel funnel read was attempted, to keep this short. Recommend Ema checks in GHL.
- Whether UTM fields fill on real submits (no test submit, read-only).
- The video on the opt-in page was not played or transcribed.
