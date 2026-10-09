---
name: lpcr-review
description: LPCR page review for a Pacow Media client. Use when Ema asks for an "LPCR review", "page review", "landing page deep dive", or asks why a client's page visitors aren't opting in. Read-only audit that ends with 5 A/B tests.
---

# LPCR page review: [CLIENT NAME]

Goal: find why page visitors aren't opting in (LPCR = leads ÷ link clicks, goal 20%, under 15% = bad) and give 5 A/B tests to fix it. Read-only. Don't change anything live.

## STEP 1. Pull the facts first (don't skip any)
- LPCR: last 7 days, last 3 days, and the best month this year, from the client's sheet (follow CLAUDE.md data steps). Note when it dropped.
- Live ads: from Meta (ads_get_ad_entities, level=ad, last 14 days, effective_status=ACTIVE). Get spend, link clicks, landing page views, leads per ad, and the share of spend per ad.
- Ad copy: pull the primary text and headline of the ads actually spending (ads_get_creatives, or ads_get_ad_preview). If Meta is blocked, use the ad files Ema shares.
- Client profile: "01. Clients → 00. Client Profiles (Claude)" in Drive. Get the offer, the real guarantee, proof/results, ICP, what makes a lead qualified.
- Page: Ema pastes the text and a screenshot. If GHL funnel stats are available, use page views → opt-ins per step.
- Playbook rules: "Pacow Playbook (from Skool)" in Drive (Free Training funnel, Setting up your forms, Conversion Ads). Follow it, not generic advice.

## STEP 2. Health checks before any copy talk
- Load rate: landing page views ÷ link clicks. Under ~80% = slow or broken page; flag it.
- Form check: default country on the phone field (must match the target country), required fields, broken dropdowns, test-data left in fields.
- Leads in Meta vs GHL: if Meta counts far fewer than GHL, flag tracking. Judge LPCR on GHL/sheet numbers.

## STEP 3. Ad-to-page match (the main event)
Put the ad and the page side by side and check each item. Quote both exactly.
1. Call-out: who the ad speaks to vs who the page says it's for.
2. Pain / hook: the problem the ad names. Does the page mention it in the first screen?
3. Promise / offer: what the ad says they'll get (free training, one-pager, roadmap, call). Same name and same thing on the page and on the button?
4. Proof: names, numbers and results in the ad. Do the same ones appear on the page near the form?
5. Guarantee: ad wording vs page wording vs the client's real terms. Flag any mismatch or weaker version.
6. Numbers: any stat that differs between ad and page (e.g. 35+ vs 40+ brands), or doesn't fit the offer (ACT stat on an SAT page).

## STEP 4. Page review against the playbook
- Headline = the offer ("Get X in X time, or guarantee"), same on every page.
- Form friction: count fields. Pre-qualifier rules from the playbook: none in competitive markets (test prep, college consulting); none when CPL is over $45-50; B2C never mentions money on the opt-in.
- Button text says what they get (not "Get Started" / "Submit"). One name for the freebie everywhere.
- Proof near the form: results with real numbers, parent reviews first when parents are the buyer.
- Squeeze page elements from the playbook: call-out, headline, subheadline, preview GIF/image of the freebie, short form, reviews block.
- Mobile: is the form visible without scrolling? (Most traffic is Instagram on phones.)

## STEP 5. Output (chat, short, plain English, no em dashes)
- One-line verdict first: the main reason LPCR is low.
- Table of live ads: spend, clicks, page views, leads, share of spend.
- "Fix first" list: broken things that aren't tests (flags, wrong guarantee, wrong stats).
- 5 A/B tests, biggest expected lift first. Each one: A (now, quoted) / B (exact new copy) / Why (tied to the ad or a playbook rule).
- How to run them: based on weekly clicks, how long each test needs (about 150 visitors per version), which tests to bundle into one version when traffic is low, and Clarity labels (T1-A / T1-B, T2-A / T2-B).
- Questions for Ema or the client (e.g. "was this form field added when LPCR dropped?").

## Rules
- Quote real copy, use real numbers, don't invent results or guarantees.
- Check the client's offer in their profile before writing any client-facing copy.
- Ema chooses the ad map, so suggest page changes, not new ad strategy.
