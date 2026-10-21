# LPCR deep dive: Pacow Media opt-in page, 21 Oct 2026

**Pacow**: LPCR 7d 11.9% (30/252), 3d 10.9% (14/129), prior week 14.2% (43/303). It went down. The main reason: the page has not changed since 19 Oct, and it still does not match the ad now taking 67% of OLead spend. "breaking vika claude" sells "HOW THIS 23-YEAR-OLD USES META ADS TO ADD 10-20+ NEW STUDENTS A MONTH FOR EDUCATION BRANDS". Its Meta headline is "Why Most Education Businesses Struggle to Enroll Students Consistently". The page leads with a different headline, shows no proof near the form and still asks a $10k revenue question while CPL is EUR 85.75.

Goal is about 15%. From 11.9% that is about 3 more leads per 100 clicks.

Tracking caveat: on 19-20 Oct, Meta counted 12 OLead leads and the sheet logged 7 on the same 82 clicks. If the sheet is missing leads, the real 3d LPCR could be about 14-15%. Check GHL before judging the drop (see NEED FROM EMA).

## Changed since Oct 19

- Clarity label on `/opt-in-499877` (T1-A to T1-B): **not done.** Both pages still run `clarity("set","variant","T1-A")`. The split is still live: 12 loads of `/access` went 5 to `/opt-in` and 7 to `/opt-in-499877`.
- Lead tracking: **changed, cause unclear.** For 14-20 Oct, Meta counts 18 OLead leads and the sheet logs 30 (60%, up from 24%). On 19-20 Oct Meta is now higher than the sheet (12 vs 7). Both pages still have `fbq('init', '888978410465183')` twice.
- Empty `<title>`: **not done** (both pages).
- Partner count, "Trusted by 35+ education brands." in the ads vs "45+ EDUCATION LEGENDS ALREADY TRUST US" on the page: **not done.**
- Guarantee: **not done.** The "looking for 5" image still says "And if they don't work... you don't pay!". The page has no guarantee.
- T1 headline/sub, T2 results strip, T3 form header/button, T4 proof headline, T5 remove the $10k question: **none done.** Page text, form and layout are word for word the same as on 19 Oct.
- Ads side, for context:
  - "ed business + course - making 10k" (OLead #1) is now PAUSED after EUR 127.26, 9 clicks, 1 Meta lead.
  - "breaking vika claude" now carries 66.9% of OLead #1 spend.
  - **New since 19 Oct:** "20 oct" in "oMessage - Fast Cash - IG Retargeting - Oct 20" (created 20 Oct, EUR 9.68). It goes to Instagram DMs, not to the page. Its copy has a new offer: "Not a fit? Your $500 comes back."

## Live ads (ACTIVE, last 7 days = 14-20 Oct, EUR)

The OLead #1 ads were created on 18 Oct, so they have 3 days of data. Share is of all active spend (EUR 1,079.32), with share of OLead #1 (EUR 751.40) in brackets. Clicks are unique link clicks.

| Ad | Spend | Clicks | LPVs | Meta leads | Share | Load rate | Meta LPCR | Headline | Hook (creative) |
|---|---|---|---|---|---|---|---|---|---|
| breaking vika claude (static) | 502.63 | 69 | 62 | 10 | 46.6% (66.9%) | 90% | 14.5% | "Why Most Education Businesses Struggle to Enroll Students Consistently" | "HOW THIS 23-YEAR-OLD USES META ADS TO ADD 10-20+ NEW STUDENTS A MONTH FOR EDUCATION BRANDS" |
| ed brands im looking for youn 100k A1 (static) | 199.30 | 21 | 20 | 1 | 18.5% (26.5%) | 95% | 4.8% | same | "I'm looking for 5 education brands who want to scale to $100k+/mo in 2026 with paid ads" / "And if they don't work... you don't pay!" |
| IG post "Follow @viktorijazykas if you..." (video) | 136.38 | 27 | n/a | 0 | 12.6% | n/a | n/a | none | "Education brands & course creators" |
| IG post "Follow @viktorijazykas for daily..." (video) | 135.80 | 93 | n/a | 0 | 12.6% | n/a | n/a | none | "Education brands & course creators" |
| ed business - 1st video ever launched (video) | 35.00 | 3 | 1 | 0 | 3.2% (4.7%) | 33% | 0% | same | frame caption "guaranteed" (audio not available) |
| Hammer Them Retargeting (8 ads) | 46.06 | 0 | 0 | 0 | 4.3% | | | | |
| 20 oct (oMessage, IG DM) | 9.68 | 10 | n/a | 0 | 0.9% | | | | |
| breaking julian / direct twitter claude / watch before you run ads / $4k spend $71k rev | 14.47 | 0 | 0 | 0 | 1.3% (1.9%) | | | | |

- All OLead #1 ads use the same primary text. It opens "ATTENTION: Education Business Owners 🎓" and ends "Trusted by 35+ education brands. / After watching, you can book a free strategy call to see if we're a fit. / 👇 Watch the free training now." It names the freebie "🎥 Watch Our Free Student Acquisition Training".
- Both page ads go to `lp.pacowmedia.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=newmay2026&utm_content=<ad>` (breakingvika, edbrandslookingforyoung100k).
- The IG boosts go to the Instagram profile (CTA "VIEW_INSTAGRAM_PROFILE"), so they are left out of the page match. The retargeting and oMessage ads are left out too (per brief).
- Paused ads that spent in the 7 days (old "OLead - OFF" set, 14-17 Oct): "1st video ever launched" EUR 984.36, 71 clicks, 1 Meta lead; "looking for 5" EUR 496.68, 52 clicks, 4 Meta leads.
- "looking for 5" is a direct done-for-you offer ("We'll script, edit, and launch your ads in 14 days") that sends people to a free training page. It has 4.8% Meta LPCR on 21 clicks. The sample is small. Ema decides the ad map, so this is a flag only.

## A. FIXES (do now, not tests)

1. **Reconcile leads for 18-20 Oct before reading this week's drop.** Meta has 4, 7, 5 OLead leads. The sheet has 7, 3, 4. Clicks match exactly (47, 46, 36). Pull GHL contacts with utm_medium = paid_social for those days. If the sheet is short, fix the sheet. If Meta is high, look at the double `fbq('init', '888978410465183')` line (see fix 4). Playbook: "DO NOT USE FACEBOOK TO TELL YOU HOW MANY LEADS YOU GOT".
2. **Label or stop the running split.** On `/opt-in-499877`, change `clarity("set","variant","T1-A")` to `clarity("set","variant","T1-B")`. Better still: pull GHL page views and opt-ins per page since 14 Oct, then stop the split. Neither headline matches the ads now running, and T1 below replaces both.
3. **Partner count.** Change "45+ EDUCATION LEGENDS ALREADY TRUST US" and "See all 45+ partners" to the confirmed number. All 7 OLead #1 ads say "Trusted by 35+ education brands." The IG post says "45+ education brands". If 45 is right, the ad text is what needs changing (Ema's call).
4. **Pixel.** Remove the second `fbq('init', '888978410465183')` line on both pages. Check with Pixel Helper that PageView and Lead each fire once. Playbook: "Opt-in form ... on submission = **Lead**".
5. **Change `<title>` "" (empty, both pages) To "Free Student Acquisition Training | Pacow Media".**
6. **Guarantee.** Keep any guarantee off the page until the wording is approved. Right now, 26.5% of OLead #1 spend promises "And if they don't work... you don't pay!" and the page never mentions it. The docs have "15-booked-call guarantee" (Team Onboarding) and "1x ROAS conditional guarantee" (Offer Suite, Tier 2). The new DM ad has "Not a fit? Your $500 comes back." These are three different terms.

## B. A/B TESTS (biggest lift first)

**T1. Headline and subheadline: copy the top ad**
- Change: "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month" (and the B page's "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads"), with no subheadline
- To: Headline "FREE TRAINING: How This 23-Year-Old Uses Meta Ads to Add 10-20+ New Students a Month for Education Brands" / Subheadline "Why most education businesses struggle to enroll students consistently"
- Why:
  - The headline is the "breaking vika claude" image word for word (66.9% of OLead #1 spend).
  - The subheadline is the Meta headline on every OLead #1 ad.
  - This flips the order proposed on 19 Oct. Playbook: creative comes first ("Order of importance: 1) creative, 2) headline, 3) ad copy") and "Headline = the offer". The image line carries the offer (10-20+ students). The Meta headline only carries the pain.
  - Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad".
  - "23" is backed by the live IG post: "I'm 23 and run Pacow Media."

**T2. Form header and button: one name for the freebie, same CTA as the ad**
- Change: "Instant access to the free training in 30 sec!" / "GET ACCESS NOW!"
- To: "Watch the Free Student Acquisition Training now" / "WATCH THE FREE TRAINING"
- Why:
  - The ad text says "🎥 Watch Our Free Student Acquisition Training" and "👇 Watch the free training now.". The image button says "WATCH NOW →".
  - Process rule: "Button text says what they get". One name for the freebie everywhere.

**T3. Named results right under the button**
- Change: below "GET ACCESS NOW!" there are only logos and "45+ EDUCATION LEGENDS ALREADY TRUST US"
- To: "Julian: $4k ad spend to $71k revenue · Sarah: $250k in 60 days · Alex: $110k in 90 days", then the logos
- Why:
  - Word for word from Pacow's own notes app ad ("Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days"). It is already the planned B in the sheet's "LPCR A/B tests" tab.
  - The page has no numbers near the form. Index rule 5: "Specificity plus proof beats cleverness."

**T4. Add the ad's 3 "inside" bullets under the subheadline**
- Change: nothing between the headline and the form
- To: "✅ How education brands consistently add 10–20+ students per month / ✅ Why most enrollment problems are really systems problems / ✅ What makes paid student acquisition actually work"
- Why:
  - These are the first 3 bullets of the primary text on 100% of OLead #1 ads. The page currently tells the visitor nothing about what the training covers.
  - Keep it to 3 lines so the button stays in the first phone screen. Playbook: "the page should be short". Right now the button top sits at 784px of an 844px phone screen, so check B on a phone first. If it pushes the button down, place the bullets under the button.

**T5. Remove the $10k question from the opt-in**
- Change: "Which best describes you? *" with "I'm a business doing less than $10k/mo" / "I'm a business doing $10k+/mo"
- To: First Name, Phone, Email and consent only. Move the $10k question to Q1 of the qualification survey.
- Why:
  - CPL is EUR 85.75 (7d) and EUR 80.77 (3d), almost twice the sheet max of $45. Playbook: "If CPL is already $45-50, don't" (add a pre-qualifier).
  - The callout pill and the vika image ("EDUCATION BRANDS & COURSE CREATORS MAKING $10K+/MO") already filter.
  - Run it alone and last. Judge it on LPCR plus pre-qualified and qualified leads per 100 clicks (7d: 9 pre-qualified, 2 qualified). If B goes live, fire Lead on form submit.

**Run plan:** About 250 OLead clicks a week (252 on 14-20 Oct, 36-47 a day lately). At 150 visitors per version, each test takes about 8-9 days. Stop the current split after the GHL pull. Then bundle T1 + T2 as one B against the current `/opt-in` (both copy the ad's own words). Then run T3, then T4 against the winner, then T5 alone. Use Clarity labels T1-A/T1-B and so on, and log each change in the sheet notes.

## NEED FROM EMA

- **GHL opt-ins for 18, 19 and 20 Oct** (utm_medium = paid_social, by day and by utm_content). Meta has 16 leads and the sheet has 14, and on 19-20 Oct Meta has more than the sheet (12 vs 7). I need this to know whether LPCR really dropped.
- **GHL funnel stats per page** for `/opt-in` and `/opt-in-499877` since 14 Oct (page views, opt-ins). Clarity can't split them because both pages are tagged T1-A.
- **One test submission from a phone** (read-only here, so I did not submit). Confirm that Lead fires once and where the page sends people after submit.
- **Real partner count**: 35 or 45.
- **Approved guarantee wording** for Pacow's own funnel: "you don't pay", 15 booked calls, 1x ROAS, or the $500 trial refund.
- **Julian, Sarah and Alex results**: confirm they can go on the page as written in the notes app ad (for T3).
- **Video audio or transcript** for "1st video ever launched" (still live, 4.7% of OLead #1). I only have frames.
- **Who paused "making 10k", and why.** Is the "20 oct" Fast Cash trial the offer the strategy call now sells? If so, the page and ads say nothing about it yet.

---

## Appendix: facts pulled

### LPCR (sheet "(PCW) - Business Reporting Daily Official 2026", Oct tab col E "Link Clicks", col H "Lead"; Dash tab for months)

- The sheet is filled through 20 Oct (21 Oct is empty). Its clicks match Meta unique link clicks for the OLead campaign every day.
- 7d (14-20 Oct): 30 / 252 = **11.9%**. Spend EUR 2,572.56, CPL EUR 85.75. Pre-qualified 9, qualified 2.
- 3d (18-20 Oct): 14 / 129 = **10.9%**. Spend EUR 1,130.71, CPL EUR 80.77. Pre-qualified 7, qualified 0.
- Prior week (7-13 Oct): 43 / 303 = **14.2%**. CPL EUR 49.95.
- Daily, 14-20 Oct: leads 8, 2, 1, 5, 7, 3, 4 on 58, 15, 19, 31, 47, 46, 36 clicks.
- Oct 1-20: 102 / 871 = 11.7%. Best month: Feb 15.5% (88/568).
- Sheet notes: 7 Oct "new A/B test launched"; 14 Oct "paused complete reg / launched new ads"; 18 Oct "dupped adset and turned off the OG / budget 300$". There is no note for 19-20 Oct.
- "LPCR A/B tests" tab: same as on 19 Oct. Row 8 headline "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads" still has no date. The T1-B Clarity snippet is in the tab but not on the page.

### Meta (account 3720107534883410, EUR)

- OLead campaign by day, 14-20 Oct:
  - Unique clicks 58, 15, 19, 31, 47, 46, 36 (252).
  - LPVs 55, 13, 20, 29, 40, 40, 32 (229): **load rate 91%**.
  - Leads 1, 0, 0, 1, 4, 7, 5 (18).
- OCompleteRegistration: campaign PAUSED. Its last leads were on 14 Oct (2) and 16 Oct (1), so the OCompleteReg sheet was not used.
- Per-ad numbers are in the table above.

### Page (loaded 21 Oct, Playwright, desktop 1440x900 and phone 390x844)

- `lp.pacowmedia.com/access?...` redirects to `/opt-in` (5 of 12 loads) or `/opt-in-499877` (7 of 12). UTMs reach the hidden fields (meta / paid_social / newmay2026 / breakingvika).
- A `/opt-in`: callout pill "Education brands & course creators making $10k+/mo". H1 "FREE TRAINING: The Meta ads system that gets education brands 10-20+ new students every month".
- B `/opt-in-499877`: same pill. H1 "FREE TRAINING: Add 10-20 New Students Every Month With Meta Ads".
- Both pages:
  - No subheadline.
  - Form header "Instant access to the free training in 30 sec!".
  - Fields: First Name *, Phone * (country picker, default "United States: +1", matches US targeting), Email *, "Which best describes you? *" (2 radios, none preselected), required consent checkbox "I agree to the Terms & Conditions provided by Pacow Media. By providing my phone number, I consent to receive text messages from Pacow Media. Reply STOP to opt out. View our Terms & Privacy Policy." No prefilled test data.
  - Button "GET ACCESS NOW!".
  - Below the form: training preview GIF (tap scrolls to the form), "VIKTORIJA, CO-FOUNDER OF PACOW MEDIA", "45+ EDUCATION LEGENDS ALREADY TRUST US / FEATURED PARTNERS" (College Essay Guy, Examkrackers, Lingua Verna, College Consulting.us), "See all 45+ partners" (expands, works).
  - Footer: "© 2026 MB Pacow Media. All rights reserved. Made with ♥ for education legends · Terms · Privacy" (links work).
  - No guarantee, no named results, no reviews, no mention of the strategy call, no "Student Acquisition Training" name.
- Health:
  - TTFB about 0.35s, FCP about 0.77s, load about 0.9s, 290 KB. Fast.
  - Pixel 888978410465183 PageView fires. The init line appears twice.
  - Clarity tag uv3lmuplsf with "T1-A" on both pages.
  - Empty `<title>`.
  - The Cloudflare Turnstile iframe loads.
  - On phone the button top is at 784px of an 844px screen, so it is just visible without scrolling.
- Screenshots in /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/pacow/:
  - optin-desktop.png, optin-mobile.png
  - optin499877-desktop.png, optin499877-mobile.png
  - `-full` versions of each.
  - Ad images in ads/ (vika.jpg, look5.jpg).

### Profile facts (Playbook Index doc 1r8p8hBq..., playbook lines 1-107)

- Offer: Growth OS. Offer Suite: Tier 1 DIY $5k/12 months; Tier 2 DWY $10k PIF with "1x ROAS conditional guarantee"; Tier 3 DFY $3.5k/mo + 10% of spend.
- Guarantee: "15-booked-call guarantee" (conditional). Rule 13: "the condition is always stated before the number."
- Proof:
  - Julian $4k ad spend to $71k rev, Sarah $250k in 60 days, Alex $110k in 90 days (notes app ad).
  - "$5M+ in client revenue for 45+ education brands and course creators" and "~$45K in ads made my business ~$280K in sales" (live IG posts).
- ICP: US high-ticket education brands and course creators.
- Hard disqualifiers: under $5k/mo, or can't spend $100/day on ads.

### Could not get

- A form submission, the Lead event location and the post-submit redirect (read-only).
- GHL lead and per-page stats (no GHL access used in this session).
- Video audio for "1st video ever launched". IG post frames were reused from the 19 Oct capture (same ads, created 16 Oct).
- link_url from ads_get_creatives (empty). I took the URLs from the Meta preview HTML instead.
