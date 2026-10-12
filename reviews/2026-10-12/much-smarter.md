# LPCR page review: Much Smarter ("The Game", 30-day free trial)

**Verdict:** The ad talks to parents about a teen who freezes on test day and offers "Free for 30 Days". The page opens with "For SAT & ACT Students Only" and a headline about tests being games. The offer, the form and the proof all sit lower down or behind a button. On top of that, 1 in 3 clicks never loads the page. LPCR is 4.1% against a 20% goal.

Data caveat: the campaign started 2026-10-08, so this is 4 days, 74 clicks and 3 leads. The gap to 20% is big enough to act on, but expect the numbers to move.

## Live ads (Meta, last 14 days, ACTIVE only)

| Ad | Spend | Link clicks | LPVs | Leads (Meta) | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| P4 Black notes checklist ("Bad at Standardized Tests") | $117.61 | 39 | 29 | 2 | 56% | 74% | 5.1% |
| P5 Black notes checklist (SAT/ACT Math) | $39.03 | 25 | 14 | 0 | 19% | 56% | 0% |
| P3 Black notes checklist (tried tutoring, still stuck) | $27.96 | 11 | 6 | 0 | 13% | 55% | 0% |
| P1 Black notes checklist (smart teens who freeze) | $21.25 | 3 | 3 | 0 | 10% | 100% | 0% |
| P2 Black notes checklist | $3.82 | 0 | 0 | 0 | 2% | n/a | n/a |
| **Total** | **$209.67** | **78** | **52** | **2** | 100% | **67%** | **2.6%** |

- The sheet logs $209.28, 74 clicks and 3 leads (LPCR 4.1%). Meta counts 2 leads, so the two sources are close and tracking looks fine. I judge LPCR on the sheet number.
- Cost per lead on the sheet is $69.76. The sheet's own max is $45. CPM is $33.37 (target under $30). CTR is 1.18% (target over 1%), so the ads get clicks and the drop happens after the click.

## Fix first (broken things, not tests)

1. **Load rate is 67% (flag, under 80%).** P5 loads 56% and P3 loads 55%. The first screen has an 11 MB MP4 that autoplays muted and has no poster image, so it shows as a grey box until it loads. Compress the video, add a poster frame, and check page speed on a phone over 4G. This could cost more leads than any copy change.
2. **"No credit card" does not match the funnel.** All 5 ads say "No credit card. No commitment. No pressure." Step 2 of the funnel (/login) says "Secure checkout", "Won't be charged today", and the GHL funnel has "requireCreditCard": true. The strategy doc says "no credit card charge until the trial ends". This hurts trial starts more than LPCR, but parents who feel misled will not finish. Ema and the client should decide which wording is true and use it everywhere. Nurture Email 1 also says "No credit card".
3. **"1400+ SAT" has no proof behind it.** The ad headline is "From Test Anxiety to 1400+ SAT - Free for 30 Days". No doc I read has a 1400+ SAT result. All score proof on the page is ACT ("Reading: 21 → 31", "Math: under 25% correct → 25", "34 ACT"). The strategy doc also crossed out the score angle ("1400+ SAT / 31+ ACT is closer than you think"). Confirm with the client, or drop the number.
4. **The ad testimonials are not on the page and I could not verify them.** The ad says: "My child walked into the SAT relaxed for the first time ever." "He finally believed he wasn't bad at tests." I only found these in the strategy doc's ad copy draft, with no name or source. Confirm they are real before reusing them anywhere.
5. **Check that the form actually blocks empty fields.** The labels show "First Name *", "Phone *" and "Email *", but none of the inputs has the HTML `required` attribute. GHL may still check them on submit. Test it with one dummy submission. I stayed read-only and did not submit anything.
6. **The "Real Results" scrolling strip cuts off on mobile.** In the 390px screenshot it reads "25% correct → 25" and "ACT: hopeles...". Make it a static 3-line block (see T3).

## 5 A/B tests (biggest expected lift first)

### T1. Parent call-out + offer headline
- **A (now):** "For SAT & ACT Students Only" / "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." / "Watch how MuchSmarter's game-based system turns test-day panic into a repeatable, learnable skill - then grab your teen's free 30-day trial below."
- **B:** Call-out: "For parents of smart teens who freeze up on the SAT or ACT" / Headline: "The SAT & ACT Are Games. Teach Your Teen to Win, Free for 30 Days." / Subheadline: "MuchSmarter's game-based system turns test-day panic into a skill your teen can learn. Start the free 30-day trial below."
- **Why:** All 5 creatives open with "Parents of Teens Who...", and the primary text opens with "ATTENTION: Parents of teens who freeze up on the SAT/ACT". The page says students only. Playbook: "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page", plus "Call-out line on the first 3 pages, kept to one line". The B headline is adapted from the client's own strategy headline: "The SAT/ACT Is a Game. Teach Your Teen to Win It."

### T2. Form on the first screen vs form behind a button
- **A (now):** The "Start My Free Trial" button opens a pop-up with First Name, Phone, Email, a consent box and "Start My Free 30-Day Trial". On mobile, the button sits at the bottom of the first screen (about 690px down) and the form is one tap away.
- **B:** Put the same form inline, right under the subheadline. First name and phone side by side, email full width, the consent box, then the button "Start My Free 30-Day Trial". On desktop, put the video to the left of the form. On mobile, put the video below the form.
- **Why:** Playbook squeeze page elements: "short form". Opt-in form: "first name + phone (two columns), email full width". The extra tap on a pop-up is friction for cold Instagram traffic. Keep the pop-up for the buttons lower on the page.

### T3. Trial proof next to the form
- **A (now):** A scrolling "Real Results" strip below the "What's included" list. The reviews block is mostly 1:1 tutoring stories ("Steve worked with me for 6 months", "Five months of tutoring", "He met with us for an hour, free of charge"), and the first parent review appears 7th.
- **B:** A static block directly under the form button:
  "Real results from MuchSmarter students:
  Reading: 21 → 31 (Jake E., ACT)
  Math: under 25% correct → 25 (Chris C., ACT)
  34 ACT (Nicky B.)"
  Then move the two parent reviews already on the page to the top of the reviews block: Victoria R. ("My son Bryce told me he learned more in an hour and a half than in the past six months with his previous math tutor.") and Sabrina's Parent.
- **Why:** Playbook: "Proof near the form: results with real numbers, parent reviews first when parents are the buyer." Each proof line here is already on the page and in the strategy doc's nurture emails. The P5 math ad and the P3 "already tried tutoring" ad both match Chris C. and Victoria R.

### T4. Light video preview vs heavy autoplay video
- **A (now):** An 11 MB MP4 that autoplays muted, with no poster, so it shows as a grey box with "0:00".
- **B:** A 10-second preview GIF of Steve inside the platform, with the caption "Take a 5-minute look inside with Steve, founder of MuchSmarter". Tapping it opens the form pop-up. Play the full video after the opt-in (on the trial or thank-you step).
- **Why:** Playbook squeeze page elements: "VSL preview GIF (10-second clip in the Canva GIF frame, quality ~0.4...)". The strategy doc places Steve's sneak peek after the form ("You just filled out your information..."). This should also lift the 67% load rate. Only run it after Fix 1 if Fix 1 alone does not bring load rate above 80%.

### T5. Risk reversal under the main button
- **A (now):** "Cancel anytime in 2 clicks. We'll remind you before your trial ends." This appears only inside the pop-up, after the click.
- **B:** Under every "Start My Free Trial" button on the page: "Free for 30 days. Won't be charged today. Cancel anytime in 2 clicks."
- **Why:** The ads promise "No commitment. No pressure." and the page shows no risk reversal before the click. Every phrase in B is already used in the live funnel (pop-up and step 2). There is no money-back guarantee in any doc, so do not add one.

## How to run them

- **Traffic:** about 18.5 link clicks a day (74 in 4 days), so about 130 clicks a week. At a 67% load rate that is about 87 real visitors a week.
- **Time per test:** about 150 visitors per version means 300 per test. That is about 2.3 weeks on clicks, or about 3.5 weeks on real visitors. Running 5 single tests in a row would take 3 to 4 months, which is too slow.
- **Bundle (low traffic):**
  - Before any test: do Fix 1 (video weight and poster) and recheck the load rate after 3 days.
  - **Round 1 (about 3 weeks):** A = current page. B = T1 + T2 + T5 together (new first screen: parent call-out, offer headline, inline form, risk line). This is the biggest expected lift.
  - **Round 2 (about 3 weeks):** The winner of Round 1 as A. B = winner + T3 + T4 (proof block and video preview).
  - If budget goes up to $100 a day or more, split the bundles back into single tests to learn which part did the work.
- **Setup:** Use a GHL split test on the "Start Trial" step of "THE GAME FUNNEL" (split is off right now). Microsoft Clarity is already on this funnel (project uhr8ka2z10). Tag the versions in Clarity: R1-A / R1-B (T1+T2+T5), then R2-A / R2-B (T3+T4). If you split them later, use T1-A / T1-B through T5-A / T5-B.
- **Judge on** sheet leads ÷ link clicks per version, plus trial starts (step 2) so a cheaper opt-in does not hide fewer trials.

## Questions for Ema or the client

1. Is the ad link go.muchsmarter.com/start-trial? Meta did not return the link_url, so I took the URL from step 1 of the GHL "THE GAME FUNNEL".
2. Does the trial take a card or not? The ads and Email 1 say "No credit card". Step 2 says "Secure checkout... Won't be charged today".
3. Is there a real student behind "1400+ SAT"? Are the two ad quotes ("relaxed for the first time ever", "wasn't bad at tests") from real parents, and can we name them?
4. Is the page video Steve's sneak peek from the strategy doc? How long is it? Did he record the case study and trial-vs-paid sections?
5. Should the reviews about 1:1 tutoring (Steve, Tom Schecter, "Five months of tutoring") stay on a $40/month self-serve trial page? They could make parents think a tutor is included.
6. Is the US the only target country? The phone field defaults to the US flag.
7. There is no client profile in "00. Client Profiles (Claude)". Can we build one (offer, real guarantee terms, approved proof, ICP)?

---

## Appendix: Facts pulled

### LPCR (sheet)
- **Source:** "(MS) - Business Reporting B2C - TheGame" (fileId 1xFKdhYq...), tab "Oct", columns E "Link Clicks" and H "Lead". The tab says "Link Clicks", so I cannot tell whether these are unique clicks.
- Daily rows: Oct 8: 14 clicks / 1 lead. Oct 9: 19 / 0. Oct 10: 16 / 1. Oct 11: 25 / 1. Oct 1 to 7 are empty because the campaign had not started.
- **Last 7 days (Oct 5 to 11):** 3 / 74 = **4.1%**. Only 4 days had spend.
- **Last 3 days (Oct 9 to 11):** 2 / 60 = **3.3%**.
- **Best month of 2026:** this sheet has no history before October. The older sheet "(MS) - Business Reporting Daily 2026" (fileId 1IJC5zP6..., Dash tab, Link Clicks and Lead columns) covers a different offer, the 1:1 coaching free training funnel (/book-now). It shows Jan 6/228 = 2.6%, **Feb 14/138 = 10.1% (best)**, Mar 24/541 = 4.4%, Apr 19/414 = 4.6%. Logging stops on Apr 14. Even the best month there was under 15%.
- **When it dropped:** there is no drop to date. "The Game" has been under 5% since day 1 (Oct 8).
- Other October numbers: spend $209.28, CPM $33.37, CTR 1.18%, CPC $2.83, CPL $69.76. Free trial starts and paid subs are both 0.

### Ad copy (identical for all 5 live ads)
- **Headline (title):** "From Test Anxiety to 1400+ SAT - Free for 30 Days"
- **CTA:** Learn More
- **Primary text (key lines):** "ATTENTION: Parents of teens who freeze up on the SAT/ACT" / "Your teen is smart. You know it. Their teachers know it." / "But on test day - something shuts down." / "It's a strategy problem." / "🎮 Step 1: Claim your free 30-day trial of MuchSmarter" / "✔️ 150+ training videos broken down by skill and question type" / "✔️ Mixed practice sections..." / "✔️ Full-length practice tests..." / "✔️ MyGame mindset training to beat anxiety under pressure" / "✔️ Weekly live coaching sessions with expert instructors" / "No credit card. No commitment. No pressure." / "Just a proven system - free for 30 days." / "Parents tell us: 'My child walked into the SAT relaxed for the first time ever.' 'He finally believed he wasn't bad at tests.'" / "👇 Click below to start your free 30-day trial."
- **Creatives (black notes-app checklist, each with "Try our game-based system free for 30 days" and "Start your FREE trial today"):**
  - P4: "Parents of Teens Who've Decided They're Just 'Bad at Standardized Tests':"
  - P5: "Parents of Teens Who Struggle With SAT / ACT Math:" ("Heal years of 'math wounds'...")
  - P3: "Parents of Teens Who've Already Tried Test Prep / Tutoring And Are Still Stuck:"
  - P1: "Parents of Smart Teens Who Freeze Up on the SAT / ACT:"
  - P2: not previewed (spent $3.82).

### Page copy (go.muchsmarter.com/start-trial)
- **First screen:** "For SAT & ACT Students Only" / "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." / "Watch how MuchSmarter's game-based system turns test-day panic into a repeatable, learnable skill - then grab your teen's free 30-day trial below." / video / button "Start My Free Trial".
- **Below:** "What's included (30-day free trial)": "Expert, live online group workshops", "Unlimited practice with our online game", "Videos and practice sets for all problem types", "Personal dashboard to track progress", "MyGame training to think like a champion", "Training for every aspect of game mastery".
- "Real Results": "Reading: 21 → 31", "Math: under 25% correct → 25", "ACT: hopeless on test day → 34".
- "How MuchSmarter Actually Works" has 4 steps (expert, learn the moves, "150+ training videos", mixed practice, full-length practice tests).
- "What Parents & Students Are Saying" has 12 reviews: Nicky B., Chris C., Jake E., Jeffrey G., Sarah O., Maceda, Sabrina's Parent, Victoria R., Chris C. (UVM), Aaron B., Rachel Z. Footer has Privacy Policy and Terms links. There is no menu.
- **Form (pop-up):** First Name *, Phone * (country picker, US default), Email *, consent checkbox ("By submitting, I consent to receive emails and SMS messages about my free trial and related updates."), hidden UTM Source / Medium / Campaign / Content, Cloudflare Turnstile. No dropdowns and no prefilled values. Button: "Start My Free 30-Day Trial". Under the button: "Cancel anytime in 2 clicks. We'll remind you before your trial ends." No pre-qualifier and no mention of money. Both are correct for a B2C test prep market per the playbook.
- **Step 2 (/login):** "Step 2 of 2 / One Step Left. Your Free Trial Is Ready. / Sign Up For Your Free Trial / Secure checkout / Cancel anytime / Won't be charged today".
- **Screenshots:** much-smarter-desktop.png and much-smarter-mobile.png. Pop-up shots and full-page shots are saved next to them. On mobile, the button is in the first screen and the form is not.
- **Tracking in the GHL funnel head:** Meta pixel 1929070941048101 (PageView) and Clarity uhr8ka2z10.

### Profile facts (from "(MS) The Game Strategy" and "(MS) GHL fields/forms"; no client profile exists)
- **Offer:** a 30-day free trial of the MuchSmarter game-based SAT/ACT system, then $40/month. Funnel: Page 1 signup form, then Step 2 card info, then a thank-you page. The strategy says "we don't need to qualify - we just need to convert on emotion + low risk."
- **Real guarantee / risk reversal:** "Thirty days, completely free, no credit card charge until the trial ends", "Cancel anytime. No contracts." There is no money-back or score guarantee. Email 8 only says "if their score doesn't improve, I want to hear about it personally."
- **Proof:** Jake: ACT reading 21 → 31. Chris: "less than a quarter of math questions right" → 25. Nicky: 34 ACT. Dylan: "I got a score I never thought was possible for myself" (no number). Steve: "20+ years of working with students".
- **ICP:** parents of capable teens who "freeze on test day" (Angle 1, cold traffic). Angles 2 (score results) and 3 (risk-free) are crossed out.
- **Qualified lead:** not defined. The strategy says no qualification is needed (self-serve). The business goal is a trial start, then a paid sub.
- **Planned form (GHL doc):** First Name, Email, Phone (with country picker), hidden UTMs. This matches the live form. The strategy's Page 1 also listed a password field, which is not live.

### Playbook rules used
- "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page. Call-out line on the first 3 pages, kept to one line."
- "Squeeze page elements: logo, call-out, headline, subheadline, VSL preview GIF..., short form, Google/Trustpilot reviews block."
- "Opt-in form: first name + phone (two columns), email full width, consent checkboxes..."
- "Pre-qualifier (only for niche markets...; not for competitive ones like college consulting, SAT/ACT, fitness)" and "B2C: never mention money".
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- "CPL > $45 (with upstream fine) → landing page and offer."
- "Quality comes from calling out ONLY your ideal client."

### What I could NOT get, and why
- **Ad link_url:** ads_get_creatives returned no link_url, and the preview HTML and Ads Library had none either. I used the GHL funnel step URL (go.muchsmarter.com/start-trial, the only live "start-trial" page on the client domain). This needs confirmation (Question 1).
- **Video playback and length:** headless Chromium could not decode the MP4 (readyState 0). The file itself serves fine (HTTP 200, 11,076,678 bytes). I cannot say what is in it or how long it is.
- **GHL opt-in stats per page:** I did not pull them. I found the funnel (read-only) but did not query page-level stats.
- **Required-field behavior:** not tested, because I made no form submissions (read-only).
- **First Meta field lookup:** one ads_get_field_context call was blocked by the permission classifier. A retry with fewer fields worked, so all Meta numbers above are complete.
- **Client profile:** missing from the profiles folder. I used the strategy and GHL fields docs instead.
- **Best month for "The Game":** there is none yet (the campaign is 4 days old). I used the older 1:1 coaching sheet as a reference only.
