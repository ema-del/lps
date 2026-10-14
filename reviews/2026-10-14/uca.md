# LPCR page review: UCA (Ultimate College Admissions, $67/mo membership, B2C)

**Verdict:** LPCR is 7.9% for the last 7 days (12 leads / 152 clicks) because the page still does not say what the ad says. The top ad (P1) sells "25 Years of Admissions Expertise For a Fraction of The Price" and "Junior year is where most of it gets decided". Version A of the page leads with a vague "Find out how..." headline, and version B leads with the price angle from P2 and P5, the two ads that get under 10% of spend and 0 leads. None of the Oct 12 "Fix first" items were made.

What changed since the Oct 12 review:
- A headline split test is now live. /opt-in sends visitors (302 redirect) half to /more-information (A, old headline) and half to /opt-in-885953 (B, "The Affordable Alternative to $5,000-$50,000 Private College Counseling"). 4 of 8 test loads went to each. Clarity variant tags T1-A and T1-B are on the pages.
- The sheet now has an "LP AB tests" tab with this T1 and a planned freebie-name test (not live yet: both pages still say "See What's Inside >>").
- Not fixed: the UCLA stat, the dead bottom button, the "1,000+" families number, the empty browser tab title.

## LPCR numbers (sheet, tab "Oct", columns E "Link Clicks" and H "Lead")

| Window | Leads | Link clicks | LPCR |
|---|---|---|---|
| Last 7 days (Oct 7 to 13; data only Oct 9 to 13) | 12 | 152 | **7.9%** |
| Last 3 days (Oct 11 to 13) | 9 | 70 | **12.9%** |
| Best month 2026 (October, the only month with data) | 12 | 152 | **7.9%** |

- Daily: Oct 9 0/48 (0%), Oct 10 3/34 (8.8%), Oct 11 5/31 (16.1%), Oct 12 3/18 (16.7%), **Oct 13 1/21 (4.8%)**.
- When it dropped: Oct 13, from about 16% to 4.8%. One day and 21 clicks, so not proof. Worth checking whether the split test went live on Oct 12 or 13 (the sheet has no comment saying when).
- Goal is 20%, under 15% is bad. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."

## Live ads (account 1150974895696033, campaign "OPurchase - UCA - Membership - 30+", last 7 days, ACTIVE only)

No new ads. Still the same 5 carousels, all launched Oct 9, all linking to https://go.ultimatecollegeadmissions.com/opt-in.

| Ad | Card headline | Spend | Share | Link clicks | LPVs | Load rate | Meta leads | LPCR (Meta) |
|---|---|---|---|---|---|---|---|---|
| P1 - Carousel | "Parents of 11th Graders: 25 Years of Admissions Expertise For a Fraction of The Price" | $175.56 | 40.8% | 50 | 40 | 80% | 10 | 20.0% |
| P3 - Carousel | "Parents of 8th-11th Graders: Join the Admissions Insiders' Membership" | $170.82 | 39.7% | 57 | 47 | 82% | 5 | 8.8% |
| P4 - Carousel | "Parents of College-Bound Students: Stop Guessing at Admissions" | $41.72 | 9.7% | 26 | 20 | 77% | 3 | 11.5% |
| P2 - Carousel | "Private College Counseling Runs $5,000-$50,000. This Is A Fraction of The Price" | $21.82 | 5.1% | 7 | 5 | 71% | 0 | 0% |
| P5 - Carousel | "The Affordable Alternative to Pricey College Counseling" | $20.33 | 4.7% | 20 | 16 | 80% | 0 | 0% |
| **Total** | | **$430.25** | 100% | **160** (152 unique) | **128** | **80%** | **18** | **11.3%** |

- P1 is top spender over 7 days, by $4.74. In the last 3 days P3 took over ($153.08 vs $106.63). P1 still converts best on Meta's count (20% vs 8.8%).
- Load rate last 3 days fell to 76% (56 LPVs / 74 clicks). **P1 dropped to 61% (14 / 23).** Small numbers, but this lines up with the new split-test redirect.
- Meta trend tool: CTR falling on P1, P2, P5, rising on P3, P4; CPM up on most ads. Benchmark: campaign CTR "in line with your industry peer group. Peer median: 3.57." Sheet CTR fell from 2.8% (Oct 9) to 1.7% (Oct 13), CPC rose from $0.98 to $4.33.

## Fix first (broken things, not tests)

1. **Wrong UCLA stat, still live on both versions.** Page: "25+ YEARS ON THE UCLA COMMITTEE". Offer doc and live ad: "25+ years as leaders and experts in college admissions, including 15+ years on the UCLA Scholarship Admissions Committee." Change to "15+ YEARS ON THE UCLA SCHOLARSHIP COMMITTEE". (Also the ICP doc's sample line "We spent 25 years on the admissions committee" repeats the same error. Don't copy it onto the page.)
2. **Bottom button still does nothing, on both versions.** "Get My Free One-Pager >>" (id button-OTxjiNokxF_btn) did not move the page in mobile tests on A and B (scroll position stayed at 3,521 and 3,472). Point it at the form.
3. **Families number still differs.** Ad: "Thousands of families guided." Page: "1,000+ OF FAMILIES GUIDED". Use one true number in both.
4. **The live headline test matches the smallest ads.** B ("The Affordable Alternative to $5,000-$50,000 Private College Counseling") mirrors P2 and P5, which together got $42.15 (9.8% of spend) and 0 leads. About 80% of traffic comes from P1 and P3, whose headlines talk about 25 years of expertise and the membership. At ~150 clicks a week split two ways, reaching the sheet's own bar ("about 20 opt-ins" per variant) will take 4+ weeks at current LPCR. Check the GHL split stats. If it has under 7 days of data, restart T1 with the P1 headline below.
5. **Load rate dropped after the redirect.** /opt-in now returns a 302 to the variant page. Last 3 days load rate is 76% (P1 61%). Check in Meta after a few more days. If it stays under 80%, ask GHL whether the split can run without the extra redirect, or link ads straight to the variant URLs with the split set up another way.
6. **Meta counts more leads than the sheet again.** Meta: 18 leads. Sheet: 12 leads on the same spend ($430.25 vs $429.90). Check with Pixel Helper that Lead fires once, only on form submit. In one desktop load of B, the pixel init and PageView appeared twice in the page. Judge LPCR on the sheet.
7. **Clarity tags load late.** T1-A and T1-B showed up in mobile loads, but not in desktop loads that I left idle for 8 seconds (the trackers seem to load after user interaction). In Clarity, confirm both variants are showing sessions before trusting it.
8. **Empty browser tab title** on both versions (`<title>` is blank). Minor.
9. **Form sometimes slow to show.** In 1 of 4 desktop test loads, the form box showed no fields after 5 seconds. Watch for this in Clarity recordings.

## Ad-to-page match (P1 first, it has the most spend)

| Check | Ad | Page (A / B) | Match? |
|---|---|---|---|
| Call-out | Primary text (all 5 ads): "ATTENTION: Parents of 11th Graders Aiming at Competitive Colleges". P1 card: "Parents of 11th Graders". P1 slide 1: "Parents of 8th-11th graders:" | "FOR PARENTS OF 8TH–11TH GRADERS" | Partly. Matches the slides, loses "Aiming at Competitive Colleges" |
| Pain / hook | "Junior year is where most of it gets decided. And most families are guessing their way through it." P1 slide 1: "if you have no idea whether your child is taking the right classes, or whether you're already behind, read this." | No pain line on the first screen of A or B | No |
| Promise | P1 card: "25 Years of Admissions Expertise For a Fraction of The Price". Text: "Join today." Last slide: "Everything we know, organized by grade" / "Click below to learn more." | A: "Find out how one membership puts 25 years of admissions-committee experience in your family's corner." B: "The Affordable Alternative to $5,000-$50,000 Private College Counseling" | A has the 25 years, not the price. B has the price, not the 25 years. Neither has both |
| Freebie name | Ad never names a freebie | "See what's inside the membership", "full breakdown", "See What's Inside >>", "Get My Free One-Pager >>" | Three names for one thing |
| Proof | "25 years inside admissions. Thousands of families guided. $10M+ in scholarships earned by their students." | "25+ YEARS ON THE UCLA COMMITTEE", "$10M+ IN SCHOLARSHIPS & AWARDS", "1,000+ OF FAMILIES GUIDED" | Partly. UCLA stat wrong, families number differs |
| Guarantee | "Cancel anytime." | Nothing | No |

## Page vs playbook

- **Headline is not the offer.** Rule: "Headline = the offer ("Get X in X time, or guarantee") and it must be the same on every page." The free thing (the one-pager) is never named in either headline.
- **Freebie name.** Rule: parents get "a free roadmap / one-pager". The page calls it three things.
- **Form:** First Name *, Last Name *, Phone * (US +1 default, correct for a US ICP), Email *, consent checkbox, button "See What's Inside >>". Rule: "Opt-in form: first name + phone (two columns), email full width, consent checkboxes, button "Access"". Last Name is extra.
- **No pre-qualifier, no money question.** Correct. Rule: pre-qualifier "not for competitive ones like college consulting, SAT/ACT". "B2C: never mention money".
- **UTMs pass through the redirect.** Hidden fields filled "meta" and "P1" in the test. Good.
- **Squeeze page elements:** no preview image of the one-pager, no reviews block near the form. Rule: "Squeeze page elements: logo, call-out, headline, subheadline, VSL preview GIF..., short form, Google/Trustpilot reviews block". The "Wall of Love" (6 parent quotes) sits far below the form.
- **Mobile (390x844): no form field on the first screen on either version.** A: form starts at 842px. B: form starts at 794px, first field at about 849px. The screen shows only the call-out, headline, subheadline and the form title box.

## 5 A/B tests (biggest expected lift first)

**T1. Headline: match P1 (top spend)**
- Change (A, now): "Find out how one membership puts 25 years of admissions-committee experience in your family's corner." (B now live: "The Affordable Alternative to $5,000-$50,000 Private College Counseling")
- To: "25 Years of Admissions Expertise For a Fraction of The Price"
- Why: P1 is 40.8% of spend and the only ad near 20% LPCR. Its card headline already works on the people who click. Playbook: "headline/offer must match the ad".
- One headline per live ad, matched to its card (if Ema wants to map pages to ads later):
  - **P1 (recommended, top spend): "25 Years of Admissions Expertise For a Fraction of The Price"**
  - P3: "Join the Admissions Insiders' Membership"
  - P4: "Stop Guessing at Admissions"
  - P5: "The Affordable Alternative to Pricey College Counseling"
  - P2: "Private College Counseling Runs $5,000-$50,000. This Is A Fraction of The Price" (the live B is already close to this one)

**T2. Subheadline: the ad's pain line on the first screen**
- Change: "Drs. Brian & Jeffrey Haig spent 25 years inside university admissions - reading the applications, in the room where the decisions were made. See exactly how the membership works, and what's inside."
- To: "Junior year is where most of it gets decided. And most families are guessing their way through it. Drs. Brian & Jeffrey Haig: 25+ years in college admissions, 15+ on the UCLA Scholarship Admissions Committee."
- Why: word for word from the primary text all 5 ads share, plus the proof line from the same ad. The page currently has no pain line. Playbook hook rule: "call out avatar + problem/goal".

**T3. One name for the freebie, buttons say what they get** (already drafted in the sheet's "LP AB tests" tab, not live yet)
- Change: "See what's inside the membership" / "Enter your details below to see the full breakdown - what's inside, how it works, and what it costs." / "See What's Inside >>" / "Get My Free One-Pager >>"
- To: "Get the free one-pager" / "See what's inside the membership, how it works, and what it costs." / "Send My Free One-Pager >>" on both buttons
- Why: three names for one thing. Playbook: parents get "a free roadmap / one-pager". Skill rule: "One name for the freebie everywhere."

**T4. Form field visible on the first phone screen**
- Change: on mobile, the full subheadline plus "Enter your details below to see the full breakdown - what's inside, how it works, and what it costs." sit above the form, and the first field starts below the fold (about 849px on an 844px screen).
- To: on mobile only, hide the subheadline and the form intro line so "First Name" shows on screen one. Keep the call-out, headline and form title "Get the free one-pager".
- Why: most traffic is Instagram on phones. Skill rule: "Mobile: is the form visible without scrolling?"

**T5. Shorter form**
- Change: First Name *, Last Name *, Phone *, Email * (one per row) + consent, button "See What's Inside >>"
- To: First Name * and Phone * (two columns), Email * full width, consent, button "Send My Free One-Pager >>". Last Name removed.
- Why: playbook form spec "first name + phone (two columns), email full width, consent checkboxes". One field less also shortens the form on mobile (helps T4).

Left out on purpose:
- "The First Month Promise" refund. The offer doc labels it "Guarantee Draft", so it stays off the page until the client confirms. The live ad only says "Cancel anytime", which is safe to use.
- "1,000+" vs "Thousands": not used in any B copy until the client confirms the true number.
- "Ivy+ & TOP-TIER ACCEPTANCES": no number behind it in the docs. Not repeated in any test.

## How to run them

- Traffic: 152 unique link clicks in the 5 logged days (about 210 a week). The last 3 days ran slower (70 clicks, about 160 a week).
- About 150 visitors per version = 300 clicks = **about 2 weeks per test**. Five separate tests would take about 10 weeks, so bundle.
  - **Round 1 (about 2 weeks): T1 + T2 + T3 in one B version** (new first screen: P1 headline, pain subheadline, one freebie name). This replaces the live price-angle B. Do Fix first items 1 to 3 on both versions before starting, so they don't skew the result.
  - **Round 2 (about 2 weeks): T4 + T5** on top of the Round 1 winner (mobile layout and short form, both about friction).
- Clarity labels: Round 1 A = "T1-A", B = "T1-B" (reuse the tag already on the pages; it covers T1 to T3). Round 2 A = "T4-A", B = "T4-B" (covers T4 and T5). Watch in Clarity whether A visitors on mobile scroll down to the form.
- Call the winner with the sheet's own rules: 7+ days, about 20 opt-ins per variant, 30%+ better, nothing changed mid-test. Judge on sheet leads per link click, and watch New Sign-Ups (still 0).

## Questions for Ema or the client

1. What date did the headline split test (more-information vs opt-in-885953) start? Was it Oct 12 or 13, when LPCR fell to 4.8%?
2. What do the GHL split stats show so far (views and opt-ins per variant)?
3. Is "The First Month Promise" approved, or only "Cancel anytime"?
4. Which is true: "Thousands of families guided" (ad) or "1,000+" (page)?
5. What do people get after opting in: a one-pager PDF, a sales page, or both? (Sets the name for T3.)
6. Why does Meta show 18 leads against the sheet's 12? Where does the sheet's Lead number come from?

---

## Appendix: Facts pulled

### LPCR
- Source: sheet "(UCA) - Business Reporting B2C (Low-Ticket)" (1L23VKg6j2MG5g7f8vq5XuF-LWgIMP7K9QMTulyDijw4), tab "Oct", columns E "Link Clicks" and H "Lead"; tab "Dash" row Oct. Sheet clicks (152) equal Meta unique link clicks (152), so the sheet logs unique clicks.
- Daily rows (spend / impr / clicks / leads): Oct 9 $47.04 / 1,690 / 48 / 0. Oct 10 $96.08 / 1,120 / 34 / 3. Oct 11 $108.51 / 1,179 / 31 / 5. Oct 12 $87.25 / 828 / 18 / 3. Oct 13 $91.02 / 1,206 / 21 / 1.
- Oct 13 is logged, so 7d and 3d windows are complete. Before Oct 9 every month is blank or 0.
- Oct totals: spend $429.90, impressions 6,023, CTR 2.52%, CPC $2.83, CPL $35.83, LPCR 7.89%, New Sign-Ups 0, Collected Revenue $0.
- Meta last 3 days (Oct 11 to 13): P3 $153.08 / 45 clicks / 38 LPVs / 4 leads. P1 $106.63 / 23 / 14 / 5. P2 $14.05 / 2 / 1 / 0. P4 $7.10 / 3 / 3 / 3. P5 $5.97 / 1 / 0 / 0.
- "LP AB tests" tab: Clarity snippets for T1-A and T1-B; T1 "Change "Find out how one membership puts 25 years of admissions-committee experience in your family's corner." To "The Affordable Alternative to $5,000-$50,000 Private College Counseling"; a freebie-name test (T3 above); winner rules (7 days, ~20 opt-ins per variant, 30%+ better, fair test, tie after 2 weeks).

### Ad copy (same primary text on all 5 ads; emojis removed)
- "ATTENTION: Parents of 11th Graders Aiming at Competitive Colleges / Junior year is where most of it gets decided. And most families are guessing their way through it. / Not because they don't care. Because nobody ever showed them what actually matters. / Course selection. Activity depth. Testing timing. Which schools to target and which are a waste of an application. / Join Ultimate College Admissions - built by two people with 25+ years as leaders and experts in college admissions, including 15+ years on the UCLA Scholarship Admissions Committee. / Inside the membership: A month-by-month roadmap tied to the real admissions calendar - what to do now, what can wait, what you're already late for / Straight answers on what admissions committees actually weigh (and what they quietly ignore) / How to build a profile that reads as coherent instead of padded / Direct access to ask your own questions and get a real answer from a real person / 25 years inside admissions. Thousands of families guided. $10M+ in scholarships earned by their students. / Cancel anytime. / You get one junior year. Stop guessing your way through it. Join today."
- Title "Ultimate College Admissions", CTA Learn More. Every card links to https://go.ultimatecollegeadmissions.com/opt-in.
- Creative IDs: P1 1140064208579194, P3 1111960024669880, P4 1571711481424014, P2 1244844147839182, P5 1636796287845664.
- P1 slides (all 8 viewed): 1 "Parents of 8th-11th graders: if you have no idea whether your child is taking the right classes, or whether you're already behind, read this. Here's how selective colleges actually judge your child's schedule". 2 "Colleges compare your child's schedule to what your own high school offers. There's no national standard." 3 "Every school sends one document with every application: the School Profile. How many APs are offered. The grade distribution. What was available to your child." 4 "3 APs out of 5 offered is exceptional. 3 APs out of 22 offered is average. Same student. Different read." 5 "Most parents have never seen this document. Their child's counselor sends it anyway." 6 "This matters every February, when next year's course form comes home. Then the year after." 7 "Here's the good news. You just learned one thing most parents never find out. There are hundreds more like it. We spent 25 years on the inside collecting them." 8 "Everything we know, organized by grade, for parents of 8th-11th graders. What to do in 8th, 9th, 10th and 11th, and when. What admissions committees actually weigh, from the people who read the files. Your questions answered by a real person on our team. Click below to learn more."
- P3 slide 1: "Parents of 8th-11th graders: you've looked at private college counselors. $5,000. $20,000. $50,000. Here's what that money actually buys". P3 last slide is the same "Everything we know, organized by grade..." slide (shared by P2, P3, P4).
- Images are 1080x1350 (4:5). The playbook says "Carousels are always square". Ad strategy, so noted only.

### Page copy (loaded 2026-10-14)
- /opt-in: 302 redirect to /more-information (A) or /opt-in-885953 (B), about 50/50, UTMs kept.
- Both: "FOR PARENTS OF 8TH–11TH GRADERS".
- A H1: "Find out how one membership puts 25 years of admissions-committee experience in your family's corner." B H1: "The Affordable Alternative to $5,000-$50,000 Private College Counseling".
- Both sub: "Drs. Brian & Jeffrey Haig spent 25 years inside university admissions - reading the applications, in the room where the decisions were made. See exactly how the membership works, and what's inside."
- Form box: "See what's inside the membership" / "Enter your details below to see the full breakdown - what's inside, how it works, and what it costs." / "Your information is 100% secure and never shared".
- Form (GHL tvqAd1wLtwIwIDGE3A5A): First Name *, Last Name *, Phone * (United States +1), Email *, checkbox "I consent to receive emails and SMS messages regarding my submission and related updates.", button "See What's Inside >>", 4 hidden UTM fields, Cloudflare Turnstile. No prefilled test data.
- Stats: "25+ YEARS ON THE UCLA COMMITTEE", "$10M+ IN SCHOLARSHIPS & AWARDS", "1,000+ OF FAMILIES GUIDED", "Ivy+ & TOP-TIER ACCEPTANCES".
- "Our Wall of Love" / "25 YEARS OF FAMILIES WE WORKED WITH ONE-TO-ONE, AT PRIVATE-COUNSELING PRICES." 6 quotes: Arvin S. (UC Santa Barbara), Kristin & Frank D. (USC), Rachael K. (Texas A&M Engineering), Sheila E. (Cornell), Bill D. (UC Berkeley), Shyamala & Raja (UT Forty Acres Scholar). "See More Stories".
- "Ready to get your free one-pager?" / "Get My Free One-Pager >>" (does nothing). Footer "© 2026 Ultimate College Admissions. | Privacy Policy"; form footer "Privacy Policy | Terms of Service".
- Tracking: Meta pixel 1057989850466986 (PageView), Clarity project yuystg3rza with variant tags.
- Load: DOM ready 1.4 to 2.4s, full load 2.8 to 5.7s in tests.
- Screenshots (in oct14/uca/): uca-desktop.png, uca-mobile.png (first random load), uca-A-desktop.png, uca-A-mobile.png, uca-B-desktop.png, uca-B-mobile.png, plus full-page uca-desktop-full.png and uca-mobile-full.png. Ad slides: p1-first.jpg, p1-s2..s7.jpg, p1-last.jpg, p3-first.jpg, p3-last.jpg.

### Profile facts (no client profile; from "(UCA) Offer and guarantee" and "(UCA) ICPs & Personas")
- Offer: "An affordable alternative to traditional private college counseling." Membership $67/mo or $697/yr. "Drs. Brian and Jeffrey Haig spent 25+ years as leaders and experts in college planning and admissions, including 15+ years on the UCLA Scholarship Admissions Committee".
- Guarantee: only a draft. "The First Month Promise. Try it for 30 days. If it hasn't given you more clarity than everything else you've tried combined, email us and we'll refund it - no form, no call, no questions." Live ad uses only "Cancel anytime."
- Proof: 25+ years, 15+ on UCLA Scholarship Admissions Committee, "$10M+ in scholarships earned by their students" and "Thousands of families guided" (ad), parent testimonials from 1:1 work (page).
- ICP: US parent, 35-55, student in 8th-11th grade aiming at competitive universities, confused about strategy, ready to act. Seniors left out on purpose. Archetypes: Junior-Year Reality Check (primary), Sticker-Shock Refugee (primary), Early Strategist (phase 2).
- Qualified lead: "Affordability is not the qualifier... the real qualifier is intent, not income."
- Mechanism line (ICP doc): "it's $67 because it's one-to-many, not one-to-one."

### Could not get
- Client profile: none exists; used the two UCA docs.
- GHL split-test stats and opt-ins per variant: no GHL access tried (kept short). So the live T1 can't be scored yet.
- Test start date: not logged in the sheet.
- What happens after submit: not tested. I did not submit the live form, to keep test leads out of GHL.
- Real "best month" and drop history: the sheet only has Oct 9 to 13.
- Google Sheets connector needs re-authorization; read the sheet through Drive instead.
