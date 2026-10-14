# LPCR page review: Much Smarter ("The Game", 30-day free trial), Oct 14

**Verdict:** The page still talks to students ("For SAT & ACT Students Only") while every ad talks to parents, the form is still one tap away behind a pop-up, and 1 in 3 clicks still never loads the page. The only change since Oct 12 is a headline split test (T1) that leaves all three problems in place. LPCR is 2.9% over 7 days and 1.9% over the last 3 days (goal 20%). There have been 0 leads from 29 clicks since the last review.

**What changed since Oct 12**
- **New: a GHL split test is live.** go.muchsmarter.com/start-trial now sends a 302 redirect to one of two pages: /start-trial-page (Clarity tag "T1-A") or /start-trial-986126 (Clarity tag "T1-B"). In 12 test requests, 7 went to A and 5 went to B. The only text that differs is the headline:
  - A: "The SAT & ACT Aren't Knowledge Tests. They're Games. Here's How to Win."
  - B: "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days."
- **Planned but not live.** The sheet tab "LP A/B test" (dated Oct 12) also lists a new subheadline ("Your teen is smart. But on test day, something shuts down...") and an inline form ("Move the video below the form"). Neither is on the live B page.
- **Not changed:** the same 11,076,678-byte MP4 autoplays with no poster (it still shows as a grey "0:00" box), the call-out is still "For SAT & ACT Students Only", the form is still in a pop-up, the load rate is still 68%, and step 2 still says "Secure checkout".
- **New ads:** none. The same 5 ads (P1 to P5, all created Oct 8) are the only ads created since Oct 1, and all 5 are ACTIVE. The copy and creatives are unchanged.
- **Ad link confirmed:** the P4 preview links to `go.muchsmarter.com/start-trial?utm_source=meta&utm_medium=paid_social&utm_campaign=pacow_freetrial&utm_content=p4blacknoteschecklist`.

## Live ads (Meta, last 7 days = Oct 7 to 13, ACTIVE only)

| Ad | Spend | Link clicks | LPVs | Leads (Meta) | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| P4 Black notes checklist ("Bad at Standardized Tests") | $175.24 | 58 | 41 | 2 | 59% | 71% | 3.4% |
| P5 Black notes checklist ("Struggle With SAT / ACT Math") | $57.47 | 35 | 23 | 0 | 19% | 66% | 0% |
| P3 Black notes checklist ("Already Tried Test Prep / Tutoring") | $30.74 | 11 | 6 | 0 | 10% | 55% | 0% |
| P1 Black notes checklist ("Smart Teens Who Freeze Up") | $27.42 | 4 | 3 | 0 | 9% | 75% | 0% |
| P2 Black notes checklist | $3.92 | 0 | 0 | 0 | 1% | n/a | n/a |
| **Total** | **$294.79** | **108** | **73** | **2** | 100% | **68%** | **1.9%** |

- All 5 ads share the headline "From Test Anxiety to 1400+ SAT - Free for 30 Days" and the same primary text.
- The sheet logs $293.91, 103 clicks and 3 leads. Meta counts 2 leads, which is close, so tracking looks fine. I judge LPCR on the sheet.
- Cost per lead on the sheet is $97.97 (the sheet's own max is $45, up from $69.76 on Oct 12). CTR is 1.09% (target over 1%), so the ads still get clicks and the loss happens after the click. CPM is $31.12 (target under $30).

## Fix first (broken things, not tests)

1. **Load rate is 68% (flag, under 80%). No change since Oct 12.** The first screen still has an 11 MB MP4 with autoplay, muted, `preload="metadata"` and no poster image. The split test also adds a 302 redirect hop before the page loads. Compress the video, add a poster frame, and recheck after 3 days. Apply the same fix to both A and B so the test stays fair.
2. **The "Start My Free Trial" button can do nothing on the first tap.** On a phone-size screen I tapped the button on both variants 31 times. 11 taps opened no pop-up, including all 6 taps made within 1 second of the page load. Every tap after 2.5 seconds or more worked. A parent who taps right after the page appears can get no response, and on 4G this window will be longer. Check this on a real phone and in Clarity (project uhr8ka2z10, "dead clicks" on the button). Putting the form inline (T2) removes this risk.
3. **"No credit card" still does not match the funnel.** All 5 ads say "No credit card. No commitment. No pressure." Step 2 (/login) still shows "Secure checkout" and "Won't be charged today", and the funnel still has the `requireCreditCard` setting. The strategy doc says "no credit card charge until the trial ends". Ema and the client should decide which wording is true and use it everywhere.
4. **"1400+ SAT" has no proof.** It is still the headline on every ad. All score proof on the page is ACT ("Reading: 21 → 31", "Math: under 25% correct → 25", "34 ACT"). The strategy doc crossed out the score angle ("1400+ SAT / 31+ ACT is closer than you think"). Confirm it with the client or drop it. I left it out of every B below.
5. **The ad quotes are still unverified.** "My child walked into the SAT relaxed for the first time ever." and "He finally believed he wasn't bad at tests." appear only in the strategy doc's ad copy draft, with no name. Do not reuse them on the page until the client confirms they are real.
6. **The live T1 test cannot pick a winner as it stands.** At about 17 clicks a day and LPCR near 3%, each version gets about 1 lead a week. A headline-only change on top of a slow page and a student call-out needs months to read. See "How to run them".
7. **The desktop button sits below the first screen** (top at 898px on a 900px screen, on both variants). On mobile it is visible (top at 665px on A and 704px on B). The form itself is not visible on either.

## 5 A/B tests (biggest expected lift first)

### T1. Parent call-out + subheadline (expand the live headline test)
- **Change:** "For SAT & ACT Students Only" / "Watch how MuchSmarter's game-based system turns test-day panic into a repeatable, learnable skill - then grab your teen's free 30-day trial below."
- **To:** "For Parents of Smart Teens Who Freeze Up on the SAT / ACT" / keep the live B headline "Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." / subheadline "Your teen is smart. But on test day, something shuts down. It's a strategy problem. Our game-based system teaches them to approach every question with calm, clarity, and control."
- **Why:** The call-out is the P1 creative's own line ("Parents of Smart Teens Who Freeze Up on the SAT / ACT:"), and every creative opens with "Parents of Teens Who...". The B headline already uses the P4/P5 creative line "Your teen will stop struggling and play the SAT / ACT as a game of skill". The subheadline is the one already written in the sheet's "LP A/B test" tab, built from the ad's primary text. Playbook: "Call-out line on the first 3 pages, kept to one line" and "Headline = the offer ... same on every page."

### T2. Inline form vs pop-up
- **Change:** the "Start My Free Trial" button that opens a pop-up (First Name *, Phone *, Email *, consent box, "Start My Free 30-Day Trial").
- **To:** the same form right under the subheadline, with First Name and Phone side by side, then Email full width, the consent box and the button "Start My Free 30-Day Trial". Move the video below the form.
- **Why:** Playbook: "Opt-in form: first name + phone (two columns), email full width" and "short form". This is already planned in the sheet (rows 12 to 13). It also removes the dead-tap risk in Fix 2. Keep the pop-up for the buttons lower on the page.

### T3. Risk line under every button
- **Change:** "Cancel anytime in 2 clicks. We'll remind you before your trial ends." This only shows inside the pop-up, after the tap.
- **To:** under every "Start My Free Trial" button: "Free for 30 days. Won't be charged today. Cancel anytime in 2 clicks."
- **Why:** The ads promise "No commitment. No pressure." and the page shows no risk reversal before the tap. Every phrase in B is already live in the funnel (pop-up and step 2). There is no money-back or score guarantee in any doc, so do not add one. Settle Fix 3 first.

### T4. Proof next to the form, parents first
- **Change:** the scrolling "Real Results" strip ("Reading: 21 → 31 / Math: under 25% correct → 25 / ACT: hopeless on test day → 34"), which is placed after "What's included", and a reviews block that opens with three student reviews.
- **To:** a static block directly under the form button: "Real results from MuchSmarter students: Reading: 21 → 31 (Jake E., ACT). Math: under 25% correct → 25 (Chris C., ACT). 34 ACT (Nicky B.)". Then move Victoria R. ("My son Bryce told me he learned more in an hour and a half than in the past six months with his previous math tutor.") and Sabrina's Parent to the top of the reviews block.
- **Why:** The skill checklist says "Proof near the form: results with real numbers, parent reviews first when parents are the buyer." Every line is already on the page. P5 (math) is the second-biggest spender and matches Chris C. and Victoria R.

### T5. Light preview vs heavy autoplay video
- **Change:** the 11 MB autoplay MP4 with no poster, which shows as a grey "0:00" box.
- **To:** a 10-second preview GIF of Steve inside the platform, captioned "Take a 5-minute look inside with Steve, founder of MuchSmarter". A tap opens the form. Play the full video after the opt-in.
- **Why:** Playbook squeeze page elements: "VSL preview GIF (10-second clip in the Canva GIF frame, quality ~0.4...)". The strategy doc places Steve's sneak peek after the form ("You just filled out your information..."). Run this only if Fix 1 alone does not lift the load rate above 80%.

## How to run them

- **Traffic:** 103 clicks in 6 days of spend, so about 17 a day or 120 a week. At a 68% load rate that is about 80 real visitors a week, or about 40 per version.
- **Time per test:** about 150 visitors per version means about 2.5 weeks on clicks, or about 4 weeks on real visitors, per test. Five single tests would take about 4 to 5 months, which is too slow.
- **Bundle:**
  - **Now:** do Fixes 1 and 2 on both variants. The live T1 is only about 2 days old, with 0 leads on both sides (29 clicks), so very little is lost by restarting it.
  - **Round 1 (about 4 weeks):** A = the current page. B = the live B headline + T1 call-out and subheadline + T2 inline form + T3 risk line. Change B's Clarity tag from "T1-B" to "R1-B", and A's to "R1-A", so the new data is not mixed with the old headline-only data.
  - **Round 2 (about 4 weeks):** the winner as A, and B = winner + T4 + T5. Clarity tags R2-A / R2-B.
  - If the budget goes to $100 a day or more, split the bundles back into single tests (T1-A / T1-B through T5-A / T5-B).
- **Judge on:** leads ÷ link clicks per variant from GHL (page stats or utm_content plus page URL), plus trial starts at step 2, so a cheaper opt-in does not hide fewer trials. The sheet does not split leads by variant yet. Add two columns or a weekly note.

## Questions for Ema or the client

1. When did the T1 split start, and what split % is set in GHL? (In 12 requests I saw 7 go to A and 5 go to B.)
2. Was B meant to include the new subheadline and the inline form from the sheet's "LP A/B test" tab? Only the headline is live.
3. Does the trial take a card or not? The ads say "No credit card". Step 2 says "Secure checkout ... Won't be charged today".
4. Is there a real student behind "1400+ SAT"? Are the two ad quotes from real parents, and can we name them?
5. Is the page video Steve's sneak peek? How long is it?
6. Should the 1:1 tutoring reviews ("Steve worked with me for 6 months", "Five months of tutoring") stay on a $40/month self-serve trial page?
7. Can we build a client profile in "00. Client Profiles (Claude)"? There is still none.

---

## Appendix: Facts pulled

### LPCR (sheet)
- **Source:** "(MS) - Business Reporting B2C - TheGame" (fileId 1xFKdhYq...), tab "Oct", column E "Link Clicks" and column H "Lead". The tab says "Link Clicks", so I cannot tell whether they are unique.
- **Daily (clicks / leads / spend):** Oct 8: 14 / 1 / $46.51. Oct 9: 19 / 0 / $46.21. Oct 10: 16 / 1 / $43.28. Oct 11: 25 / 1 / $73.28. Oct 12: 18 / 0 / $51.23. Oct 13: 11 / 0 / $33.40. The sheet is filled through Oct 13. Oct 1 to 7 are empty because the campaign had not started.
- **Last 7 days (Oct 7 to 13):** 3 / 103 = **2.9%** (6 days had spend). CPL $97.97.
- **Last 3 days (Oct 11 to 13):** 1 / 54 = **1.9%**.
- **Best month of 2026:** October, 2.9%. The Dash tab shows $0 and 0 clicks for Jan to Sep. As a reference only, the older 1:1 coaching sheet had its best month in Feb at 10.1% (a different offer and funnel).
- **When it dropped:** it never started high. It was 4.1% at the Oct 12 review and has had 0 leads on Oct 12 and 13 (29 clicks). The headline split test began around then, but the data is too thin to blame or credit it.
- **"LP A/B test" tab:** Clarity snippets for "T1-A" and "T1-B". Row 4: "A: The SAT & ACT Aren't Knowledge Tests..." (dated Oct 12). Row 5: "B: Help Your Teen Stop Struggling and Play the SAT / ACT as a Game of Skill. Free for 30 Days." Rows 7 to 8: subheadline A/B. Rows 12 to 13: the inline form change.
- **KPI tab:** Landing Page Conversion Rate "> 25%", CPL "Target: < $15, Max: $45", CPM "< $30", CTR "> 1%", CPC "< $4".

### Ad copy (identical for all 5 live ads)
- **Headline (title):** "From Test Anxiety to 1400+ SAT - Free for 30 Days". **CTA:** Learn More.
- **Primary text (key lines):** "ATTENTION: Parents of teens who freeze up on the SAT/ACT" / "Your teen is smart. You know it. Their teachers know it." / "But on test day - something shuts down." / "It's a strategy problem." / "🎮 Step 1: Claim your free 30-day trial of MuchSmarter" / "✔️ 150+ training videos broken down by skill and question type" / "✔️ Weekly live coaching sessions with expert instructors" / "No credit card. No commitment. No pressure." / "Just a proven system - free for 30 days." / "Parents tell us: 'My child walked into the SAT relaxed for the first time ever.' 'He finally believed he wasn't bad at tests.'" / "👇 Click below to start your free 30-day trial."
- **Creatives viewed today (black notes-app checklist):**
  - P4: "Parents of Teens Who've Decided They're Just 'Bad at Standardized Tests':" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play the SAT / ACT as a game of skill" / "Watch years of frustration turn into a score they're proud of!" / "Start your FREE trial today".
  - P5: "Parents of Teens Who Struggle With SAT / ACT Math:" / "Try our game-based system free for 30 days" / "Your teen will stop struggling and play SAT / ACT Math as a game of skill" / "Heal years of 'math wounds' and watch the scores rise!" / "Start your FREE trial today".
  - P3, P1, P2: these spend less, so I did not re-view them today. Their copy is unchanged per ads_get_creatives.

### Page copy (both variants, captured Oct 14)
- **First screen:** "For SAT & ACT Students Only" / headline (A or B, above) / "Watch how MuchSmarter's game-based system turns test-day panic into a repeatable, learnable skill - then grab your teen's free 30-day trial below." / video / "Start My Free Trial".
- **Below:** "What's included (30-day free trial)" (6 items), "Real Results" strip, "How MuchSmarter Actually Works" (4 steps), and "What Parents & Students Are Saying" with 11 reviews (Nicky B. first and Victoria R. 8th). The footer has Privacy Policy and Terms. There is no menu.
- **Pop-up form:** First Name *, Phone * (US flag default), Email *, consent checkbox, hidden UTM Source / Campaign / Medium / Content, and Cloudflare Turnstile. None of the inputs has the HTML `required` attribute. The button is "Start My Free 30-Day Trial", with "Cancel anytime in 2 clicks. We'll remind you before your trial ends." under it. There is no pre-qualifier and no mention of money. Both are correct for SAT/ACT per the playbook.
- **Video:** `6ac6082e195f9172edc6b0a1.mp4`, 11,076,678 bytes, autoplay, muted, no poster. It is the same file as on Oct 12.
- **Tracking:** Meta pixel 1929070941048101 and Clarity uhr8ka2z10 are on both variants, plus the variant tags T1-A and T1-B.
- **Screenshots:** `much-smarter-desktop.png` and `much-smarter-mobile.png` in the scratchpad (variant A). Variant B, the pop-up and full-page shots are in `oct14/ms/`.

### Profile facts (from "(MS) The Game Strategy"; no client profile exists)
- **Offer:** a 30-day free trial, then $40/month. "we don't need to qualify - we just need to convert on emotion + low risk."
- **Real guarantee / risk reversal:** "Thirty days, completely free, no credit card charge until the trial ends." / "Cancel anytime. No contracts." There is no money-back or score guarantee.
- **Proof:** Jake ACT reading 21 → 31. Chris "less than a quarter of math questions right" → 25. Nicky 34 ACT. Dylan "I got a score I never thought was possible for myself". Steve "20+ years of working with students".
- **ICP:** parents of capable teens who "freeze on test day" (Angle 1). Angles 2 and 3 are crossed out.
- **Qualified lead:** none is defined (self-serve). The goal is a trial start, then a paid sub.

### Playbook rules used
- "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page. Call-out line on the first 3 pages, kept to one line."
- "Squeeze page elements: logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block."
- "Opt-in form: first name + phone (two columns), email full width, consent checkboxes..."
- "Pre-qualifier (only for niche markets...; not for competitive ones like college consulting, SAT/ACT, fitness)" and "B2C: never mention money".
- "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."
- "CPL > $45 (with upstream fine) → landing page and offer."

### What I could NOT get, and why
- **Leads per variant (A vs B):** the sheet does not split them, and I did not pull GHL page stats.
- **When the split started and the configured split %:** these are not in any doc. I only saw the redirect behavior (7 to A and 5 to B in 12 requests).
- **Video length and content:** headless Chromium cannot decode the MP4 (readyState 0).
- **Required-field behavior:** I did not test it, because I made no form submissions (read-only).
- **Google Sheets connector:** it needs re-authorization. I read the sheet through a Drive export instead, so the numbers are complete.
- **Client profile:** none exists. I used the strategy doc.
