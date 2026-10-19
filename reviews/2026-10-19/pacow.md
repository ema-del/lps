# LPCR deep dive: Pacow Media opt-in page, 19 Oct 2026

**Pacow**: LPCR 7d 13.1% (34/260), 3d 13.4% (13/97), prior week 14.2% (43/303). Flat, slightly down. Main reason: the page headline still sells "The Meta ads system..." while the new ads (launched 18 Oct) lead with "Why Most Education Businesses Struggle to Enroll Students Consistently" and "HOW THIS 23-YEAR-OLD USES META ADS...". The page also shows no proof near the form and still asks a $10k revenue question while CPL is EUR 74.71.

Goal is about 15%. That is about 2 more leads per 100 clicks.

## Changed since Oct 14

- Fix 1, broken URL on "1st video ever launched": **done.** The old ad is paused. The new copy goes to `lp.pacowmedia.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=newmay2026&utm_content=1stvideoever`. UTMs reach the hidden form fields.
- Fix 2, split test labels: **not done.** Both pages still run `clarity("set","variant","T1-A")`. The split changed. `/opt-in-page-4921` is no longer served. `/access` now sends about half of visitors to `/opt-in` and half to a new `/opt-in-499877` (6 of 12 loads each).
- Fix 3, confirm the guarantee: **not done.** The page has no guarantee. "looking for 5" still says "And if they don't work... you don't pay!". The "GUARANTEED" headline on the 1st video ad is gone. The new copy uses "Why Most Education Businesses Struggle to Enroll Students Consistently".
- Fix 4, partner count: **not done.** The ad text says "Trusted by 35+ education brands." The page says "45+ EDUCATION LEGENDS ALREADY TRUST US". The IG post says "45+ education brands".
- Fix 5, tracking gap: **worse.** Meta counts 8 leads and the sheet logs 34 for 12-18 Oct, so Meta sees 24% (42% on 14 Oct).
- Fix 6, empty `<title>`: **not done** on either page.
- T1 headline/sub with the call: **not done.** A new headline variant runs instead ("FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads").
- T2 guarantee line, T3 results strip, T4 form header/button, T5 remove the $10k question: **none done.** The rest of the page is the same as on 14 Oct.
- Other changes (ads side, for context):
  - All OLead ads were rebuilt on 18 Oct in a new ad set "OLead #1". The old set is now "OLead - OFF" (paused).
  - The OCompleteRegistration campaign is paused. Its last spend was 14 Oct.
  - Two Instagram follower boosts started 16 Oct.
  - On 15-17 Oct, OLead got only 15, 22 and 36 link clicks on EUR 181, 473 and 462 of spend (CPC EUR 12-21), so traffic to the page dropped.

## Live ads (ACTIVE, last 7 days = 12-18 Oct, EUR)

The OLead #1 ads have only spent since 18 Oct (one day), so read their numbers as early. Share is of all active spend (EUR 392.95), with share of OLead #1 (EUR 194.14) in brackets.

| Ad | Format | Spend | Link clicks | LPVs | Meta leads | Share | Meta headline | Hook (creative) |
|---|---|---|---|---|---|---|---|---|
| ed business + course - making 10k | video 73s | 63.81 | 5 | 4 | 0 | 16.2% (32.9%) | "Education Brand Founders: Ready for 10-20+ New Students Every Month?" | first frame caption "Look," |
| breaking vika claude | static | 56.82 | 6 | 5 | 0 | 14.5% (29.3%) | "Why Most Education Businesses Struggle to Enroll Students Consistently" | "HOW THIS 23-YEAR-OLD USES META ADS TO ADD 10-20+ NEW STUDENTS A MONTH FOR EDUCATION BRANDS" |
| ed brands im looking for youn 100k A1 | static | 56.45 | 8 | 8 | 0 | 14.4% (29.1%) | "Why Most Education Businesses Struggle to Enroll Students Consistently" | "I'm looking for 5 education brands who want to scale to $100k+/mo in 2026 with paid ads" |
| ed business - 1st video ever launched | video 37s | 14.36 | 2 | 1 | 0 | 3.7% (7.4%) | "Why Most Education Businesses Struggle to Enroll Students Consistently" | frame caption "guaranteed" (audio not available) |
| direct twitter claude / watch before you run ads / breaking julian / $4k spend $71k rev | mixed | 2.70 total | 0 | 0 | 0 | 0.7% (1.4%) | | |
| IG post "Follow @viktorijazykas for daily..." | video, goes to IG profile | 78.73 | 40 | n/a | 0 | 20.0% | none | "Education brands & course creators" |
| IG post "Follow @viktorijazykas if you..." | video, goes to IG profile | 77.98 | 16 | n/a | 0 | 19.8% | none | "Education brands & course creators" |
| Hammer Them Retargeting (8 ads) | mixed | 42.10 | 0 | 0 | 0 | 10.7% | | |

- The IG boosts send people to the Instagram profile (CTA "VIEW_INSTAGRAM_PROFILE"). They do not reach the page and are not in the sheet. Retargeting is ignored for page match (per brief).
- Paused ads that carried most of the 7-day spend: old "1st video ever launched" (EUR 1,500.16, 152 clicks, 131 LPVs, 3 Meta leads) and old "looking for 5" (EUR 550.74, 70 clicks, 4 Meta leads).
- **New since 14 Oct:**
  - "breaking vika claude", "direct twitter claude" and "breaking julian" (first created 14 Oct, rebuilt 18 Oct).
  - Both IG boosts (16 Oct).
  - The whole OLead #1 ad set (18 Oct).
- The primary text on 5 of the 8 OLead #1 ads (66.5% of OLead #1 spend) is the "ATTENTION: Education Business Owners" text that ends "👇 Watch the free training now." The two "Education Brand Founders" videos use "Free Growth Training + Free Growth Call 🎯 ... Book a 45-min call with Viktorija ...".

## A. FIXES (do now, not tests)

1. **Label the running split.** On `/opt-in-499877`, change `clarity("set","variant","T1-A")` to `clarity("set","variant","T1-B")`. Add B's start date in the "LPCR A/B tests" tab (row 8 has no date). Until then, nobody can read this split in Clarity.
2. **Lead tracking.** Meta counts 8 leads and the sheet logs 34 (12-18 Oct), so Meta sees 24%. The new ad set has to learn on about 1 in 4 real leads. Check that the opt-in form fires Lead on submission (playbook: "Opt-in form ... on submission = Lead") or, if the $10k answer gates it, that Lead fires on the training page. Also check that CAPI sends Lead. Both pages have the `fbq('init', '888978410465183')` line twice. Check with Pixel Helper that PageView fires only once.
3. **Change `<title>` "" (empty, both pages) To "Free Training | Pacow Media".**
4. **Partner count.** Change "45+ EDUCATION LEGENDS ALREADY TRUST US" / "See all 45+ partners" To the confirmed number. The ad text on 5 live ads says "Trusted by 35+ education brands." and the IG post says "45+ education brands". If 45 is right, the ad text is what needs changing (Ema's call).
5. **Guarantee.** Hold any guarantee on the page until the wording is approved. "looking for 5" (29% of OLead #1) promises "And if they don't work... you don't pay!". The docs have a "15-booked-call guarantee" (Team Onboarding) and a "1x ROAS conditional guarantee" (Offer Suite, Tier 2).

## B. A/B TESTS (biggest lift first)

**T1. Headline and subheadline: match the new ads** (replaces the current A vs B headline split)
- Change: "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads" (B), and A "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month" (no subheadline)
- To: Headline "FREE TRAINING: Why Most Education Businesses Struggle to Enroll Students Consistently" / Subheadline "How this 23-year-old uses Meta ads to add 10-20+ new students a month for education brands"
- Why:
  - The headline is the Meta headline on 5 of 8 live OLead ads (66.5% of OLead #1 spend). It is one of the two headlines Ema has been considering.
  - The subheadline copies the "breaking vika claude" image (29%) word for word.
  - "23" is backed by the live IG post: "I'm 23 and run Pacow Media."
  - Playbook rules:
    - "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad"
    - Pre-launch checklist: "pain-led headline"
    - The offer (10-20+ students) stays in the first screen through the subheadline.

**T2. Named results right under the button**
- Change: below "GET ACCESS NOW!" there are only logos and "45+ EDUCATION LEGENDS ALREADY TRUST US".
- To: "Julian: $4k ad spend to $71k revenue · Sarah: $250k in 60 days · Alex: $110k in 90 days", then the logos.
- Why:
  - These are word for word from Pacow's own notes app ad: "Backed by 40+ brands: Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days".
  - The page has no numbers near the form. Index rule 5: "Specificity plus proof beats cleverness."
  - This is already the planned T1-B in the sheet tab.

**T3. Form header and button: use the ads' call to action**
- Change: "Instant access to the free training in 30 sec!" / "GET ACCESS NOW!"
- To: "Watch the free training now" / "WATCH THE FREE TRAINING"
- Why:
  - Five live ads end with "👇 Watch the free training now.", and the "breaking vika" image button says "WATCH NOW →".
  - Process rule: "Button text says what they get".

**T4. Proof-led headline (Ema's idea), run against the T1 winner**
- Change: the T1 winning headline.
- To: "$4k in Ads. $71k in Revenue. Here's the Exact System We Used." Keep the T1 subheadline and the callout pill "Education brands & course creators making $10k+/mo".
- Why:
  - The numbers are Julian's result from Pacow's own notes app ad, so the claim is backed.
  - It runs second because no ad with spend carries it yet ("ed business $4k spend $71k rev" spent EUR 0.36 this week), and T1 matches 2/3 of current spend.
  - If that ad starts to spend, this headline is its page match. Confirm with Julian's numbers that the $71k is revenue from the Pacow-run ads before it goes live.

**T5. Remove the $10k question from the opt-in**
- Change: "Which best describes you? *" with "I'm a business doing less than $10k/mo" / "I'm a business doing $10k+/mo"
- To: First Name, Phone, Email and consent only. Move the $10k question to Q1 of the qualification survey.
- Why:
  - CPL is now EUR 74.71 (7 days, sheet). On 14 Oct it was EUR 49.95. Playbook: "If CPL is already $45-50, don't" (add a pre-qualifier).
  - The callout pill and the "breaking vika" image ("EDUCATION BRANDS & COURSE CREATORS MAKING $10K+/MO") already filter.
  - Run it alone and last. Judge it on LPCR plus pre-qualified and qualified leads per 100 clicks. Move the Lead event to form submit if B goes live.

**Run plan:**
- About 260-330 OLead clicks a week (260 on 12-18 Oct; 47 on 18 Oct alone). At 150 visitors per version, each test takes about 7-9 days.
- First pull GHL per-page stats for the running split, then stop it.
- Bundle T1 + T3 as one B (both copy the ads' own words) against the current `/opt-in`. Then run T2, then T4 against the winner, then T5 alone.
- Clarity labels T1-A/T1-B, T2-A/T2-B and so on. Log every change in the sheet notes (last note 9 Mar).

## NEED FROM EMA

- **GHL funnel stats** for `/opt-in` and `/opt-in-499877` since 14 Oct (page views and opt-ins per step). Clarity can't split them, so GHL is the only way to read the current test.
- **Video audio or transcripts** for "making 10k" (73s) and "1st video ever launched" (37s). `download_hd_url` is null. I only saw frames ("Look,", "guaranteed").
- **Approved guarantee wording** for Pacow's own funnel: "you don't pay", 15 booked calls, or 1x ROAS.
- **Real partner count**: 35 or 45.
- **One test submission** of the opt-in form from a phone. I did not submit (read-only). The Cloudflare Turnstile host on the form was blocked in my sandbox, so I could not confirm the form submits or where Lead fires.
- **Julian's numbers.** Confirm that $4k to $71k is revenue from the Pacow-run ads (for T4).
- **Who added `/opt-in-499877`, and when.** Also, should the IG follower boosts (EUR 157 this week) stay out of the sheet?
- **Ads side (your call, not a page issue):** OLead CPC jumped to EUR 12-21 on 15-17 Oct, which cut page traffic.

---

## Appendix: facts pulled

### LPCR (sheet "(PCW) - Business Reporting Daily Official 2026", Oct tab col E "Link Clicks" and col H "Lead"; Dash tab for months)

- The sheet is filled through 18 Oct. Its clicks match Meta unique link clicks for the OLead campaign.
- 7d (12-18 Oct): 34 / 260 = **13.1%**. Spend EUR 2,540.13, CPL EUR 74.71. Pre-qualified 4, qualified 3.
- 3d (16-18 Oct): 13 / 97 = **13.4%**. Spend EUR 1,381.78.
- Prior week (7-13 Oct): 43 / 303 = **14.2%**. CPL EUR 49.95.
- Daily, 12-18 Oct: leads 8, 3, 8, 2, 1, 5, 7 on 51, 39, 58, 15, 19, 31, 47 clicks.
- Months: Jan 14.4%, **Feb 15.5% (88/568, best)**, Mar 15.4%, Apr 6.9%, May 14.6%, Jun 14.8%, Jul 11.3%, Aug 12.2%, Sep 10.5%, Oct 1-18 12.0% (95/789).
- "LPCR A/B tests" tab:
  - Row 4: "headline: Discover how to add 10-20+ new students every single month" (2026-10-08).
  - Row 7: "FREE TRAINING: The Meta ads system..." (2026-10-14).
  - Row 8: "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads" (no date).
  - The T1-B Clarity snippet is in L2.
  - Stop rule: "about 50+ opt-ins per version ... ahead by 3+ percentage points".

### Meta (account 3720107534883410, OLead campaign by day)

- 12-18 Oct: 283 link clicks, 241 LPVs (load rate 85%), 8 leads.
- 18 Oct: 50 clicks, 40 LPVs, 4 leads.
- OCompleteRegistration: last spend 14 Oct (EUR 116.87, 7 clicks, 2 leads). Now paused.

### Page (loaded 19 Oct, Playwright, desktop 1440x900 and phone 390x844)

- `lp.pacowmedia.com/access?...` redirects to `/opt-in` (6 of 12 loads) or `/opt-in-499877` (6 of 12). UTMs are kept and fill the hidden fields (meta / paid_social / newmay2026 / utm_content).
- **A `/opt-in`:**
  - Callout pill "Education brands & course creators making $10k+/mo".
  - H1 "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month".
- **B `/opt-in-499877`:**
  - Same pill.
  - H1 "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads".
  - Desktop preview GIF shows "Revenue (12 months): $130,001.64".
- **Both pages:**
  - No subheadline.
  - Form header "Instant access to the free training in 30 sec!".
  - Fields: First Name *, Phone * (country picker, default "United States: +1"), Email *, "Which best describes you? *" (2 radios), required consent checkbox.
  - Button "GET ACCESS NOW!".
  - Below the form: training preview GIF, "VIKTORIJA, CO-FOUNDER OF PACOW MEDIA", "45+ EDUCATION LEGENDS ALREADY TRUST US / FEATURED PARTNERS" (College Essay Guy, Examkrackers, Lingua Verna, College Consulting.us), "See all 45+ partners".
  - Footer: "© 2026 MB Pacow Media. All rights reserved.", Terms, Privacy.
  - No guarantee, no named results, no reviews, no mention of the call with Viktorija.
- **Health:**
  - Load about 0.8-1.3s, FCP about 0.8-1.0s, 287 KB.
  - Pixel 888978410465183 PageView fires (init line appears twice).
  - Clarity tag uv3lmuplsf with "T1-A" on both pages.
  - Empty `<title>`.
  - Cloudflare Turnstile on the form.
  - On phone the button top is at 784px of an 844px screen, so it is just visible without scrolling.
  - Terms and privacy links work.
- **Screenshots in /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/pacow/:**
  - optin-desktop.png, optin-mobile.png
  - optin499877-desktop.png, optin499877-mobile.png
  - `-full` versions of each.
  - Ad images in the ads/ subfolder.

### Profile facts (Playbook Index doc 1r8p8hBq..., playbook lines 1-107)

- Offer: Growth OS, a 90-day done-for-you engagement.
- Offer Suite: Tier 1 DIY $5k/12 months; Tier 2 DWY $10k PIF with "1x ROAS conditional guarantee"; Tier 3 DFY $3.5k/mo + 10% of spend.
- Guarantee: "15-booked-call guarantee", conditional on following the process. Rule 13: "the condition is always stated before the number."
- Proof:
  - Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days (notes app ad).
  - "$5M+ in client revenue for 45+ education brands" and "~$45K in ads made my business ~$280K in sales" (live IG posts).
  - Clients: College Essay Guy, Lingua Verna, Zinkerz.
- ICP: US high-ticket education brands and course creators.
- Hard disqualifiers: under $5k/mo, or can't spend $100/day on ads.

### Could not get

- Video audio and transcripts (download URL null).
- link_url from ads_get_creatives (empty). I took the URLs from the Meta preview HTML instead.
- A form submission, the Lead pixel location and the post-submit redirect (read-only; Turnstile host blocked here).
- GHL per-page stats (not available in this session).
- Start date of `/opt-in-499877`.
