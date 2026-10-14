# LPCR page review: Pacow Media (own funnel), 14 Oct 2026

**Verdict:** The ad with 60% of spend sells "10-20+ New Students Every Month - GUARANTEED" and "Book a 45-min call with Viktorija". Neither live version of the page mentions a guarantee or the call. That ad's URL is also broken, so its visitors arrive with no UTMs. LPCR is 14.2% for the last 7 days (sheet), up from 9.4% the week before, and still under the 20% goal.

What changed since the 12 Oct review:
- The "making 10k" video fell from 49% to 17% of spend. "1st video ever launched" now takes 60%.
- The OCompleteRegistration campaign has no active ads today (its sheet logs spend through 13 Oct). Per the brief, it is left out of the ad table.
- `lp.pacowmedia.com/access` now splits traffic about 50/50 between two pages: the old `/opt-in-page-4921` and a new `/opt-in` with a different headline. Both pages tag Clarity as "T1-A".

## Live ads (Meta, account 3720107534883410 "Pacow Backup", EUR, last 7 days = 7-13 Oct, effective_status ACTIVE)

15 active ads: 7 in "OLead - Free Training - Ed biz - 30+ - US" (ad set "OLead - Control") and 8 in "Hammer Them Retargeting Strategy V2" (€44.77 total, 0 link clicks, left out of the table below).

| Ad | Format | Spend € | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR (Meta leads) |
|---|---|---|---|---|---|---|---|---|
| ed business - 1st video ever launched | video 37s | 1,264.77 | 217 | 183 | 13 | 59.6% | 84% | 6.0% |
| ed business + course - making 10k | video 73s | 369.16 | 54 | 55 | 2 | 17.4% | 102% | 3.7% |
| ed business black notes app | static | 277.12 | 22 | 16 | 3 | 13.1% | 73% | 13.6% |
| ed brands im looking for youn 100k A1 | static | 164.46 | 17 | 14 | 0 | 7.8% | 82% | 0% |
| ed business slack screenshot | static | 40.91 | 16 | 13 | 0 | 1.9% | 81% | 0% |
| ed business watch before you run ads | video | 4.60 | 2 | 1 | 0 | 0.2% | 50% | 0% |
| ed business $4k spend $71k rev | video | 0.80 | 0 | 0 | 0 | 0.0% | n/a | n/a |
| **OLead total** | | **2,121.82** | **328** | **282** | **18** | **100%** | **86%** | **5.5%** |

- Meta counts 18 leads. The sheet logs 43 for the same 7 days. Meta sees 42% of the leads (it was 52% on 12 Oct). Read the per-ad LPCR as a ranking only.
- Unique link clicks in Meta: 297. The sheet logs 303 link clicks, so the sheet is close to unique clicks.

## Fix first (broken, not tests)

1. **The top ad's URL is broken.** "ed business - 1st video ever launched" (59.6% of spend) goes to: `lp.pacowmedia.com/access?https://lp.pacowmedia.com/access/?utm_source=meta&utm_medium=paid_social&utm_campaign=newmay2026&utm_content=edbusiness1stvideoeverlaunched...` The full URL was pasted into the URL parameters box. I loaded this URL: the redirect drops every UTM and lands on `/opt-in?https://lp.pacowmedia.com/access/` or `/opt-in-page-4921?https://lp.pacowmedia.com/access/`. The form's hidden UTM Source/Medium/Campaign/Content fields stay empty. The other 4 spending ads have clean URLs (checked notes app, making 10k, looking for 5, slack). Playbook: "URL parameters on every ad ... Paste without a leading "?"" and leads come "from GHL (filter utm_medium = paid social + tags)". If the sheet uses that filter, it misses or mislabels leads from 60% of spend. Changing the ad is Ema's call.
2. **A live split test has no labels.** About half the visits to `/access` go to `/opt-in` (5 of 12 test loads) and half to `/opt-in-page-4921` (7 of 12). Both pages run `clarity("set","variant","T1-A")`, so Clarity can't tell them apart. The sheet's "LPCR A/B tests" tab says T1-B is a results strip. The live B is a headline change. Tag `/opt-in` with its own label, write its start date in the sheet notes, and update the tab.
3. **The guarantee is still unconfirmed (same as 12 Oct).** The top ad's headline says "10-20+ New Students Every Month - GUARANTEED". The notes app static says "If the ads don't get you results - you simply don't pay" and the "looking for 5" static says "And if they don't work... you don't pay!". The docs say something else: the Team Onboarding doc has a "15-booked-call guarantee" and the Offer Suite has "1x ROAS conditional guarantee" (Tier 2). Neither page has any guarantee. Confirm the approved wording before T2.
4. **The partner count still differs (same as 12 Oct).** Ad primary text: "Trusted by 35+ education brands." Notes app image: "Backed by 40+ brands". Both pages: "45+ EDUCATION LEGENDS ALREADY TRUST US" and "See all 45+ partners". Pick the real number and use it everywhere.
5. **Tracking gap.** Meta 18 leads vs sheet 43 (7 days). Pre-qualified in the sheet for the same days: 11. Meta sits between the two, so check where the Lead event fires (form submit, or only after the $10k answer). Judge LPCR on the sheet.
6. **Both pages have an empty `<title>`.** Set it to "Free Growth Training | Pacow Media".
7. **Checks that passed:**
   - Load rate 86% overall. Notes app is 73%, but only 16 of 22 clicks.
   - Pages load in 1.5 to 4.7s.
   - Phone field shows the country picker (US default on 12 Oct, matches US targeting).
   - Terms and Privacy links are in the footer.
   - Pixel 888978410465183 fires PageView.
   - On mobile the button is visible without scrolling (top at about 793-799px on an 844px screen), just above the fold line.
   - Minor: on one desktop load of `/opt-in-page-4921`, the training preview GIF was still a blank white box at 4.7s. It loads later.

## 5 A/B tests (biggest expected lift first)

**T1. Headline and subheadline: say what the top two ads promise**
- Change: "Discover how to add 10-20+ new students every single month" / "Powered by GrowthOS™ - Meta ads, automated sales funnels, and AI bots." (and the running variant "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month")
- To: Headline "Free Growth Training + Free Growth Call: build a system that adds 10-20+ students monthly" / Subheadline "Watch the short training, then book a 45-min call with Viktorija to get clarity on scaling your education brand."
- Why: every word comes from the primary text of the two videos that take 77% of spend ("Free Growth Training + Free Growth Call 🎯 / ✔️ Watch the short training / ✔️ Book a 45-min call with Viktorija / ✔️ Get clarity on scaling your education brand / ✔️ Build a system that adds 10-20+ students monthly"). Neither live headline mentions the call. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". This replaces the running headline split.

**T2. Guarantee line under the headline (only after Fix first #3)**
- Change: no guarantee anywhere on the page.
- To: "If the ads don't get you results, you don't pay." If the approved terms are the onboarding doc's 15-call guarantee, use the condition first: "Follow the process and get 15 booked, qualified calls in 90 days."
- Why: the top ad's headline is "10-20+ New Students Every Month - GUARANTEED", and two statics say "you don't pay". The page drops the risk reversal the click was based on. Playbook: "Headline = the offer ("Get X in X time, or guarantee")" and "Headline = main offer; guarantee lower on the page." Index rule 13: "the condition is always stated before the number." I left out "10-20+ new students GUARANTEED" as page copy because no doc backs it.

**T3. Named results right under the button**
- Change: below "GET ACCESS NOW!" there are only logos and "45+ EDUCATION LEGENDS ALREADY TRUST US".
- To: "Julian: $4k ad spend to $71k revenue · Sarah: $250k in 60 days · Alex: $110k in 90 days", then the logos.
- Why: these exact results are on the live notes app image ("Backed by 40+ brands: Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days"). Index rule 5: "Specificity plus proof beats cleverness. Real numbers, real named client results". This is also T1-B in the sheet's "LPCR A/B tests" tab.

**T4. Form header and button name the freebie from the ads**
- Change: "Instant access to the free training in 30 sec!" / "GET ACCESS NOW!"
- To: "Get the Free Growth Training in 30 sec" / "WATCH THE FREE TRAINING"
- Why: the ads say "Free Growth Training", "Watch the short training" and "Watch the FREE training today and book your free call with me". The process says "Button text says what they get" and "One name for the freebie everywhere". The ads use three names ("Free Growth Training", "Free Student Acquisition Training", "Student Enrollment System"). The page uses "the free training" and "GrowthOS™".

**T5. Remove the $10k question from the opt-in**
- Change: "Which best describes you? *" with "I'm a business doing less than $10k/mo" / "I'm a business doing $10k+/mo" (first name, phone, email, radio, consent).
- To: first name, phone, email and consent only. The $10k question moves to Q1 of the qualification survey.
- Why: CPL for the last 7 days is €49.95 (sheet). Playbook: "only add one if you have enough leads and can afford a higher CPL. If CPL is already $45-50, don't". The callout pill already filters ("Education brands & course creators making $10k+/mo"), and so do the ads ("Education Brands Doing $10k+/mo"). Pacow's own hard DQ is "under $5k/mo revenue", so the opt-in is stricter than the rules. If B goes live, move the Lead event back to form submit ("Opt-in form ... on submission = Lead"). Judge on LPCR plus pre-qualified and qualified leads per 100 clicks.

## How to run them

- **Traffic:** about 300 clicks a week reach this page from OLead (303 in the sheet, 328 in Meta for 7-13 Oct). That is about 43 a day.
- **Time per test:** at 150 visitors per version (300 per test), a test takes about 7 days. The sheet's own rule ("about 50+ opt-ins per version") needs about 360 visitors per version at 14% LPCR, which is about 17 days.
- **Bundle:** stop the current headline split. Run T1 + T3 + T4 as one B version against the old page. All three only copy the ads' own words and need no approvals. Then run T2 once the guarantee is confirmed. Run T5 alone last, because it changes lead quality and where the pixel fires.
- **Fix the top ad's URL before starting.** Otherwise GHL can't split leads by utm_content.
- **Clarity labels:** T1-A / T1-B (bundle: headline + results strip + form header and button), T2-A / T2-B (guarantee line), T3-A / T3-B (no pre-qualifier). Give each page its own label and update the "LPCR A/B tests" tab to match.
- Log every page change in the sheet's notes column. The last note is from 9 Mar.

## Questions for Ema

1. Who started the `/opt-in` headline split, and on what date? LPCR went from 9.4% (30 Sep to 6 Oct) to 14.2% (7-13 Oct). I can't tell if the split caused it, because both pages report "T1-A".
2. Since when has the "1st video ever launched" ad had the pasted-in full URL? Are its leads showing up in the GHL smart list the sheet uses?
3. Which guarantee is approved for Pacow's own funnel: "you don't pay", 15 booked qualified calls, or the 1x ROAS terms?
4. What is the real partner count: 35, 40 or 45?
5. Where does the Lead pixel fire on the opt-in page?
6. Is the OCompleteRegistration campaign paused for good? Its sheet logs €265.71 spend on 13 Oct, but no ads in it are active today.
7. What does the top video say after "Do you own..."? I could not get the audio.

---

## Appendix: Facts pulled

### LPCR (sheet "(PCW) - Business Reporting Daily Official 2026": month tabs col E "Link Clicks", col H "Lead"; Dash col L "LPCR". LPCR = Lead / Link Clicks)
- Sheet is filled through 13 Oct.
- **Last 7 days (7-13 Oct): 43 / 303 = 14.2%.** Spend €2,147.76, CPL €49.95.
- **Last 3 days (11-13 Oct): 20 / 144 = 13.9%.** CPL €49.91.
- Week before (30 Sep to 6 Oct): 33 / 352 = 9.4%, CPL €63.86.
- Daily leads 7-13 Oct: 1, 8, 9, 5, 9, 8, 3 on 35, 42, 55, 27, 54, 51, 39 clicks.
- 2026 by month (Dash): Jan 14.4%, **Feb 15.5% (best, 88/568)**, Mar 15.4%, Apr 6.9%, May 14.6%, Jun 14.8%, Jul 11.3%, Aug 12.2%, Sep 10.5%, Oct 1-13 11.6% (72/619).
- When it dropped: a dip in April, back to about 15% in May and June, then weekly LPCR fell from 13.7% (week of 6 Jul) to 10.2% (week of 13 Jul). It stayed at 9-12% through 6 Oct. The last 7 days are the best week since August.
- Pre-qualified 7-13 Oct: 11. Qualified: 5. Oct to date: 23 pre-qualified, 8 qualified. Pre-qualified rate 32% (Dash).
- Sheet notes: "2026-03-07 changed to $10k/mo and $1k+ offer only", "2026-03-09 chnaged back to $5k+ and $1k+ offer". No notes after that.
- "LPCR A/B tests" tab: T1-A "4 logos and "35+ education legends."", T1-B "a results strip: "Julian: $4k ad spend → $71k · Sarah: $250k in 60 days · Alex: $110k in 90 days."" Other rows: mobile order headline/form/video, 6-10 reviews, "something new - idk" headline. Stop rule: "about 50+ opt-ins per version ... ahead by 3+ percentage points".
- OCompleteReg sheet (not in scope): 9-13 Oct 144 clicks, 21 leads (14.6%).
- The Oct tab labels spend "EUR" and the Sep tab "USD". The Meta account is EUR.

### Ad copy (live, quoted)
- **1st video ever launched (59.6%)**, video 37s.
  - Headline: "10-20+ New Students Every Month - GUARANTEED".
  - Primary text: "Free Growth Training + Free Growth Call 🎯 / ✔️ Watch the short training / ✔️ Book a 45-min call with Viktorija / ✔️ Get clarity on scaling your education brand / ✔️ Build a system that adds 10-20+ students monthly / 📞 Education brands only / 👇 Click to watch the training and book your call >>".
  - First frame: "EDUCATION BRANDS" text overlay, Viktorija on camera, caption "Do you own".
- **Making 10k (17.4%)**, video 73s.
  - Same primary text with "Education brands & Course Creators only".
  - Headline: "Education Brand Founders: Ready for 10-20+ New Students Every Month?".
  - First frame caption "Look,".
- **Black notes app (13.1%)**, static image: "Education Brands Doing $10k+/mo. Here's My Promise: / We build & launch your ads in 14 days - you scale to 10-20+ new students a month / Backed by 40+ brands: Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days / If the ads don't get you results - you simply don't pay / Watch the FREE training today and book your free call with me".
- **Looking for 5 (7.8%)**, static image: "I'm looking for 5 education brands who want to scale to $100k+/mo in 2026 with paid ads / We'll script, edit, and launch your ads in 14 days / And if they don't work... you don't pay!"
- **Slack screenshot (1.9%)**, static image: Slack messages "$6k with possibility for $15k!" and "sale for $6k!!" from Ashleigh, then "This is what a real paid ads acquisition system does for education brands - no referrals, no guesswork. / Want this for yours? Book a free call with me".
- **Static primary text** (notes app, looking for 5, slack): "ATTENTION: Education Business Owners 🎓 ... 🎥 Watch Our Free Student Acquisition Training ... ✅ How education brands consistently add 10–20+ students per month ... our Student Enrollment System ... Trusted by 35+ education brands. After watching, you can book a free strategy call to see if we're a fit. 👇 Watch the free training now."
  - Headline: "Why Most Education Businesses Struggle to Enroll Students Consistently".
- **Landing URLs** (from Meta preview):
  - Clean: `lp.pacowmedia.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=newmay2026&utm_content=<ad>` for notes app, making 10k, looking for 5 and slack.
  - Broken: 1st video (see Fix first #1).

### Page copy (loaded 14 Oct with Playwright, desktop 1440x900 and mobile 390x844)
- **Version A, `/opt-in-page-4921`:**
  - Callout pill: "Education brands & course creators making $10k+/mo".
  - Headline: "Discover how to add 10-20+ new students every single month".
  - Sub: "Powered by GrowthOS™ - Meta ads, automated sales funnels, and AI bots."
- **Version B, `/opt-in`:**
  - Same callout.
  - Headline: "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month".
  - No subheadline.
- **Both versions:**
  - Training preview GIF ("Pacow training preview") with "VIKTORIJA, CO-FOUNDER OF PACOW MEDIA" (desktop left of the form, mobile below it).
  - Form header "Instant access to the free training in 30 sec!".
  - Fields: First Name *, Phone *, Email *, "Which best describes you? *" (radios "I'm a business doing less than $10k/mo", "I'm a business doing $10k+/mo"), consent checkbox (required), hidden UTM Source/Medium/Campaign/Content. No prefilled values.
  - Button "GET ACCESS NOW!".
  - Below the form: "45+ EDUCATION LEGENDS ALREADY TRUST US / FEATURED PARTNERS" (logo grid), "See all 45+ partners", footer Terms and Privacy.
  - No guarantee, no named results, no reviews block, no mention of the call with Viktorija.
- **Tech:** Meta pixel 888978410465183 PageView, Clarity `clarity("set","variant","T1-A")` on both pages, empty `<title>`.
- **Screenshots** (scratchpad/oct14/):
  - Version A: `pacow-desktop.png`, `pacow-mobile.png` (copied to scratchpad/), plus `-full` versions.
  - Version B: `pacow-optin-desktop.png`, `pacow-optin-mobile.png`.

### Profile facts (no client profile; from the Playbook Index and the 12 Oct review)
- Offer: Growth OS, "a 90-day, done-for-you engagement" (Team Onboarding doc).
- Offer Suite tiers:
  - Tier 1 DIY: $5k for 12 months.
  - Tier 2 DWY: $10k PIF, 90 to 120 days, "1x ROAS conditional guarantee".
  - Tier 3 DFY: $3.5k/mo + 10% of spend (per the index; the 12 Oct review said $5k/mo).
- Real guarantee: "15-booked-call guarantee" (Team Onboarding doc), "conditional on the client following the process". Rule 13: "guarantees are conditional on the client following the process, and the condition is always stated before the number." No doc backs "10-20+ new students GUARANTEED" or "you don't pay".
- Proof: Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days (live notes app ad). Slack screenshot (Ashleigh $6k sales). Logos on the page. Clients named in the docs: College Essay Guy, Lingua Verna, Zinkerz.
- ICP: "US high-ticket education" brands (Team Onboarding doc).
- Qualified lead: hard DQs "under $5k/mo revenue or can't spend $100/day on ads" (Disqualification criteria). Calling script qualifies on "$10k/mo, $2k+ program".

### Playbook rules used
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- "Headline = the offer ("Get X in X time, or guarantee") and it must be the same on every page."
- "Headline = main offer; guarantee lower on the page. Ads can carry both."
- Pre-qualifiers: "only add one if you have enough leads and can afford a higher CPL. If CPL is already $45-50, don't". Also "B2B can ask revenue."
- "With a pre-qualifier: remove the pixel from the opt-in form and fire Lead on the training/VSL page."
- "URL parameters on every ad ... utm_content=[the ad's name]. Paste without a leading "?"."
- "DO NOT USE FACEBOOK TO TELL YOU HOW MANY LEADS YOU GOT..."
- "Comment in the sheet whenever you change budget, landing page or ads."
- Squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block". Both pages are missing the reviews block.

### Could not get
- **Video audio and script** for the two top videos (77% of spend). `download_hd_url` came back null and no transcription tool is installed. I only saw the first frame, the primary text and the headline.
- **link_url from `ads_get_creatives`** (empty). I took the landing URLs from the Meta preview HTML instead.
- **GHL funnel step stats and the GHL smart list filter.** Not tried, to save time. Lead counts come from the sheet.
- **Start date of the `/opt-in` split and per-version results.** Both versions share one Clarity label.
- **Form submit.** Not done (read-only), so where the Lead pixel fires and the post-submit redirect are unchecked.
- **Phone default country.** It was not readable from the DOM this time (the picker renders as "countryphone"). It showed US on 12 Oct.
