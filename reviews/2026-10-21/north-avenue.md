# LPCR deep dive: North Avenue Education (Scott Clyburn), Oct 21 2026

Read-only. Nothing was changed in Meta, GHL, Drive or the sheet. No form was submitted.

**North Avenue Education**: LPCR 7d 5.5% (6/109), 3d 1.9% (1/53), prior week 11.0% (11/100). Main reason: the page still doesn't continue the ad (ad: "stop juggling a different tutor for every subject" + "free breakdown"; page: "Stop Buying Tutoring Packages" or the unsourced "$600+ a Month", "FREE ONE-PAGER", no form in the first phone screen). New worry: the sheet logged 0 leads on Oct 19 and Oct 20 (36 clicks) right after the button text changed, while Meta counted 2. Check that leads are reaching GHL.

## LPCR (sheet "(NAE) - Business Reporting Daily 2026", tab "Oct", columns B Adspend, E Link Clicks, H Lead)

| Window | Spend | Clicks | Leads | LPCR | CPL |
|---|---|---|---|---|---|
| Last 7d (10/14 to 10/20) | $463.94 | 109 | 6 | **5.5%** | $77.32 |
| Last 3d (10/18 to 10/20) | $223.18 | 53 | 1 | **1.9%** | $223.18 |
| Prior week (10/7 to 10/13) | $470.78 | 100 | 11 | **11.0%** | $42.80 |
| Oct to date (10/1 to 10/20) | $1,288.12 | 310 | 24 | 7.7% | $53.67 |

- Did it move? Yes, down 5.5 points week over week, and down from 8.2% in the Oct 19 review. Clicks went up (109 vs 100), leads went down (6 vs 11). Small numbers, but two full days with 0 leads on 18 clicks each has not happened before in October.
- Daily 10/14 to 10/20 (clicks / leads): 20/1, 16/3, 12/0, 8/1, 17/1, 18/0, 18/0. Sheet is filled through Oct 20.
- Best month 2026: still October at 7.7% (Jun 2.4%, Jul 3.3%, Aug 0.2%, Sep 1.1%). Goal is 15% (KPI tab says "Landing Page Conversion Rate > 25%").
- Sheet vs Meta, same 7 days: sheet 6 leads, Meta 10 (P2 9, P4 1). Oct 19 to 20: sheet 0, Meta 2 (P4 1 on Oct 19 with no clicks, so likely a delayed or view attribution; P2 1 on Oct 20). Meta higher, so no Meta undercount, but the sheet may be missing leads. GHL decides.
- "LP AB test" tab: unchanged since Oct 19. Still no per-version results.

## Live ads (Meta, last 7 days, effective status ACTIVE)

| Ad | Spend | Link clicks | LPVs | Leads (Meta) | Share | Load rate | LPCR (Meta, unique clicks) |
|---|---|---|---|---|---|---|---|
| Founder Image P2 | $463.00 | 117 (108 unique) | 98 | 9 | 99.4% | 84% (91% of unique) | 8.3% |
| Founder Image P4 | $1.44 | 0 | 0 | 1 | 0.3% | n/a | n/a |
| Founder Image P3 | $1.44 | 0 | 0 | 0 | 0.3% | n/a | n/a |
| Testimonials Post, Carousel Post, NAE Scholars x2, New Sales Ad | $0 | 0 | 0 | 0 | 0% | n/a | n/a |

- No ads launched since Oct 19 (newest live ads created 9/25). P2 copy unchanged; P2 image byte-identical to Oct 19 (viewed).
- P2 headline: "Parents of high schoolers: stop juggling a different tutor for every subject".
- P2 hook: "You've got a high schooler with a math tutor, an SAT course, and an essay coach. And you're the one keeping all three straight."
- P2 image: "The membership every parent of a disorganized teen needs before the homework battles start again." / "Smart kid, still missing assignments? One membership covers subject tutoring, study skills, and executive-function coaching - one team teaching your teen how to run their own school life, so you can stop hovering." / "Tap to get the free breakdown of how it all works."
- P2 body CTA still: "📞 Book a Free Academic Game Plan Call." and "⬇️ Book your Free Academic Game Plan Call."

## Changed since Oct 19

- Button renamed: **partly done**. "Get Started >>" is now "Get Access >>" (on-page form and pop-up). Still does not name what they get.
- "$600+ a Month" version B stopped or sourced: **not done**. 7 of 10 loads of /start-here went to it today (T1-B).
- Freebie named "free breakdown" like the ad: **not done** ("FREE ONE-PAGER", "GET YOUR FREE ONE-PAGER").
- Reviews heading to parents: **not done** ("What Do Students Love About North Avenue Education?").
- Page title: **not done** ("North Avenue Education — Reviews Wall", em dash still in it).
- Guarantee on the page: **not done**.
- Form in first phone screen: **not done** (First Name still at about 853px on an 844px screen).
- "See more reviews": still does nothing in my test.
- Ad body still says "Book a Free Academic Game Plan Call": **not done**.
- Tests T1 to T5: **none started**.
- New since Oct 19 (good): UTM Source hidden field now fills from the URL on load ("meta"). The Turnstile challenge frame now loads on the page (blocked in my headless run, as expected).

## Health checks

- Load rate: 98 LPVs / 117 clicks = 84% (91% of unique). OK. One soft day: Oct 20 was 12 LPVs on 19 clicks (63%). Watch it.
- Pixel: 596511900828054 loads on both versions; PageView request seen on phone loads. Clarity loads with "T1-A" / "T1-B" tags.
- Phone field: US flag, "+1 (555) 000-0000". Correct.
- Form: First Name *, Phone *, Email *, consent checkbox (required), 4 hidden UTM fields. No dropdowns, no prefilled visible values, no pre-qualifier. "Get Access >>" is clickable (trial click, nothing sent). Pop-up form from "GET YOUR FREE ONE-PAGER" opens and works (no heading in the pop-up).
- Turnstile: the Cloudflare challenge frame now loads; my headless browser cannot reach Cloudflare (proxy refused). Not tested, per brief. Since the button text changed in the same window as two 0-lead days, a real phone test submission is the first thing to do.
- Speed (rough, headless): A loads in about 1.0s desktop / 1.5s phone, B about 1.5s / 1.3s. Fine.
- Phone first screen: logo, 3-line call-out, headline, subheadline, "FREE ONE-PAGER", "Get Instant Access" fill the screen. No form field visible.

## A. FIXES (do now, not tests)

1. Confirm leads are getting through. Sheet logged 0 leads on Oct 19 and Oct 20 (36 clicks), right after "Get Started >>" became "Get Access >>". Do one real submission from an iPhone in the Instagram in-app browser and check: Turnstile passes, the contact lands in GHL, the Lead event shows in Events Manager. Then compare GHL leads for 10/14 to 10/20 with the sheet (6) and Meta (10).
2. Stop the unsourced number. Change "Most Families Pay 3 Separate Tutors $600+ a Month. Get One Team for Every Subject Instead." To: end the /start-here split and send 100% to /opt-in, until Scott backs up "$600+". It is not in the profile, the ad or the strategy notes, and it now gets about 70% of loads. Playbook: "Your offer needs to match your service. Don't promise what you can't deliver."
3. Button says what they get. Change "Get Access >>" To "Send Me the Free Breakdown" (on-page form and pop-up form). Process: "Button text says what they get (not "Get Started" / "Submit")."
4. One name for the freebie, the ad image's name. Change "FREE ONE-PAGER" To "FREE BREAKDOWN". Change "Enter your information below and we'll send you a one-pager on how the North Avenue Education membership works." To "Enter your information below and we'll send you the free breakdown of how the North Avenue Education membership works." Change "GET YOUR FREE ONE-PAGER" To "GET THE FREE BREAKDOWN". Ad image: "Tap to get the free breakdown of how it all works."
5. Parents are the buyer. Change "💬 STUDENT REVIEWS" / "What Do Students Love About North Avenue Education?" To "💬 PARENT REVIEWS" / "What Do Parents Say About North Avenue Education?" Profile: "Parents - the students are below 18 years old". 5 of 6 reviews shown are parents.
6. Page title. Change "North Avenue Education — Reviews Wall" To "Free Breakdown | North Avenue Education".
7. Fix or remove "See more reviews" (does nothing in my test; check by hand).
8. Ad side (Ema's call): body asks twice to "Book a Free Academic Game Plan Call" while the page gives a one-pager. The "LP AB test" tab already says the one-pager won ("WINNER: Free One-Pager / Get Instant Access").

## B. A/B TESTS (biggest lift first)

**T1. Headline uses the ad's pain**
Change "Stop Buying Tutoring Packages. Get One Membership for All Subjects." To "Stop Juggling a Different Tutor for Every Subject. Get One Team for All of Them."
Why: ad headline is "Parents of high schoolers: stop juggling a different tutor for every subject". Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Replaces "$600+" as version B.

**T2. Form in the first phone screen, one-line call-out from the ad**
Change "FOR PARENTS OF MIDDLE & HIGH SCHOOL STUDENTS" (3 lines on a phone) To "FOR PARENTS OF HIGH SCHOOLERS" (one line), smaller logo, and move the subheadline below the form so First Name and Phone show in the first screen.
Why: ad says "Parents of high schoolers" and "You've got a high schooler". Playbook: "Call-out line on the first 3 pages, kept to one line." Process: "Mobile: is the form visible without scrolling?"

**T3. Subheadline uses the ad image's hook**
Change "3 sessions a month, used for whatever your student needs right now: math help this week, SAT prep next month, essays in the fall. Each session is with the right tutor on our team." To "Smart kid, still missing assignments? One membership covers subject tutoring, study skills, and executive-function coaching, with one team and one person you talk to."
Why: word for word from the ad image and body ("One person you talk to"). Profile's qualified lead includes "neurodivergent or diagnosed with learning differences".

**T4. The ad's proof and the real guarantee at the button, parent review next to the form**
Change: stats bar "3,000+ STUDENTS TUTORED / 4.9/5 FROM 95+ FAMILIES / Top 2% TUTOR TEST SCORES / One Team EVERY SUBJECT" below the form and no guarantee. To: above the button "Since 2013: 3,000+ students, 4.9/5 stars across 95+ verified reviews." Under the button "If your first tutor match isn't an expert, tell us. We'll rematch you and give you that session free." Then Tuan Anh Nguyen's review ("Our daughter was diagnosed with ADHD and struggled with executive functioning skills.") right under the form.
Why: proof copied from the ad; guarantee from the profile ("If your first tutor match isn't an expert, let us know and we'll repair and give you the session for free"). Left out the ad's "within 3 sessions" (not in the profile). Process: "parent reviews first when parents are the buyer."

**T5. Show the freebie**
Change: only the "FREE ONE-PAGER" pill, no picture. To: a small image of the breakdown above the form with "What's inside: how the 3 monthly sessions work across subjects, who your student works with, and what happens if the tutor match isn't right."
Why: playbook squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block." The preview is the one missing element.

Run plan: about 109 clicks a week (sheet), so 150 visits per version takes about 19 days per test. Do Fixes 1 to 6 first. Round 1 (about 3 weeks): bundle T1 + T2 + T3 (first screen) into one version B, Clarity labels T2-A / T2-B. Round 2 (about 3 weeks): T4 + T5 (form area) on the winner, labels T3-A / T3-B. Call it at 150+ visits per version with a 3+ point lead, per the sheet. No pre-qualifier: CPL is $77 (7d); playbook: "If CPL is already $45-50, don't" and "not for competitive ones like college consulting, SAT/ACT".

## NEED FROM EMA

- One real test submission on an iPhone from the Instagram in-app browser: does Turnstile pass, does the contact reach GHL, does Lead fire in Events Manager, are the 4 UTM fields filled. I did not submit (read-only; Turnstile blocked headless).
- GHL lead count per day for 10/14 to 10/20 (sheet 6, Meta 10; sheet 0 on 10/19 and 10/20).
- When "Get Started >>" was changed to "Get Access >>", and what else changed in that edit (form settings, Turnstile, workflow).
- Scott's source for "$600+ a Month", or OK to end version B.
- Per-version leads for T1-A / T1-B (GHL by page, or Clarity). The sheet only has totals.
- The one-pager file (PDF or image) for T5.
- Scott to confirm whether "within 3 sessions" is part of the guarantee.
- Will the ad body switch from "Book a Free Academic Game Plan Call" to the free breakdown?

---

## Appendix: facts pulled

- Sheet downloaded as .xlsx today: /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/north-avenue/sheet/nae.xlsx (tabs "Oct", Jun to Sep, "LP AB test"). Only the Dash totals changed in other tabs since Oct 19.
- Meta daily P2 10/14 to 10/20 (clicks / LPVs / leads): 22/18/2, 20/17/4, 13/11/0, 8/9/1, 17/14/1, 18/17/0, 19/12/1. Oct 21 so far 4/2/0.
- Ad copy: P2 creative 1096851773201403 (P4 982068638244330 same text, different image). link_url empty from the API; landing used go.northaveeducation.com/start-here, which splits to /opt-in (T1-A) and /opt-in-523814 (T1-B), 3 and 7 of 10 loads today.
- Page text identical to Oct 19 except the button ("Get Access >>"). Full text: /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/north-avenue/out/A.txt and B.txt.
- Screenshots in /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/north-avenue/: north-avenue-A-desktop.png, north-avenue-A-mobile.png, north-avenue-B-desktop.png, north-avenue-B-mobile.png (+ -full), cta-390.png / cta-1440.png (pop-up form), formarea-A-mobile.png. Ad image: img/p2.jpg.
- Profile facts (from Oct 19 read of 1Sd4YaTkLxZLgmSLXmn6U0kE7iWiJo_DFRUth2QgSF_o): guarantee "Tutor expertise: if you're not confident your tutor knows the material, we'll repair you and give you a free session to make up for it."; buyer "Parents - the students are below 18 years old"; qualified lead "Based in US, local to PNW, can afford $2500+ program, applying to out of state colleges, neurodivergent or diagnosed with learning differences". No proof numbers in the profile.
- Could NOT get: form submission / Turnstile / Lead event on submit; GHL lead counts; per-version split results; when the button changed; link_url from the creative API. Meta returned no next_actions.
