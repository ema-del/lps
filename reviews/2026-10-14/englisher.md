# LPCR page review: Englisher (PGCE for international teachers, GBP)

Date: 2026-10-14. Read-only review. Nothing was changed in Meta, Drive or on the page.

Heads-up: Englisher is not English tutoring. It is Englisher Ltd (Julian Millidge), a free consultancy that places working international teachers on the Leeds Beckett University online PGCE. The ads and page are about the PGCE.

## Verdict

**The ads sell a "Free PGCE Eligibility Call" that answers "PGCE vs iPGCE vs QTS". The page never mentions a call or iPGCE/QTS. The first thing people see is "September 2026 applications are now closed". On top of that, about 1 in 3 clicks never loads the page.**

## LPCR numbers

Lead = the Meta pixel **Lead** event (website form submit). The campaign is named "OCompleteRegistration" but Meta reports its results as `offsite_conversion.fb_pixel_lead`, so it is set to optimise for Lead. The reporting sheet's "Lead" column means the same thing. I also show CompleteRegistration (CR), which the playbook treats as the qualified lead.

| Period | Spend | Link clicks | LPVs | Load rate | Leads | **LPCR** | CR | CR / clicks |
|---|---|---|---|---|---|---|---|---|
| Last 7d (Oct 7-13) | £37.04 | 170 | 118 | 69% | 8 | **4.7%** | 5 | 2.9% |
| Last 3d (Oct 11-13) | £16.95 | 76 | 56 | 74% | 5 | **6.6%** | 2 | 2.6% |
| Last 30d | £149.92 | 753 | 511 | 68% | 23 | **3.1%** | 9 | 1.2% |

Monthly trend (Meta, campaign level):

| Month | Spend | Clicks | Load rate | Leads | LPCR |
|---|---|---|---|---|---|
| **Mar (best)** | £949.94 | 5,114 | 71% | 468 | **9.2%** |
| Apr | £991.72 | 6,753 | 62% | 479 | 7.1% |
| May | £1,319.86 | 13,269 | 44% | 808 | 6.1% |
| Jun | £1,431.93 | 9,630 | 51% | 371 | 3.9% |
| Jul | £1,558.21 | 6,230 | 60% | 199 | 3.2% |
| Aug | £1,630.12 | 4,934 | 55% | 113 | 2.3% |
| Sep | £158.44 | 779 | 67% | 22 | 2.8% |
| Oct 1-13 | £65.98 | 298 | 70% | 10 | 3.4% |

- **When it dropped:** LPCR slid through April and May and fell below 4% in June. The images on the current page are dated 2026-04-28, which suggests the base44 page (mypgce.co.uk) replaced the old page around May. Spend then fell from £1,630 (Aug) to £158 (Sep), after the 4 Sep 2026 application deadline.
- **Sheet** "(Englisher) - Business Reporting Daily 2026", Dash tab, columns "Link Clicks" and "Lead": Mar 414/4,782 = **8.7%**, Apr 276/3,915 = 7.1%, May 144/14,073 = 1.0% (May is only partly logged). The sheet has no data after May, so the 7d, 3d and trend numbers above all come from Meta.
- Every period is far below the 20% goal and the 15% "bad" line.

## Live ads (last 7 days, ACTIVE, campaign "Englisher//OCompleteRegistration//Free Consultation//THVNMYSG//ABO")

| Ad | Spend | Share | Clicks | LPVs | Load rate | Leads | LPCR | CR |
|---|---|---|---|---|---|---|---|---|
| Notes app Expat teachers | £16.96 | 45.8% | 69 | 43 | 62% | 4 | 5.8% | 3 |
| Twitter pgce/igpce/qts | £13.94 | 37.6% | 87 | 61 | 70% | 1 | 1.1% | 1 |
| Founder UGC 1 | £6.14 | 16.6% | 14 | 14 | 100% | 3 | 21.4% | 1 |
| **Total** | **£37.04** | 100% | 170 | 118 | 69% | 8 | 4.7% | 5 |

- 30d per ad: Notes app 7/126 (5.6%), Twitter 8/387 (2.1%), Founder UGC 8/240 (3.3%).
- All 3 ads link to the same URL (the homepage, see Fix first): `http://www.mypgce.co.uk/?https://mypgce.co.uk/?utm_source=Facebook&utm_medium={{placement}}&utm_campaign=...`
- Headlines: Notes app and Founder UGC use "Advance Your Teaching Career - Free PGCE Call". Twitter uses "PGCE Clarity Call for International Teachers". The CTA button on all three is "Book now".

## Fix first (broken, not tests)

1. **Phone default is UK (+44) on a campaign that targets Thailand, Vietnam, Malaysia and Singapore** (THVNMYSG, confirmed in the strategy doc: "Thailand, Vietnam, Malaysia, Singapore"). The placeholder "e.g. 7700 900123" is also a UK number. Thailand, Malaysia and Singapore are in the top block of the list, but Vietnam is further down. Fix: default to the visitor's country by IP, or to Thailand (+66), and move TH/VN/MY/SG to the top.
2. **Load rate 69% (7d), 68% (30d), only 44-60% from May to Aug.** Under the 80% line. In my test the page took 12.8s to reach the load event on mobile (3.1s on desktop). The ad URL also adds two redirects (http to https, www to no-www) and has a second URL pasted inside the query string. Fix: set the ad's website URL to `https://mypgce.co.uk/` and move the UTMs into the URL parameters field. This is an ad setting, so it's Ema's call. Then check page speed on mobile.
3. **The top banner kills urgency on every visit:** "September 2026 applications are now closed [dash] enrolling for September 2027 intake." (shown on screen with a dash). It's the first line on both desktop and mobile.
4. **Stale urgency in the Twitter ad** (37.6% of spend): "Limited advisor slots before the September deadline." The 2026 deadline was 4 Sep 2026 (FAQ doc), and the next intake is September 2027. This is ad copy, so flag it to Ema.
5. **The course length contradicts itself on one screen.** The headline says "9 Months" while the stat row says "1 Year Online". The client FAQ says "Course lasts 10 months: Sept-July" and "many students finish as early as May". The strategy doc says "within 1 academic year". Pick one wording that the FAQ backs up.
6. **Unproven numbers:**
   - Page: "3,500+ Teachers". This number isn't in any Englisher doc I found.
   - Twitter ad: "96% pass rate with guided support groups". This only appears in Pacow's draft "(Englisher) Booking Ad Copy" and is not in the client FAQ.
   - Get a source from Julian, or remove both. Until then I left them out of every B version.
7. **The button text is cut off on mobile.** At 390px it reads "heck My Eligibility for September 2027" (the first letter is clipped). See englisher-mobile.png.
8. **No privacy policy or terms links.** The page has zero links. The playbook says "Terms and privacy policy links in every footer (required by Facebook...)".
9. **Proof is locked.** The 4 video tiles ("Why Teachers Choose PGCE", "Flexible Payment Options", "Our Graduates at LBU", "Do You Qualify?") say "Click 'Check My Eligibility' to watch". Nobody gets to see proof before they opt in.
10. **Tracking:**
    - The campaign name says CompleteRegistration, but it optimises for Lead.
    - The reporting sheet stopped in May.
    - In headless Chromium I saw `fbq('init', '2601525220193047')` and fbevents.js load, but no PageView hit. Meta does record LPVs, so the pixel probably fires in real browsers. Check it with Pixel Helper.
    - I could not compare Meta leads with CRM leads. There is no GHL funnel (the page is on base44) and the sheet is empty after May.
11. **No client profile** in "00. Client Profiles (Claude)". Englisher needs one (offer, real terms, proof, ICP). I built the facts below from the strategy, ICP and FAQ docs.

## Ad vs page, side by side

| Check | Ad (quoted) | Page (quoted) | Match? |
|---|---|---|---|
| Call-out | "International & Expat Teachers Working Abroad" / "ATTENTION: International teachers working abroad" | "FOR INTERNATIONAL TEACHERS ONLY" | Yes |
| Pain / hook | "PGCE. iPGCE. QTS. Which qualification do international schools actually recognise?" (also the Twitter image) | Not mentioned anywhere | **No** |
| Offer | "Book a FREE PGCE Eligibility Call" / "Book a Free PGCE Eligibility Call with Englisher" / "PGCE Clarity Call", button "Book now" | Headline "Get a UK PGCE in just 9 Months 100% Online", form "Check your eligibility and learn more", button "Check My Eligibility for September 2027". No call. | **No** |
| Proof | "Thousands of international teachers have already used our guidance", "96% pass rate" | "3,500+ Teachers", partner logos, locked videos | Partly (numbers differ and are unverified) |
| Guarantee / risk | none in ads | none | Real terms exist (see appendix) but neither side uses them |
| Numbers / time | "In 30 minutes", "before the September deadline" | "9 Months", "1 Year Online", "September 2026 applications are now closed" | **No** |

## 5 A/B tests (biggest expected lift first)

**T1. Headline and subheadline (offer match)**
- Change: "Get a UK PGCE in just 9 Months 100% Online" / "Qualified international teachers: earn a UK-accredited PGCE online while continuing to teach abroad. Check your eligibility!"
- To: "PGCE, iPGCE or QTS? Book a Free PGCE Eligibility Call" / "In 30 minutes, see if a PGCE is the right move for your career, what international schools really recognise, and how to study online without quitting your job."
- Why: every live ad sells the call and the PGCE/iPGCE/QTS question, and the page sells neither. The playbook's rule for LPCR under 25% is "headline/offer must match the ad". All the words come from the ads.

**T2. Form fields (5 to 3)**
- Change: First Name, Last Name, Email, Nationality, WhatsApp Number (all required)
- To: First Name, Email, WhatsApp Number (remove Last Name and Nationality; ask "Where are you currently teaching from?" after the opt-in, as planned in "(Englisher) Booking Form Questions")
- Why: the playbook opt-in is "first name + phone (two columns), email full width". Nationality doesn't screen anyone out, because the FAQ says "Anyone from any country!" can apply. CPL is already low (£4.63 in 7d), so this test is about LPCR. Lead quality is screened later by the qualification survey.

**T3. Button and form title**
- Change: "Check your eligibility and learn more" / "Check My Eligibility for September 2027"
- To: "Book your free PGCE eligibility call" / "Book My Free Eligibility Call"
- Why: the ad button says "Book now" and the ad promises a call. The playbook says the button should say what they get. The shorter text also fixes the clipped button on mobile.

**T4. Top banner**
- Change: "September 2026 applications are now closed [dash] enrolling for September 2027 intake."
- To: "Now enrolling for September 2027 • Free eligibility call" (built from the page's own line "Now enrolling for September 2027" plus the ad offer)
- Why: the first thing on screen says "closed". The playbook says the page should give two options, "take the action or LEAVE", and this banner pushes people to leave.

**T5. Stat row under the headline (proof)**
- Change: "3,500+ Teachers" | "1 Year Online" | "UK Recognised"
- To: "Leeds Beckett University" | "100% online, no exams" | "Our service is 100% free"
- Why: each claim comes from the client FAQ: "FAQs PGCE COURSE LEEDS BECKETT UNIVERSITY", "3 assignments – no exams, no practical work!", "Our services are 100% FREE! The university covers our costs". It drops the unsourced 3,500+ and the "1 Year" vs "9 Months" clash. The ICP doc says "Lead with credibility proof (UK university, identical certificate...)".

Left out on purpose:
- "96% pass rate" and "3,500+", because I found no source for either.
- Any guarantee wording. The real terms are a refund policy ("Full refund within 28 days of the course start", "defer your place to the next course year at no extra cost"). That is a university policy, not an Englisher guarantee, so ask Julian before using it as risk reversal.

## How to run them

- Traffic: 170 clicks a week, but only about 118 page views a week at the current load rate. Fix the load rate first, or each test takes longer.
- About 150 visitors per version means 300 per test, which is about 2.5 weeks per test at today's traffic. Running 5 tests one by one would take about 13 weeks, so bundle them:
  - **Round 1 (about 2.5 weeks): T1 + T3 + T4 as one "offer match" version.** Clarity labels T1-A / T1-B.
  - **Round 2 (about 2.5 weeks): T2 form fields.** T2-A / T2-B.
  - **Round 3 (about 2.5 weeks): T5 proof row.** T3-A / T3-B.
- The page is on base44, not GHL, so a split needs a page duplicate plus a redirect-split tool, or two ads with different URLs at equal budget. Tag each version in Clarity with the labels above.
- Do the Fix first items (phone country, ad URL, mobile button, links, 9 vs 12 months) before Round 1. They are fixes, not tests.

## Questions for Ema / Julian

1. Who runs this now? The "(Englisher) Off-boarding" docs date from April 2026. Is Pacow still responsible for this funnel and the sheet?
2. When did mypgce.co.uk (base44) replace the old landing page? LPCR went from 9.2% (Mar) to 3.9% (Jun).
3. What happens after "Check My Eligibility"? Is a call booked, and which step fires Lead and which fires CompleteRegistration?
4. What is the source for "3,500+ Teachers" and "96% pass rate"?
5. Is the campaign meant to optimise for Lead even though its name says CompleteRegistration?
6. How many leads did their CRM log for Oct 7-13? (To check Meta's count of 8.)

---

## Appendix: Facts pulled

**LPCR sources**
- Meta API, account 926522605529299, campaign 120242218807900364. Ad level for last_7d, last_3d and last_30d; campaign level monthly for 2026-01-01 to 2026-10-13. Fields: amount_spent, link_click, unique_link_click (7d: 160), omni_landing_page_view, lead, omni_complete_registration.
- Sheet "(Englisher) - Business Reporting Daily 2026" (id 1EIDLXUP3JRf3TWYVn319jo4MHTuJ-BOKHMZhePTNghw), Dash tab, columns E "Link Clicks" and H "Lead". Data only for Mar, Apr and May. Monthly tabs from Jun to Aug are empty, and there are no Sep or Oct tabs.

**Ad copy (emojis removed)**
- *Notes app Expat teachers*: "International & Expat Teachers Working Abroad / If you're teaching in English, you could be eligible for a PGCE without putting your career on hold. / But first, you need clarity. / PGCE. iPGCE. QTS. MA ed. / Which qualification do international schools actually recognise? / And which route makes the most sense for your career goals? / Book a FREE PGCE Eligibility Call / Check for free whether a PGCE is the right route for your teaching career. / Check your eligibility / Understand PGCE vs iPGCE vs QTS / Learn what international schools look for / Explore flexible online study options / Get answers tailored to your teaching background / Thousands of international teachers have already used our guidance to move forward with confidence. / Reserve your free eligibility call now." Headline "Advance Your Teaching Career - Free PGCE Call". Creative: Notes-app card "How expat teachers are thriving with the PGCE:" with the lines "They understand the difference between PGCE, iPGCE & QTS", "Didn't waste money on the wrong route.", "Now getting better paid salaries at better paying international schools.", "Got their clarity from the free eligibility call." and "Book your eligibility call".
- *Twitter pgce/igpce/qts*: "ATTENTION: International teachers working abroad / Are you confused about PGCE vs iPGCE vs QTS? / Not sure which qualification schools actually respect? / You're not behind. You just haven't had clarity yet. / Book a Free PGCE Eligibility Call with Englisher / In 30 minutes, you will: See if a PGCE is the right move for your career / Understand what international schools really recognise / Check eligibility before you apply / Learn how to study online without quitting your job / 96% pass rate with guided support groups. / Thousands of teachers have already moved forward with confidence. / Limited advisor slots before the September deadline. / Book a free Call now." Headline "PGCE Clarity Call for International Teachers". Image: tweet-style post from "Julian Millidge @EnglisherLBU" that says "PGCE. iPGCE. QTS. Which qualification do international schools actually recognise? And which route makes the most sense for your career goals? Read caption to learn more!"
- *Founder UGC 1*: "PGCE Clarity Call / PGCE vs iPGCE explained / Eligibility check before applying / Study online while working full time / Trusted support from start to finish / Book a Call before the next intake deadline." Headline "Advance Your Teaching Career - Free PGCE Call". Creative: a 1:12 video of Julian talking to camera (I saw the thumbnail only; I did not hear the audio).

**Page copy (https://mypgce.co.uk/, title "Study PGCE online")**
- Page text, in order:
  - Banner: "September 2026 applications are now closed [dash] enrolling for September 2027 intake."
  - Call-out: "FOR INTERNATIONAL TEACHERS ONLY"
  - Headline: "Get a UK PGCE in just 9 Months 100% Online"
  - Subheadline: "Qualified international teachers: earn a UK-accredited PGCE online while continuing to teach abroad. Check your eligibility!"
  - Stat row: "3,500+ Teachers" "1 Year Online" "UK Recognised"
  - Form title: "Check your eligibility and learn more"
  - Under the button: "Now enrolling for September 2027 • Takes 2 minutes" and "We'll use your details to share your eligibility results via email and WhatsApp. You can opt-out at any time."
  - Locked video tiles, then "Click 'Check My Eligibility' to watch"
  - "IN PARTNERSHIP WITH" plus logos (Leeds Beckett, University of Buckingham, University of Chichester, Totally Teach and others)
- Form: First Name*, Last Name*, Email*, Nationality* (searchable list, includes Vietnam), WhatsApp Number* (default UK +44, placeholder "e.g. 7700 900123", 34-country list with TH/MY/SG near the top). Submitting it empty shows a "Required" error on every field. Nothing was prefilled. I did not submit the form.
- Mobile 390x844: the form starts about 460px down and the button sits at about 736px, so the form is visible without scrolling. The button text is clipped.
- Screenshots: oct14/englisher-desktop.png, oct14/englisher-mobile.png (plus -full versions).

**Profile facts (no profile exists; taken from the strategy, ICP and FAQ docs)**
- Offer (strategy doc): "We help working teachers become fully UK-PGCE qualified within 1 academic year - through a 100% online, university-accredited programme - without relocating, quitting their job, or navigating the process alone."
- Facts: Leeds Beckett University PGCE. 60 credits. 3 assignments, "no exams, no practical work". Tuition £3,350 (overseas) or £2,890 (British). 9-month instalment plan (exclusive through Englisher). One intake a year. 2026 deadline was 4 Sep 2026. Englisher's service is "100% FREE! The university covers our costs".
- Real terms (FAQ): "Full refund within 28 days of the course start. 50% refund after 3 months." Students can defer a year "at no extra cost". There is no Englisher-specific guarantee.
- Proof: no verified numbers. "96% pass rate" appears only in the Pacow draft ad copy. "3,500+" appears nowhere. The ad says "Thousands of teachers".
- ICP: expat ESL/EFL and international-school teachers working in Asia (TH, VN, MY, SG to start), British and non-British. Archetypes: International Career Builder, Credential-Constrained Professional, Leadership-Oriented Educator.
- Qualified lead ("(Englisher) Booking Form Questions"): currently teaching or holds/completing an undergraduate degree; comfortable studying 100% online while working; "prepared to proceed financially" or interested in instalments.

**Could NOT get**
- Sheet data after May 2026, because the sheet was not updated after the April off-boarding. 7d, 3d and the trend come from Meta only.
- CRM / GHL lead counts to check against Meta's. The page is on base44, not a GHL funnel.
- Which step fires Lead and which fires CompleteRegistration. I did not submit the form, to stay read-only.
- A confirmed PageView pixel hit in headless Chromium.
- The audio of the Founder UGC video. I only reviewed the thumbnail and the copy.
- A client profile. None exists in "00. Client Profiles (Claude)".
