# LPCR page review: Institute of Pediatric Sleep (IPSP, Violet Giannone)

**Verdict:** It is too early to call this page low. The campaign went live on Oct 13. Day 1 LPCR is 25% (4 leads / 16 clicks), which is above the 20% goal. The real risks are things that will hurt LPCR once traffic grows. There is no Meta pixel on the opt-in page. The page is slow on mobile (about 9 s before it is usable in our test). The form sits below the fold on phones. The page also has no reviews near the form.

**Traffic warning:** Data is tiny. The campaign has spent $37.52 in total, and last_30d returns exactly the same numbers as last_7d, so Oct 13 is the only day with data. None of the numbers below are reliable yet. Treat them as a first read only.

## LPCR numbers (sheet: "(IPS) - Business Reporting B2C", tab "Oct", columns "Link Clicks" and "Lead")

| Window | Spend | Link clicks | Leads | LPCR | CPL |
|---|---|---|---|---|---|
| Last 7d (Oct 7-13) | $36.89 | 16 | 4 | **25.0%** | $9.22 |
| Last 3d (Oct 11-13) | $36.89 | 16 | 4 | **25.0%** | $9.22 |
| Best month 2026 | Oct (only month with data) | 16 | 4 | 25.0% | |

- Oct 13 is the only filled row. Jan to Sep are all zero, so there is no drop yet.
- Oct 14 is not logged yet, which is normal because the sheet logs yesterday each morning.
- Meta now shows $37.52 spend, 20 link clicks (18 unique) and 4 leads. That works out to 20% (all clicks) or 22% (unique). The sheet's 16 clicks were logged earlier, before Meta finished updating.

## Live ads (Meta, act 54671718, level=ad, ACTIVE, last_7d = last_30d)

Campaign "OLead - Free Training - US - 28+". All 5 ads have the same primary text and the same headline. Only the text on the image changes (one pain point per ad).

| Ad | Image hook (first line on creative) | Spend | Share | Link clicks | LPVs | Leads | Load rate | LPCR |
|---|---|---|---|---|---|---|---|---|
| P3 Founder Image | "Still love helping people, but can't keep doing it like this?" | $14.45 | 38.5% | 9 | 3 | 4 | 33% | 44% |
| P2 Founder Image | "Want to earn money without missing more of your kids' lives?" | $14.13 | 37.7% | 6 | 0 | 0 | 0% | 0% |
| P1 Founder Image | "Feel stuck in a job that no longer fits your life?" | $4.00 | 10.7% | 3 | 0 | 0 | 0% | 0% |
| P4 Founder Image | "Worried you'll spend the money and still not know how to find clients?" | $3.07 | 8.2% | 1 | 0 | 0 | 0% | 0% |
| P5 Founder Image | "Not sure which sleep consultant certifications you can actually trust?" | $1.87 | 5.0% | 1 | 0 | 0 | 0% | 0% |
| **Total** | | **$37.52** | | **20** | **3** | **4** | **15%** | **20%** |

- Load rate of 15% looks broken, but Meta records 3 LPVs and 4 leads, and a page view cannot be lower than the leads it produced. The cause is the pixel (see Fix first), so do not judge page speed from this number.
- Meta leads (4) match the sheet (4), so the lead tracking itself works.
- Other old "ACTIVE" ads in the account (2015-2023 boosts and page likes) had no spend and are left out.

## Fix first (these are fixes, not tests)

1. **No Meta pixel on the opt-in page.** The page loads Microsoft Clarity (tag yudjn77jmf) and ActiveCampaign scripts. It makes zero requests to Facebook: no fbq and no fbevents.js, even after waiting 12 s. Meta's 3 LPVs probably come from the next page. Add the pixel (PageView) to the ActiveCampaign page header. Playbook: "paste the full pixel in funnel Settings → head tracking so **PageView** fires on every page." Without it, load rate cannot be measured and Meta has less signal to optimize on.
2. **Slow page.** The page is an ActiveCampaign page (violetsleepbabysleep.ac-page.com/access), not GHL. In our phone test, TTFB was 1.4 s, first paint 3.2 s, DOMContentLoaded 9.2 s and full load 11.8 s. It loads about 26 app scripts from landing-pages-cdn.app-us1.com. Our test ran through a proxy, so real users may get it faster, but please run it through PageSpeed Insights on mobile. On desktop the video box showed a cartoon nurse placeholder until it loaded.
3. **No Privacy Policy or Terms links in the footer.** The footer has only "© 2011–2026 INSTITUTE OF PEDIATRIC SLEEP AND PARENTING LLC. ALL RIGHTS RESERVED." Playbook: "**Terms and privacy policy links in every footer** (required by Facebook...)."
4. **Check the date in the proof line.** The page says "Trusted by 2,000+ students since 2014", but the footer says "© 2011–2026". The strategy doc says "2000 total students" and "10+ years training sleep consultants". Pick one start year.
5. **Re-pull clicks for Oct 13 in the sheet.** The sheet has 16 clicks. Meta now shows 20 clicks (18 unique), and spend changed from $36.89 to $37.52.

Checks that passed:
- Phone field defaults to "United States +1", which matches the US targeting.
- The form has 3 fields (First Name*, Email*, Phone*) plus a required consent checkbox.
- No test data is left in any field.
- UTMs reach hidden fields (field[45]-[48] filled with pcw_freetraining / p3founderimage / paid_social / meta).
- The button "WATCH THE FREE TRAINING" says what you get.
- There is no pre-qualifier and no mention of money (correct for B2C).

## Ad-to-page match

| Item | Ad | Page | Match? |
|---|---|---|---|
| Call-out | "🍼 Moms and Caregivers Ready for Something More" | "FOR MOMS, CAREGIVERS & PEDIATRIC PROFESSIONALS" | Close. The page adds a group the ad never mentions and drops "Ready for Something More" |
| Hook / pain | "Before you spend money on a certification... Watch this free training first." / "how to build a real plan so you don't end up with a certificate and no clients" | Not on the page | **No** |
| Image headline | "Here's How To Become a Sleep Consultant & Build a Flexible Business in as Little as 4 Weeks" | "Learn How To Become a Sleep Consultant & Build a Flexible Business in as Little as 4 Weeks" | Yes (the offer from the strategy doc) |
| Ad headline | "Get Certified as a Sleep Consultant AND Get Clients - FREE Training" | "Get instant access to the free training" | Partly. "Get clients" is missing next to the form |
| Winning pain (P3, all 4 leads) | "I loved nursing. I loved helping families. I just couldn't keep doing it on someone else's schedule." | Only "Taught by a Registered Nurse" | Weak |
| Next step | "Watch the free training. Then book your free Career Call." | No mention of the call | Fine for an opt-in (the call is sold later) |
| Proof | "Violet Giannone @instituteofpediatricsleep" + "After 10+ years in this field" (P5) | "Trusted by 2,000+ students since 2014" + accreditation logos, below the form | Proof sits under the fold and there are no reviews |
| Guarantee | None in the ad | None on the page | OK (playbook: "guarantee lower on the page") |

## Page vs playbook

- Squeeze page elements. Playbook: "logo, call-out, headline, subheadline, **VSL preview GIF**..., short form, Google/Trustpilot reviews block."
  - Has: logo, call-out, headline, subheadline, preview video and a short form.
  - Missing: the reviews block. It has accreditation logos instead.
- Mobile (390x844): the first screen shows the logo, call-out, headline, subheadline and the top of the video. The form card starts at about 870 px and the First Name field at 951 px, so **no form field shows without scrolling**. The button is at 1260 px.
- Form layout. Playbook: "first name + phone (two columns), email full width." Here all three fields are stacked, which makes the form longer on mobile.
- Reading the data. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short." Day 1 sits right at 25%.

## 5 A/B tests (biggest expected lift first)

**T1. Mobile first screen: show the form sooner**
- Change: subheadline "The 3-step process our graduates use to get certified, land their first clients and build a flexible business around their life. Taught by a Registered Nurse and expert faculty, not gurus." and the video above the form on mobile
- To: subheadline "Watch this free training first. Get certified AND get clients, taught by a Registered Nurse." Then put the form card directly under it on mobile, with the video below the form.
- Why: Most traffic comes from Instagram on phones, and right now no form field is visible without scrolling. The new words come from the ad ("Watch this free training first", "Get Certified as a Sleep Consultant AND Get Clients").

**T2. Form heading = the ad's headline and pain**
- Change: "Get instant access to the free training" / "Takes 30 seconds."
- To: "Get Certified as a Sleep Consultant AND Get Clients" / "A certification alone won't get you clients. The right plan will."
- Why: The ad headline and the ad's main pain ("a certificate and no clients") never appear on the page. This reuses the ad's exact words. Playbook rule: "headline/offer must match the ad."

**T3. Proof next to the button**
- Change: "Trusted by 2,000+ students since 2014" (below the form, off screen)
- To: right under "WATCH THE FREE TRAINING": "2,000+ students trained. Graduates featured on NBC, FOX, Today's Parent, Forbes & GMA." Then add 3 short graduate reviews copied word for word from instituteofpediatricsleep.com/institute-of-pediatric-sleep-and-parenting-reviews/.
- Why: The playbook asks for a reviews block on the squeeze page, and the page has none. Both stats are approved in the strategy doc ("2000 total students", "Grads Featured on NBC, FOX, Today's Parent, Forbes, & GMA").
- Left out on purpose: "Graduates report annual incomes ranging $60,000-$160,000, with highest earner making $600k". These are earnings claims that need proof and a disclaimer before going on a cold opt-in page.

**T4. Call-out = the ad's first line**
- Change: "FOR MOMS, CAREGIVERS & PEDIATRIC PROFESSIONALS"
- To: "FOR MOMS AND CAREGIVERS READY FOR SOMETHING MORE"
- Why: These are the exact words of the ad's first line. Playbook: "Call-out line on the first 3 pages, kept to one line."

**T5. The winning pain (P3, nurse) above the form**
- Change: "VIOLET GIANNONE, RN · FOUNDER OF IPSP®"
- To: "VIOLET GIANNONE, RN · FOUNDER OF IPSP®" plus one line under it: "I loved nursing. I loved helping families. I just couldn't keep doing it on someone else's schedule. So I found a way to keep helping families on my own terms."
- Why: P3 got all 4 leads (44% LPCR on 9 clicks), and this line is copied word for word from the P3 creative.
- Guarantee: the approved guarantee from the strategy doc ("If you don't land any clients at all, I'll keep working with you until you do, at no additional cost") stays off the opt-in page for now. The client profile (Sep 1) says "we currently don't have a guarantee", so confirm with Violet first. Once confirmed, it belongs lower on the page or the training page (playbook: "guarantee lower on the page").

## How to run them

- Traffic: about 16-20 clicks a day at the current ~$37/day, so about 115-140 clicks a week. At the planned $3,000/month (~$100/day, CPC $2.31) it would be about 300 clicks a week.
- Each test needs about 150 visitors per version (300 total). That is about 2-2.5 weeks per test at today's spend, or about 1 week at $100/day.
- Do the 5 fixes first, then collect 1 week of baseline. Day 1 is already at goal, so do not change the page on one day of data.
- Bundle because traffic is low:
  - Version B1 = T1 + T4 (mobile first screen + call-out)
  - Version B2 = T2 + T3 (form heading + proof)
  - Version B3 = T5
- Clarity is already on the page (tag yudjn77jmf). Label sessions T1-A / T1-B (B1), T2-A / T2-B (B2), T3-A / T3-B (B3), and watch mobile scroll depth to the form.

## Questions for Ema / Violet

1. Where does the Meta Lead event fire today: training page, CAPI or Zapier? Meta counts 4 leads but there is no pixel on the opt-in page.
2. Is the strategy-doc guarantee approved to use in public copy? The profile says there is no guarantee.
3. Is "since 2014" or 2011 the right start year for "2,000+ students"?
4. Which 3 graduate reviews from the reviews page should go near the form?
5. The strategy says US + Canada, but the campaign is US only. Is that intended? (The page phone default is US, which is fine for now.)
6. Once there are 2+ weeks of leads: CPL is $9.22. The playbook says "If CPL is $10-20, you SHOULD" add a pre-qualifier. Should we test "Do you know what a sleep consultant does?" later, given the profile's qualified-lead rule ("maybe knows what a sleep consultant is")?

---

## Appendix: Facts pulled

**LPCR (sheet "(IPS) - Business Reporting B2C", id 1gEF5m_tq_UkkBfkJDcnIN3bJK8b4n8lTig0FcTSXNZU, tab Oct, cols "Adspend (USD)", "Link Clicks", "Lead")**
- Oct 13: $36.89 spend, 1,011 impressions, 16 link clicks, CTR 1.58%, CPC $2.31, 4 leads, 0 pre-qualified, 0 qualified, 0 calls, CPL $9.22. CPM is $36.49, above the playbook's $30 flag, but that is an ad/audience issue.
- Every other day of 2026 is empty. Dash tab: Jan-Sep all 0.

**Ad copy (identical primary text on all 5 ads, from the ad previews)**
> 🍼 Moms and Caregivers Ready for Something More
> Before you spend money on a certification...
> Watch this free training first.
> Learn:
> ✔ What actually makes a sleep consultant certification credible
> ✔ How to avoid picking the wrong program
> ✔ How to build a real plan so you don't end up with a certificate and no clients
> ✔ How to fit this around naps, school pickup, or clients you already have
> A certification alone won't get you clients. The right plan will.
> 🎥 Watch the free training. Then book your free Career Call.
> 👇 Tap to watch and book.

- Headline: "Get Certified as a Sleep Consultant AND Get Clients - FREE Training". CTA: Learn more.
- Creative: the same founder photo on every ad, titled "Here's How To Become a Sleep Consultant & Build a Flexible Business in as Little as 4 Weeks 👇", with a different story per ad.
  - P1: "Feel stuck in a job that no longer fits your life? I was too. I spent over a decade working hospital shifts, picking between my career and my family. Then I built a sleep consulting business around my life. In this free training, I'll walk you through the 3 steps I used, so you can see if it fits yours."
  - P2: "Want to earn money without missing more of your kids' lives? On Christmas Day 2005, I was crying and begging to leave a shift early. I missed too many moments I couldn't get back. Now I work from my kitchen table and drop everything when my kids need me. In this free training, I'll show you what that work life looks like and how to start building it."
  - P3: "Still love helping people, but can't keep doing it like this? I loved nursing. I loved helping families. I just couldn't keep doing it on someone else's schedule. So I found a way to keep helping families on my own terms. In this free training, I'll show you how, step by step."
  - P4: "Worried you'll spend the money and still not know how to find clients? It's the fear I hear most from the women I talk to. In this free training, I'll show you how women go from certified to booked with real families, and where most of them get stuck."
  - P5: "Not sure which sleep consultant certifications you can actually trust? After 10+ years in this field, I've seen a lot of programs taught by people with no medical background. In this free training, I'll show you what to look for before you spend a dollar."
- Landing URL (from the preview link): https://violetsleepbabysleep.ac-page.com/access?utm_source=meta&utm_medium=paid_social&utm_campaign=pcw_freetraining&utm_content=p3founderimage

**Page copy (loaded Oct 14 with Playwright; screenshots oct14/ipsp-desktop.png and oct14/ipsp-mobile.png)**
> FOR MOMS, CAREGIVERS & PEDIATRIC PROFESSIONALS
> Learn How To Become a Sleep Consultant & Build a Flexible Business in as Little as 4 Weeks
> The 3-step process our graduates use to get certified, land their first clients and build a flexible business around their life. Taught by a Registered Nurse and expert faculty, not gurus.
> VIOLET GIANNONE, RN · FOUNDER OF IPSP®
> Get instant access to the free training / Takes 30 seconds.
> First Name* / Email* / Phone* (United States +1) / [required] I consent to receive emails and SMS messages regarding my submission and related updates.
> WATCH THE FREE TRAINING
> Your info is safe with us. Unsubscribe any time.
> Trusted by 2,000+ students since 2014 / ACCREDITED & RECOGNIZED BY / Led by a Registered Nurse / Accredited certification / Free, instant access / Self-paced, from home / [logos: RN, American Association of Drugless Practitioners, ICES, AASM member, Approved Training Provider, IACSC]
> © 2011–2026 INSTITUTE OF PEDIATRIC SLEEP AND PARENTING LLC. ALL RIGHTS RESERVED.

- Mobile positions: form heading about 870 px, First Name 951 px, button 1260 px, viewport 844 px.
- Speed (iPhone 13 emulation): TTFB 1.4 s, FCP 3.2 s, DCL 9.2 s, load 11.8 s.
- Tracking on the page: Clarity yes, Meta pixel no.

**Profile and strategy facts**
- Offer (strategy doc): "Become a Sleep Consultant & Build a Flexible Business In As Little as 4 Weeks." Profile: "We help women work from home as certified baby sleep consultants in as little as 30 days (we've been selling it as 4-6 weeks...)".
- Guarantee: the strategy doc (marked approved) says "go through the training, do the work, show up to mentorship, and follow the steps. If you don't land any clients at all, I'll keep working with you until you do, at no additional cost." The profile (Sep 1) says "we currently don't have a guarantee". Confirm before using.
- Proof (strategy doc, marked approved): 10+ years training sleep consultants; 15+ years clinical/nursing; 2000 total students; grads hired by companies like Sleep Shop OC; brand deals (Newton Baby, Nanit, 4Moms, Kinedu, Frida); grads featured on NBC, FOX, Today's Parent, Forbes, GMA. Income claims ($60k-$160k, $600k) are left out of the tests.
- ICP: adult students (18+), women working from home; buyers are the students themselves. The campaign targets US 28+.
- Qualified lead: "Can afford 4k, maybe knows what a sleep consultant is."
- Product: the sleep consultant certification (plus bundles), about $4k, on Thinkific, with 6 months of 1:1 mentorship after the course.

**Could not get**
- More than 1 day of data. The campaign started Oct 13, so last_30d = last_7d, there is no best month and no drop to date.
- Unique link clicks per day in the sheet. The sheet logs "Link Clicks" only, so I used it as the denominator.
- Separate primary texts per ad. The previews show the same text on all 5, and ads_get_creatives returned no body/title/link_url for these creatives. If the ads use several primary texts, only the first one was visible.
- Real-world load speed. The test ran through a proxy, so confirm with PageSpeed Insights.
- Funnel stats per step (opt-in to training page). The page is on ActiveCampaign, not GHL, and I have no ActiveCampaign access.
- Review quotes. I did not copy any reviews, so Ema or Violet should pick 3 from the reviews page.
