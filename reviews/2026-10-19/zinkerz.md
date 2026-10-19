# Zinkerz LPCR deep dive, Oct 19 2026

**Zinkerz**: LPCR 7d 10.5% (16/152), 3d 8.3% (5/60), prior week (Oct 7-13) 6.8% (13/190). Main reason: the opt-in still asks a money question ("We're good to invest...") that the playbook bans for SAT prep, and the page sells "Give Us 90 Days" while the ad (97.6% of spend) sells "How to Finally Make Sense of the SAT" and the "Free SAT Roadmap". Since Oct 14, nothing on the page has changed.

## LPCR (sheet "(ZK) - Business Reporting Daily 2026", tab Oct: E Link Clicks, H Lead, I Pre-Qualified, B Adspend)

| Window | Leads / clicks | LPCR | Spend | CPL | Pre-qualified |
|---|---|---|---|---|---|
| Last 7d (Oct 12-18) | 16 / 152 | **10.5%** | $645.36 | $40.34 | 5 |
| Last 3d (Oct 16-18) | 5 / 60 | **8.3%** | $245.37 | $49.07 | 2 |
| Prior week (Oct 7-13) | 13 / 190 | 6.8% | $704.45 | $54.19 | 5 |
| Best month 2026: Aug | 52 / 610 | 8.5% | $1,798.41 | $34.58 | 15 |
| Oct to date (1-18) | 27 / 402 | 6.7% | $1,781.82 | $66.00 | 9 |

- Did it move? Up 3.7 points on paper. But 6 of the 16 leads are from Oct 13 (6 leads on 16 clicks, still unconfirmed). Without Oct 13 the week is 10 / 136 = **7.4%**, so the real gain is small. Since Simple Text stopped (Oct 15-18): 8 / 84 = 9.5%.
- Still far from the 15% goal and the playbook line: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- Sheet comment Oct 15: "dropped budget to 80". Clicks per day fell to 15-24.
- Sheet filled through Oct 18.

## Changed since Oct 14

| Oct 14 item | Status |
|---|---|
| T1 call-out test: call it at ~150 per version | **Not done.** /access still 302s to both pages (8 test hits: 5 to -538225, 3 to /squeeze-page). Both T1 tags still live. No result logged in the sheet's "LP AB test" tab. |
| Remove the scholarship pre-qualifier | **Not done.** Same 4th required question in the form and in the bottom pop-up. |
| Headline = ad headline | **Not done.** Still "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." |
| Mobile: form higher | **Not done.** Same layout. First Name at about 760px, button about 1,480px down on a 390x844 phone. |
| Score proof under the button | **Not done.** Same 6 reviews, no scores. |
| One freebie name, clear button | **Not done.** "Get My 300-Point Roadmap" / "Get Started >>" / "Get Your Free One-Pager >>". |
| Remove "+6 Avg. ACT Point Increase" | **Not done.** |
| Confirm "5,000+ SAT Students Taught" | **Not done** (still on page). |
| Terms link in footer | **Not done.** Footer: "Copyrights 2026 \| Zinkerz™ \| Privacy Policy". |
| One guarantee wording | **Not done.** Page still "..if they don't hit their target, we'll run a free intensive session on us". |
| Form showing late (7-9s on Oct 14) | **Looks fixed.** Form fields showed in 1.0 to 1.7s in 6 of 6 phone loads. Full page load 3.7 to 5.4s (was 17-22s). Confirm on real phones in Clarity. |
| Meta lead tracking (Meta saw 38%) | **Better, not fixed.** Meta 10 vs sheet 16 (63%). |
| Ads (not a page fix) | PP5 Simple Text (68.6% on Oct 14) is now PAUSED. Last spend Oct 14 ($6.23). No new ads since Oct 14 (newest created Oct 7). |

## Live ads (Meta, "OLead//FreeTraining//US", ACTIVE, last 7d Oct 12-18)

| Ad | Spend | Link clicks | LPVs | Meta leads | Share | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| PP5 notes checklist (video, Oct 7) | $524.75 | 115 | 103 | 10 | **97.6%** | 89.6% | 8.7% |
| PP5 Black Notes 1,2,3 (static) | $10.40 | 3 | 3 | 0 | 1.9% | 100% | 0% |
| PP5 black notes reminder (static) | $2.76 | 0 | 0 | 0 | 0.5% | n/a | n/a |
| **Total active** | **$537.91** | **118** | **106** | **10** | 100% | **89.8%** | 8.5% |

- Also in this window: PP5 Simple Text (now PAUSED) spent $109.90 Oct 12-14, 41 clicks, 33 LPVs, **0 Meta leads**. Retargeting ("Hammer Them Retargeting", Obj 1-5) spent $35.50, left out of the page match.
- Notes checklist: headline "Free SAT Roadmap: Add 300+ Points Before the Next Test". Primary text opens "If your child is preparing for the SAT and the score isn't where it needs to be - grab this free one-pager." Video (22s, frames viewed, same card the whole clip): "How to Finally Make Sense of the SAT: ✓ Understand why smart kids still get stuck on the SAT ✓ See which test date and prep actually fit your child ✓ Learn the exact system that removes the guesswork ✓ Discover how students add 300+ points in 90 days. Get the free SAT roadmap 👇". Link: sites.zinkerz.com/access?utm_content=pp5noteschecklist.

## Ad vs page (the ad with 97.6% of spend)

| | Ad says | Page says |
|---|---|---|
| Hook | "How to Finally Make Sense of the SAT:" | Not on the page |
| Pain | "why smart kids still get stuck", "which test date and prep actually fit your child", "removes the guesswork" | "No long, generic grind. Just focused practice on the exact points holding them back." |
| Offer | "Free SAT Roadmap" / "The SAT Roadmap - How to Add 300+ Points Before Your Next Test Date" | "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." Card: "Get My 300-Point Roadmap" |
| Guarantee | "we keep coaching until your child hits their target score - no extra cost" | "..if they don't hit their target, we'll run a free intensive session on us" |
| Proof | "Our students average a 310+ point jump" | "310+ Point Average Improvement" in the stats bar, below the form |
| Button | "Get the free SAT roadmap 👇" | "Get Started >>" |

## Health checks

- Load rate: 89.6% on the notes ad, 89.8% overall. Fine (Simple Text was 80.5%).
- Pixel: Meta pixel 361058407608544 loads on both variants, PageView request seen. Clarity tag xbzwtroqg5 loads with `clarity("set","variant","T1-A")` on /squeeze-page-538225 and `"T1-B"` on /squeeze-page.
- Form: GHL form OJl5wq0yL7h0wbLkL9P5 in an iframe. First Name *, Phone *, Email *, scholarship radio *, consent box, "Get Started >>". Phone defaults to US +1 (matches the US campaign). No prefilled or test data. 4 hidden fields (likely UTMs). Cloudflare Turnstile captcha loads in the background.
- Buttons: the bottom "Get Your Free One-Pager >>" opens a pop-up with the same form (worked on phone and desktop when clicked a few seconds after load).
- Speed: text in about 0.4 to 2s, form in 1.0 to 1.7s, full load 3.7 to 5.4s (headless Chrome).
- Screenshots: /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/zinkerz/ (zinkerz-A-desktop.png, zinkerz-A-mobile.png, zinkerz-B-desktop.png, zinkerz-B-mobile.png, plus -full versions and the pop-up shots). Desktop 1440x900: First Name and Phone visible, Email cut off, button below the fold. Phone 390x844: only the card title and "First Name" label show on the first screen.

## A. FIXES (do now, not tests)

1. **Call T1 now.** About 289 clicks since Oct 7 (sheet), so roughly 145 per version. Pull Clarity sessions and form submits per tag (T1-A vs T1-B) since Oct 7. Use the sheet rule: "if one version is ahead by 3+ percentage points" keep it, then point /access at the winner only. Log the result in "LP AB test".
2. **ACT stat.** Change "+6 / Avg. ACT Point Increase" To "350+ / SAT Camp Point Improvement" (profile: "SAT Camp, 350+ score improvement").
3. **Guarantee, same words as the ad** (once Carlos confirms it). Change "..if they don't hit their target, we'll run a free intensive session on us" To "Our students average a 310+ point jump, and we keep coaching until your child hits their target score, at no extra cost." Both parts are from the live ad. If Carlos says the real term is the free intensive session, change the ad instead.
4. **"5,000+".** Change "5,000+ / SAT Students Taught" and "5.0 Rating · 5,000+ Students Taught" To "100% / Early Action / Early Decision Rate (2025)" (already on the page) and "5.0 Rating", unless Carlos confirms 5,000+. The profile says "~400" active students.
5. **One name for the freebie.** Change card title "Get My 300-Point Roadmap" To "Get the Free SAT Roadmap". Change "Get Started >>" To "Send Me the SAT Roadmap >>". Change "Get Your Free One-Pager >>" To "Send Me the SAT Roadmap >>". (Ad: "Get the free SAT roadmap 👇". Process: "Button text says what they get... One name for the freebie everywhere.")
6. **Footer.** Change "Copyrights 2026 | Zinkerz™ | Privacy Policy" To "Copyrights 2026 | Zinkerz™ | Privacy Policy | Terms & Conditions". Playbook: "Terms and privacy policy links in every footer (required by Facebook...)".
7. **Tracking.** Do one test submit and check in Events Manager that Lead fires on form submit. Meta still sees only 63% of sheet leads.

## B. A/B TESTS (biggest lift first; T1 is the call-out test, so these start at T2)

**T2. Form: remove the scholarship question.**
Change "We keep a few partial-scholarship spots each cohort for families who need a little help getting started. Which sounds like you? *" ("We're good to invest in the right program for our child" / "A scholarship would be nice, but we don't necessarily need it" / "We'll need significant scholarship help") To (no field): First Name, Phone, Email, consent, "Send Me the SAT Roadmap >>". Ask the scholarship question in the qualification survey after opt-in.
Why: Playbook, Setting up your forms: "Pre-qualifier (only for niche markets with plenty of leads; not for competitive ones like college consulting, SAT/ACT, fitness)" and "B2C: never mention money ('It is a complete drop off moment')". Option 1 says "invest". It also adds about 230px on a phone between Email and the button. Watch pre-qualified and qualified counts in GHL along with LPCR.

**T3. Headline and sub: match the ad.**
Change "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." To "Free SAT Roadmap: Add 300+ Points Before the Next Test".
Change "No long, generic grind. Just focused practice on the exact points holding them back." To "How to finally make sense of the SAT: which test date, which prep, and the exact system that removes the guesswork."
Why: "Free SAT Roadmap: Add 300+ Points Before the Next Test" is the headline on every live ad, and "How to Finally Make Sense of the SAT" is the hook on the creative with 97.6% of spend. Neither is on the first screen. Playbook: "headline/offer must match the ad".

**T4. Card: the ad's checklist as "what's inside".**
Change "Enter your information below and we'll send you a one-pager on how this system works." To:
"✓ Understand why smart kids still get stuck on the SAT
✓ See which test date and prep actually fit your child
✓ Learn the exact system that removes the guesswork
✓ Discover how Zinkerz students add 300+ points"
Why: these are the video's own lines, so the visitor sees the same card they just clicked. I left out "in 90 days" from the 4th line: the profile has no timeframe, so it needs Carlos's OK before it goes on the page twice.

**T5. Phone layout: fields on the first screen.**
Change: on 390x844 the first screen shows the logo bar (about 145px), the call-out, headline, sub, a large empty gap, the italic guarantee line, another gap, and the card title. The First Name box starts about 760px down and the button about 1,480px down.
To: logo bar about half height, remove both empty gaps, guarantee as one line right above the button, card title only ("Get the Free SAT Roadmap"). Goal: First Name, Phone and Email visible on the first screen (with T2, the button sits right under Email).
Why: Process: "Mobile: is the form visible without scrolling? (Most traffic is Instagram on phones.)" Playbook: "Pages give leads 2 options: take the action or LEAVE... very simple."

**T6. Proof next to the button.**
Change: stats bar and "Our Wall of Love" start below the form, with "Mikaela / SAT STUDENT" first and the PARENTS reviews third and fourth, no scores.
To: one line under the button: "Our students average a 310+ point jump. 100% Early Action / Early Decision admits in 2025." Move "Laura & Martin" and "Andres & Luciana" (PARENTS) to the top of the wall.
Why: "Our students average a 310+ point jump" is in the live ad copy and the profile ("310+ score improvement", "All students in 2025 admitted in early action/decision"). Process: "Proof near the form: results with real numbers, parent reviews first when parents are the buyer." I did not reuse "Mikaela went from 1260 to 1530" / "Andre went from 1100 to 1500": they were on the Simple Text ad, which is now paused, and are not in the profile.

**Run plan:** about 150 link clicks a week (sheet, Oct 12-18, budget now $80/day), so about 14 days per test at 150 visitors per version. Order: call T1 today, then T2 alone (14 days, it changes lead quality), then bundle T3 + T4 + T5 into one B version (14 days, all "make the page match the ad"), then T6 (14 days). Clarity labels: `clarity("set","variant","T2-A")` / `"T2-B"`, then T3-A / T3-B for the bundle, then T6-A / T6-B. Comment in the sheet on the day each goes live.

## NEED FROM EMA

- **T1 result:** Clarity dashboard filtered by custom tag variant = T1-A vs T1-B since Oct 7 (sessions and clicks on the form submit), or the GHL opt-in list with the page URL each lead came from. The sheet does not split leads by variant, and I have no Clarity or GHL access.
- **Guarantee:** Carlos's real term: "keep coaching until your child hits their target score, no extra cost" (ad) or "a free intensive session" (page).
- **"300+ points in 90 days"** and **"5,000+ SAT Students Taught"**: where these come from, or OK to drop.
- **Oct 13:** is "6 leads from 16 clicks" one day, or a catch-up of earlier leads? It changes the 7-day number from 10.5% to 7.4%.
- **Video audio:** the notes checklist video files I could download had no audio track. If it has a voiceover, send the script or the file.
- **Lead event:** a test submission (I did not submit the form) and a look at Events Manager to confirm Lead fires on submit.
- **GHL funnel stats** for /squeeze-page and /squeeze-page-538225 (views and opt-ins per step).
- **Real phones:** 2 or 3 Clarity recordings to confirm the form now shows in about 1 to 2 seconds.

---

## Appendix: facts pulled

- Sheet daily (Oct 12-18, spend / clicks / leads / pre-qualified): 10-12 $103.51 / 37 / 1 / 0; 10-13 $81.31 / 16 / 6 / 2; 10-14 $97.60 / 15 / 1 / 0; 10-15 $117.57 / 24 / 3 / 1; 10-16 $93.73 / 23 / 3 / 1; 10-17 $57.00 / 18 / 0 / 0; 10-18 $94.64 / 19 / 2 / 1.
- Sheet comments Oct: 10-01 "A/B testing free 300-point roadmap vs. free one pager"; 10-07 "launched new ads" / "new A/B test LP too"; 10-15 "dropped budget to 80".
- Months (Dash, LPCR = Lead / Link Clicks): Jun 4.3%, Jul 3.5%, Aug 8.5%, Sep 4.2%, Oct to date 6.7%.
- Meta daily, notes checklist (clicks / LPVs / leads): 10-12 8/7/0, 10-13 8/9/2, 10-14 13/11/0, 10-15 28/25/1, 10-16 23/19/5, 10-17 17/18/0, 10-18 18/14/2.
- Ad copy: all main-campaign ads use the same primary text: "If your child is preparing for the SAT and the score isn't where it needs to be - grab this free one-pager. It breaks down how Zinkerz students add 300+ points through 1:1 coaching, weekly mock exams, and a plan built around each student's specific gaps. Our students average a 310+ point jump, and we keep coaching until your child hits their target score - no extra cost. 📄 Get the free one-pager: The SAT Roadmap - How to Add 300+ Points Before Your Next Test Date 📞 Then book your SAT Score Breakthrough Session. 👇 Start with the free one-pager." CTA: Learn more. Creative names: notes checklist = "Tried SAT Prep Already and the Score Didn't Move - Here's What Was Actually Missing"; Black Notes 1,2,3 = "Already Paid for SAT Prep? Get the Free 300-Point Roadmap".
- Page copy (both variants identical except the call-out): T1-A "FOR PARENTS OF HIGH-ACHIEVING STUDENTS", T1-B "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET". Then the headline, sub and italic line quoted above; "📄 Free SAT Roadmap / Get My 300-Point Roadmap / Enter your information below and we'll send you a one-pager on how this system works. / 🔒 Your information is 100% secure and never shared"; stats "+6 Avg. ACT Point Increase", "310+ Point Average Improvement", "5,000+ SAT Students Taught", "100% Early Action / Early Decision Rate (2025)"; "Our Wall of Love", "5.0 Rating · 5,000+ Students Taught", 6 text reviews and YouTube videos, "See More Stories", "Ready to get your free one-pager?", "Get Your Free One-Pager >>", footer.
- Profile: offer "We help high school students improve their SAT scores through personalized 1:1 coaching and structured accountability systems, with qualifying students averaging +310 points of combined score improvement in 2025." No guarantee listed. Proof: 310+ online, 350+ camp, 100% EA/ED admits 2025, ~400 active students. Buyer: parents. Qualified: can afford US college, private school, HNW.
- Playbook rules used: pre-qualifier not for SAT/ACT; "B2C: never mention money"; "If CPL is already $45-50, don't" (3d CPL $49.07); "Headline = the offer... same on every page"; "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short"; "Pages give leads 2 options: take the action or LEAVE"; "Terms and privacy policy links in every footer"; parents get the "roadmap / one-pager" version.
- Could not get: T1 per-variant results (no Clarity/GHL access, sheet not split); video audio (download had no audio track); `ads_get_creatives` returned no body/title/link (used the ad previews instead); no form submission (read-only); GHL funnel stats not tried; speed measured in headless Chrome only.
