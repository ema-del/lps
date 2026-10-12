# LPCR page review: Zinkerz (Carlos Hafeitz)

**Verdict:** The opt-in form asks a money question ("partial-scholarship spots... We're good to invest") that the playbook bans for SAT prep and for a CPL this high. On top of that, the page sells a different offer ("Give Us 90 Days") than the ad's free "SAT Roadmap" one-pager. On mobile, the phone, email and button all sit below the fold. LPCR is 4.6% (goal 20%).

## Live ads (Meta, last 14 days, ACTIVE, ads with spend)

All 4 "PP5" ads run the same primary text and headline, and all link to sites.zinkerz.com/access, which redirects to the split test (/squeeze-page or /squeeze-page-538225).

| Ad | Spend | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| PP5 Simple Text | $566.99 | 211 | 181 | 4 | 66.0% | 85.8% | 1.9% |
| PP5 notes checklist | $110.12 | 21 | 18 | 0 | 12.8% | 85.7% | 0% |
| PP5 Black Notes 1,2,3 | $96.38 | 16 | 13 | 0 | 11.2% | 81.3% | 0% |
| Obj 2 (video, "Chat with us") | $22.07 | 3 | 0 | 0 | 2.6% | n/a | 0% |
| Obj 4 (video) | $20.60 | 2 | 0 | 0 | 2.4% | n/a | 0% |
| PP5 black notes reminder | $16.14 | 2 | 0 | 0 | 1.9% | 0% | 0% |
| Obj 1 (video) | $16.11 | 2 | 0 | 0 | 1.9% | n/a | 0% |
| Obj 3 (video) | $9.13 | 1 | 0 | 0 | 1.1% | n/a | 0% |
| Obj 5 (video) | $1.33 | 0 | 0 | 0 | 0.2% | n/a | n/a |
| **Total** | **$858.87** | **258** | **212** | **4** | 100% | **82.2%** (PP5 only: 84.8%) | **1.6%** |

- Load rate is fine (about 85% on the PP5 ads). The page itself loads, so the leak happens after people land.
- The sheet logs 15 leads for the same 14 days (2026-09-28 to 10-11). Meta shows 4, about 27% of that. Meta's 4 is close to the sheet's 6 pre-qualified leads, so the Lead event may only fire for pre-qualified people. Judge LPCR on the sheet.

## Fix first (broken things, not tests)

1. **The guarantee says two different things.** The ad says "we keep coaching until your child hits their target score - no extra cost." The page says "..if they don't hit their target, we'll run a free intensive session on us." The client profile lists no guarantee at all. Confirm the real terms with Carlos, then use the same words in the ad and on the page.
2. **ACT stat on an SAT page.** The stats bar opens with "+6 Avg. ACT Point Increase". This page sells SAT, and the profile has no ACT stat. Remove it, or swap in "100% Early Action / Early Decision Rate (2025)", which the profile backs.
3. **"5,000+ SAT Students Taught" is not in the profile.** The profile says "~400" active students. Check the number with Carlos before it stays on the page.
4. **No Terms link in the footer.** The footer only says "Copyrights 2026 | Zinkerz™ | Privacy Policy". Playbook: "Terms and privacy policy links in every footer (required by Facebook...)".
5. **Meta tracking.** Meta shows 4 leads, the sheet shows 15. Check where the Lead pixel fires (form vs next page) so Meta optimizes on the right event.
6. **Finish the live T1 test before starting new ones.** T1 has been running since 2026-10-07: "FOR PARENTS OF HIGH-ACHIEVING STUDENTS" (T1-A, /squeeze-page-538225) vs "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET" (T1-B, /squeeze-page). Clarity tags are firing. It has about 137 clicks total so far (around 68 per version). Let it reach 150 per version.

## 5 A/B tests (biggest expected lift first)

Labels start at T2 because T1 (call-out) is already live.

### T2. Remove the scholarship pre-qualifier
- **A (now):** 4th required field: "We keep a few partial-scholarship spots each cohort for families who need a little help getting started. Which sounds like you?" Options: "We're good to invest in the right program for our child" / "A scholarship would be nice, but we don't necessarily need it" / "We'll need significant scholarship help".
- **B:** Delete the question. The form becomes First Name, Phone, Email, consent box, button. Ask the scholarship question in the qualification survey instead, after the opt-in.
- **Why:** Playbook, Setting up your forms: "Pre-qualifier (only for niche markets with plenty of leads; not for competitive ones like college consulting, SAT/ACT, fitness)". Conversion Ads: "If CPL is already $45-50, don't". CPL over the last 7 days is $88.69 ($709.49 / 8 leads). B2C rule: "never mention money... It is a complete drop off moment." Option 1 says "invest". The sheet shows the question went live on 2026-07-03 ("added prequalifier about scholarship"). The playbook says to remove it outright. Run it as a test only if Ema wants to watch the effect on lead quality.

### T3. Headline = the ad's offer
- **A (now):** "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." Subheadline: "No long, generic grind. Just focused practice on the exact points holding them back."
- **B:** Headline: "Free SAT Roadmap: How Your Teen Can Add 300+ Points Before the Next Test Date". Subheadline: "Your kid isn't the problem. The process is a mess. This one-pager shows how our students average a 310+ point jump with 1:1 coaching built around their gaps."
- **Why:** The ad headline is "Free SAT Roadmap: Add 300+ Points Before the Next Test" and the copy says "Get the free one-pager: The SAT Roadmap - How to Add 300+ Points Before Your Next Test Date". "90 Days" appears in no live PP5 ad, and the Obj 3 ad says "It's not something a 90-day crash course gives you". The ad creative's pain ("Your kid isn't the problem. The process is a mess.") is missing from the first screen. Playbook, reading the data: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."

### T4. Form visible on the first mobile screen
- **A (now):** On a 390x844 phone, the screen shows the logo, call-out, headline, subheadline, the italic guarantee line, then only the form card title "Get My 300-Point Roadmap". Phone, email and the button start roughly 2 screens down (the form iframe starts about 700px down and is about 918px tall).
- **B:** Cut the black header to a thin logo bar. Put the form card directly under a one-line subheadline. Move the guarantee line to a badge directly above the button. Drop the "Free SAT Roadmap" eyebrow and the "Enter your information below..." line inside the card. Goal: the first name field and the top of the phone field show without scrolling.
- **Why:** The process says "Mobile: is the form visible without scrolling? (Most traffic is Instagram on phones.)" Playbook: "Pages give leads 2 options: take the action or LEAVE... very simple."

### T5. Score proof right under the button
- **A (now):** The reviews have no scores ("With flexible scheduling, intense marathons, and expert support, I stayed on track..." from Mikaela, SAT student). Students come first, parents third. The only number near the form is in the stats bar, which opens with the ACT stat.
- **B:** Directly under the button: "Mikaela went from 1260 to 1530, admitted to Vanderbilt. Andre went from 1100 to 1500, admitted to NYU. Our students average a 310+ point jump (2025)." In the Wall of Love, move the parent reviews ("Laura & Martin", "Andres & Luciana") to the top.
- **Why:** These exact results are on the live ad creative people just saw ("Mikaela went from 1260 to 1530 → admitted to Vanderbilt / Andre went from 1100 to 1500 → admitted to NYU"), and the page doesn't repeat them. The process says "Proof near the form: results with real numbers, parent reviews first when parents are the buyer." The profile says the buyers are parents.

### T6. One name for the freebie, a button that says what they get, and a preview image
- **A (now):** Three names: "Get My 300-Point Roadmap" (form title), "Get Started >>" (button), "Get Your Free One-Pager >>" (bottom button). No image of the one-pager.
- **B:** Form title: "Get the Free SAT Roadmap". Button: "Send Me the SAT Roadmap". Bottom button: "Send Me the SAT Roadmap". Add a tilted mockup image of the one-pager's first page next to the form (above it on mobile).
- **Why:** The process says "Button text says what they get (not 'Get Started' / 'Submit'). One name for the freebie everywhere." Squeeze page elements in the playbook include a "preview GIF/image of the freebie". The ad calls it "The SAT Roadmap".

## How to run them

- **Traffic:** about 173 link clicks a week (sheet, 2026-10-05 to 10-11). At about 150 visitors per version (300 per test), each test needs about **12 days**. Running all 5 one at a time would take about 2 months.
- **Order:**
  1. Let T1 (call-out) finish, about 1 more week (around 2026-10-19). Keep the winner.
  2. **T2 (pre-qualifier) alone**, about 12 days. It is the biggest change and it touches lead quality, so check pre-qualified and qualified counts in GHL as well as LPCR.
  3. **Bundle T3 + T4 + T6 into one B version** (headline, mobile layout, button/name/preview). These are all "make the page match the ad" changes. Label it T3-A / T3-B. About 12 days.
  4. **T5 (proof)** last, about 12 days.
- **Clarity labels:** `clarity("set","variant","T2-A")` / `"T2-B"`, then `T3-A` / `T3-B` for the bundle, then `T5-A` / `T5-B`. Use the same script format already on the page for T1.
- **When to call it** (from the sheet's LP A/B test tab): "at about 150+ visits per version, if one version is ahead by 3+ percentage points... If it's closer than that, keep it running another week." Log every change as a comment in the sheet on the day it goes live.

## Questions for Ema / Carlos

1. What is the real guarantee: "keep coaching until they hit their target score, no extra cost" or "a free intensive session"?
2. LPCR was 8.5% in August and fell to 3.6% after the 2026-09-05 relaunch. What changed on the page and in the ads at the relaunch? The PP5 creatives are dated 2026-09-03.
3. Was the scholarship question on the August page too? The sheet shows it was added 2026-07-03, and that "the urgency qualification" was removed 2026-08-04, just before the best month.
4. Where is "5,000+ SAT Students Taught" from? And the "+6 Avg. ACT Point Increase"?
5. Is the Lead pixel on the form or on the next page? (Meta shows 4 leads vs 15 in the sheet.)
6. Is the campaign US only? The phone field defaults to the US (+1). If LatAm countries are back in targeting, the default should match.
7. Where do the "Obj" video ads ("Chat with us") send people? They got 8 clicks and 0 page views.

---

## Appendix: Facts pulled

### LPCR (sheet "(ZK) - Business Reporting Daily 2026")
- Columns used: daily month tabs (Jun to Oct): A date, B Adspend (USD), E Link Clicks, H Lead, I Pre-Qualified Leads. Dash tab col I (LPCR) for months. LPCR = Lead / Link Clicks.
- **Last 7 days (2026-10-05 to 10-11): 8 leads / 173 clicks = 4.6%** (spend $709.49, CPL $88.69, 3 pre-qualified)
- **Last 3 days (2026-10-09 to 10-11): 4 / 84 = 4.8%** (spend $297.23)
- Week before (09-28 to 10-04): 7 / 182 = 3.8%
- **Best month 2026: August, 52 / 610 = 8.5%** (spend $1,798.41). Late July 27-31 was also strong: 19 / 202 = 9.4%.
- Other months: Jun 4.3% (121/2,801), Jul 3.5% (358/10,185, mostly cheap international clicks at $0.30 CPC), Sep 4.2% (52/1,252), Oct to date 4.4% (11/250).
- **When it dropped:** at the relaunch on 2026-09-05 (paused 08-19 to 09-03). Sep 1-14: 3.6% (25/688). Sep 15-30: 4.8%. It has stayed at 4-5% since.
- Sheet comments: 07-03 "added prequalifier about scholarship"; 07-07 "reduced survey questions"; 07-16 "changed to only US"; 07-22 "changed button to 'book a call'", "also removed SAT score one"; 08-04 "made LP changes", "also removed the urgency qualification"; 08-17 "a/b testing 'See if my child qualifies vs. book ym free call'"; 08-21 "paused"; 09-05 "relaunched"; 09-09 "made smal changes to LP"; 09-24 "added LAL"; 10-01 "A/B testing free 300-point roadmap vs. free one pager"; 10-07 "launched new ads", "new A/B test LP too".
- The sheet already has an "LP A/B test" tab with T1 (call-out, now live), plus ideas for a guarantee badge, score reviews, and one freebie name. T5 and T6 above build on those.
- Sheet 14-day totals (09-28 to 10-11): $1,405.20 spend, 355 clicks, 15 leads. The sheet shows more spend and clicks than the 9 active Meta ads ($858.87 / 258), so the sheet also counts ads that are paused now or clicks from other campaigns.

### Live ad copy (all 4 PP5 ads, from ad previews)
- Primary text: "If your child is preparing for the SAT and the score isn't where it needs to be - grab this free one-pager. It breaks down how Zinkerz students add 300+ points through 1:1 coaching, weekly mock exams, and a plan built around each student's specific gaps. Our students average a 310+ point jump, and we keep coaching until your child hits their target score - no extra cost. 📄 Get the free one-pager: The SAT Roadmap - How to Add 300+ Points Before Your Next Test Date 📞 Then book your SAT Score Breakthrough Session. 👇 Start with the free one-pager."
- Headline: "Free SAT Roadmap: Add 300+ Points Before the Next Test". CTA: Learn more.
- Creative (Simple Text): "To parents of a high school student prepping for the SAT: Your kid isn't the problem. The process is a mess. Which prep, which test date, how many times to sit it, nobody gives you a straight answer, and the clock keeps running. Students who get a program built around them are seeing real results: Mikaela went from 1260 to 1530 → admitted to Vanderbilt. Andre went from 1100 to 1500 → admitted to NYU. All with 1:1 coaching built around their specific gaps. The next test is just weeks away."
- Link: https://sites.zinkerz.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=pcw_offer&utm_content=pp5simpletext...
- Obj ads (headline "Chat with us"), for example Obj 1: "...a dedicated 1:1 coach who knows your kid, 4 sessions a week built around their gaps, and a guarantee - we keep coaching until they hit their target score. No extra cost." Obj 3: "It's not something a 90-day crash course gives you..."

### Page copy (sites.zinkerz.com/squeeze-page, loaded 2026-10-12)
- Call-out: "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET" (T1-B). The variant /squeeze-page-538225 says "FOR PARENTS OF HIGH-ACHIEVING STUDENTS" (T1-A). Everything else is the same on both.
- Headline: "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT."
- Subheadline: "No long, generic grind. Just focused practice on the exact points holding them back."
- Guarantee line (italic): "..if they don't hit their target, we'll run a free intensive session on us"
- Form card: "📄 Free SAT Roadmap" / "Get My 300-Point Roadmap" / "Enter your information below and we'll send you a one-pager on how this system works."
- Form (GHL widget OJl5wq0yL7h0wbLkL9P5): First Name *, Phone * (defaults to United States +1), Email *, scholarship radio question * (3 options, quoted in T2), SMS/email consent checkbox, button "Get Started >>". No prefilled or test data. No dropdowns.
- "🔒 Your information is 100% secure and never shared"
- Stats: "+6 Avg. ACT Point Increase", "310+ Point Average Improvement", "5,000+ SAT Students Taught", "100% Early Action / Early Decision Rate (2025)"
- "Our Wall of Love", "5.0 Rating · 5,000+ Students Taught", 6 text reviews (Mikaela, Gaby, Laura & Martin, Andres & Luciana, Brian, Daniel) with no scores, plus 6 YouTube testimonial videos.
- Bottom: "Ready to get your free one-pager?" / "Get Your Free One-Pager >>". Footer: "Copyrights 2026 | Zinkerz™ | Privacy Policy".
- Mobile (390x844): the form card title shows at the bottom of the first screen. The fields and button are below the fold. Desktop (1440x900): the first name, phone and email fields show, and the button is below the fold.
- Load: about 4.7 to 7.8 seconds in headless Chromium, including the /access redirect. Screenshots: zinkerz-desktop.png, zinkerz-mobile.png (full-page versions: zinkerz-desktop-full.png, zinkerz-mobile-full.png).

### Client profile facts
- Offer (SAT): "We help high school students improve their SAT scores through personalized 1:1 coaching and structured accountability systems, with qualifying students averaging +310 points of combined score improvement in 2025." Price $100-150/hr, about 4 sessions a week.
- Guarantee: **none listed.** "Stats, bonuses, guarantees, urgency" only lists: "SAT Camp, 350+ score improvement SAT online prep 310+ score improvement All students in 2025 admitted in early action/decision Free consultation free readiness assessment".
- Proof: 310+ average (online), 350+ (camp), 100% EA/ED admits in 2025, about 400 active students.
- ICP / buyer: parents (students under 18). Strongest markets: Brazil, Honduras, Panama, Colombia, Dominican Republic, and the US Northeast, South Florida and Miami.
- Qualified lead: "Can afford college in the US", understands the SAT and US college basics, "Goes to a private school", "HNW families".

### Playbook rules relied on
- "Pre-qualifier (only for niche markets with plenty of leads; not for competitive ones like college consulting, SAT/ACT, fitness)"
- "If CPL is already $45-50, don't" (add a pre-qualifier)
- "B2C: never mention money ('It is a complete drop off moment')"
- "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page."
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- "Squeeze page elements: logo, call-out, headline, subheadline, VSL preview GIF..., short form, Google/Trustpilot reviews block"
- "Parents/test prep/college prep: use the more direct roadmap / one-pager version"
- "Terms and privacy policy links in every footer"
- "DO NOT USE FACEBOOK TO TELL YOU HOW MANY LEADS YOU GOT..."

### What I could NOT get
- `ads_get_creatives` returned no body, title or link_url for the PP5 creatives (they appear to be built from an asset feed). I pulled the copy from the ad preview pages and the link from the preview's outbound URL instead.
- Link URLs for the "Obj" video ads were not returned, so I don't know where they send people.
- GHL funnel stats (page views to opt-ins per step): not tried, to keep within time. I judged LPCR on the sheet.
- The August version of the page and the ads that ran before 2026-09-05, so I can't say exactly what changed at the drop.
- Which page Meta's Lead event fires on (I can't see it from outside).
