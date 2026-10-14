# LPCR review: Cyber6 (Marquis Carroll), 2026-10-14

**Verdict: there is no landing page to review. All 3 live ads open a Meta Instant Form, so the page review stops here. Form LPCR is 27.6% for the last 7 days, above the 20% goal, but it has slid every month since July (33.7% to 25.6%) and the last 3 days hit 20.0%. The bigger risk is what happens after the form. The ad says "skool.com/cyber6", and I can't confirm the form actually sends people into Skool.**

## Where the ads send people
- All 3 creatives are `object_type: SHARE` with `display_link: https://www.skool.com/cyber6`. The API returns no `link_url`.
- Ad preview data for Skool Ad 3 shows `"hasLeadGenFormID": true` with CTA "Learn more". That means an Instant Form.
- Landing page views = null on every ad, while Skool Ad 3 has 105 link clicks and 29 leads. A website destination would log landing page views.
- Meta's trend tool reports the optimized event as "leadgen".
- Conclusion: ad, then Instant Form. No GHL page and no Skool page sit in between. Because of that I took no Playwright screenshots, since there is no page to load.

## LPCR (Meta numbers: the sheet is empty)
LPCR = Meta leads / link clicks, campaign "Cyber6 Skool Community - Leads".

| Period | Spend | Link clicks | Leads | LPCR | CPL |
|---|---|---|---|---|---|
| Last 7d (Oct 7-13) | $141.46 | 105 | 29 | **27.6%** | $4.88 |
| Last 3d (Oct 11-13) | $65.44 | 50 | 10 | **20.0%** | $6.54 |
| Jul (best month) | $1,854.82 | 813 | 274 | **33.7%** | $6.77 |
| Aug | $621.32 | 552 | 160 | 29.0% | $3.88 |
| Sep | $595.12 | 532 | 156 | 29.3% | $3.82 |
| Oct 1-13 | $257.91 | 207 | 53 | 25.6% | $4.87 |

- When it dropped: it fell from 33.7% in July to about 29% in Aug and Sep. In October it fell again to 25.6%, and the last 3 days are 20.0%. That is a slow slide with no single cliff.
- Meta's trend tool flags Skool Ad 3 as "CPR: 54.06% change, Trend: BAD" and "CPM: 58.58% change, Trend: BAD", which means rising costs. Its CTR trend is "GOOD". Meta's benchmark puts the ad set "Cyber6 Community" at "CPR: 24.16% below benchmark", which is better than peers.

## Live ads (last 7 days, ACTIVE)
| Ad | Spend | Link clicks | LPVs | Leads | Share of spend | Load rate | LPCR |
|---|---|---|---|---|---|---|---|
| Skool Ad 3 | $140.90 | 105 | n/a (form) | 29 | 99.6% | n/a | 27.6% |
| Skool Ad 2 | $0.46 | 0 | n/a | 0 | 0.3% | n/a | n/a |
| Skool Ad 1 | $0.10 | 0 | n/a | 0 | 0.1% | n/a | n/a |

- All 3 ads use the same primary text and the same headline (from the FB feed preview). Only the image changes.
- One ad gets all the money. Meta has effectively turned off Ads 1 and 2.

## Fix first (checks, not tests)
- **Check that the form delivers the Skool link.** The ad ends "👉 skool.com/cyber6" and the image buttons say "Join the Community". After submitting, a lead should get a "Join the Community" button to skool.com/cyber6 on the completion screen, plus the same link by email or SMS. If the completion screen only says "thanks", the free community promise breaks right after the opt-in.
- **Check where the leads go.** Nothing in Drive shows a CRM count. Confirm the form is connected to GHL (or a Zapier sheet) and that someone calls or texts them. The playbook says of lead-form leads: "These are the coldest and cheapest leads. Speed and follow-up decide everything."
- **The client sheet is an empty template.** "(C6) - Business Reporting Daily 2026" has only an "Apr" tab with blanks, and it was last modified 2026-05-25. Nothing has been logged since ads started in July.
- **The client profile conflicts with Meta.** The profile says "Ads launched: not yet" and "90-day status: ENDED EARLY". Meta shows about $3,329 spent since July. Ema should confirm whether Pacow is still running this account.
- **There is no qualifier, and the targeting is broad.** The profile defines a qualified lead as "Based in US, Can afford the program, action takers", and the geography as "Global". A $3.82-$6.77 CPL for a $6,000 program is the "freebie seekers" signal in the playbook (rule quoted under T3).
- **Playbook mismatch for later.** The playbook says Lead Form Ads are "Only for brick-and-mortar / local businesses. Online businesses should use the free training funnel." It also says: "not Meta instant forms, which 'only bring in bad quality leads'". This is an ad-strategy call for Ema, so I am only flagging it.

## 5 tests (Instant Form copy and questions, biggest expected lift first)
I could not read the form itself, because no available tool returns Instant Form content. So the "Change" side of each test is a placeholder for whatever is in the form now. Ema should paste the current form text so A can be quoted exactly. Every B is built from the ad's own words.

**T1. Completion screen (thank-you):**
- Change: "<current completion headline / button>"
- To: headline "Access granted. You're in." / body "Tap below to join the free Cyber6 community on Skool. Live mentorship calls, certification courses, and Q&A with cyber pros." / button "Join the Community" linking to skool.com/cyber6
- Why: Ad 2's image says "access granted", every image's button says "Join the Community", and the primary text ends "👉 skool.com/cyber6". The lead should land where the ad promised.

**T2. Form intro headline + description:**
- Change: "<current intro headline>"
- To: headline "Join FREE: The Free Cybersecurity Community" / description "You don't have to break into cyber alone. Live mentorship calls, certification courses, and real Q&A with people already in the field. 100% free to join."
- Why: these are exact words from the ad text, the Ad 3 image ("JOIN FREE.", "You don't have to break into cyber alone.") and the headline "Free Cybersecurity Community". The playbook says "Headlines = the offer", with one name for the freebie everywhere.

**T3. Add one US qualifier (radio):**
- Change: "<no qualifying question>"
- To: "Are you based in the United States?" with answers "Yes" and "No, I'm outside the US". "No" goes to a DQ end page that has no schedule link.
- Why: the profile's qualified lead is "Based in US", and targeting is Global. The playbook rule: "If CPL is $10-20, you SHOULD [add a pre-qualifier]: CPL will climb, 'but that's FINE! You WANT more qualified leads.'" CPL here is $4.88. Also: "Conditional logic: Yes → next question... No → disqualified end page."

**T4. Add one career-changer call-out question (radio, no money talk):**
- Change: "<no second question>"
- To: "Are you looking to break into cybersecurity?" with answers "Yes, I want to start a cyber career" and "No, just browsing"
- Why: the profile offer is "We help career changers start their cybersecurity career within 6 months". The words come from the ad ("Breaking into cybersecurity", "Break into cyber."). Playbook: "B2C: never mention money ('It is a complete drop off moment')". This question does that job without naming a price.

**T5. Form type:**
- Change: "More volume"
- To: "Higher intent" (adds a review/confirm step)
- Why: the playbook says "Form type 'More volume.' Switch to 'Higher intent' if lead quality is bad." Run this only after T1 and T3 tell you whether lead quality is the problem. It will lower LPCR. Judge it on joined members and booked calls, not form fills.

Left out on purpose: "within 6 months" and "We will serve you until you accomplish your goals, no extra costs". Those terms belong to the paid $6,000 program and are not part of the free community offer. The ads never use them, so putting them on the form would mismatch the ad. I also used no student results or numbers, because the profile has none.

## How to run them
- Traffic is about 105 link clicks a week (7d), or 50 in 3 days. At about 150 form-openers per version, one A/B needs about 300 clicks, which is about 3 weeks per test at this budget.
- Bundle T1 and T2 into one "B" form: both are copy-only, low risk and on-message. Run T3 and T4 together as the second test, since both are qualifiers. Run T5 last, alone.
- How to split: duplicate Skool Ad 3 and attach form B to the copy, leaving everything else the same. Name the forms and ads "T1-A" / "T1-B", "T2-A" / "T2-B". Clarity can't track Instant Forms (they live inside Meta), so read results from Meta leads per form plus Skool joins and GHL tags.
- Success metric: Skool members joined and calls booked per $ (from GHL or Skool admin), not form fills alone.
- Nothing has been changed live. All of the above is for Ema to approve.

## Questions for Ema / the client
- Is Pacow still managing Cyber6? The profile says "ENDED EARLY" and "Ads launched: not yet", but the campaign has spent since July.
- What does the Instant Form say now (intro, questions, completion screen)? Does it link to skool.com/cyber6?
- Where do form leads go (GHL, email, CSV)? Is anyone following up?
- How many Skool members joined from ads, and how many booked calls or bought?
- Was anything on the form changed around early August, when LPCR fell from 33.7% to 29%?

---

## Appendix: Facts pulled

**Data sources**
- Meta account 32594844736826895, campaign "Cyber6 Skool Community - Leads". Ad-level last_7d and Oct 11-13 data filtered to ACTIVE, campaign monthly Jan 1-Oct 13 (spend starts in July). Fields: amount_spent, link_click, omni_landing_page_view, lead, creative_id.
- Sheet "(C6) - Business Reporting Daily 2026" (16lKCbxulFNYoSBJUkdjQXRIHyycorRYHUMRNnAHMgYU): tabs "Dash" and "Apr" only. All cells are blank or $0.00, so I used Meta numbers instead.

**Ad copy (identical on all 3 ads)**
- Primary text: "Breaking into cybersecurity alone is brutal — endless roadmaps, no feedback, no one to ask. It doesn't have to be that way. Join a free community of learners and pros figuring it out together. Live mentorship calls, certification courses, and real Q&A with people already in the field. 100% free to join. 👉 skool.com/cyber6"
- Headline (FB feed preview): "Free Cybersecurity Community". The API `title` and `headlines` fields come back empty.
- Description: "100% free to join. Mentorship, courses & Q&A. "
- CTA: "Learn more" (LEARN_MORE)

**Creative images (viewed)**
- Ad 3 (99.6% of spend): "THE FREE CYBERS COMMUNITY", "JOIN FREE.", "You don't have to break into cyber alone.", three tiles "Live mentorship calls" / "Certification courses" / "Q&A with cyber pros", button "Join the Community →".
- Ad 2: terminal-style box "$ join cyber6 --free / > live mentorship calls [ok] / > certification courses [ok] / > q&a with cyber pros [ok] / access granted", headline "Break into cyber. Not by yourself.", tag "[ FREE ACCESS ]", button "Join the Community →", "skool.com/cyber6 no cost, ever".
- Ad 1: "// BREAK INTO CYBERSECURITY", "You don't have to break into cyber alone.", "Join a free community of learners and pros breaking into security together.", same 3 tiles, "Join the Community →", "skool.com/cyber6 100% free to join".
- Ad preview link (Skool Ad 3, Instagram feed): https://business.facebook.com/ads/api/preview_iframe.php?d=AQItJMf9ojCFZmMCpYk_dDnAeBbLTFSyM-P-BHmDseGZxTuQYE65am692Ucmsogr9ZyEGLX2bHOTbPx7Yno5Oi-PTKLiCSMuqGt1ilTFRVZbaki_Lx7DlTAN03nKm_LP4oMm6-k0hKQ3LktjEQEz2bbF1aBWHVvuFaBNJFhvvyZvbu7Sm_eh9QUxfUxQLZy4bWwMzQ5c9gU3Mf3HpMpf_1vH7FpgKfuE6UaFqbKx3sAgTA&t=AQK5OYuA5eN8C22j6x0
- Ads Manager: https://www.facebook.com/adsmanager/manage/ads/edit?act=32594844736826895&selected_ad_ids=120251328421890415

**Page copy**
- None. The ads open a Meta Instant Form, and there is no landing page.

**Profile facts (Client Profile: Marquis Carroll (Cyber6))**
- Offer: "We help career changers start their cybersecurity career within 6 months or we work with you until you accomplish your goals". Programs: "Cyber6 Career Starter Program - $6,000" and "Cyber6 Career Growth Program - $10,000".
- Real guarantee: "We will serve you until you accomplish your goals, no extra costs". This is for the paid program.
- Proof: none listed. The profile has "37" active students and "I have several technical certifications". No results with numbers.
- ICP: "Adults", career changers. Geography: "Global".
- Qualified lead: "Based in US, Can afford the program, action takers".
- Pacow status: "90-day status: ENDED EARLY", "Ads launched: not yet", "Client relationship score: 1/10".

**Could NOT get, and why**
- Instant Form intro, questions, form type and completion screen: no Meta tool here reads lead forms, and the ad preview does not render the form.
- Sheet LPCR: the sheet is an empty template.
- GHL or Skool lead and member counts: not attempted beyond Drive, and there is no evidence the form feeds GHL.
- Meta vs GHL lead comparison: no GHL numbers.
- Landing page screenshots: there is no landing page.
