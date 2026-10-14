# LPCR page review: Lingua Verna (Alex Willson)

Date: 2026-10-14. Page reviewed: https://linguaverna.com/access (the real live URL, confirmed from the ad preview's display link for the top ad).
Screenshots: oct14/lingua-verna-desktop.png, oct14/lingua-verna-mobile.png (full-page versions: -desktop-full.png, -mobile-full.png).

## Verdict
The page never says what the ad promised. The video sells "the free Levantine Arabic Roadmap" to people whose "partner's family speaks Levantine Arabic". The page says "FOR ADULTS WHO WANT TO SPEAK LEVANTINE ARABIC", "Training access in just 30 sec!" and a "Submit" button. The word "Roadmap" and the word "free" appear nowhere on the page. On top of that, a 15.8 MB preview GIF slows the page on phones (load rate 79%). LPCR has sat at 9 to 12% since launch in June. It has not dropped. It has never been near the 20% goal.

## LPCR (sheet, leads / link clicks)
| Window | Clicks | Leads | LPCR |
|---|---|---|---|
| Last 7 logged days (Oct 6-12) | 1,656 | 173 | **10.4%** |
| Last 3 logged days (Oct 10-12) | 669 | 85 | **12.7%** |
| Best month: Jun (from Jun 8) | 2,893 | 351 | **12.1%** |
| Jul / Aug / Sep / Oct 1-12 | 8,174 / 11,285 / 9,679 / 3,044 | 850 / 1,086 / 915 / 326 | 10.4% / 9.6% / 9.5% / 10.7% |

- The sheet has no row for Oct 13 yet, so I used the latest 7 and 3 logged days.
- No real drop. By week it has moved between 7.5% (Jul 13 week) and 13.7% (launch week, Jun 8). It has been about 10% since late July.
- Goal is 20% and anything under 15% counts as bad. Playbook: "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad; cut friction; the page should be short."

**What "Lead" means in the sheet: the opt-in, not the booked call.** The sheet logs "Lead" (col H), "Pre-Qualified Leads", "Qualified Lead" and calls booked in separate columns. Last 7 days it shows 173 leads, 157 pre-qualified, 37 qualified and 28 booked. Meta shows 175 leads for Oct 7-13, which is almost the same as the sheet's 173 opt-ins, so Meta's Lead event also fires on the opt-in. Tracking looks fine. Meta is not undercounting.

## Live ads (Meta, last 7 days, Oct 7-13, ACTIVE, main campaign "OLead//LV//StrategyCall//USUKDENLFR")
| Ad | Spend | Link clicks | LPVs | Leads | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| P3P4VideoAdArabic (video) | $1,487.34 | 1,677 | 1,332 | 167 | 95.8% | 79.4% | 10.0% |
| P3P4CoupleImage (static) | $64.53 | 48 | 30 | 8 | 4.2% | 62.5% | 16.7% |
| P3P4VideoAdEnglish | $1.26 | 0 | 0 | 0 | 0.1% | n/a | n/a |
| VSLPreviewA3A4 | $0.13 | 2 | 2 | 0 | 0.0% | n/a | n/a |
| **Total** | **$1,553.26** | **1,727** | **1,364** | **175** | | **79.0%** | **10.1%** |

- The retargeting campaign "Hammer Them Retargeting" (Obj1-5, $35.39, 0 clicks) is left out of the page match, as asked.
- All ads link to https://linguaverna.com/access.

## Fix first (broken things, no test needed)
1. **The 15.8 MB preview GIF.** The animated preview image (source file 6a255f81da24932f12475cbc.gif, 38.8 MB) comes out of GHL's resizer at about 15.8 MB, even at the 768px phone size. The top ad's load rate is 79.4% (1,332 of 1,677 clicks) and the static ad's is 62.5%, so about 1 in 5 paid clicks never sees the page. Playbook: "VSL preview GIF (10-second clip in the Canva GIF frame, quality ~0.4, transparent background)". Re-export it as a 10-second clip at quality ~0.4 (aim for under 2 MB).
2. **Mobile form is pushed below the fold.** On a 390x844 phone you see the logo, call-out, headline, the GIF and "Training access in just 30 sec!", plus the First Name field at 649px. Email starts at 826px and the "Submit" button sits at 1,208px. Make the GIF shorter on mobile so Email and the button show without scrolling. Most of this traffic is Instagram Reels on phones.
3. **Phone field defaults to US (+1).** The placeholder is "+1 (555) 000-0000" and the default flag is "United States: +1". The campaign name says US, UK, DE, NL, FR. UK and EU visitors have to change the country before the number will validate. Turn on auto-detect by IP, or drop the "+1" from the placeholder.
4. **Review count does not match the ad.** The ad says "180+ five-star reviews". The page shows "5.0 · 94 reviews" (Google) and "4.9 · 72 reviews" (Trustpilot), which is 166 in total. The profile (May 2026) said "about 80" reviews, all 5-star. Either the ad number or the widget needs updating. This is Ema's call.
5. **No page title.** The `<title>` tag is empty, so the browser tab and link shares show a bare URL. Set it to "Free Levantine Arabic Roadmap | Lingua Verna".
6. **Call-out differs between pages.** The opt-in says "FOR ADULTS WHO WANT TO SPEAK LEVANTINE ARABIC" and /roadmap says "FOR ADULTS WHO WANT TO SPEAK ARABIC". Playbook: "Call-out line on the first 3 pages, kept to one line", same on every page. Fix this together with T1.

Checked and fine: Terms and Privacy links are in the footer. There is no menu bar. UTM hidden fields are on the form (Source, Campaign, Medium, Content). The pixel and Microsoft Clarity are both installed. Every field is required. No test data is left in the fields.

## Ad-to-page match
| Item | Ad (quoted) | Page (quoted) | Match? |
|---|---|---|---|
| Call-out | Video hook: "If your partner's family speaks Levantine Arabic and you still don't understand them after months of Duolingo then stay with me". Copy: "You've wanted to learn your family's Arabic for years." | "FOR ADULTS WHO WANT TO SPEAK LEVANTINE ARABIC" | No. The ad calls out partner and family. The page is generic. |
| Pain | "Maybe it's a family dinner where everyone switches to Arabic, but you just smile and nod." Video: "after months of Duolingo" | Not on the first screen. It only shows up in reviews below the form. | No |
| Offer name | "Step 1: Watch the Levantine Arabic Roadmap - free". Video: "click below now and watch the free roadmap" | "Training access in just 30 sec!" Button: "Submit" | No. "Roadmap" and "free" are missing. |
| Promise | "Make your first Levantine Arabic conversation happen in 6 weeks." | "Hold Your First Real Levantine Arabic Conversation in 6 Weeks" | Yes, a good match |
| Proof | "500+ students. 180+ five-star reviews. 50+ years of combined instructor experience." Video: "500 adults", "Matt who learned enough to talk with his wife's family in Lebanon without her translating", and Emily with her "Syrian" partner's family | Review carousel below the form, which includes Matt Lopez and Émilie. "500+" and "50+ years" are not on the page. | Partly. The proof sits below the form, and the numbers differ (see Fix 4). |
| Guarantee | Couple image: "And if you don't love it... full refund!" The video has none. | None | Only matters for the static ad (4% of spend). The opt-in is free, and the playbook says to put the guarantee "lower on the page". |

## 5 A/B tests (biggest expected lift first)

**T1. Call-out line (match the video hook)**
- Change: "FOR ADULTS WHO WANT TO SPEAK LEVANTINE ARABIC"
- To: "FOR ADULTS WHOSE PARTNER OR FAMILY SPEAKS LEVANTINE ARABIC"
- Why: 96% of spend is a video that opens with "If your partner's family speaks Levantine Arabic", and the copy says "your family's Arabic". The profile says the best students "have a family member who speaks Arabic... a parent or grandparent... or a spouse". Playbook: call out "ONLY your ideal client". Use the same line on /roadmap too.

**T2. Form header (name the freebie, say it's free)**
- Change: "Training access in just 30 sec!"
- To: "Watch the free Levantine Arabic Roadmap"
- Why: The ad says "Step 1: Watch the Levantine Arabic Roadmap - free" and the video says "click below now and watch the free roadmap". Playbook: "One name for the freebie everywhere." Right now the page uses neither "Roadmap" nor "free".

**T3. Button**
- Change: "Submit"
- To: "Watch the Free Roadmap"
- Why: Playbook: button text says what they get, not "Submit". Built from the video's "watch the free roadmap". Bundle it with T2 (same naming change).

**T4. Add a subheadline (there is none now)**
- Change: (nothing between the headline and the preview GIF)
- To: "Why apps get you a streak, but not conversations, and the speaking-first method that gets adults talking from week one."
- Why: Both lines come word for word from the video's "what's inside" checklist ("Why apps get you a streak, but not conversations." / "The speaking-first method that gets adults talking from week one."). It also hits the ad's pain ("after months of Duolingo"). The playbook's squeeze page elements include a subheadline.

**T5. One proof line right above the form**
- Change: (the proof sits only below the form: "Verified Google Reviews ★★★★★ 5.0 · 94 reviews")
- To: "500+ adults taught. 5.0 on Google (94 reviews). "I feel like I'm finally able to participate in conversations without my wife always needing to translate." Matt Lopez"
- Why: The ad's proof is "500+ students" and the video names Matt and his wife's family in Lebanon. The quote is from Matt Lopez's real review, which is already on the page. I left out "180+ five-star reviews" (the page only shows 166) and "50+ years of combined instructor experience" (not in the profile, and I could not confirm it).

Left out on purpose:
- The 3-week money-back guarantee. It is real (profile: "money-back guarantee if they don't like it within the first three weeks of the program"), but it covers the paid program, and the opt-in is free.
- "Spots open in the next cohort". The profile says "seats are not limited".
- Removing "Why Levantine Arabic?". The cost per lead is about $9.23 (sheet, last 7 days), and the playbook says "If CPL is $10-20, you SHOULD" have a pre-qualifier. It also matches the ICP.

## How to run them
- Traffic: about 1,656 clicks a week (sheet, Oct 6-12), or about 237 a day. 150 visitors per version takes about 1.3 days. At a 10% LPCR that is only about 15 leads per version, so run each test a full 7 days (about 800 visitors and 80+ leads per version) to cover weekdays and weekends.
- Do Fixes 1 to 3 first (GIF, mobile fold, phone country) and let them run 3 to 4 days, so the tests don't measure the speed fix.
- Order: week 1 T1. Week 2 T2+T3 bundled (one "Roadmap naming" version). Week 3 T4. Week 4 T5. If Ema wants it faster, bundle T1+T2+T3 into one "message match" version in week 1, then T4, then T5.
- Clarity labels (Clarity is already on the page): T1-A / T1-B, T2-A / T2-B (covers T3), T4-A / T4-B, T5-A / T5-B. Judge on GHL opt-ins per unique click, and check that pre-qualified rate (91% now) and lead-to-qualified (21% last week vs 28% baseline) don't fall.

## Questions for Ema or Alex
1. Are the target countries really US, UK, DE, NL, FR (going by the campaign name)? If so, what share of leads is non-US, and do non-US people fail the phone field?
2. Which answers to "Why Levantine Arabic?" send people to the disqualified page? Is "I'm curious about languages in general" a disqualifier?
3. Mobile loads a Cloudflare Turnstile check on the form. Does it ever show a visible challenge to real users? It could not be tested from here.
4. Is "180+ five-star reviews" from a newer count than the page widget (166)?
5. Does clicking the preview GIF open a pop-up form? The cursor is a pointer, but I did not trigger it.
6. Weekly LPCR has been about 10% since July 20 (that week's clicks doubled). Was this /access version live from launch, or did the form change around then?

## Appendix: Facts pulled

**Sources used**
- Sheet "(LV) - Business Reporting Daily 2026": tab `_RollingData` (Date, Spend, Impr, Clicks, Lead, PreQual, Qual, Booked, Taken, NewClients), the month tabs (col E "Link Clicks", col H "Lead"), and `Dash` and `Rolling` for monthly totals. Daily data runs Jun 8 to Oct 12. Oct 13 is not logged yet.
- Meta account 323807146523531, level=ad, last_7d, ACTIVE only.
- Profile doc "Client Profile: Alex Willson (Lingua Verna)".
- Page loaded with Playwright (desktop 1440x900, mobile 390x844), plus the playbook text.

**LPCR numbers**
- 7d (Oct 6-12): 173 / 1,656 = 10.4%. 3d (Oct 10-12): 85 / 669 = 12.7%.
- Months: Jun 12.1% (best), Jul 10.4%, Aug 9.6%, Sep 9.5%, Oct 1-12 10.7%.
- Rolling tab, last week vs trailing 3 months: CPL $9.23 vs $7.87. Lead to qualified 21.4% vs 28.0%. Cost per booked call $57.01 vs $88.88. Show-up 46% vs 51%.
- Meta 7d: 175 leads / 1,727 link clicks = 10.1%. Unique link clicks 1,564. LPVs 1,364. Load rate 79.0%.

**Ad copy (top ad P3P4VideoAdArabic, creative 1823484571709257; same text on the couple image ad)**
- Headline: "The Levantine Arabic Roadmap: Why You Haven't Learned Your Family's Language Yet - And How To Change That"
- Primary text (key lines): "You've wanted to learn your family's Arabic for years." / "Maybe it's a family dinner where everyone switches to Arabic, but you just smile and nod." / "I met my wife, realized Arabic was going to be part of my life, and learned the language from scratch as an adult" / "🎥 Step 1: Watch the Levantine Arabic Roadmap - free / 📞 Step 2: Book your Arabic Strategy Session - a free call with me to map out your personal path to fluency" / "500+ students. 180+ five-star reviews. 50+ years of combined instructor experience." / "Make your first Levantine Arabic conversation happen in 6 weeks." / "👇 Watch the Levantine Arabic Roadmap and book your Arabic Strategy Session."
- CTA: Learn More.
- Video: 104 seconds, vertical. It is spoken in English (the "Arabic" in the ad name is a label only). It is Alex talking to camera with word-by-word captions. On-screen text and captions, read from extracted frames: "If your partner's family speaks Levantine Arabic and you still don't understand them after months of Duolingo then stay with me" / "I've worked with so many adults ... in exactly your spot" / "they drill the words, keep their streak alive for few months and still can't hold a real conversation with the mother in law" / "Duolingo just wasn't built to get anyone speaking. It teaches you to recognize words on a screen. That's a completely different skill from talking to a real person" / "the speaking-first method that we use to get adults holding real conversations fast" / "the actual dialect your partner's family speaks at home, not formal textbook Arabic" / "click below to watch it, it's completely free" / "500 adults" (counter animation) / "Matt who learned enough to talk with his wife's family in Lebanon without her translating, or Emily who tried apps and tutors for years before finally speaking with her [Syrian] partner's family in a matter of months" / "we've taught hundreds like them who came in with no Arabic" / an "Our Wall of Love" overlay of Google and Trustpilot review cards / a checklist: "Why apps get you a streak, but not conversations." "The reason most programs teach the wrong Arabic entirely." "The speaking-first method that gets adults talking from week one." "What a real 12-month path from zero to immersion actually looks like." / "CLICK BELOW" buttons / "So click below now and watch the free roadmap while we still have some spots open in the next cohort". The thumbnail is Alex at a desk with the caption "If your partner's family".
- Couple image (P3P4CoupleImage): "I'm looking for 5 adults who want to speak Levantine Arabic with their partner's family THIS year" / "From your first word to real conversations in under 12 months, even if Duolingo never worked" / "And if you don't love it... full refund!"

**Page copy (linguaverna.com/access)**
- Call-out: "FOR ADULTS WHO WANT TO SPEAK LEVANTINE ARABIC"
- Headline: "Hold Your First Real Levantine Arabic Conversation in 6 Weeks"
- No subheadline. Animated preview of Alex (captions like "your family speaks it", "or it's just part of the heritage").
- Form header: "Training access in just 30 sec!"
- Fields (all required): First Name (placeholder "Enter your first name"), Phone (placeholder "+1 (555) 000-0000", default "United States: +1"), Email, "Why Levantine Arabic? *" (radio: "My family speaks it" / "My partner / spouse speaks it" / "I'm interested in Arab culture and the region" / "I'm curious about languages in general"), and a consent checkbox "I consent to receive Emails and SMS messages regarding my submission and related updates." There are 4 hidden UTM fields. Button: "Submit".
- Below the form: "Verified Google Reviews ★★★★★ 5.0 · 94 reviews", "Verified Trustpilot Reviews ★★★★★ 4.9 · 72 reviews", and a 16-review carousel (Matt Lopez, Matthew K, Carla, Ben And Eileen Lakies, Nadine Mustafa, Émilie, Maryam S, and others).
- Footer: "Privacy Policy | Terms of Service". No `<title>`.
- Load: about 2.7s desktop and 2.2s mobile on this connection. Preview image about 15.8 MB.
- Next page /roadmap: "FOR ADULTS WHO WANT TO SPEAK ARABIC" / same headline / "Watch this short training to see how our speaking-first method works - and decide if it's right for you." / "SEE IF YOU QUALIFY".

**Profile facts**
- Offer: online, live Levantine Arabic courses for adults in the West. Two one-hour calls a week (large-group instruction plus small-group conversation). Levantine Arabic Foundations has 4 levels of 3 months each ($400 for level 1, $1,600 for the year). Levantine Living is the intermediate subscription at $1,600 a year.
- Real guarantee: "money-back guarantee if they don't like it within the first three weeks of the program."
- Proof: "about 500 new students in the last 18 months. All reviews (about 80) are 5-star", 245 active students. Two refunds.
- ICP: adults 18+, best fit 28-55, Western (North America, Western Europe). Best students "have a family member who speaks Arabic", meaning Arab heritage or "a spouse, meaning they married into it".
- Qualified lead: age 28-55 plus strong family motivation.

**Could NOT get**
- The full spoken script. No audio transcription tool was available, so the video text above comes from captions read off frames (3 per second). A few middle lines were covered by the checklist overlay.
- A link_url from ads_get_creatives (it came back empty). The URL comes from the ad preview's display link instead.
- GHL funnel stats (page views to opt-ins). Not tried, because the sheet and Meta numbers agree.
- Cloudflare Turnstile on the mobile form: the proxy blocked it, so I could not test a real submit, and did not submit anyway (read-only).
- What the preview GIF click does, and which radio answers disqualify.
