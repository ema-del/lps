# LPCR page review: Pacow Media (own funnel)

**Verdict:** The ads sell a guarantee, a 45-min call with Viktorija and named client results. The page (lp.pacowmedia.com/access) only offers "the free training", shows no guarantee and no results near the form, and adds a revenue question. LPCR is 11.6% (last 7 days, main funnel) against a 20% goal, and has been stuck at 10-12% since July.

## Live ads (Meta, account 3720107534883410 "Pacow Backup", EUR, last 14 days, effective_status ACTIVE)

Both live lead campaigns send traffic to the same page: `lp.pacowmedia.com/access` (302 redirect to `/opt-in-page-4921`).
- **OLead - Free Training - Ed biz - 30+ - US** (ad set "OLead - Control") = main sheet "(PCW) - Business Reporting Daily Official 2026".
- **OCompleteRegistration - Free Training - Ed biz - 30+ - US** (started about 8-9 Oct) = sheet "(PCW) - OCompleteReg - Business Reporting Daily Official 2026".
- No OSchedule campaign is live. The OSchedule sheet has data only for 16-28 Sep.
- Also live: "Hammer Them Retargeting Strategy V2" (8 awareness ads, about €94 total, 0 link clicks). Left out of the table below.

| Campaign | Ad | Spend € | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR (Meta leads) |
|---|---|---|---|---|---|---|---|---|
| OLead | ed business + course - making 10k (video) | 2,168.78 | 402 | 354 | 19 | 49.2% | 88% | 4.7% |
| OLead | ed business - 1st video ever launched (video) | 748.60 | 139 | 117 | 11 | 17.0% | 84% | 7.9% |
| OLead | ed business black notes app (static) | 482.01 | 63 | 50 | 7 | 10.9% | 79% | 11.1% |
| OLead | ed brands im looking for youn 100k A1 (static) | 110.24 | 9 | 8 | 0 | 2.5% | 89% | 0% |
| OLead | ed business watch before you run ads (video) | 68.29 | 13 | 9 | 0 | 1.6% | 69% | 0% |
| OLead | ed business slack screenshot (static) | 52.28 | 18 | 15 | 0 | 1.2% | 83% | 0% |
| OLead | ed business $4k spend $71k rev (video) | 42.28 | 0 | 0 | 0 | 1.0% | n/a | n/a |
| OCR | ed brands im looking for youn 100k A1 (static) | 541.46 | 85 | 68 | 10 | 12.3% | 80% | 11.8% |
| OCR | ed business - 1st video ever launched (video) | 130.69 | 14 | 12 | 2 | 3.0% | 86% | 14.3% |
| OCR | 5 other ads (notes app, watch before, slack, $4k/$71k, making 10k) | 59.23 | 12 | 9 | 0 | 1.3% | 75% | 0% |
| **OLead total** | | **3,672.48** | **644** | **553** | **37** | **83.4%** | **86%** | **5.7%** |
| **OCR total** | | **731.38** | **111** | **89** | **12** | **16.6%** | **80%** | **10.8%** |

- Meta under-counts leads. Sheet logs 71 OLead leads for the same 14 days (28 Sep to 11 Oct) on 654 clicks. Meta logs 37 on 644 clicks. So read the per-ad LPCR above as a ranking only. The real LPCR is in the sheet.
- One video ad takes half the spend and has the weakest Meta LPCR (4.7%). Its copy promises "Book a 45-min call with Viktorija", and the page never mentions that call.

## Fix first (broken, not tests)

1. **Client count differs across ads and page.** Ads say "Trusted by 35+ education brands." (OCR/slack statics) and "Backed by 40+ brands" (notes app). The page says "45+ EDUCATION LEGENDS ALREADY TRUST US" and "See all 45+ partners". The sheet's own test plan says "35+". Pick the real number and use it everywhere.
2. **Guarantee wording doesn't match the docs.** Ads say "10-20+ New Students Every Month - GUARANTEED" (headline, second-biggest ad), "If the ads don't get you results - you simply don't pay" and "And if they don't work... you don't pay!". The page has no guarantee at all. The docs say something else:
   - Team Onboarding doc (Growth OS): "15 booked, qualified calls within the engagement period - conditional on the client following the process".
   - Offer Suite (Tier 2): "anything over 1x roas on contracted is considered 'profitable'", with 7 conditions ($100+/day for 3 months, attend all calls, and so on).
   - No doc guarantees "10-20+ new students". Confirm the approved wording before T1 below goes live. Changing the ads themselves is Ema's call.
3. **Tracking gap.** Meta counts about half the leads the sheet logs (37 vs 71). Check where the Lead event fires: on form submit, or only after the $10k answer. The sheet logs 27 pre-qualified leads, which is close to Meta's 37. Judge LPCR on the sheet.
4. **Page has an empty `<title>`.** The browser tab shows the URL. Set it to "Free Growth Training | Pacow Media".
5. **Small checks that passed:** load rate is fine (OLead 86%, OCR 80%, borderline). The page loads in about 1.2s even with the redirect. The phone field defaults to US (matches the US target). Terms and Privacy links are in the footer and the consent box. On mobile the form is visible without scrolling (button top at about 790px on an 844px screen). The Cloudflare Turnstile on the form is the invisible type, so visitors don't see it.

## 5 A/B tests (biggest expected lift first)

**T1. Headline: say the offer and the guarantee the ads already promise**
- A (now): "Discover how to add 10-20+ new students every single month" / "Powered by GrowthOS™ - Meta ads, automated sales funnels, and AI bots."
- B: Headline: "Add 10-20+ new students a month with ads we build and launch in 14 days" / Subheadline: "If the ads don't get you results, you don't pay. Watch the free growth training, then book your free 45-min growth call with Viktorija."
- Why: the top static ads say "We build & launch your ads in 14 days" and "If the ads don't get you results - you simply don't pay". The page drops both. Playbook: "Headline = the offer ("Get X in X time, or guarantee") and it must be the same on every page." Also "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Ship B only with the guarantee wording confirmed in Fix first #2. If the approved wording is the 15-calls version, use: "Follow the process and get 15 booked, qualified calls in 90 days."

**T2. Named results right under the form button**
- A (now): no results on the page. Below the form there are only logos and "45+ EDUCATION LEGENDS ALREADY TRUST US" (about 1,260px down on mobile, after the video).
- B: a one-line strip directly under "GET ACCESS NOW!": "Julian: $4k ad spend to $71k revenue · Sarah: $250k in 60 days · Alex: $110k in 90 days". Keep the logos below it.
- Why: these exact results are in the live notes app ad ("Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days"). The process says proof with real numbers goes near the form. Pacow's index rule 5: "Specificity plus proof beats cleverness." This is also T1-B in the sheet's "LPCR A/B tests" tab.

**T3. Remove the $10k question from the opt-in**
- A (now): "Which best describes you? *" with "I'm a business doing $10k+/mo" / "I'm a business doing less than $10k/mo" (4 fields plus consent).
- B: first name, phone, email and consent only. Move the revenue question to Q1 of the qualification survey.
- Why: playbook: "only add one if you have enough leads and can afford a higher CPL. If CPL is already $45-50, don't". Main funnel CPL in Oct is €54.50 and OCR is €52.21. Pre-launch checklist: "Hardest disqualifier is Q1" of the qualification form. The callout already filters ("Education brands & course creators making $10k+/mo"). If B goes live, move the Lead event back to form submit ("Opt-in form ... on submission = Lead"). Judge this test on LPCR plus pre-qualified and qualified leads per 100 clicks.

**T4. Form header and button name what the ad promised**
- A (now): form header "Instant access to the free training in 30 sec!" and button "GET ACCESS NOW!"
- B: form header "Free Growth Training + Free Growth Call" and button "Watch the Free Growth Training"
- Why: 70% of spend runs on ads whose copy opens "Free Growth Training + Free Growth Call 🎯" and "Book a 45-min call with Viktorija". The process says: "Button text says what they get" and "One name for the freebie everywhere". Right now the ads use three names: "Free Growth Training", "Free Student Acquisition Training" and "Student Enrollment System". The page uses "the free training" and "GrowthOS™".

**T5. Two lines of framing above the form**
- A (now): no framing. The form starts at "First Name *".
- B: above the form fields: "We're looking for 5 education brands who want to scale with paid ads. Enter your details to watch the training and see if you qualify for a free growth call."
- Why: Pacow pre-launch checklist: "2-3 lines of framing copy above the qual form explaining why the form exists and creating exclusivity". "I'm looking for 5 education brands" is the hook of the live OCR static, which takes 12.3% of spend.

## How to run them

- **Traffic:** about 550 clicks a week to this page (OLead 328 in the last 7 days, OCR about 230 a week based on 98 clicks in 3 days). That is about 79 a day.
- **Time per test:** at 150 visitors per version (300 per test), each test takes about 4 days. The sheet's own stopping rule ("about 50+ opt-ins per version") needs about 420 visitors per version at 12% LPCR, so about 11 days. Use 150 per version as the minimum and 50 opt-ins as the call.
- **Bundle to save time:** T1 + T2 + T4 all bring the page in line with the ad. Run them as one B version first (about 11 days to 50 opt-ins each). Then run T3 alone, because it changes lead quality and the pixel. Then T5.
- **Both campaigns hit the same page.** Split results by utm_campaign (oLead vs ocompleteregistration) in GHL so one campaign doesn't hide the other.
- **Clarity labels:** the live page already has `clarity("set","variant","T1-A")`. Re-label to match this plan: T1-A / T1-B (bundle: headline + proof strip + form header/button), T2-A / T2-B (pre-qualifier off), T3-A / T3-B (framing copy). Update the "LPCR A/B tests" tab to match.
- Log every page change in the sheet's notes column (it is empty for Jul to Oct).

## Questions for Ema

1. When was the "$10k+/mo" radio added to the opt-in? The sheet starts logging Pre-Qualified at the end of June, and LPCR fell from 14.8% (Jun) to 11.3% (Jul) and has not recovered.
2. Is the T1 test in the "LPCR A/B tests" tab live? The page served "T1-A" on both loads and I never saw a B version. Since when?
3. Which guarantee is approved for Pacow's own funnel: "you don't pay", 15 booked qualified calls in 90 days, or the 1x ROAS terms?
4. What is the real partner count: 35, 40 or 45?
5. Where does the Lead pixel fire on this page (form submit, or after a $10k answer)?
6. Should "Student Enrollment System" (OCR static copy) be renamed GrowthOS™ to match the page?
7. What does the "making 10k" video (49% of spend) promise in the first 10 seconds? I could not hear the audio.

---

## Appendix: Facts pulled

### LPCR (sheet "(PCW) - Business Reporting Daily Official 2026", month tabs, col E "Link Clicks", col H "Lead"; LPCR = H / E. Dash col L matches)
- Last 7 days (5-11 Oct): 38 leads / 328 clicks = **11.6%** (spend €2,051.71).
- Last 3 days (9-11 Oct): 23 / 136 = **16.9%**.
- With the OCompleteReg sheet added (9-11 Oct: 14 leads / 98 clicks = 14.3%): 7 days 52 / 426 = 12.2%, 3 days 37 / 234 = 15.8%.
- 2026 by month: Jan 14.4%, **Feb 15.5% (best, 88/568)**, Mar 15.4%, Apr 6.9%, May 14.6%, Jun 14.8%, Jul 11.3%, Aug 12.2%, Sep 10.5%, Oct (1-11) 11.5%.
- When it dropped: a dip in April (weekly 6-10%), back to about 15% in May-Jun, then down from the week of 13 Jul (10.2%). It has stayed at 9-12% weekly since.
- Other Oct numbers: CPL €54.50 (sheet target "< €22", max €65), pre-qualified rate 36%, 3 qualified leads, CTR 1.6%.
- OSchedule sheet: Sep 3,670.51 spend, 336 clicks, 26 leads (7.7%), 16-28 Sep only.
- The sheet's month tabs label spend "USD" and the Dash says "EUR". The Meta account is EUR.

### Ad copy (live, quoted)
- Video ads, OLead (making 10k, 1st video), primary text: "Free Growth Training + Free Growth Call 🎯 / ✔️ Watch the short training / ✔️ Book a 45-min call with Viktorija / ✔️ Get clarity on scaling your education brand / ✔️ Build a system that adds 10-20+ students monthly / 📞 Education brands & Course Creators only" (1st video says "Education brands only").
  - Headlines: "Education Brand Founders: Ready for 10-20+ New Students Every Month?" and "10-20+ New Students Every Month - GUARANTEED".
- Static "black notes app" image: "Education Brands Doing $10k+/mo. Here's My Promise: / We build & launch your ads in 14 days - you scale to 10-20+ new students a month / Backed by 40+ brands: Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days / If the ads don't get you results - you simply don't pay / Watch the FREE training today and book your free call with me".
- Static "looking for 5" image: "I'm looking for 5 education brands who want to scale to $100k+/mo in 2026 with paid ads / We'll script, edit, and launch your ads in 14 days / And if they don't work... you don't pay!"
  - Primary text (also notes app and slack): "ATTENTION: Education Business Owners 🎓 ... 🎥 Watch Our Free Student Acquisition Training ... our Student Enrollment System ... Trusted by 35+ education brands. After watching, you can book a free strategy call to see if we're a fit."
  - Headline: "Why Most Education Businesses Struggle to Enroll Students Consistently".

### Page copy (lp.pacowmedia.com/opt-in-page-4921, loaded 12 Oct with Playwright)
- Callout pill: "Education brands & course creators making $10k+/mo"
- Headline: "Discover how to add 10-20+ new students every single month"
- Sub: "Powered by GrowthOS™ - Meta ads, automated sales funnels, and AI bots."
- Video preview image ("Pacow training preview") with "VIKTORIJA, CO-FOUNDER OF PACOW MEDIA". On mobile it sits below the form.
- Form header: "Instant access to the free training in 30 sec!"
- Fields: First Name *, Phone * (US flag default), Email *, "Which best describes you? *" (2 radios: $10k+/mo, less than $10k/mo), consent checkbox (required). No prefilled values.
- Button: "GET ACCESS NOW!"
- Below: "45+ EDUCATION LEGENDS ALREADY TRUST US / FEATURED PARTNERS" (logos: College Essay Guy, examkrackers, Lingua Verna, College Consulting.us), "See all 45+ partners". Footer has Terms and Privacy.
- No guarantee, no testimonials, no reviews block, no named results.
- Tech: Meta pixel 888978410465183 PageView, Clarity tag "T1-A", invisible Cloudflare Turnstile.
- Screenshots: pacow-desktop.png, pacow-mobile.png (plus -full versions).

### Profile facts (no client profile exists; taken from Drive docs)
- Offer: Growth OS™, "a 90-day, done-for-you engagement" covering the Meta ads build, VSL, survey and booking funnel, tracking, and sales coaching (Pacow_Media_Team_Onboarding_What_We_Do). Offer Suite: Tier 1 DIY $5,000/12 months, Tier 2 DWY $10k PIF 90-120 days, Tier 3 DFY $5k/mo + 10% of spend.
- Real guarantee: "15 booked, qualified calls within the engagement period - conditional on the client following the process" (onboarding doc). Tier 2: "anything over 1x roas on contracted is considered 'profitable'", with conditions (Offer Suite).
- Proof: the live ad names Julian, Sarah and Alex results. The onboarding doc names clients "College Essay Guy, Lingua Verna, Zinkerz".
- ICP: "US-based, high-ticket education businesses" (test prep, tutoring, admissions, language schools, vocational, course creators).
- Qualified lead (index, "Disqualification criteria"): hard DQs are "under $5k/mo revenue or can't spend $100/day on ads". The page's opt-in question uses $10k/mo.

### Playbook rules used
- "Headline = the offer ("Get X in X time, or guarantee") and it must be the same on every page."
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- Pre-qualifiers: "only add one if you have enough leads and can afford a higher CPL. If CPL is already $45-50, don't". Also "B2B can ask revenue."
- "With a pre-qualifier: remove the pixel from the opt-in form and fire Lead on the training/VSL page."
- Squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block". The page is missing the reviews block.
- Pre-launch checklist: "2-3 lines of framing copy above the qual form", "Hardest disqualifier is Q1", "Testimonials have real first names + last initial + specific outcomes".

### Could not get
- Audio and script of the video ads (49% + 17% of spend). I only had the primary text, headline and a preview frame.
- The ads' destination URL from `ads_get_creatives` (link_url came back empty). I got it from the Meta preview HTML instead: `lp.pacowmedia.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=ocompleteregistration&utm_content=edbrandslookingforyoung100k`.
- GHL funnel step stats (page views to opt-ins). I didn't try HighLevel, to save time. GHL lead counts come from the sheet.
- A B version of the live T1 test. Only A was served.
- `ads_get_ad_accounts` was not needed, because the Pacow Backup account had active spend.
- The form was not submitted (read-only), so the Lead pixel firing and the redirect after submit are unchecked.
