# LPCR page review: Zinkerz (Carlos Hafeitz), Oct 14 2026

**Verdict:** The form still asks a money question ("partial-scholarship spots... We're good to invest") that the playbook bans for SAT prep at a $54 CPL. The page also sells "Give Us 90 Days" while the top ad (69% of spend) sells the "Free SAT Roadmap" one-pager. LPCR has improved to 6.8% over the last 7 days (it was 4.9% the week before), but the goal is 20%.

## LPCR (sheet, Lead / Link Clicks)

| Window | Leads / clicks | LPCR | Spend | CPL |
|---|---|---|---|---|
| Last 7 days (Oct 7 to 13) | 13 / 190 | **6.8%** | $704.45 | $54.19 |
| Last 3 days (Oct 11 to 13) | 9 / 91 | **9.9%** | $316.45 | $35.16 |
| Week before (Sep 30 to Oct 6) | 7 / 142 | 4.9% | $700.65 | $100.09 |
| Best month 2026: **August** | 52 / 610 | **8.5%** | $1,798.41 | $34.58 |

- The 3-day number leans on one day. Oct 13 logged 6 leads from 16 clicks. Oct 11 and 12 together were 3 / 75 (4.0%). Check that Oct 13 is a real single day before reading too much into it.
- When it dropped: at the relaunch on 2026-09-05 (the sheet comment says "relaunched"). September came in at 4.2%. It went up after 2026-10-07 ("launched new ads", "new A/B test LP too"), so the new notes checklist ad and the T1 call-out test went live together.

## Live ads (Meta, main campaign "OLead//FreeTraining//US", ACTIVE, last 7 days)

| Ad | Spend | Link clicks | LPVs | Meta leads | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| PP5 Simple Text (static) | $473.37 | 160 | 132 | 3 | 68.6% | 82.5% | 1.9% |
| PP5 notes checklist (video, new Oct 7) | $190.81 | 37 | 34 | 2 | 27.7% | 91.9% | 5.4% |
| PP5 black notes reminder (static) | $16.18 | 2 | 0 | 0 | 2.3% | 0% | 0% |
| PP5 Black Notes 1,2,3 (static) | $9.36 | 0 | 1 | 0 | 1.4% | n/a | n/a |
| **Total** | **$689.72** | **199** | **167** | **5** | 100% | **83.9%** | **2.5%** |

- All 4 ads use the same primary text and the same headline: "Free SAT Roadmap: Add 300+ Points Before the Next Test". Only the creative differs.
- Retargeting ("Hammer Them Retargeting", Obj 1 to 5) spent $34.38 in the same 7 days. I left it out of the page match, as you asked.
- Load rate is fine at 84% (just above the ~80% line).
- Meta counts 5 leads. The sheet counts 13 for the same days (Meta sees 38% of them). Judge LPCR on the sheet.

## Fix first (broken things, not tests)

1. **The guarantee says three different things.** Ad: "we keep coaching until your child hits their target score - no extra cost." Black Notes 1,2,3 creative: "stays accountable until the score moves". Page: "..if they don't hit their target, we'll run a free intensive session on us". The client profile lists no guarantee. Get the real terms from Carlos, then use the same words in the ads and on the page.
2. **The form shows up late.** In 8 of 8 phone loads (headless Chrome), the page text showed in about 1 second, but the form fields stayed hidden for about **7 to 9 seconds**. Until then the card only shows "Get My 300-Point Roadmap / Enter your information below..." with nothing to fill in. Twice the form was still hidden when I took the screenshot. The form also loads a Cloudflare captcha (a hidden "cf-turnstile-response" field). Watch a few Clarity recordings on real phones. If the blank card shows up there too, check the GHL form's captcha/spam setting with the GHL team.
3. **ACT stat on an SAT page.** The stats bar opens with "+6 Avg. ACT Point Increase". Remove it. "100% Early Action / Early Decision Rate (2025)" is backed by the profile and can stay.
4. **"5,000+ SAT Students Taught" / "5,000+ Students Taught".** The profile only says "~400" active students. It may be a lifetime number. Confirm it with Carlos or remove it.
5. **No Terms link in the footer.** The footer only has "Copyrights 2026 | Zinkerz™ | Privacy Policy". Playbook: "Terms and privacy policy links in every footer (required by Facebook...)".
6. **Meta tracking.** Meta shows 5 leads, the sheet shows 13. Check whether Lead fires on the form or on the next page.
7. **Let T1 finish.** Both variants are live and tagged: /squeeze-page-538225 = "FOR PARENTS OF HIGH-ACHIEVING STUDENTS" (`clarity("set","variant","T1-A")`), /squeeze-page = "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET" (`T1-B`). /access returns a 302 to one variant and keeps the UTMs. Everything else on both pages is the same. About 190 clicks since Oct 7, so roughly 95 per version. It needs about 150 per version.

## 5 A/B tests (biggest expected lift first)

Labels start at T2 because T1 (call-out) is still running.

### T2. Form: remove the scholarship pre-qualifier
- **Change:** 4th required field "We keep a few partial-scholarship spots each cohort for families who need a little help getting started. Which sounds like you? *" with "We're good to invest in the right program for our child" / "A scholarship would be nice, but we don't necessarily need it" / "We'll need significant scholarship help"
- **To:** (field removed) First Name, Phone, Email, consent box, button. Move the scholarship question into the qualification survey after the opt-in.
- **Why:** Playbook, Setting up your forms: "Pre-qualifier (only for niche markets with plenty of leads; not for competitive ones like college consulting, SAT/ACT, fitness)". Conversion Ads: "If CPL is already $45-50, don't". CPL over the last 7 days is $54.19. "B2C: never mention money... It is a complete drop off moment", and option 1 says "invest". On a phone the radio question takes up about 230px between the email field and the button.

### T3. Headline: same offer as the top ad
- **Change:** "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." / sub: "No long, generic grind. Just focused practice on the exact points holding them back."
- **To:** "Free SAT Roadmap: Add 300+ Points Before the Next Test" / sub: "Your kid isn't the problem. The process is a mess. Get the free one-pager that shows how Zinkerz students add 300+ points through 1:1 coaching, weekly mock exams, and a plan built around each student's specific gaps."
- **Why:** Every live ad's headline is "Free SAT Roadmap: Add 300+ Points Before the Next Test". The top ad (Simple Text, 68.6% of spend) opens with "Your kid isn't the problem. The process is a mess." Neither appears on the first screen. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Note: the new notes checklist ad (27.7%) does say "Discover how students add 300+ points in 90 days", so "90 days" is only in the smaller ad. If Ema wants to keep it, B2 could be "Free SAT Roadmap: How Students Add 300+ Points in 90 Days". I recommend the first version because it matches the ad with the most spend.

### T4. Mobile: form fields and button higher up
- **Change:** On a 390x844 phone, the first screen shows the logo bar, call-out, headline, sub, the italic guarantee line, a big gap, then the card with only the First Name field. Phone starts at about 853px, Email at about 954px, and the "Get Started >>" button at about 1,540px (almost 2 screens down).
- **To:** Thin logo bar (about half the height). Remove the empty space above and below the italic line. Put the guarantee in one line directly above the button. Inside the card, keep "Get the Free SAT Roadmap" and cut "Enter your information below and we'll send you a one-pager on how this system works." With T2's field removed, the goal is First Name, Phone and Email on the first screen and the button right after.
- **Why:** Process: "Mobile: is the form visible without scrolling? (Most traffic is Instagram on phones.)" Playbook: "Pages give leads 2 options: take the action or LEAVE... very simple."

### T5. Proof: the ad's score results right under the button
- **Change:** No reviews with scores. The first review is "With flexible scheduling, intense marathons, and expert support, I stayed on track and maximized my prep..." (Mikaela, SAT STUDENT). Parent reviews come third and fourth.
- **To:** Directly under the button: "Mikaela went from 1260 to 1530 → admitted to Vanderbilt. Andre went from 1100 to 1500 → admitted to NYU. Our students average a 310+ point jump." In "Our Wall of Love", move "Laura & Martin" and "Andres & Luciana" (PARENTS) to the top.
- **Why:** These are the exact results on the top ad's creative, and the 310+ line is from the ad copy (the profile backs "310+ score improvement"). Process: "Proof near the form: results with real numbers, parent reviews first when parents are the buyer." Buyers are parents (profile).

### T6. One name for the freebie, a clear button, and a preview image
- **Change:** "Get My 300-Point Roadmap" (card title), "Get Started >>" (form button), "Get Your Free One-Pager >>" (bottom button). No image of the one-pager.
- **To:** Card title "Get the Free SAT Roadmap". Form button "Send Me the SAT Roadmap". Bottom button "Send Me the SAT Roadmap". Add a tilted image of the one-pager's first page above the card.
- **Why:** The ads call it "The SAT Roadmap" and the checklist video ends with "Get the free SAT roadmap 👇". Process: "Button text says what they get (not 'Get Started' / 'Submit'). One name for the freebie everywhere." The playbook squeeze page elements include a preview of the freebie.

## How to run them

- **Traffic:** about 190 link clicks a week (sheet, Oct 7 to 13). At about 150 visitors per version (300 per test), each test takes about **11 days**.
- **Order:**
  1. Let T1 finish. It needs about 110 more clicks, so 4 to 6 more days (around Oct 19). Keep the winner.
  2. **T2 alone** (about 11 days). It is the biggest change and affects lead quality, so check pre-qualified and qualified counts in GHL along with LPCR.
  3. **Bundle T3 + T4 + T6 into one B version** (headline, mobile layout, freebie name/button/image). These all make the page match the ad. About 11 days.
  4. **T5** last, about 11 days.
- **Clarity labels:** use the same script format as T1: `clarity("set","variant","T2-A")` / `"T2-B"`, then `T3-A` / `T3-B` for the bundle, then `T5-A` / `T5-B`.
- **When to call it** (sheet's LP AB test tab): "at about 150+ visits per version, if one version is ahead by 3+ percentage points... If it's closer than that, keep it running another week." Comment in the sheet on the day each change goes live.

## Questions for Ema / Carlos

1. What is the real guarantee: "keep coaching until they hit their target score, no extra cost", "stays accountable until the score moves", or "a free intensive session"?
2. Is "300+ points in 90 days" a real number Carlos can back up? It's in the checklist ad and the page headline, but the profile has no timeframe.
3. Oct 13 shows 6 leads from 16 clicks. Is that one day, or were leads from earlier days logged that day?
4. Where is "5,000+ SAT Students Taught" from? Can "+6 Avg. ACT Point Increase" come off?
5. Is the Lead pixel on the form or on the next page? (Meta 5 vs sheet 13.)
6. Do Clarity recordings on phones show the empty form card for several seconds?

---

## Appendix: Facts pulled

### Sheet "(ZK) - Business Reporting Daily 2026"
- Tabs used: daily month tabs Jun to Oct (A Month/date, B Adspend (USD), E Link Clicks, H Lead, I Pre-Qualified Leads). Dash tab (I = LPCR) for months. LPCR = Lead / Link Clicks. Downloaded as .xlsx and parsed. Filled through Oct 13.
- Daily, Oct 7 to 13 (spend, clicks, leads, pre-qualified): 10-07 $122.41 / 27 / 1 / 1; 10-08 $99.99 / 26 / 1 / 0; 10-09 $79.73 / 26 / 1 / 0; 10-10 $85.87 / 20 / 1 / 0; 10-11 $131.63 / 38 / 2 / 2; 10-12 $103.51 / 37 / 1 / 0; 10-13 $81.31 / 16 / 6 / 2.
- 7d: 13 leads, 5 pre-qualified. 3d: 9 leads, 4 pre-qualified.
- Months: Jun 4.3% (121/2,801), Jul 3.5% (358/10,185), **Aug 8.5% (52/610)**, Sep 4.2% (52/1,252), Oct to date 5.9% (18/303).
- Sheet comments: 09-04 "relaunched"; 09-09 "made smal changes to LP"; 09-24 "added LAL"; 10-01 "A/B testing free 300-point roadmap vs. free one pager"; 10-07 "launched new ads" / "new A/B test LP too". (Earlier ones are in the Oct 12 review: 07-03 "added prequalifier about scholarship", 08-04 "also removed the urgency qualification".)
- LP AB test tab: T1-A "FOR PARENTS OF HIGH-ACHIEVING STUDENTS." / T1-B "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET.", plus ideas for a guarantee badge, score reviews and one freebie name. No per-variant results logged.

### Live ad copy (from ad previews, all 4 PP5 ads use the same text)
- Primary text: "If your child is preparing for the SAT and the score isn't where it needs to be - grab this free one-pager. It breaks down how Zinkerz students add 300+ points through 1:1 coaching, weekly mock exams, and a plan built around each student's specific gaps. Our students average a 310+ point jump, and we keep coaching until your child hits their target score - no extra cost. 📄 Get the free one-pager: The SAT Roadmap - How to Add 300+ Points Before Your Next Test Date 📞 Then book your SAT Score Breakthrough Session. 👇 Start with the free one-pager."
- Headline: "Free SAT Roadmap: Add 300+ Points Before the Next Test". CTA: Learn more.
- **Simple Text** image (downloaded and viewed): "To parents of a high school student prepping for the SAT: Your kid isn't the problem. The process is a mess. Which prep, which test date, how many times to sit it, nobody gives you a straight answer, and the clock keeps running. Students who get a program built around them are seeing real results: Mikaela went from 1260 to 1530 → admitted to Vanderbilt / Andre went from 1100 to 1500 → admitted to NYU. All with 1:1 coaching built around their specific gaps. The next test is just weeks away."
- **Notes checklist** video (22 seconds, frames viewed): Notes app card over b-roll: "How to Finally Make Sense of the SAT: ✓ Understand why smart kids still get stuck on the SAT ✓ See which test date and prep actually fit your child ✓ Learn the exact system that removes the guesswork ✓ Discover how students add 300+ points in 90 days. Get the free SAT roadmap 👇". The same card stays on screen for the whole clip.
- **Black notes reminder** image: "Don't let another test date sneak up on you. Stop guessing which prep, which date, how many times. Nobody gives parents a straight answer on the SAT, so a capable kid ends up with a number that doesn't match them, and you're left piecing it together alone. There's a clearer way, and it starts with one plan built around your child."
- **Black Notes 1,2,3** image: "Confused about your kid's SAT plan? Here's how we fix that: 1 - Pinpoint exactly which test date, which prep, and what score your child actually needs 2 - Build a plan around your child's exact gaps, not generic advice for 20 other kids 3 - One team that runs the diagnostic, builds the plan, and stays accountable until the score moves. Click below to learn more 👇"
- Landing link: sites.zinkerz.com/access (UTMs like utm_content=pp5simpletext). It returns a 302 to /squeeze-page or /squeeze-page-538225 and keeps the UTMs.

### Page copy (both variants loaded 2026-10-14)
- Call-out: T1-A "FOR PARENTS OF HIGH-ACHIEVING STUDENTS" / T1-B "FOR PARENTS WHOSE TEEN'S SAT SCORE ISN'T THERE YET". Everything else is identical.
- Headline: "Give Us 90 Days and We'll Help Your Teen Jump 300+ Points on the SAT." Sub: "No long, generic grind. Just focused practice on the exact points holding them back." Italic: "..if they don't hit their target, we'll run a free intensive session on us".
- Card: "📄 Free SAT Roadmap" / "Get My 300-Point Roadmap" / "Enter your information below and we'll send you a one-pager on how this system works." / "🔒 Your information is 100% secure and never shared".
- Form (GHL OJl5wq0yL7h0wbLkL9P5, unchanged since Oct 12): First Name *, Phone * (defaults to United States +1, matches the US campaign), Email *, scholarship radio question * (3 options), consent checkbox "I consent to receive emails and SMS messages regarding my submission and related updates.", button "Get Started >>". No prefilled or test data. No dropdowns.
- Stats: "+6 Avg. ACT Point Increase", "310+ Point Average Improvement", "5,000+ SAT Students Taught", "100% Early Action / Early Decision Rate (2025)".
- "Our Wall of Love", "5.0 Rating · 5,000+ Students Taught", 6 text reviews (Mikaela, Gaby, Laura & Martin, Andres & Luciana, Brian, Daniel) with no scores, plus 6 YouTube videos.
- Bottom: "Ready to get your free one-pager?" / "Get Your Free One-Pager >>". Footer: "Copyrights 2026 | Zinkerz™ | Privacy Policy".
- Speed: HTML loads in about 0.4s. Text shows in about 1.1 to 1.7s. Form fields became visible after about 7 to 9s (8 phone runs). The full "load" event takes 17 to 22s because of the 6 YouTube embeds.
- Screenshots: zinkerz-desktop.png and zinkerz-mobile.png in the scratchpad (taken 12s after load, form showing). Desktop 1440x900: First Name and Phone visible, Email cut off, button below the fold. Mobile 390x844: only First Name visible, button about 1,540px down.

### Client profile facts
- Offer (SAT): "We help high school students improve their SAT scores through personalized 1:1 coaching and structured accountability systems, with qualifying students averaging +310 points of combined score improvement in 2025." $100-150/hr, about 4 sessions a week.
- Guarantee: **none listed.** Stats line: "SAT Camp, 350+ score improvement SAT online prep 310+ score improvement All students in 2025 admitted in early action/decision Free consultation free readiness assessment".
- Proof: 310+ average (online), 350+ (camp), 100% EA/ED admits in 2025, about 400 active students. No "90 days" and no "5,000+" in the profile.
- Buyer: parents (students under 18). US markets: Northeast (Boston, NYC, New Jersey), South Florida, Miami.
- Qualified lead: "Can afford college in the US", understands the SAT and US college basics, "Goes to a private school", "HNW families".

### Playbook rules relied on
- "Pre-qualifier (only for niche markets with plenty of leads; not for competitive ones like college consulting, SAT/ACT, fitness)"
- "If CPL is already $45-50, don't" (Conversion Ads, pre-qualifiers)
- "B2C: never mention money ('It is a complete drop off moment')"
- "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page."
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- "Pages give leads 2 options: take the action or LEAVE. No menu bar, very simple."
- "Terms and privacy policy links in every footer"
- "Parents/test prep/college prep: use the more direct roadmap / one-pager version"
- "DO NOT USE FACEBOOK TO TELL YOU HOW MANY LEADS YOU GOT..."

### What I could NOT get
- `ads_get_creatives` again returned no body, title or link_url (even when I named the fields). I took the copy from ad previews (Instagram and Facebook feed) and downloaded the images through the preview pages.
- The previews had no outbound link, so I used the /access link from the Oct 12 review and checked that it still redirects to both variants.
- The notes checklist video would not play in the preview. I matched it to the account video "(ZK) ads.mp4" (22s, uploaded 2026-10-07, the day the ad launched) and read its frames. That match is by date, not confirmed through the creative's video_id.
- T1 results per variant: the sheet does not split leads by variant, and I have no Clarity or GHL access from here.
- GHL funnel stats: not tried.
- The form delay was measured in headless Chrome. Real phones may be faster or slower.
