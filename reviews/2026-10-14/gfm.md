# LPCR page review: GFM (Global Frontier Missions)

**Verdict:** LPCR is not readable this week. The campaign is nearly off (ad set budget cut to $1.01/day on 5 Oct), so the last 7 days are 8 clicks and 2 leads. On the last real traffic (14 Sep to 4 Oct, ~$25/day) LPCR was 16.2% on Meta numbers, under the 20% goal. The main page issue: every ad sells a "Free Readiness Framework" plus a "Missions Pathway Call", and the page never names either, never shows the guarantee, and on phones the form sits below the first screen.

**Campaign status (asked: just launched or nearly off?):** nearly off, and not new.
- Campaign "OLead//GFM//Free Consultation//US//ABO" was created 22 Mar 2026. Ad set "OLead//MTS//Broad//US//18-65+" created the same day.
- Ran Mar to May, off Jun to Aug, back on in Sep at about $25/day (not the $150/day in the off-boarding plan).
- Ad set `daily_budget` is now **$1.01**, last updated **5 Oct 2026 10:20**. Daily spend went from $29.99 (4 Oct) to $9.71 (5 Oct) to about $1/day since 6 Oct.
- No client profile exists in "00. Client Profiles (Claude)". Facts below come from the GFM Marketing Strategy doc, Off-boarding plan, Booking questions, UGC scripts and the reporting sheet. **A GFM profile needs to be made.**

## Live ads (Meta, account 3430858818430, USD, effective_status ACTIVE)

All 6 ads sit in one ad set and all go to the same page: `rdy.gogfm.org/booknow` (a GHL split that serves `/opt-in` or `/booknow-page`). All 6 use the headline "Missions Readiness: Free Framework + Clarity Call". They are flexible creatives, so Meta may rotate other primary texts; the ones quoted below are what the previews served on 14 Oct.

**Last 7 days (7 to 13 Oct). Too small to judge anything.**

| Ad | Spend $ | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR |
|---|---|---|---|---|---|---|---|
| Genz Beta Ad 1 Future Missionaries (video) | 4.43 | 5 | 3 | 2 | 55.7% | 60% | 40% |
| Founder Video ad A2 (video) | 1.93 | 1 | 0 | 0 | 24.3% | 0% | 0% |
| High Prod Image A1 (static) | 0.85 | 1 | 0 | 0 | 10.7% | 0% | 0% |
| Genz Beta Ad 1 (video) | 0.50 | 1 | 0 | 0 | 6.3% | 0% | 0% |
| Twitter Color A1 (static) | 0.16 | 0 | 0 | 0 | 2.0% | n/a | n/a |
| Founder Video ad A1 (video) | 0.08 | 0 | 0 | 0 | 1.0% | n/a | n/a |
| **Total** | **7.95** | **8** | **3** | **2** | 100% | 38% | 25% |

**Last 30 days (14 Sep to 13 Oct). Use this for the ranking.**

| Ad | Spend $ | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR |
|---|---|---|---|---|---|---|---|
| Founder Video ad A2 | 424.64 | 773 | 651 | 131 | 77.6% | 84% | 16.9% |
| Genz Beta Ad 1 Future Missionaries | 106.15 | 189 | 152 | 22 | 19.4% | 80% | 11.6% |
| High Prod Image A1 | 5.26 | 9 | 7 | 3 | 1.0% | 78% | 33% |
| Twitter Color A1 | 5.13 | 8 | 7 | 2 | 0.9% | 88% | 25% |
| Genz Beta Ad 1 | 3.91 | 4 | 3 | 1 | 0.7% | 75% | 25% |
| Founder Video ad A1 | 1.99 | 0 | 0 | 0 | 0.4% | n/a | n/a |
| **Total** | **547.08** | **983** | **820** | **159** | 100% | **83%** | **16.2%** |

- CPL is $3.44 (30 days). Meta benchmark says the ad set's cost per result is 56.7% better than peers. Cheap leads are not the problem; lead quality was (see Questions).
- The one ad that matters is Founder Video ad A2 (78% of spend). Its copy promises a call with a written outcome and says "June 1 deadline."

## Fix first (broken, not tests)

1. **The campaign can't produce data at $1.01/day.** 8 clicks a week means no LPCR, no test, no learning. Confirm with Ema whether GFM is paused on purpose (cohort timing?) before any page test. Budget is Ema's call; nothing was changed.
2. **"June 1 deadline." is still live** in the primary text of Founder Video ad A2 (78% of 30-day spend) and Twitter Color A1. It is October. The off-boarding plan said: "update all the ad copy to be for the new dates, not June 1st." Replace with the real next-cohort date, or cut the line. (Ad change, so Ema's call.)
3. **UTMs are broken on every ad.** The click lands on `rdy.gogfm.org/booknow?https%3A%2F%2Frdy.gogfm.org%2Fbooknow%2F%3Futm_source=meta&utm_medium=paid_social&utm_campaign=pcw_bookings&utm_content=...`. The full URL got pasted into the URL parameters box, so `utm_source` arrives under a garbage key. On the page the hidden "UTM Source" field is empty; "UTM Medium" = paid_social, "UTM Campaign" = pcw_bookings, "UTM Content" = founderugca2. Playbook: "URL parameters on every ad ... utm_campaign=[same for the campaign] ... Paste without a leading '?'." Fix: URL parameters = `utm_source=meta&utm_medium=paid_social&utm_campaign=olead_gfm_free_consultation&utm_content=<ad name>`. "pcw_bookings" also looks copied from another account.
4. **Mobile form is below the first screen.** On a 390x844 phone the first field starts at 911px and "Access" at 1,248px. The first screen is logo, headline, subheadline and the video preview. Desktop is borderline too: the "Access" button starts at 902px on a 900px screen.
5. **No guarantee on the page.** Ads say "30-day clarity guarantee." and "if you fully participate and discern it's not your calling, your tuition is refundable." The approved guarantee (Marketing Strategy) is "30-Day Clarity Guarantee: If by Day 30 you've actively participated and decide it's not the right fit, we refund your tuition." The page has nothing. See T3.
6. **Trust line misstates the proof.** Page: "TRUSTED BY 500+ FUTURE MISSIONARIES PREPARING FOR THE FIELD". The approved stat is "500+ missionaries trained through GFM programs". Change to "500+ MISSIONARIES TRAINED THROUGH GFM PROGRAMS".
7. **Reporting sheet stopped in May.** "(GFM) - Business Reporting Daily 2026" has Mar to May only. Jun to Oct are blank, so Sep and Oct have no GHL lead counts to judge LPCR on. The sheet linked in the Marketing Strategy doc (id 1ibF0W...) no longer exists.
8. **Small page fixes:** the page `<title>` is empty (tab shows the URL); footer has "Privacy Policy" only, no Terms link (playbook: "Terms and privacy policy links in every footer"). Two different freebie names across ads ("Free Readiness Framework", "Free Missions Framework" on the Twitter static) and two call names ("Missions Pathway Call" in copy, "Clarity Call" in the headline, "Free Mission Clarity Call" in nurture emails).
9. **A call-out split is running that can't finish.** `/booknow` sends people to `/opt-in` ("FOR FUTURE MISSIONARIES ONLY") or `/booknow-page` ("FOR ASPIRING MISSIONARIES ONLY"). The rest of the copy is the same. At $1/day it will never reach a result; stop it or fold it into the run plan.
10. **Checks that passed:** load rate 83% over 30 days (fine). Phone defaults to US (+1), which matches US targeting. 3 fields only, no test data, no pre-qualifier. Meta lead counts are close to the sheet (May: Meta 370, sheet 329), so no tracking undercount flag.

## 5 A/B tests (biggest expected lift first)

LPCR is not reliable yet, so these are mostly ad-to-page match fixes. Run them only once the budget is back.

**T1. Subheadline: name the freebie and the call the ads promise**
- Change: "Discover how 500+ missionaries have gained clarity, preparation, and a pathway to the field."
- To: "Watch the Free Readiness Framework, then book a 30-minute Missions Pathway Call. You'll leave with your training track, your timeline to the field, and your next three steps, in writing."
- Why: Founder Video ad A2 (78% of spend) says "Watch our Free Readiness Framework" and "Then book a Missions Pathway Call. In 30 minutes you'll have your training track, your timeline to the field, and your next three steps - in writing." The page names neither. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Keep the headline "Become Mission-Ready in Just 5 Months"; it matches the High Prod static ("HOW TO GO FROM "CALLED" TO PREPARED FOR LONG-TERM MISSIONS IN 5 MONTHS") and playbook says "Headline = the offer".

**T2. Mobile: form first, video preview under it**
- Change: on mobile, order is headline, subheadline, video preview, "Framework video access in just 30 sec!", then form (first field at 911px).
- To: headline, subheadline, "Framework video access in just 30 sec!", form, then the video preview. Shrink the logo on mobile.
- Why: process rule "Mobile: is the form visible without scrolling? (Most traffic is Instagram on phones.)" Right now it isn't.

**T3. Guarantee line under the button**
- Change: nothing under "Access" except "Privacy Policy".
- To: "30-Day Clarity Guarantee: if you fully participate in Missionary Training School and discern it's not your calling, your tuition is refundable."
- Why: both top ads carry the guarantee ("30-day clarity guarantee." / "your tuition is refundable"). The wording is the ad's, and it matches the approved Marketing Strategy terms. Playbook: "Headline = main offer; guarantee lower on the page."

**T4. Form header and button say what they get**
- Change: form header "Framework video access in just 30 sec!" and button "Access".
- To: form header "Get the Free Readiness Framework in 30 sec" and button "Watch the Free Readiness Framework".
- Why: every ad says "Free Readiness Framework" and the headline says "Free Framework". Process rule: "Button text says what they get" and "One name for the freebie everywhere." (The playbook form default is "Access", so this is a real test, not a fix.)

**T5. Proof line under the headline, from the ad's own words**
- Change: proof only below the form, as logos plus "TRUSTED BY 500+ FUTURE MISSIONARIES PREPARING FOR THE FIELD".
- To: one line right under the subheadline: "25+ years training missionaries. 500+ missionaries trained through GFM programs." Keep the logos below the form.
- Why: the May founder scripts and carousels open "After 25 years of training missionaries" and "training over 500 missionaries"; both are in the approved stat list. Process rule: "Proof near the form: results with real numbers". Left out on purpose: "72% of graduates currently serving on the field" and "3X higher retention" (in the strategy's options list but not used in any live ad, so not confirmed for public use). No testimonials are used because none are on file.

**Not a test for LPCR, but flagged:** a one-question pre-qualifier on the opt-in, using the approved Q4: "Are you in a season where you could realistically step into a 5-month, full-time, in-person program?" Playbook: "If CPL is $10-20, you SHOULD" (GFM is at $3.44), and the off-boarding plan already asks for it. It will lower LPCR on purpose. Judge it on qualified calls, not LPCR, and only after T1 to T4.

## How to run them

- **Traffic now:** 8 clicks in 7 days. At 150 visitors per version (300 per test) that is about 37 weeks per test. Nothing can be tested at $1.01/day.
- **Traffic at the Sep level (~$25/day):** about 320 clicks a week (313, 316, 322 in the three full weeks), so each test needs about 1 week.
- **At the planned $150/day:** about 1,900 clicks a week, so 2 to 3 days per test.
- **Bundle:** T1 + T3 + T4 are all "say what the ad says" and touch only copy. Ship them as one B version first (1 week at $25/day). Then T2 (layout) alone, then T5.
- **Before starting:** stop the FUTURE vs ASPIRING split (Fix 9) so only one variable runs. Fix UTMs (Fix 3) so GHL can count leads per version and per ad.
- **Clarity labels** (Clarity is already on the page): T1-A / T1-B (bundle: subheadline + guarantee + form header/button), T2-A / T2-B (mobile form first), T3-A / T3-B (proof line).
- Log every change in the reporting sheet notes, and restart the sheet from Sep.

## Questions for Ema

1. Was the ad set cut to $1.01/day on 5 Oct on purpose (between cohorts, or client asked)? When is the next MTS start date?
2. Should "June 1 deadline." be replaced with the next cohort date, or cut?
3. Who logs GFM's daily numbers now? Is there a newer sheet than the one that stops in May?
4. The 19 May coaching notes say booked-call leads had "No money" or were "Just interested in something different, no the residency". Did Peter share the numbers? That decides whether the pre-qualifier goes ahead of the page tests.
5. Which call name is right: "Missions Pathway Call" (ads) or "Free Mission Clarity Call" (emails, calendar)?
6. Who started the `/opt-in` vs `/booknow-page` split, and does it have results in GHL?

---

## Appendix: Facts pulled

### LPCR
- **Sheet** "(GFM) - Business Reporting Daily 2026" (Dash tab, col E "Link Clicks", col H "Lead"; LPCR = H / E): Mar 42/370 = 11.4%, Apr 117/1,201 = 9.7%, **May 329/2,187 = 15.0% (best month)**. Jun to Oct: blank.
- **Meta** (campaign level, link clicks and Meta leads):
  - Last 7 days (7 to 13 Oct): 2 / 8 = **25%** ($7.95, 3 LPVs). Not meaningful.
  - Last 3 days (11 to 13 Oct): 0 / 3 = **0%** ($4.34).
  - Last 30 days (14 Sep to 13 Oct): 159 / 983 = **16.2%**, load rate 83%, CPL $3.44.
  - Weekly before the cut: 14 to 20 Sep 16.3%, 21 to 27 Sep 17.1%, 28 Sep to 4 Oct 15.2%.
  - By month: Mar 10.4% (43/415), Apr 10.2% (135/1,326), May 15.6% (370/2,372), Jun to Aug off, Sep 13.6% (151/1,111), Oct 1 to 13 14.7% (31/211).
- **When it dropped:** LPCR did not drop. Volume dropped on 5 Oct (budget to $1.01/day). LPCR has sat at 14 to 17% since May.
- Strategy doc KPI was "Landing Page Conversion: ≥ 3%"; the Pacow goal is 20%.

### Ad copy (live, quoted from Meta previews on 14 Oct)
- **Founder Video ad A2** (1:25 founder talking-head video, world map behind him): "Feel called to missions but unsure how to prepare or where to start? 🎥 Watch our Free Readiness Framework ✔️ What readiness actually requires ✔️ How long-term missionaries are formed ✔️ How to discern if this is your season to step forward. Then book a Missions Pathway Call. In 30 minutes you'll have your training track, your timeline to the field, and your next three steps - in writing. No pressure. Just clarity on your next step. 30-day clarity guarantee. June 1 deadline. 👇 Watch the Free Readiness Framework & book your Missions Pathway Call today." Twitter Color A1 uses the same text.
- **Genz Beta Ad 1 Future Missionaries** (10-sec video, backpacker, overlay "POV: you're called to long-term missions and you find a free resource that isn't secretly a $2k course / link below"): "Feel called to long-term missions? Get your personalised pathway to the field - free. ... That's why we created a Free Readiness Framework ... 📞 Step 2: Book your Missions Pathway Call - a 30-minute conversation where you'll walk away with your training track, deployment timeline, and next three steps ... We're so committed to clarity that if you join MTS and, within the first 30 days of full participation, you discern it's not your calling, your tuition is refundable. ... The next term starts soon and applications are open."
- **Genz Beta Ad 1 / High Prod Image A1**: "Still saying "someday" about missions? Let's turn that into a date. ... 🎥 Step 1: Watch the Free Readiness Framework 📞 Step 2: Book a Missions Pathway Call ... We offer a 30‑day clarity guarantee: if you fully participate and discern it's not your calling, your tuition is refundable."
  - High Prod image: "ATTENTION: ASPIRING MISSIONARIES / HOW TO GO FROM "CALLED" TO PREPARED FOR LONG-TERM MISSIONS IN 5 MONTHS / Understand what real missionary readiness requires / Avoid going overseas unprepared or burning out / Get a clear pathway to long-term missions / WATCH NOW FREE FRAMEWORK".
  - Genz Beta Ad 1 video overlay: "POV: you find a free missions resource that isn't secretly a 2k course / link below".
- **Twitter Color A1** image (Rory Bonte tweet): "How to Discern Your Path to Long-Term Missions: 1 - Watch our Free Missions Framework ... Watch the framework today 👇 (for those serious about long-term missions only)".
- Headline on all 6: "Missions Readiness: Free Framework + Clarity Call". CTA: Learn more.
- Landing URL on all 6: `rdy.gogfm.org/booknow` with the broken parameter string in Fix 3 (utm_content: founderugca2, genz1futuremissionaries, genz1, highprodimage, twittercolor).

### Page copy (rdy.gogfm.org/booknow, loaded 14 Oct with Playwright, desktop 1440x900 and phone 390x844)
- Split: 5 of 8 loads went to `/opt-in`, 3 to `/booknow-page`. Only the call-out differs.
- Call-out: "FOR FUTURE MISSIONARIES ONLY" (`/opt-in`) or "FOR ASPIRING MISSIONARIES ONLY" (`/booknow-page`).
- Headline: "Become Mission-Ready in Just 5 Months"
- Subheadline: "Discover how 500+ missionaries have gained clarity, preparation, and a pathway to the field."
- Video preview (founder, captions "sensing a real calling to long-term missions," / "but you don't know your next step,").
- Form header: "Framework video access in just 30 sec!"
- Fields: First Name *, Phone * (US flag, +1), Email *, consent checkbox (not required) "I consent to receive emails and SMS messages regarding my submission and related updates." Hidden: UTM Source (empty), UTM Medium, UTM Campaign, UTM Content. No prefilled test data. Cloudflare Turnstile.
- Button: "Access". Below: "Privacy Policy".
- Below the fold: "TRUSTED BY 500+ FUTURE MISSIONARIES PREPARING FOR THE FIELD" + logos (Global Fellowship, Africa Inland Mission, Pioneers, East West, OMF). Footer: "Copyrights 2026 | Global Frontier Missions™ | Privacy Policy".
- No guarantee, no testimonials, no mention of the call, no "Readiness Framework" name. Empty `<title>`. Meta pixel 1062481109247318, Clarity present.
- Mobile: first field at 911px, "Access" at 1,248px (screen is 844px). Desktop: "Access" at 902px (screen is 900px).
- Screenshots: `oct14/gfm-desktop.png`, `oct14/gfm-mobile.png` (full-page versions `-full.png`).

### Profile facts (no profile on file; from Drive docs)
- **Offer** (Marketing Strategy): "In just 5 months at Missionary Training School, you'll go from burdened for missions but unsure of your next steps to having a clear long-term missions pathway ... backed by a 30-Day Clarity Guarantee." 20+ hrs/week guided learning, 12-15 hrs/week cross-cultural ministry, weekly mentoring, Next-Step Deployment Plan. Tuition $5,500 (Booking Reminders doc), 5-month Atlanta residency.
- **Real guarantee:** "30-Day Clarity Guarantee: If by Day 30 you've actively participated and decide it's not the right fit, we refund your tuition."
- **Proof (approved stat options):** 500+ missionaries trained through GFM programs; 72% of graduates currently serving on the field; 25+ years mobilizing and training missionaries; 3X higher retention. Live ads use only 500+ and 25 years.
- **ICP:** US, "Young Christians (18-35)": aspiring long-term missionaries, students, young professionals, career changers, persistent calling to long-term cross-cultural missions, serious about the unreached, urgency but no clear pathway. Research deck: ads can't say "Christians" outright, so the landing page has to do the qualifying.
- **Qualified lead** (Booking questions survey): 18+; "I feel clearly called and want to prepare to go" or "seriously considering it"; can realistically step into a 5-month, full-time, in-person program now or soon (not 1+ years out).
- **Funnel:** /opt-in → /framework (VSL + survey) → /slots → /confirmed. Off-boarding plan: relaunch at $150/day, add a short-form pre-qualifier and move the pixel to the second page, update ads off "June 1st".

### Could NOT get
- **GFM client profile:** none in "00. Client Profiles (Claude)". Built from strategy docs instead.
- **Sheet/GHL leads for Sep and Oct:** the reporting sheet stops at May; the sheet linked in the strategy doc returns "not found". LPCR for Sep and Oct is Meta-only.
- **GHL funnel stats** (page views to opt-ins per split variant): not pulled.
- **Video audio** for Founder Video ad A2: thumbnail and copy only.
- **Other rotating primary texts** in the flexible creatives: previews show one text per ad.
