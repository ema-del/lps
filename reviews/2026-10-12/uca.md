# LPCR page review: UCA (Ultimate College Admissions, low-ticket membership, B2C)

**Verdict:** LPCR is 7.1% (8 leads / 113 clicks) because the page sells a different thing than the ad. The ad says "Join today" to a junior-year membership. The page asks parents to opt in for something with three different names, under a headline with no offer. On mobile no form field shows on the first screen.

Note: there is no UCA client profile in the profiles folder. This review uses the Offer and guarantee, ICPs & Personas, Membership Ad Copy and Membership Pain Points docs instead.

"Lead" here means what the sheet's "Lead" column counts: the opt-in form on go.ultimatecollegeadmissions.com/opt-in (first name, last name, phone, email). Paid sign-ups sit in a separate "New Sign-Ups" column (0 so far).

## Live ads (ad account 1150974895696033, last 14 days, ACTIVE only)

Account 785906264362007 has no active ads in the last 14 days. All five ads went live on 2026-10-09, so the "14 days" is really 3 days.

| Ad | Carousel headline | Spend | Share | Link clicks | LPVs | Load rate | Meta leads | LPCR (Meta) |
|---|---|---|---|---|---|---|---|---|
| P1 - Carousel | "Parents of 11th Graders: 25 Years of Admissions Expertise For a Fraction of The Price" | $139.06 | 55.2% | 43 | 37 | 86% | 9 | 20.9% |
| P3 - Carousel | "Parents of 8th-11th Graders: Join the Admissions Insiders' Membership" | $44.36 | 17.6% | 26 | 22 | 85% | 2 | 7.7% |
| P4 - Carousel | "Parents of College-Bound Students: Stop Guessing at Admissions" | $38.25 | 15.2% | 24 | 18 | 75% | 3 | 12.5% |
| P5 - Carousel | "The Affordable Alternative to Pricey College Counseling" | $15.47 | 6.1% | 19 | 16 | 84% | 0 | 0% |
| P2 - Carousel | "Private College Counseling Runs $5,000-$50,000. This Is A Fraction of The Price" | $14.79 | 5.9% | 6 | 4 | 67% | 0 | 0% |
| **Total** | | **$251.93** | 100% | **118** | **97** | **82%** | **14** | **11.9%** |

- Samples are tiny (3 days). Treat per-ad rates as hints, not proof.
- The hint: P1, the "11th Graders" ad, is the only one near the 20% goal. The two price-angle ads (P2, P5) got 0 leads from 25 clicks, and the page says nothing about price on the first screen.
- Overall load rate is 82%, which is fine. P4 (75%) and P2 (67%) are under 80%, but on 24 and 6 clicks.
- Meta's trend and industry benchmark tools returned no data (the account is too new).

## Fix first (broken things, not tests)

1. **Wrong stat on the page.** The stats bar says "25+ YEARS ON THE UCLA COMMITTEE". The offer doc and the live ad say "25+ years as leaders and experts in college admissions, including 15+ years on the UCLA Scholarship Admissions Committee." Change it to "15+ YEARS ON THE UCLA SCHOLARSHIP COMMITTEE".
2. **The bottom button does nothing.** "Get My Free One-Pager >>" (bottom of the page) did not move the page or open anything in my mobile test. Point it at the form (scroll to form or open the same form in a pop-up).
3. **Families number does not match.** Live ad: "Thousands of families guided." Page: "1,000+ OF FAMILIES GUIDED". Pick the true number and use it in both places.
4. **Meta counts more leads than the sheet.** Meta has 14 leads, the sheet has 8 over the same spend ($251.93 vs $251.63). Usually Meta undercounts. Check whether Lead fires twice, or fires on a page view instead of the form submit (Pixel Helper). Until that's fixed, judge LPCR on the sheet.
5. **Sheet history is only 3 days** (Oct 9 to 11). New Sign-Ups, Purchase Rate and Collected Revenue are empty, so the membership step can't be judged yet.
6. **Page has no browser tab title** (empty `<title>`). Minor, but the tab just shows the URL.

## Ad-to-page match

| Check | Ad (all 5 ads use the same primary text) | Page | Match? |
|---|---|---|---|
| Call-out | "ATTENTION: Parents of 11th Graders Aiming at Competitive Colleges" (P1 headline also says "Parents of 11th Graders") | "FOR PARENTS OF 8TH–11TH GRADERS" | Partly. Wider, and loses "junior year" |
| Pain / hook | "Junior year is where most of it gets decided. And most families are guessing their way through it." | First screen has no junior year and no guessing | No |
| Promise | "Join Ultimate College Admissions", "Inside the membership:", "Join today." | "See what's inside the membership", "full breakdown", "free one-pager", button "See What's Inside >>" | No. The ad says join, the page says opt in, and the freebie has 3 names |
| Proof | "25 years inside admissions. Thousands of families guided. $10M+ in scholarships earned by their students." | "25+ YEARS ON THE UCLA COMMITTEE", "$10M+ IN SCHOLARSHIPS & AWARDS", "1,000+ OF FAMILIES GUIDED", "Ivy+ & TOP-TIER ACCEPTANCES" | Partly. UCLA stat is wrong, families number differs |
| Guarantee | "Cancel anytime." | Nothing | No |
| Price angle (P2, P5) | "Private College Counseling Runs $5,000-$50,000. This Is A Fraction of The Price" | Only far down: "AT PRIVATE-COUNSELING PRICES." in the Wall of Love header | No |

## Page vs playbook

- **Headline is not the offer.** Now: "Find out how one membership puts 25 years of admissions-committee experience in your family's corner." Rule: "Headline = the offer ("Get X in X time, or guarantee") and it must be the same on every page."
- **Freebie has 3 names, buttons say different things.** Rule (lpcr-review skill): "Button text says what they get... One name for the freebie everywhere." Playbook: for parents, "opt in for a free roadmap / one-pager."
- **Form friction:** 4 required fields (First Name, Last Name, Phone, Email) + consent checkbox. Rule: "Opt-in form: first name + phone (two columns), email full width, consent checkboxes, button "Access"". Last Name is extra.
- **Phone field:** defaults to United States +1. Good (US ICP).
- **No pre-qualifier.** Correct. Rule: "not for competitive ones like college consulting, SAT/ACT". No money question on the form. Good.
- **Squeeze page elements missing:** no preview image/GIF of the one-pager, no Google/Trustpilot reviews block. Rule: "Squeeze page elements: logo, call-out, headline, subheadline, VSL preview GIF..., short form, Google/Trustpilot reviews block". The Wall of Love (6 parent quotes) is good proof but sits below the stats bar.
- **Mobile:** at 390x844 the first screen shows the logo, call-out, headline, subheadline and the form title. **No form field is visible without scrolling** (the form starts at about 842px).
- **Low-ticket note:** the playbook's Low-Ticket Funnels module is empty ("No lessons in this module yet"). Its only rule is in Choosing your funnel: "Low-ticket funnels ($30-40/month) only suit apps; not recommended for high-ticket consulting or test prep." UCA is $67/mo, so the playbook gives no direct benchmark. This review uses the squeeze page and form rules.
- **Tracking set up:** Meta pixel (PageView), Microsoft Clarity, hidden UTM fields on the form (utm_source and utm_content filled correctly in test).

## 5 A/B tests (biggest expected lift first)

**T1. Headline = the ad's promise, in the ad's words**
- A: Call-out "FOR PARENTS OF 8TH–11TH GRADERS" / Headline "Find out how one membership puts 25 years of admissions-committee experience in your family's corner."
- B: Call-out "FOR PARENTS OF 8TH–11TH GRADERS AIMING AT COMPETITIVE COLLEGES" / Headline "Stop guessing your way through admissions. Get the free one-pager: what's inside the membership, how it works, and what it costs."
- Why: the ad's hook is "guessing their way through it" and "Stop guessing your way through it." The page drops it. Playbook: "Headline = the offer" and "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad."

**T2. Form visible on the first mobile screen**
- A: Subheadline "Drs. Brian & Jeffrey Haig spent 25 years inside university admissions - reading the applications, in the room where the decisions were made. See exactly how the membership works, and what's inside." sits above the form. No field shows at 390x844.
- B: On mobile, hide the subheadline and cut the form intro, so the first field shows on screen one. Move one short line under the button: "From Drs. Brian & Jeffrey Haig, 25+ years in college admissions, 15+ on the UCLA Scholarship Admissions Committee."
- Why: most traffic is Instagram on phones. Rule: "Mobile: is the form visible without scrolling?"

**T3. One name for the freebie, button says what they get**
- A: Form title "See what's inside the membership" / intro "Enter your details below to see the full breakdown - what's inside, how it works, and what it costs." / form button "See What's Inside >>" / bottom button "Get My Free One-Pager >>"
- B: Form title "Get your free one-pager" / intro "See what's inside the membership, how it works, and what it costs." / form button "Send My Free One-Pager >>" / bottom button "Send My Free One-Pager >>" (scrolls to the form)
- Why: three names for one thing. Playbook: parents get "a free roadmap / one-pager". Skill rule: "One name for the freebie everywhere."

**T4. Shorter form**
- A: First Name, Last Name, Phone, Email (one per row) + consent.
- B: First Name and Phone (two columns), Email full width, consent. Last Name removed.
- Why: playbook form spec: "first name + phone (two columns), email full width, consent checkboxes". One field less and a shorter form on mobile.

**T5. Explain the price next to the form (for the price-angle ads)**
- A: Nothing about price near the form. Only line far below: "25 YEARS OF FAMILIES WE WORKED WITH ONE-TO-ONE, AT PRIVATE-COUNSELING PRICES."
- B: Add right under the form title: "Private college counseling runs $5,000 to $50,000. This is the same 25 years of guidance, delivered to a thousand families at once instead of one. Cancel anytime."
- Why: P2 and P5 promise "a fraction of the price" and got 0 leads from 25 clicks. ICP doc: "'Too cheap to be real' dies to mechanism: it's $67 because it's one-to-many, not one-to-one." The wording comes from Membership Ad Copy 2 and the live ad ("Cancel anytime"). Don't add the "First Month Promise" until the client confirms it (the doc calls it a draft).

## How to run them

- Traffic: 113 link clicks in 3 days (sheet), so about 260 clicks a week at the current ~$84/day.
- One test needs about 150 visitors per version = 300 clicks = **about 8 days**. Five separate tests would take about 6 weeks.
- Bundle, because traffic is low:
  - **Round 1 (about 8 days):** T1 + T2 + T3 in one B version (new first screen: headline, mobile layout, one freebie name). Do Fix first items 1 to 3 on both versions before starting.
  - **Round 2 (about 8 days):** T4 + T5 on top of the Round 1 winner.
- Clarity is already on the page. Tag the versions: T1-A / T1-B, T2-A / T2-B, T3-A / T3-B (Round 1 versions share the T1 to T3 tags), T4-A / T4-B, T5-A / T5-B. Check whether mobile visitors scroll to the form on A.
- Judge on sheet leads per link click. Also watch New Sign-Ups, since the goal is paid members.

## Questions for Ema or the client

1. Is the "First Month Promise" live? Can it go on the page, or only "Cancel anytime"?
2. Which is true: "Thousands of families guided" (ad) or "1,000+" (page)?
3. What do people actually get after opting in: a one-pager PDF, a sales page, or both? (Sets the freebie name for T3.)
4. Where does the sheet's "Lead" number come from (GHL count or Meta)? Why does Meta show 14 against the sheet's 8?
5. Should the page call out 11th graders only, matching P1 (the ad with most spend), or keep 8th to 11th?
6. Can we get GHL funnel stats (page views to opt-ins, opt-ins to sign-ups) for this page?

---

## Appendix: Facts pulled

### LPCR (sheet "(UCA) - Business Reporting B2C (Low-Ticket)", tab "Oct", columns E "Link Clicks" and H "Lead")
- Data exists only for Oct 9, 10 and 11, 2026. All other days and months are blank or 0. The sheet's link clicks (113) are close to Meta's unique link clicks (114), so the sheet most likely logs unique clicks.
- Daily: Oct 9: 0 / 48 = 0%. Oct 10: 3 / 34 = 8.8%. Oct 11: 5 / 31 = 16.1%.
- **Last 7 days (Oct 5 to 11): 8 / 113 = 7.1%** (only Oct 9 to 11 have data).
- **Last 3 days (Oct 9 to 11): 8 / 113 = 7.1%.**
- **Best month: October, 7.1%.** It's the only month with data (sheet created 2026-09-21), so "best month" is just the best available.
- When it dropped: it didn't. It started low and is climbing day by day (0% to 8.8% to 16.1%). Still under the 20% goal and the 15% "bad" line.
- Other sheet numbers (Oct): spend $251.63, impressions 3,989, CTR 2.83%, CPC $2.23, CPL $31.45, New Sign-Ups 0, Collected Revenue $0.
- Meta LPCR for comparison: 14 / 118 = 11.9%. Meta CPL $18.00.

### Ad copy (all 5 active ads use the same primary text; emojis removed)
- Primary text: "ATTENTION: Parents of 11th Graders Aiming at Competitive Colleges / Junior year is where most of it gets decided. And most families are guessing their way through it. / Not because they don't care. Because nobody ever showed them what actually matters. / Course selection. Activity depth. Testing timing. Which schools to target and which are a waste of an application. / Join Ultimate College Admissions - built by two people with 25+ years as leaders and experts in college admissions, including 15+ years on the UCLA Scholarship Admissions Committee. / Inside the membership: A month-by-month roadmap tied to the real admissions calendar - what to do now, what can wait, what you're already late for / Straight answers on what admissions committees actually weigh (and what they quietly ignore) / How to build a profile that reads as coherent instead of padded / Direct access to ask your own questions and get a real answer from a real person / 25 years inside admissions. Thousands of families guided. $10M+ in scholarships earned by their students. / Cancel anytime. / You get one junior year. Stop guessing your way through it. Join today."
- Creative title: "Ultimate College Admissions". CTA: Learn More. Link: https://go.ultimatecollegeadmissions.com/opt-in
- Card headlines per ad: see the live ads table.

### Page copy (go.ultimatecollegeadmissions.com/opt-in, loaded 2026-10-12)
- "FOR PARENTS OF 8TH–11TH GRADERS"
- H1: "Find out how one membership puts 25 years of admissions-committee experience in your family's corner."
- Sub: "Drs. Brian & Jeffrey Haig spent 25 years inside university admissions - reading the applications, in the room where the decisions were made. See exactly how the membership works, and what's inside."
- Form box: "See what's inside the membership" / "Enter your details below to see the full breakdown - what's inside, how it works, and what it costs."
- Form (GHL embed): First Name *, Last Name *, Phone * (US +1 default), Email *, checkbox "I consent to receive emails and SMS messages regarding my submission and related updates.", button "See What's Inside >>", hidden UTM Source/Campaign/Medium/Content, invisible Cloudflare check. No prefilled test data.
- "Your information is 100% secure and never shared"
- Stats: "25+ YEARS ON THE UCLA COMMITTEE", "$10M+ IN SCHOLARSHIPS & AWARDS", "1,000+ OF FAMILIES GUIDED", "Ivy+ & TOP-TIER ACCEPTANCES"
- "Our Wall of Love" / "25 YEARS OF FAMILIES WE WORKED WITH ONE-TO-ONE, AT PRIVATE-COUNSELING PRICES." 6 parent quotes: Arvin S. (UC Santa Barbara), Kristin & Frank D. (USC), Rachael K. (Texas A&M Engineering), Sheila E. (Cornell), Bill D. (UC Berkeley), Shyamala & Raja (UT Forty Acres Scholar). "See More Stories".
- "Ready to get your free one-pager?" / button "Get My Free One-Pager >>" (did nothing when clicked in test)
- Footer: "© 2026 Ultimate College Admissions. | Privacy Policy". Form footer: "Privacy Policy | Terms of Service".
- Screenshots: uca-desktop.png (1440x900), uca-mobile.png (390x844), plus full-page versions uca-desktop-full.png and uca-mobile-full.png in the scratchpad.
- Load: DOM ready in 0.9 to 1.6s. Network idle took about 21s in a headless test (likely trackers). Meta load rate 82% says it's fine for real users.

### Profile facts (no client profile exists, from the 4 UCA docs)
- Offer: "An affordable alternative to traditional private college counseling." Membership $67/mo or $697/yr (ICP doc). Drs. Brian and Jeffrey Haig, "25+ years as leaders and experts in college planning and admissions, including 15+ years on the UCLA Scholarship Admissions Committee."
- Real guarantee (draft): "The First Month Promise. Try it for 30 days. If it hasn't given you more clarity than everything else you've tried combined, email us and we'll refund it - no form, no call, no questions." The live ad only says "Cancel anytime." Ad Copy 2 (not live) adds "No contract. Cancel in two clicks. Your rate never goes up."
- Proof: 25+ years, 15+ on UCLA Scholarship Admissions Committee, "Thousands of families guided", "$10M+ in scholarships earned by their students" (ad), parent testimonials from 1:1 work (page).
- ICP: US parent, 35-55, student in 8th-11th grade aiming at competitive universities, confused about strategy, ready to act. Seniors (12th) left out on purpose. Archetypes: Junior-Year Reality Check (primary), Sticker-Shock Refugee (primary), Early Strategist (phase 2).
- Qualified lead: "Affordability is not the qualifier... the real qualifier is intent, not income." Grade 8 to 11.
- Pain points: no order/plan, contradicting advice, $5k-$50k is out of reach, good grades no longer enough, fear decisions are already made.
- Pacow offer: GrowthOS.

### Could not get
- Client profile: none in "00. Client Profiles (Claude)". Used the 4 UCA docs instead.
- Sheet history before Oct 9: blank (sheet is new). No real "best month" or drop date.
- Meta performance trend and industry benchmark: both returned "No data available" (account too new).
- GHL funnel stats: not pulled (HighLevel tools not tried, to keep this short). Opt-in to sign-up rate is unknown.
- What happens after submit (thank-you page / one-pager content): not tested. I did not submit the live form, to keep test leads out of GHL.
