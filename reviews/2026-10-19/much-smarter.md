# Much Smarter ("The Game", 30-day free trial): urgent check, Oct 19

**Much Smarter**: LPCR 7d 0% (0/79), 3d 0% (0/28), prior week (Oct 7-13) 2.9% (3/103). Free trial starts: 0 all of October, including the 3 leads from Oct 8-11.

**Main reason, in one line:** step 2 is broken. The "SIGN UP" button in the card checkout is hidden below the edge of the iframe on desktop and on phone, so nobody can start a trial. Step 1 also got harder: the pop-up now says "Card needed to start" while every ad says "No credit card", and the first tap on the button still does nothing.

## Diagnosis: is it a tracking problem or a real zero?

**It is a real zero at both steps. It is not a tracking gap.**
- **Ads are delivering.** Meta: $335.23 spent, 82 link clicks and 49 landing page views from Oct 12 to 18. The sheet logs $330.93 and 79 clicks. CPM rose from $26.57 (Oct 12) to $74.26 (Oct 18), so clicks fell from about 17 a day to about 10 a day.
- **Sheet vs Meta leads:** the sheet shows 0 leads and Meta shows 0 leads for Oct 12 to 18. The Meta "Lead" event fires on every load of go.muchsmarter.com/login (the page step 1 redirects to). So 0 Meta leads means no ad visitor reached /login. Both sources agree, so this is not a tracking problem.
- **Is a zero at step 1 just bad luck?** Partly. At last week's 2.9%, 79 clicks would give about 2 leads, and a week with 0 happens about 1 time in 10. So the step 1 zero is a warning plus bad luck. The step 2 zero is a hard break (see below).
- **Trials:** the sheet's "Free Trial Starts" column is 0 for every day in October. Step 2 already looked cut off in the Oct 14 screenshot (`/tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/ms3/step2-after.png`), so trials have likely been impossible since launch.

## Health checks (what I tested, read-only, no form submitted)

| Check | Result |
|---|---|
| Landing URL loads | Yes. `go.muchsmarter.com/start-trial` returns a 302 redirect to `/start-trial-page` (T1-A) or `/start-trial-986126` (T1-B). In 10 requests, 6 went to A and 4 to B. Both return 200. DOM ready in about 1.0 to 1.4s, and once in 3.2s on phone. |
| Load rate (Meta LPV / clicks) | **60%** (49/82). It was 68% on Oct 14. Flag (goal 80%+). The same 11 MB MP4 with no poster is still the first thing on the page (it shows as a grey "0:00" box). |
| Page and pop-up render | Yes on desktop 1440x900 and phone 390x844. The pop-up has First Name *, Phone * (US +1 default, correct), Email *, a consent box, and the submit button "Next: Create My Teen's Login". The submit button is present and enabled. |
| Button opens the form | **Only if you wait.** On phone, 12 of 12 taps made 0.5 to 1.5s after load opened nothing, even 7 seconds later. 6 of 6 taps after 3s worked. A second tap at about 3.5s always worked. The Oct 14 finding is still there, and now it reproduces every time. |
| Button position | Phone: the button is in the first screen (top at 662px on A and 701px on B). Desktop: the button top is at 875px on a 900px screen, so it is still almost below the first screen. |
| Cloudflare Turnstile | Present on the form (hidden `cf-turnstile-response`). **I could not verify it.** My sandbox proxy blocks `brunhild.challenges.cloudflare.com`, so the token stayed empty in my tests. That is my network, not proof of a fault. Needs a real-phone test (see "Need from Ema"). |
| Console errors | No page script errors (0 `pageerror`). There are CSP "Refused to connect to 'data:,'" errors inside the Turnstile frame (normal Turnstile noise) and harmless WebGL and font warnings. |
| Opt-in redirect | GHL form "on submit" redirects to `https://go.muchsmarter.com/login/?email={{contact.email}}&firstname={{contact.first_name}}&phone={{contact.phone}}`, and /login/ returns 200. |
| Pixel | Meta pixel 1929070941048101 and Clarity uhr8ka2z10 are on both variants. PageView fired on phone. The step 1 page has no Lead event. **Lead fires on /login page load.** /thank-you fires StartTrial. Clarity variant tags are still "T1-A" and "T1-B". |
| Step 2 page (/login/) | Loads (200, about 0.8s). "Step 2 of 2 / One Step Left. Your Free Trial Is Ready. / Sign Up For Your Free Trial / Secure checkout / Cancel anytime / Won't be charged today". The "Sign Up For Your Free Trial" button **does** open the pop-up with the iframe from `games.muchsmarter.com/embedded/billing`. The Stripe card fields and the Stripe hCaptcha load. |
| **Step 2 SIGN UP button** | **Hidden on every screen size I tested.** The custom HTML sets `--ms-frame-h: 640px` (desktop) and `660px` (phone), with `scrolling="no"` and `overflow: hidden`. The billing form inside is 690px tall on desktop and 744px on phone. SIGN UP sits at 636-674px (desktop) and 690-728px (phone) inside the frame. Desktop shows only a 4px blue line. On phone, "Name on Card" is cut in half and SIGN UP is fully hidden. The "auto-fit" script waits for a height message the billing form never sends (the height stayed at 640/660). Same result at 1280x720 and on a Pixel 7. |
| Step 2 other | 9 fields: First Name, Last Name, Email, Phone, Password, Card Number, Expiration, CVV, Name on Card. Nothing from step 1 is prefilled, because the iframe src is static (`/embedded/billing` with no query string), so parents retype name, email and phone. "Enter a valid phone number" shows as red-style text before anyone types. The console shows "payment is not allowed in this document" because the iframe has no `allow="payment"`, so Apple Pay and Google Pay cannot work. The iframe also has `sandbox="allow-scripts allow-forms allow-same-origin"` with no `allow-popups`, which can block a 3-D Secure card check. |

Screenshots (all in `/tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/much-smarter/`): `A-mobile-r0.png`, `A-mobile-r0-afterclick.png`, `B-desktop-r0.png`, `B-desktop-r0-afterclick.png`, `B-mobile-r1.png`, `B-mobile-r1-afterclick.png`, `step2-desktop.png`, `step2-desktop-afterclick.png` (SIGN UP cut off), `step2-mobile-afterclick.png`, `step2-mobile-bottom.png` (SIGN UP hidden), `step2-laptop-bottom.png`, `step2-android-bottom.png`. Raw data: `step1.json`, `step2.json`, `html/`.

## Changed since Oct 14

- Parent call-out on page 1: **DONE.** "For SAT & ACT Students Only" is now "For Parents of Smart Teens Who Freeze Up on the SAT / ACT" on both variants.
- "Step 1 of 2": **DONE.** The button is now "Start My Free Trial (Step 1 of 2)", the pop-up says "Step 1 of 2", and the submit button is "Next: Create My Teen's Login".
- Subheadline "grab your teen's free 30-day trial below": **DONE.** It is now "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account".
- Card honesty: **HALF DONE.** The pop-up now says "Takes 2 minutes. Card needed to start, you won't be charged today. Cancel anytime in 2 clicks." The ads still say "No credit card. No commitment. No pressure." The mismatch is now visible at the moment of the opt-in.
- Price: **NOT DONE.** Step 2 still says "$30/month" and the strategy doc says $40. Not confirmed.
- Video compress + poster (load rate): **NOT DONE.** Same 11 MB file, no poster. Load rate fell to 60%.
- Dead first tap: **NOT DONE.** It now fails on every early tap.
- Inline form (T2), risk line under the button (T3), proof next to the form (T4): **NOT DONE.**
- Desktop button above the fold: **NOT DONE** (875px on a 900px screen).
- Clarity tags: **NOT CHANGED.** Still "T1-A / T1-B", although both pages changed. Old and new data are mixed.
- Headline split A/B: still live and unchanged.
- Ads: **no new ads since Oct 14.** All ads were created Oct 8. **P4 (the top spender, and the only ad with Meta leads on Oct 14) is PAUSED.** It spent only Oct 12 to 14. Copy and creatives are unchanged.

## Live ads (Meta, Oct 12-18)

| Ad | Status | Spend | Share | Clicks | LPVs | Load rate | Leads |
|---|---|---|---|---|---|---|---|
| P5 Black notes checklist | Active | $141.47 | 42% | 40 | 24 | 60% | 0 |
| P1 Black notes checklist | Active | $84.86 | 25% | 16 | 8 | 50% | 0 |
| P4 Black notes checklist | **Paused** (spent Oct 12-14) | $63.60 | 19% | 20 | 12 | 60% | 0 |
| P3 Black notes checklist | Active | $45.20 | 13% | 6 | 5 | 83% | 0 |
| P2 Black notes checklist | Active, no delivery | $0.10 | 0% | 0 | 0 | n/a | 0 |
| **Total** | | **$335.23** | | **82** | **49** | **60%** | **0** |

- Every ad has the same headline, "From Test Anxiety to 1400+ SAT - Free for 30 Days", and the same primary text, including "No credit card. No commitment. No pressure." All link to go.muchsmarter.com/start-trial with UTMs.
- P5 creative (viewed): "Parents of Teens Who Struggle With SAT / ACT Math:" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play SAT / ACT Math as a game of skill" / "Heal years of "math wounds" and watch the scores rise!" / "Start your FREE trial today".
- P1 creative (viewed): "Parents of Smart Teens Who Freeze Up on the SAT / ACT:" / "...Watch the anxiety drop and the score climb!"
- P3 creative (viewed): "Parents of Teens Who've Already Tried Test Prep / Tutoring And Are Still Stuck:" / "...Watch them WIN - where previous test prep failed!"

## A. FIXES (do now, these are not tests)

### Page 2 (checkout, go.muchsmarter.com/login) first, because it blocks every trial
1. **Show the SIGN UP button.** In the custom HTML block on /login, change `--ms-frame-h: 640px;` To `--ms-frame-h: 800px;`. In the `@media (max-width: 560px)` block, change `--ms-frame-h: 660px;` To `--ms-frame-h: 820px;`. Change `scrolling="no"` To `scrolling="auto"` as a safety net. Then open /login on a real phone and a laptop and confirm SIGN UP is fully visible under "Name on Card".
2. **Let the payment run in the iframe.** Add `allow="payment"` to the iframe, and add `allow-popups allow-top-navigation-by-user-activation` to its `sandbox`, so Stripe 3-D Secure and wallet pop-ups are not blocked. Then the client runs one real card test.
3. **Prefill step 1 data.** Pass the /login query string to the iframe (`/embedded/billing?email=...&firstname=...&phone=...`), and ask the games.muchsmarter.com developer to prefill First Name, Email and Phone from it. Parents currently type their name, email and phone twice.
4. **Hide the phone error until the field is used.** "Enter a valid phone number" shows before anyone types (developer fix in the billing form).
5. **Move the Lead pixel.** Today `fbq('track', 'Lead')` fires on every /login page load (refreshes and direct visits included). Fire Lead on the step 1 form submit instead (GHL form event or CAPI). Keep StartTrial on /thank-you, which is already set up.
6. **Confirm the price.** Step 2 says "$30/month" and the strategy doc says $40. Use one number.

### Page 1 (go.muchsmarter.com/start-trial, both variants)
1. **Make the first tap work.** On phone, every tap in the first 1.5s does nothing. Put the form inline on the page (see test P1-T1, which can be the fix itself). Or, at minimum, make the button scroll to an inline form section instead of opening a pop-up that is not ready yet.
2. **Stop the card surprise.** The pop-up says "Card needed to start" right after ads that say "No credit card". The ad copy is Ema's call, but the ad line "No credit card. No commitment. No pressure." is now false and needs to change. On the page, change "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account" To "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account. You won't be charged today. Cancel anytime in 2 clicks." All of these words are already live in the funnel.
3. **Fix the load rate (60%).** Compress the 11 MB MP4 (6ac6082e195f9172edc6b0a1.mp4) and add a poster frame. Apply this to both variants.
4. **Desktop:** move "Start My Free Trial (Step 1 of 2)" above 800px (put the video under the button, or shrink the video).
5. **Reset Clarity tags.** Change "T1-A" and "T1-B" to "R1-A" and "R1-B", because both pages changed since the test started.

## B. A/B TESTS

### Page 1 (opt-in)
1. **Inline form vs pop-up.** Change: the "Start My Free Trial (Step 1 of 2)" button that opens a pop-up. To: the same form (First Name and Phone side by side, Email, consent box, "Next: Create My Teen's Login") right under the subheadline, with the video below it. Why: the playbook says "Opt-in form: first name + phone (two columns), email full width". This also removes the dead first tap. It is already planned in the sheet's "LP A/B test" tab.
2. **Risk line under the button.** Change: no text under "Start My Free Trial (Step 1 of 2)". To: "Free for 30 days. Won't be charged today. Cancel anytime in 2 clicks." Why: the ad promises "No commitment. No pressure.", and every phrase in B is already live in the funnel (pop-up and step 2). There is no money-back guarantee in any doc, so do not add one.
3. **Proof next to the form, parents first.** Change: the "Real Results" strip placed after "What's included", and reviews that open with Nicky B. (a student). To: under the button, "Reading: 21 → 31 (Jake E., ACT). Math: under 25% correct → 25 (Chris C., ACT). 34 ACT (Nicky B.)", then Victoria R. ("My son Bryce told me he learned more in an hour and a half than in the past six months with his previous math tutor.") as the first review. Why: P5 (math, 42% of spend) matches Chris C. and Victoria R. Playbook: parents are the buyer, so put parent proof near the form.
4. **Headline per ad angle.** Change (A): "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." To: keep live B, "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." Why: B uses the creative's own line "Your teen will stop struggling and play the SAT / ACT as a game of skill". Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad".

### Page 2 (checkout), run only after Fix 1 there
1. **Heading that matches the step 1 button.** Change "Sign Up" To "Create Your Teen's Login". Why: the step 1 button promises "Next: Create My Teen's Login", so the next screen should say the same thing.
2. **Reassurance next to the card fields.** Change "PAYMENT" To "PAYMENT (you won't be charged today)". Why: "Won't be charged today" is already on /login, but it sits behind the pop-up, where the parent cannot see it at the card field.
3. **Shorter account section.** Change: the "Last Name" and "Name on Card" fields. To: remove "Last Name", and prefill "Name on Card" from First Name (developer). Why: the playbook says "cut friction", and the form has 9 fields after a 3-field step 1.

**Run plan:** about 80 clicks and about 48 page views a week, so 150 visitors per version takes about 6 weeks per single test. Do all fixes first. Then run one bundle for 4 weeks: page 1 B = P1-T1 + T2 + T3 (Clarity R1-A / R1-B), and page 2 B = P2-T1 + T2 + T3. Judge on trial starts (StartTrial on /thank-you), not only opt-ins.

## NEED FROM EMA
- **A real-phone opt-in test** on 4G (Safari and Chrome, from the ad link): does the form submit, does Turnstile pass, and does it land on /login? I did not submit anything, and my sandbox blocks Cloudflare's challenge server, so I could not confirm Turnstile.
- **A real card test at step 2** after Fix 1 (the client's own card or a Stripe test mode). Confirm it reaches /thank-you and the "much-smarter:trial-started" redirect fires.
- **GHL contacts from Oct 12 to 18** with the "pacow_freetrial" UTM, plus the form submission log, to confirm the 0 (and any submissions that Turnstile rejected).
- **Clarity recordings** (project uhr8ka2z10) from Oct 12 to 18: dead clicks on the button, and pop-up closes after "Card needed" shows.
- **Client confirmation:** is a card required (yes per the live funnel), is the price $30 or $40, and who maintains games.muchsmarter.com/embedded/billing (for the height message and prefill).
- **Why P4 was paused on Oct 14.** It was the only ad with Meta leads.
- **Note:** my two test loads of /login today fired the Meta "Lead" pixel (it fires on page load). These were not from an ad, so they will not show as ad leads, but Events Manager may show 2 extra Leads on Oct 19. The Oct 14 tests did the same.
- **Google Sheets connector** needs re-authorization. I read the sheet through a Drive export instead, so the numbers are complete.

## Appendix: facts pulled
- **Sheet:** "(MS) - Business Reporting B2C - TheGame", tab "Oct", columns E (Link Clicks), H (Lead), I (Free Trial Starts). Daily clicks/leads Oct 12-18: 18/0, 11/0, 11/0, 11/0, 8/0, 10/0, 10/0. Spend $330.93. Oct 8-11: 74 clicks, 3 leads. Free Trial Starts: 0 every day. Jan to Sep: empty.
- **Page 1 first screen (A):** "For Parents of Smart Teens Who Freeze Up on the SAT / ACT" / "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." / "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account" / video / "Start My Free Trial (Step 1 of 2)". Variant B has the same text with the headline "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." Below that: "What's included (30-day free trial)" (6 items), the "Real Results" strip, "How MuchSmarter Actually Works" (4 steps), 11 reviews, and a footer with Privacy Policy and Terms & Conditions.
- **Pop-up:** "Step 1 of 2" / First Name * / Phone * (US +1) / Email * / "By submitting, I consent to receive emails and SMS messages about my free trial and related updates." / "Next: Create My Teen's Login" / "Takes 2 minutes. Card needed to start, you won't be charged today. Cancel anytime in 2 clicks." / Privacy Policy. On phone, the "Card needed" line is below the first screen of the pop-up.
- **Step 2:** "After your 30-day free trial ends, your card will be charged $30/month. Cancel anytime, no questions asked." / "Sign Up" / ACCOUNT: First Name, Last Name, Email, Phone, Password / PAYMENT: Card Number, Expiration Date, CVV, Name on Card / SIGN UP (hidden).
- **Strategy doc:** "Thirty days, completely free, no credit card charge until the trial ends", $40/month. There is no money-back or score guarantee.
