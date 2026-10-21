# Much Smarter ("The Game", 30-day free trial): deep dive, Oct 21

**Much Smarter**: LPCR 7d 4.2% (3/71), 3d 9.7% (3/31), prior week (Oct 7-13) 2.9% (3/103). The first free trial start was logged on Oct 19.
**Main reason, in one line:** the step 2 SIGN UP button was fixed on Oct 19, and leads and the first trial came back the same day (Oct 19-20: 3 leads from 21 clicks, 1 trial). What still loses people: on phone, taps in the first ~2.4s do nothing on both pages, only 58% of clicks become landing page views, and every ad says "No credit card" while step 2 asks for a card.

## Hard break re-check (Oct 19 findings)

### 1. Step 2 checkout (go.muchsmarter.com/login): FIXED
- Iframe height: `--ms-frame-h` is now **900px desktop** (drawn at scale 0.8, so 720px visible) and **1000px phone** (scale 1). It was 640 / 660. The code comment says: "FIX: frame was too short (640px x 0.8 = 512px), so the Sign Up button sat below the visible area. Height raised."
- `scrolling="no"`: **still there.** It is fine now, because the frame is taller than the form.
- `allow="payment"`: **still missing.** The console still shows "Potential permissions policy violation: payment is not allowed in this document." The `sandbox` now includes `allow-popups allow-top-navigation-by-user-activation` (added).
- SIGN UP after clicking "Sign Up For Your Free Trial": **fully visible** on 1440x900 (button at 707-738px inside a frame that ends at 748px, 181px spare at the frame's scale) and on 390x844 (272px spare inside the frame; you scroll the pop-up to reach it, and it scrolls). Also checked at 1280x720 and on a Pixel 7: visible. A click at the button's centre lands on the billing iframe, so nothing covers it.
- Screenshots: `oct21/much-smarter/step2-desktop-afterclick-bottom.png`, `step2-mobile-signup-inview.png`.

### 2. Step 1 dead first tap (go.muchsmarter.com/start-trial): NOT FIXED
- The redirect still splits: 8 requests gave 4 to `/start-trial-page` (A) and 4 to `/start-trial-986126` (B).
- Phone 390x844, 30 tap tests on both variants. "Opened" means the First Name field became visible.
  - Taps made 1.1 to 2.4s after the page request: **17 of 18 opened nothing, even 6.5s later.** (One B tap at 2.1s opened late.)
  - Taps made 3.0 to 4.8s after the request: **12 of 12 opened.** Only 6 of those opened within 1.5s; the other 6 took 1.5 to 6.5s.
  - Page DOM ready was 0.5 to 0.9s and the load event 0.6 to 1.0s. So the button looks ready about 1.5s before it works.
- **New: the same problem is on step 2.** On /login, 4 of 4 taps on "Sign Up For Your Free Trial" at 1.7 to 2.6s opened nothing. 2 of 2 taps at 4.6s worked.
- What changed on step 1 is only the pop-up (saved Oct 19, 13:39 UTC): the "Card needed to start..." line is gone and the submit button changed from "Next: Create My Teen's Login" to "Create Login".

## Changed since Oct 19

| Item | Status |
|---|---|
| Step 2 SIGN UP visible | **DONE** (900 / 1000px frame) |
| `allow-popups` in sandbox (3-D Secure) | **DONE** |
| `allow="payment"` on iframe | NOT DONE |
| Prefill step 1 data into step 2 | NOT DONE (iframe src is still `/embedded/billing` with no query string; all 9 fields are empty) |
| "Enter a valid phone number" shown before typing | NOT DONE |
| Lead pixel fires on /login page load | NOT DONE (`fbq('track', 'Lead')` still in the /login page code) |
| Price $30 vs $40 | NOT DONE. The page now says "$30/month" twice; the strategy doc says $40 nine times |
| Step 2 page copy | **DONE (new).** Headline is now "One Step Left: Create Your Teen's Login. Free for 30 Days", with "You won't be charged today. Your card is only charged $30/month if you keep going after 30 days. We'll remind you before your trial ends. Cancel anytime in 2 clicks" and a trust row "Secure checkout / Cancel anytime / Won't be charged today" under the form |
| Step 1 dead first tap | NOT DONE (see above) |
| Card honesty on step 1 | **CHANGED.** "Card needed to start, you won't be charged today" was removed from the pop-up. Step 1 now says nothing about a card. The card first shows on step 2 |
| Step 1 subheadline risk line | NOT DONE |
| Video compress and poster (load rate) | NOT DONE (same 11.1 MB MP4, no poster, grey "0:00" box). Load rate 58% |
| Desktop button above the fold | NOT DONE (top at 875px on a 900px screen, both variants) |
| Clarity tags | NOT CHANGED (still "T1-A" / "T1-B", although both pages changed twice) |
| Inline form, risk line, proof near form (tests) | NOT DONE |
| Ads | No new ads since Oct 8. Copy and images are the same as Oct 19 (files are byte-identical). **P1 is now PAUSED** (it had 9 clicks and 1 lead on Oct 19 and 7 clicks on Oct 20). P4 is still paused. Only P5, P3 and P2 are active |

## Data

### Sheet ("(MS) - Business Reporting B2C - TheGame", tab "Oct", col E Link Clicks, H Lead, I Free Trial Starts). Logged through Oct 20.
| Window | Clicks | Leads | LPCR | Trials |
|---|---|---|---|---|
| Oct 7-13 (prior week; Oct 7 empty) | 103 | 3 | 2.9% | 0 |
| Oct 12-18 (Oct 19 review) | 79 | 0 | 0% | 0 |
| **Oct 14-20 (7d)** | **71** | **3** | **4.2%** | **1** |
| **Oct 18-20 (3d)** | **31** | **3** | **9.7%** | 1 |
| Oct 19-20 (after the fixes) | 21 | 3 | 14.3% | 1 |
- Daily Oct 14-20 clicks/leads: 11/0, 11/0, 8/0, 10/0, 10/0, 12/2, 9/1. Trials: 1 on Oct 19.
- Spend Oct 14-20 (sheet): $366.25. CPM rose from $26.97 (Oct 14) to $65.70 (Oct 20). Clicks fell from 15-25 a day (Oct 8-12) to 8-12 a day.
- October so far: $660.16, 174 clicks, 6 leads, 1 trial. Jan to Sep: empty, so there is no "best month" to compare.
- The move is real but small: 3 leads in 2 days, right after the Oct 19 fixes, versus 0 in the 7 days before.

### Meta (account 1188526852804019, campaign "OLead - MS - TheGame - US - 30+", Oct 14-20)
| Ad | Status | Spend | Share | Clicks | LPVs | Load rate | Leads (Meta) |
|---|---|---|---|---|---|---|---|
| P1 Black notes checklist | **PAUSED** (since Oct 20 or 21) | $161.14 | 43% | 31 | 20 | 65% | 1 |
| P5 Black notes checklist | Active | $138.05 | 37% | 34 | 18 | 53% | 1 |
| P3 Black notes checklist | Active | $44.39 | 12% | 6 | 5 | 83% | 0 |
| P2 Black notes checklist | Active | $22.45 | 6% | 5 | 2 | 40% | 2 |
| P4 Black notes checklist | Paused | $5.50 | 1% | 1 | 0 | 0% | 0 |
| **Total** | | **$371.53** | | **77** | **45** | **58%** | **4** |
- All 4 Meta leads came on Oct 19 (P1 1, P2 2) and Oct 20 (P5 1). Meta 4 vs sheet 3: Lead fires on every /login load, so a reload counts twice. Not a tracking gap.
- Meta's daily spend split looks wrong (spend shows on days with no clicks and $0 on days with clicks). I used the 7-day totals for spend.
- No ads were launched since Oct 19.

### Live ad copy and images (all 4 spending ads)
- Headline (all): "From Test Anxiety to 1400+ SAT - Free for 30 Days".
- Primary text (all, same): opens "ATTENTION: Parents of teens who freeze up on the SAT/ACT" / "Your teen is smart. You know it. Their teachers know it." / "But on test day - something shuts down." ... "No credit card. No commitment. No pressure." / "Just a proven system - free for 30 days." / "👇 Click below to start your free 30-day trial." CTA: Learn More.
- P1 image: "Parents of Smart Teens Who Freeze Up on the SAT / ACT:" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play the SAT / ACT as a game of skill" / "Watch the anxiety drop and the score climb!" / "Start your FREE trial today".
- P5 image: "Parents of Teens Who Struggle With SAT / ACT Math:" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play SAT / ACT Math as a game of skill" / "Heal years of "math wounds" and watch the scores rise!" / "Start your FREE trial today".
- P3 image (viewed Oct 19, unchanged): "Parents of Teens Who've Already Tried Test Prep / Tutoring And Are Still Stuck:" / "...Watch them WIN - where previous test prep failed!"
- P2 image (viewed today, first time): "Parents of Straight - A students With Weak SAT / ACT scores:" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play the SAT / ACT as a game of skill" / "Watch them WIN - as their scores catch up with their grades" / "Start your FREE trial today".

## Health checks (Oct 21, read-only, nothing submitted)
| Check | Result |
|---|---|
| Landing URL | `go.muchsmarter.com/start-trial` returns 302 to A or B (4/4 split in 8 requests). Both return 200 |
| Speed | Step 1 DOM ready 0.5-1.3s, load 0.6-1.6s. /login 0.6-1.1s |
| Load rate | **58%** (45/77). Flag. It was 60% for Oct 12-18 |
| Why LPVs are low (two causes) | (1) The 11.1 MB MP4 (`6ac6082e195f9172edc6b0a1.mp4`, no poster) is the first thing on page 1. (2) **New finding:** the Meta pixel and Clarity load only **5.4 to 6.2s after the page loads** on both variants, desktop and phone. They are added by the GHL page script, not in the raw HTML head. Anyone who leaves before ~6s is never counted as a landing page view, and Clarity never records them |
| Pixel | Meta pixel 1929070941048101 and Clarity uhr8ka2z10 on both variants. PageView fired on phone. On desktop my headless browser loaded the pixel script but sent no PageView (likely my test browser; check in Events Manager). Step 1 has no Lead event. Lead fires on /login load. /thank-you has StartTrial |
| Phone field | US +1 default on step 1 (correct). Step 2 billing form also +1 |
| Form fields step 1 | First Name *, Phone *, Email *, consent box ("By submitting, I consent to receive emails and SMS messages about my free trial and related updates."), button "Create Login", Privacy Policy. No test data prefilled. On phone the whole pop-up incl. "Create Login" fits on the first screen |
| Button position | Phone: "Start My Free Trial (Step 1 of 2)" top at 662px (A) / 701px (B) on an 844px screen. Desktop: 875px on 900px (cut off at the bottom edge) |
| Dead taps | Step 1 and step 2 buttons ignore taps in the first ~2.4s on phone (details above) |
| **Step 2 video** | **New flag:** the video under the step 2 button is **551 MB** (`6ac6095222bc27f58fb29e5b.mp4`), set to autoplay, muted, with no poster. On phone data this streams a huge file while the parent tries to fill in the card form |
| Step 2 form | 9 empty fields (First Name, Last Name, Email, Phone, Password, Card Number, Expiration, CVV, Name on Card). "Enter a valid phone number" shows before typing. Heading inside the frame still "Sign Up" |
| Console | No page script errors. Payment permission warnings inside the billing frame (see allow="payment") |
| Turnstile / card test | Not verified. I did not submit any form (by rule) |

## A. FIXES (do now, these are not tests)

### Page 1 (go.muchsmarter.com/start-trial, both variants)
1. **Make the first tap work.** Put the step 1 form inline on the page, right under the subheadline (First Name and Phone side by side, Email, consent box, button), with the video below it. Remove the pop-up. Today 17 of 18 phone taps in the first ~2.4s open nothing. This is already planned in the sheet's "LP AB test" tab, but the pop-up is broken, so ship it as a fix on both variants. Playbook: "Opt-in form: first name + phone (two columns), email full width".
2. **Say the card terms before step 2.** Change "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account" To "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account. You won't be charged today. Cancel anytime in 2 clicks." (Every word is already live on step 2.) Also flag for Ema: the ad line "No credit card. No commitment. No pressure." is false while step 2 takes a card. The ad is Ema's call.
3. **Fix the load rate (58%).** Compress `6ac6082e195f9172edc6b0a1.mp4` (11.1 MB) and add a poster image, on both variants.
4. **Load the pixel earlier.** Ask GHL support (or whoever set up tracking) why the Meta pixel and Clarity load 5.4-6.2s after the page. Meta LPVs and Clarity both miss everyone who leaves before ~6s. Until then, do not read the 58% load rate as the true bounce rate.
5. **Desktop:** move "Start My Free Trial (Step 1 of 2)" (or the inline form) above 800px. Today it sits at 875px on a 900px screen.
6. **Reset Clarity tags.** Change "T1-A" / "T1-B" To "R2-A" / "R2-B". Both pages changed on Oct 14 and Oct 19, so old and new data are mixed.

### Page 2 (go.muchsmarter.com/login)
1. **Make the first tap work here too.** Show the billing iframe inline under "Cancel anytime in 2 clicks" and remove the "Sign Up For Your Free Trial" pop-up. 4 of 4 phone taps at 1.7-2.6s opened nothing. This also removes one click before the card form.
2. **Shrink or remove the 551 MB video.** Replace `6ac6095222bc27f58fb29e5b.mp4` with a compressed file (aim under 10 MB), add a poster, and add `preload="none"`. Or move it to /thank-you, where the strategy doc already plans "Steve does a video on what the game is".
3. **Add `allow="payment"`** to the `#much-smarter-signup` iframe, so Apple Pay / Google Pay and Stripe payment features are allowed.
4. **Prefill step 1 data.** Pass the /login query string into the iframe src (`/embedded/billing?email=...&firstname=...&phone=...`) and have the games.muchsmarter.com developer prefill First Name, Email and Phone. The strategy doc says step 2 should be "Prepopulated with their sign up info. JUST credit needed here."
5. **Hide "Enter a valid phone number" until the field is used** (developer fix in the billing form).
6. **Move the Lead pixel.** Fire Lead on the step 1 form submit (GHL form event or CAPI), not on /login page load. Keep StartTrial on /thank-you.
7. **Confirm the price.** The page says "$30/month" (twice) and every email in the strategy doc says $40. Use one number before the first trial converts.

## B. A/B TESTS

### Page 1 (opt-in), after Fix 1 (inline form)
1. **Risk line under the button.** Change: no text under the button. To: "Free for 30 days. Won't be charged today. Cancel anytime in 2 clicks." Why: the ad promises "No commitment. No pressure." and every phrase in B is already live on step 2. There is no money-back guarantee in any doc, so do not add one.
2. **Proof next to the form, parents first.** Change: the "Real Results" strip after "What's included", and reviews that open with Nicky B. (a student). To: under the form, "Reading: 21 → 31 (Jake E., ACT). Math: under 25% correct → 25 (Chris C., ACT). 34 ACT (Nicky B.)", then Victoria R. first: "My son Bryce told me he learned more in an hour and a half than in the past six months with his previous math tutor." Why: P5 (math) is now the top active ad and Chris C. and Victoria R. are math proof. Parents are the buyer.
3. **Call-out for the top active ad.** Change "For Parents of Smart Teens Who Freeze Up on the SAT / ACT" To "For Parents of Teens Who Struggle With SAT / ACT Math". Why: P1 (whose call-out the page copies) is paused. P5 is now 37% of spend and its image opens "Parents of Teens Who Struggle With SAT / ACT Math:". Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad". Only run this if P5 stays the main ad.
4. **Headline (restart the live split).** A: "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." B: "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." Keep both, restart the count under R2 labels. Why: B uses the ad image line "Your teen will stop struggling and play the SAT / ACT as a game of skill" (P1, P2) and the ad headline's "Free for 30 Days".
5. **Submit button says what they get.** Change "Create Login" To "Next: Start My Teen's Free Trial". Why: every ad image ends "Start your FREE trial today", and the playbook says the button should say what they get. "Create Login" names a chore.

### Page 2 (checkout), after Fixes 1-4
1. **Heading inside the form.** Change "Sign Up" To "Create Your Teen's Login". Why: the page headline now says "One Step Left: Create Your Teen's Login", so the form should say the same.
2. **Reassurance at the card fields.** Change "PAYMENT" To "PAYMENT (you won't be charged today)". Why: "Won't be charged today" is in the trust row under the form, but the parent hesitates at the card field.
3. **Fewer fields.** Change: "Last Name" and "Name on Card" as separate empty fields. To: remove "Last Name" and prefill "Name on Card" from First Name (developer). Why: 9 fields after a 3-field step 1. Playbook: "cut friction; the page should be short."

**Run plan:** about 71-77 clicks and about 45 counted page views a week, so 150 visitors per version needs about 6-7 weeks per single test. Do all fixes first. Then run one bundle for 4-6 weeks: page 1 B = tests 1 + 2 + 5 (Clarity R2-A / R2-B), with the headline split kept as is; page 2 B = tests 1 + 2 + 3 as one version once the developer can do it. Judge on trial starts (StartTrial on /thank-you), not only opt-ins.

## NEED FROM EMA
- **A real-phone run from the ad link** (iPhone Safari and Android Chrome, on 4G): does step 1 submit, does Turnstile pass, does /login load, and can a card reach /thank-you? I did not submit anything. The 1 trial on Oct 19 suggests it can work, but nobody has confirmed the full path.
- **Who paused P1, and why.** It was the top spender (43%) and had a lead on Oct 19. P4 is also still paused.
- **GHL contacts for Oct 19-20** (3 leads) with UTMs, and the source of the Oct 19 trial (from an ad lead or not).
- **Clarity recordings (uhr8ka2z10)** for Oct 14-20: dead taps on "Start My Free Trial (Step 1 of 2)" and on "Sign Up For Your Free Trial".
- **Client confirmation:** price $30 or $40, and that a card is required (the ads and the strategy doc emails say "No credit card").
- **The games.muchsmarter.com developer contact** for prefill, the early phone error, the "Sign Up" heading and the fields.
- **GHL tracking check:** why the pixel and Clarity load 5-6s after page load.
- **Note:** my ~10 test loads of /login today fired the Meta "Lead" pixel (it fires on page load). They were not from an ad, so they will not count as ad leads, but Events Manager may show extra Leads on Oct 21.
- The "1400+ SAT" in the ad headline has no proof on the page or in the strategy doc (the page proof is ACT: 21 → 31, 25, 34). Ema's call on the ad; I kept it out of all page copy.

## Appendix: facts pulled
- Page 1 A first screen: "For Parents of Smart Teens Who Freeze Up on the SAT / ACT" / "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win." / "Start your teen's free 30-day trial in 2 quick steps: tell us where to send their login, then create their account" / video / "Start My Free Trial (Step 1 of 2)". B: same, headline "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." Then "What's included (30-day free trial)" (6 items), "Real Results" (Reading: 21 → 31 / Math: under 25% correct → 25 / ACT: hopeless on test day → 34), "How MuchSmarter Actually Works" (4 steps), "What Parents & Students Are Saying" (11 reviews, first is Nicky B.), footer Privacy Policy / Terms & Conditions. No guarantee anywhere.
- Pop-up: "Step 1 of 2" / First Name * / Phone * (US +1) / Email * / consent box / "Create Login" / Privacy Policy.
- Step 2: "Step 2 of 2" / "One Step Left: Create Your Teen's Login. Free for 30 Days" / "You won't be charged today. Your card is only charged $30/month if you keep going after 30 days. We'll remind you before your trial ends. Cancel anytime in 2 clicks" / "Sign Up For Your Free Trial" / pop-up: "After your 30-day free trial ends, your card will be charged $30/month. Cancel anytime, no questions asked." / "Sign Up" / ACCOUNT / PAYMENT / SIGN UP / trust row.
- Strategy doc: price $40/month; "Thirty days, completely free, no credit card charge until the trial ends"; step 2 "Prepopulated with their sign up info". No money-back or score guarantee.
- Files: screenshots `A-desktop.png`, `A-mobile.png`, `A-mobile-full.png`, `A-*-afterclick.png`, `B-*` (same set), `step2-desktop.png`, `step2-mobile.png`, `step2-*-afterclick-bottom.png`, `step2-*-signup-inview.png`; data `step1.json`, `step2.json`, `html/`, `ads/`, `sheet/ms.xlsx`. All in `/tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/much-smarter/`.
- Could not get: Turnstile and card checks (no submits, by rule), GHL funnel stats (not tried), why/when P1 was paused, video audio (not needed: page video only).
