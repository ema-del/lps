# LPCR deep dive: North Avenue Education (Scott Clyburn), Oct 19 2026

Read-only. Nothing was changed in Meta, GHL, Drive or the sheet. No form was submitted.

**North Avenue Education**: LPCR 7d 8.2% (8/97), 3d 5.4% (2/37), prior week 11.0% (11/100). Main reason: the page still doesn't continue the ad. The ad sells "stop juggling a different tutor for every subject" and a "free breakdown". The page says "Stop Buying Tutoring Packages" (or the unsourced "$600+ a Month"), offers a "FREE ONE-PAGER", the button says "Get Started >>", and on a phone no form field shows in the first screen. Nothing on the page copy changed since Oct 14.

## LPCR (sheet "(NAE) - Business Reporting Daily 2026", tab "Oct", columns B Adspend, E Link Clicks, H Lead)

| Window | Spend | Clicks | Leads | LPCR | CPL |
|---|---|---|---|---|---|
| Last 7d (10/12 to 10/18) | $457.88 | 97 | 8 | **8.2%** | $57.23 |
| Last 3d (10/16 to 10/18) | $194.25 | 37 | 2 | **5.4%** | $97.13 |
| Prior week (10/7 to 10/13) | $470.78 | 100 | 11 | **11.0%** | $42.80 |
| Oct to date (10/1 to 10/18) | $1,141.23 | 274 | 24 | 8.8% | $47.55 |

- Did it move? Down 2.8 points week over week, but that is 3 leads on about 100 clicks, so it is mostly noise. The real story is that it has sat around 9% all month, far under the 15% goal (KPI tab: "Landing Page Conversion Rate > 25%").
- Headline split (started 10/9): 12 / 135 = 8.9% since it started vs 12 / 139 = 8.6% for 10/1 to 10/8. The split has not moved LPCR either way. About 67 visits per version so far, under half the 150 needed. No per-version numbers in the sheet.
- Best month 2026: October 8.8% (Jun 2.4%, Jul 3.3%, Aug 0.2%, Sep 1.1%). Sheet filled through Oct 18.

## Live ads (Meta, last 7 days, effective status ACTIVE)

| Ad | Spend | Link clicks | LPVs | Leads (Meta) | Share | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| Founder Image P2 | $458.49 | 108 (95 unique) | 95 | 12 | 99.7% | 88% | 11.1% |
| Founder Image P3 | $0.95 | 0 | 0 | 0 | 0.2% | n/a | n/a |
| Founder Image P4 | $0.22 | 0 | 0 | 0 | 0.05% | n/a | n/a |
| Testimonials Post, Carousel Post, NAE Scholars x2, New Sales Ad | $0 | 0 | 0 | 0 | 0% | n/a | n/a |

- No ads launched since Oct 14 (newest live ads were created 9/25). P2 copy and image are unchanged (image file is byte-identical to Oct 14).
- P2 headline: "Parents of high schoolers: stop juggling a different tutor for every subject".
- P2 hook (body line 1): "You've got a high schooler with a math tutor, an SAT course, and an essay coach. And you're the one keeping all three straight."
- P2 image (viewed): "The membership every parent of a disorganized teen needs before the homework battles start again." / "Smart kid, still missing assignments? One membership covers subject tutoring, study skills, and executive-function coaching - one team teaching your teen how to run their own school life, so you can stop hovering." / "Tap to get the free breakdown of how it all works."
- P2 body CTA: "📞 Book a Free Academic Game Plan Call." and "⬇️ Book your Free Academic Game Plan Call."

## Changed since Oct 14

- Ad text still says "Book a Free Academic Game Plan Call" while the page gives a one-pager: **not done**.
- "$600+ a Month" version B stopped or sourced: **not done** (5 of 10 loads of /start-here today went to it).
- Button "Get Started >>" renamed: **not done**.
- Guarantee on the page / "within 3 sessions" confirmed: **not done** (still no guarantee on the page).
- Reviews heading "What Do Students Love About North Avenue Education?" changed to parents: **not done**.
- Page title "North Avenue Education" + "Reviews Wall": **not done**.
- Sitelinks: today's Facebook feed preview shows none, still can't confirm in Ads Manager.
- Tests T1 to T5 from Oct 14: **none started**.
- One thing did change: the opt-in form is now built into the page. On Oct 14 it was an iframe (links.pacowmedia.com form tFFkNwQyK12wZsAkwOaF). Same fields and wording. Need to know when this changed and whether a test lead went through after.

## Health checks

- Load rate: 95 LPVs / 108 clicks = 88% (100% of unique clickers). Fine.
- Leads Meta vs sheet: Meta 12, sheet 8 for the same 7 days. Meta is higher, so there is no undercount to flag, but 4 leads are missing from the sheet. Check GHL for 10/12 to 10/18.
- Pixel: 596511900828054 loads on both versions (fbevents.js and config). PageView request seen on phone loads. Lead on submit not tested (no submission). Clarity loads, variant tags "T1-A" and "T1-B" are on the pages.
- Phone field: US flag, "+1 (555) 000-0000". Correct for the US target.
- Form: First Name *, Phone *, Email *, consent checkbox (required), 4 hidden UTM fields (UTM Source, Medium, Campaign, Content; empty on page load even with utm_source in the URL, should fill on submit, unconfirmed). No dropdowns, no prefilled values, no pre-qualifier. "Get Started >>" is clickable (trial click, nothing sent).
- Turnstile: Cloudflare Turnstile keys are still in the page code. No visible widget, so it probably runs invisibly on submit. Not tested, per brief.
- Buttons: bottom "GET YOUR FREE ONE-PAGER" opens a pop-up with the same form (works, US flag, no heading in the pop-up, button "Get Started >>"). "See more reviews" did nothing in my headless test (no new reviews, no new tab). Check it by hand.
- Speed (rough, headless): version A loads in about 1.3s, version B in 2.2 to 3.2s. Fine.
- Phone first screen (390x844): logo, 3-line call-out, headline, subheadline, "FREE ONE-PAGER", "Get Instant Access" and the intro line fill the screen. The "First Name *" label starts at about 853px, so no form field is visible without scrolling. Same on both versions.
- Desktop (1440x900): First Name and Phone fields visible at the bottom, Email partly, button at about 1061px (below the fold).

## A. FIXES (do now, not tests)

1. Stop the unsourced number. Change "Most Families Pay 3 Separate Tutors $600+ a Month. Get One Team for Every Subject Instead." To: end the /start-here split and send 100% to /opt-in, until Scott backs up "$600+". It is not in the profile, the ad or the strategy notes. Playbook: "Your offer needs to match your service. Don't promise what you can't deliver."
2. Button says what they get. Change "Get Started >>" To "Send Me the Free Breakdown" (on-page form and pop-up form). Process: "Button text says what they get (not "Get Started" / "Submit")."
3. One name for the freebie, the ad image's name. Change "FREE ONE-PAGER" To "FREE BREAKDOWN". Change "Enter your information below and we'll send you a one-pager on how the North Avenue Education membership works." To "Enter your information below and we'll send you the free breakdown of how the North Avenue Education membership works." Change "GET YOUR FREE ONE-PAGER" To "GET THE FREE BREAKDOWN". The ad image says "Tap to get the free breakdown of how it all works." Today the freebie has three names.
4. Parents are the buyer. Change "💬 STUDENT REVIEWS" / "What Do Students Love About North Avenue Education?" To "💬 PARENT REVIEWS" / "What Do Parents Say About North Avenue Education?" Profile: "Parents - the students are below 18 years old". 5 of 6 reviews shown are parents.
5. Page title. Change "North Avenue Education" + "Reviews Wall" (with an em dash between) To "Free Breakdown | North Avenue Education". Shows in the Instagram browser bar, and the playbook says remove em dashes.
6. Ad vs page offer (Ema's call, ad side): the body asks twice to "Book a Free Academic Game Plan Call", the page gives a one-pager, and the sheet's "LP AB test" tab says the one-pager won ("WINNER: Free One-Pager / Get Instant Access"). Until the ad text says "free breakdown", part of the click-through expects a call booking.
7. Check "See more reviews" by hand. It did nothing in my test.

## B. A/B TESTS (biggest lift first)

**T1. Headline uses the ad's pain**
Change "Stop Buying Tutoring Packages. Get One Membership for All Subjects." To "Stop Juggling a Different Tutor for Every Subject. Get One Team for All of Them."
Why: ad headline is "Parents of high schoolers: stop juggling a different tutor for every subject". Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Replaces the "$600+" version B as the challenger.

**T2. Form in the first phone screen, one-line call-out from the ad**
Change "FOR PARENTS OF MIDDLE & HIGH SCHOOL STUDENTS" (3 lines on a phone, first field at about 853px on an 844px screen) To "FOR PARENTS OF HIGH SCHOOLERS" (one line), smaller logo, and move the subheadline below the form so First Name and Phone show in the first screen.
Why: ad says "Parents of high schoolers" and "You've got a high schooler". Playbook: "Call-out line on the first 3 pages, kept to one line." Process: "Mobile: is the form visible without scrolling?"

**T3. Subheadline uses the ad image's hook**
Change "3 sessions a month, used for whatever your student needs right now: math help this week, SAT prep next month, essays in the fall. Each session is with the right tutor on our team." To "Smart kid, still missing assignments? One membership covers subject tutoring, study skills, and executive-function coaching, with one team and one person you talk to."
Why: word for word from the ad image ("Smart kid, still missing assignments? One membership covers subject tutoring, study skills, and executive-function coaching") and body ("One person you talk to"). Playbook: creative is the most important part of the ad, so the page should echo it. Profile's qualified lead includes "neurodivergent or diagnosed with learning differences".

**T4. The ad's proof and the real guarantee at the button, parent review next to the form**
Change: stats bar "3,000+ STUDENTS TUTORED / 4.9/5 FROM 95+ FAMILIES / Top 2% TUTOR TEST SCORES / One Team EVERY SUBJECT" below the form and no guarantee anywhere. To: above the button "Since 2013: 3,000+ students, 4.9/5 stars across 95+ verified reviews." Under the button "If your first tutor match isn't an expert, tell us. We'll rematch you and give you that session free." Then Tuan Anh Nguyen's review ("Our daughter was diagnosed with ADHD and struggled with executive functioning skills.") right under the form, Lola Hodge (student) moved down.
Why: proof line is copied from the ad. Guarantee uses the profile's terms ("If your first tutor match isn't an expert, let us know and we'll repair and give you the session for free"). I left out the ad's "within 3 sessions" because the profile doesn't have it. Process: "parent reviews first when parents are the buyer."

**T5. Show the freebie**
Change: no picture of the one-pager, only the "FREE ONE-PAGER" pill. To: a small image of the breakdown above the form with "What's inside: how the 3 monthly sessions work across subjects, who your student works with, and what happens if the tutor match isn't right."
Why: playbook squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block." The preview is the one element missing. The 3 lines only repeat what the page and ad already say.

Run plan: about 97 clicks a week (sheet), so 150 visits per version takes about 3 weeks per test. Do Fixes 1 to 5 first on the page. Round 1 (about 3 weeks): bundle T1 + T2 + T3 (first screen) into one version B, Clarity labels T2-A / T2-B. Round 2 (about 3 weeks): T4 + T5 (form area) on the Round 1 winner, labels T3-A / T3-B. Call it at 150+ visits per version with a lead of 3+ points, per the sheet. No pre-qualifier: CPL is $57 (7d), and the playbook says "If CPL is already $45-50, don't" and "not for competitive ones like college consulting, SAT/ACT".

## NEED FROM EMA

- Source for "$600+ a Month" from Scott, or OK to end version B.
- Per-version leads for T1-A / T1-B from GHL (utm or page) or Clarity. The sheet only has totals.
- One real test submission on an iPhone from the Instagram in-app browser: does Turnstile pass, does the Lead event fire in Events Manager, are the 4 UTM fields filled on the GHL contact. I did not submit (read-only, Turnstile).
- When the form was switched from the iframe embed to the on-page form (it changed between Oct 14 and today), and whether anything else changed at the same time.
- GHL lead count for 10/12 to 10/18. Meta says 12, the sheet says 8.
- The one-pager file (PDF or image) for T5.
- Scott to confirm whether "within 3 sessions" is part of the guarantee.
- Will the ad body switch from "Book a Free Academic Game Plan Call" to the free breakdown?
- Sitelinks on the Founder Image ads (the old "SAT 3/30 Class"): check in Ads Manager.

---

## Appendix: facts pulled

### Sheet
- Downloaded as .xlsx today: /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/north-avenue/sheet/nae.xlsx. Tabs used: "Oct" (and Jun to Sep for monthly), "LP AB test".
- Daily 10/12 to 10/18 (spend / clicks / leads): 10/12 $78.07 / 9 / 1; 10/13 $62.76 / 15 / 1; 10/14 $73.21 / 20 / 1; 10/15 $49.59 / 16 / 3; 10/16 $65.13 / 12 / 0; 10/17 $52.83 / 8 / 1; 10/18 $76.29 / 17 / 1.
- Sheet clicks (97) match Meta unique link clicks (95), so the sheet logs unique link clicks.
- "LP AB test" tab unchanged: call-out B "FOR PARENTS OF HIGH SCHOOLERS (GRADES 9-12)", headline B "$600+", third idea "Give Your Teen One Team That Gets Them Ready for College, Not Just Through This Week's Homework." (left out: the live ad doesn't mention college), Clarity scripts T1-A / T1-B, start 2026-10-09, rule "at about 150+ visits per version, if one version is ahead by 3+ percentage points".
- No new cell comments since the 10/9 "A/B test".

### Ad copy (P2 creative 1096851773201403; P3 2310294716491971 and P4 982068638244330 use the same text)
- Title: "Parents of high schoolers: stop juggling a different tutor for every subject"
- Body: "You've got a high schooler with a math tutor, an SAT course, and an essay coach. And you're the one keeping all three straight. / Three schedules. Three separate bills. Three people to chase for updates. The whole operation runs through you, on top of everything else you're already doing. / North Avenue's membership puts it under one roof. SAT/ACT prep, subject tutoring, college essays, study skills, executive-function coaching. One team runs it. One person you talk to. Your student gets help across every subject and you get your evenings back. / Since 2013: 3,000+ students, 4.9/5 stars across 95+ verified reviews, every tutor at the 98th percentile with 3+ years experience. / 📞 Book a Free Academic Game Plan Call. We'll look at where your student's at and show you how the membership works for them. / If the tutor match isn't right within 3 sessions, we rematch and give you a free session. / ⬇️ Book your Free Academic Game Plan Call."
- CTA LEARN_MORE. link_url empty from the API again; used go.northaveeducation.com/start-here, which splits to /opt-in (T1-A) and /opt-in-523814 (T1-B), 5 and 5 in 10 loads today.
- Image: /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/north-avenue/img/p2.jpg (1080x1350, same as Oct 14).

### Page copy (captured today)
- Call-out: "FOR PARENTS OF MIDDLE & HIGH SCHOOL STUDENTS"
- Headline A: "Stop Buying Tutoring Packages. Get One Membership for All Subjects." Headline B: "Most Families Pay 3 Separate Tutors $600+ a Month. Get One Team for Every Subject Instead."
- Subheadline: "3 sessions a month, used for whatever your student needs right now: math help this week, SAT prep next month, essays in the fall. Each session is with the right tutor on our team."
- Form block: "FREE ONE-PAGER" / "Get Instant Access" / "Enter your information below and we'll send you a one-pager on how the North Avenue Education membership works." / fields / "I consent to receive emails and SMS messages regarding my submission and related updates." / "Privacy Policy | Terms of Service" / "Get Started >>".
- Below: stats bar, "💬 STUDENT REVIEWS / What Do Students Love About North Avenue Education? / Our Wall of Love / Verified Google Reviews 4.9 · 96 reviews", reviews (Catalina Solberg, Lola Hodge, Tuan Anh Nguyen, Kim Hasle, Sally Wilson, R Hyde), "See more reviews", "See what's possible for your student" / "GET YOUR FREE ONE-PAGER", footer "Copyright 2026 | North Avenue Education™ | Privacy Policy".
- No guarantee, no freebie image, no menu (good). Text identical to Oct 14 apart from the form now being on the page.
- Screenshots in /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/north-avenue/: north-avenue-A-desktop.png, north-avenue-A-mobile.png, north-avenue-B-desktop.png, north-avenue-B-mobile.png (+ -full versions), cta-390.png (pop-up form).

### Profile (fileId 1Sd4YaTkLxZLgmSLXmn6U0kE7iWiJo_DFRUth2QgSF_o)
- Offer: "We help ambitious, diverse-thinking students prepare for and excel in college and beyond. If your first tutor match isn't an expert, let us know and we'll repair and give you the session for free."
- Guarantee: "Tutor expertise: if you're not confident your tutor knows the material, we'll repair you and give you a free session to make up for it." No "3 sessions" limit.
- Proof: no numbers in the profile. Numbers used come from the live ad.
- Buyer: "Parents - the students are below 18 years old". Portland OR metro plus PNW.
- Qualified lead: "Based in US, local to PNW, can afford $2500+ program, applying to out of state colleges, neurodivergent or diagnosed with learning differences".

### Could NOT get
- Form submission test, Turnstile result, Lead event on submit, UTM fill (read-only, no submit).
- Per-version results of the headline split (not in the sheet; no GHL or Clarity access used).
- link_url from the creative API (empty). Sitelinks status in Ads Manager.
- When the form embed changed.
- Meta returned no next_actions, so no follow-up calls.
