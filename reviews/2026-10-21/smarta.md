# Smarta Tutoring: LPCR deep dive, Oct 21 2026

**Smarta**: LPCR 7d 9.0% (92/1,026), 3d 7.6% (37/485), prior week (Oct 7 to 13) 7.5% (61/816). Up 1.5 points on the prior week, flat since Oct 19, and still well under 15%.
Main reason: the page now shows the winning headline on every device, so the headline is no longer the problem. The form is. It has 6 inputs including a money question, the phone field is set to the US, the button says "Submit", and there is no proof until after Submit.

## Answers to the two checks
- **Phone headline: FIXED.** On a 390px phone, /optin-471135 now shows "Jump 2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks." The old "Secret Smarta System ... (With a 89% success rate)" headline is gone from both live pages.
- **Split: /optin-here does NOT send 100% to /optin-471135.** In 12 test loads it sent 4 to /optin-471135 and 8 to a NEW page, /optin-887216. The old loser /optin-325234 is now a 404, so the old split is over.
  - /optin-887216 is the control plus a VSL preview image ("If you're a Parent of year 10-11 student / GCSE maths / Science / English", Marta on the right, a play button). Clicking it opens a pop-up with the same form. All text on the page is identical to the control.
  - This lines up with the sheet comment on Oct 19 ("new LP A/B test") and the test bank row "A/B no VSL preview vs. having it". So a VSL preview test has been running since about Oct 19, and the form test has not started.
  - Note: the test bank row dated Oct 19 is the "✓ Takes 30 seconds · No payment required" line, but that line is on neither page. Ema to confirm which test is meant to be live.

## Changed since Oct 19
- DONE: winning headline now shows on phones (both live pages).
- DONE: unproven "89% success rate" is gone from the live pages.
- DONE: old split ended. /optin-325234 is a 404. (A new split, control vs VSL preview, replaced it.)
- PARTLY DONE: VSL preview is live, but only on the B page of a test, and as a still image with a play button (the playbook asks for a 10-second GIF).
- NOT DONE: call-out on phones. "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY" shows on desktop only, on both pages.
- NOT DONE: Meta pixel. No fbq, no fbevents.js, no facebook.com/tr requests on either page, desktop or phone.
- NOT DONE: phone field. Still "United States: +1" with placeholder "+1 (555) 000-0000". Typing "07123456789" is kept as typed, with no +44 added (not submitted).
- NOT DONE: form. Still 6 inputs, including Last Name and "Which best describes you?".
- NOT DONE: button. Still "Submit".
- NOT DONE: proof near the form. Reviews start after Submit; the first card is still a student (Matthias Amilegbe).
- NOT DONE: footer. Still "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS", no privacy policy.
- NOT DONE: Clarity / GTM. Neither installed, so the current VSL test has no recordings.

## Live ads (account 597834280814934, Oct 14 to 20)

| Ad (ad set) | Status now | Spend | Link clicks | LPVs | Leads (Meta) | Share | Load rate |
|---|---|---|---|---|---|---|---|
| Video - Wrong-tutor (OLead) | ACTIVE | £2,050.27 | 849 | 97 | 104 | 73.4% | 11.4% |
| Mocks 5 (OLead – Mock Exams) | PAUSED | £372.43 | 122 | 10 | 9 | 13.3% | 8.2% |
| Mocks 1 | ad set paused | £141.18 | 44 | 1 | 1 | 5.1% | 2.3% |
| Mocks 2 | ad set paused | £120.95 | 37 | 3 | 3 | 4.3% | 8.1% |
| Mocks 3 | ad set paused | £53.43 | 18 | 2 | 2 | 1.9% | 11.1% |
| Mocks 4 | ad set paused | £47.38 | 9 | 0 | 0 | 1.7% | 0% |
| Video ad style - Wrong-tutor | ACTIVE | £3.75 | 3 | 0 | 0 | 0.1% | 0% |
| Video Ad - Falling-behind | ACTIVE | £1.79 | 1 | 0 | 0 | 0.1% | 0% |
| Video - Wasted-spend | PAUSED | £0.74 | 0 | 0 | 0 | 0% | n/a |
| **Total** | | **£2,791.92** | **1,083** | **113** | **119** | 100% | **10.4%** |

- **Of the ads ACTIVE today, Wrong-tutor is 99.7% of spend.** Headline "Expert GCSE Tutors". Primary text opens "ATTENTION UK PARENTS WITH UPCOMING MOCKS" and ends "Book your free consultation today." Video hook (captions, checked Oct 19, same creative id 1866559821385323): "What if your child's tutor was also the person who marks the exam?" Preview frame today shows the caption "over 2000". Links to /optin-here (utm_content=wrongtutorvideoad).
- **Mocks ads are all off now.** Sheet comment Oct 21: "killed mocks, launching new adset". Mocks 5 was 13.3% of last week's spend; I did not pull its frames since it is paused.
- **New since Oct 19: "OLead – Pain Points" ad set, Pain 1 to 5**, created Oct 21 13:41, £0 spend so far. Same primary text and headline ("Expert GCSE Tutors") as Wrong-tutor, all video. Pain 1 links to /optin-here (utm_content=pain1). Pain 1 preview frame caption: "rereading notes". Hooks not read yet.

## Health checks
- **Load rate 10.4% (113 LPVs / 1,083 clicks).** Meta logs more leads (119) than page views (113), so the PageView pixel is missing. Confirmed in page code and network on both pages.
- **Leads, Meta vs sheet:** Meta 119 vs sheet 92 for Oct 14 to 20. Meta is higher, so Lead may be counted twice (CAPI plus another source) or late conversions are attributed. Judge LPCR on the sheet.
- **Clicks match:** Meta 1,083 link clicks vs sheet 1,026; spend £2,791.92 vs sheet 2,784.79.
- **Phone field:** US default on both pages, desktop and phone (see above).
- **Form renders and is clickable** on both pages. Submit is enabled and nothing covers it. Hidden UTM fields present and empty on load. No test data.
- **VSL pop-up works:** clicking the preview opens a pop-up with the same form (same US phone default, same 6 inputs).
- **Phone layout:**
  - Control (471135): first field at about 467px, Submit at about 1,207px, first review at about 1,650px on an 844px screen.
  - VSL page (887216): the preview pushes the first field to about 687px and Submit to about 1,426px. Only First Name and part of Last Name show without scrolling.
  - Both: an empty gap of about 100px between the headline and the next block.
- **Desktop VSL page:** the preview image sits low in the left column (starts at about 657px of 900px), with a large empty area above it.
- **Speed:** 0.8s to 1.4s to load (headless Chrome, not from the UK), first paint about 0.6s to 0.8s. Fine.

## A. FIXES (do now, not tests)
Apply each fix to BOTH /optin-471135 and /optin-887216 on the same day, so the running test stays fair.
1. **Add the Meta pixel** in funnel Settings, head tracking, so PageView fires. Playbook: "Opt-in form (name, email, phone): form settings → pixel ID → on submission = Lead." Check the CAPI workflow first, since Meta already shows more leads (119) than the sheet (92).
2. **Set the phone field to UK.** Change default "United States: +1" and placeholder "+1 (555) 000-0000" To default "United Kingdom: +44" and placeholder "07123 456789".
3. **Show the call-out on phones.** Change: no call-out on mobile To: "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY" above the headline on mobile, same as desktop. Playbook: "Call-out line on the first 3 pages, kept to one line."
4. **Install Microsoft Clarity** in head tracking now, so the running VSL test and T1 have recordings.
5. **Fix the footer.** Change "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS" To "COPYRIGHT 2026 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS | PRIVACY POLICY" (linked).
6. **Close the empty gap** under the headline on mobile (about 100px), so the form starts higher.
7. **Decide on the running VSL test.** It started about Oct 19, so 7 days ends Oct 26. Recommended: let it finish on Oct 26 (client rule: "nothing changed mid-test"), log the winner in "OLD TESTS WINNER vs LOSER", then start T1 on the winner. If Ema wants the form test sooner, stop the VSL test now and put both pages back to the control.

## B. A/B TESTS (control = winning headline page, biggest lift first)

**T1. Form: cut the money question and Last Name (6 inputs to 4)**
- Change: "Last Name (Parent's ONLY)" and "Which best describes you? *" ("I want the best outcome, and I'm ready to invest" / "I want good results, but price matters to me" / "I want the lowest-cost option available"). Layout: First/Last on row 1, Phone/Email on row 2.
- To: remove both. Row 1: "First Name (Parent's ONLY) *" + "Phone (Parent's ONLY) *". Row 2: "Email (Parent's ONLY) *" full width. Keep "What year is your child in? *" (10 / 11).
- Why: playbook "B2C: never mention money ('It is a complete drop off moment')", and pre-qualifiers are "not for competitive ones" and "If CPL is already $45-50, don't". 7-day CPL is £30.27 (sheet 2,784.79 / 92). Playbook form layout: "first name + phone (two columns), email full width". Watch calls booked per lead (23 booked Oct 14 to 20).

**T2. Button: say what they get**
- Change: "Submit"
- To: "Show Me How It Works", with "✓ Takes 30 seconds · No payment required" directly under it.
- Why: the page promises "learn how this system works" and "Submit" names nothing. Playbook button: "Access". The line under it is already in the client's test bank. If the next page is the booking calendar, use "Book My Free Consultation" (matches the ad's "Book your free consultation today.").

**T3. Subheadline: name the method the ad sells**
- Change: "Enter your information below to learn how this system works:"
- To: "Smarter preparation focused on exam technique and how examiners actually mark. Enter your details to see how it works:"
- Why: "this system" is never explained on the page. The new line is word for word from the ad's primary text and fits the hook "What if your child's tutor was also the person who marks the exam?". The stronger "every tutor is a current GCSE exam marker" line is left out until Marta confirms it in writing (not in her profile).

**T4. Parent proof above the form, parents first**
- Change: no proof above Submit; review wall starts after Submit with "Matthias Amilegbe, Student". Parent reviews are 4th (Kiran Hayre) and 8th (Magdalena Manthey).
- To: a strip directly above the first field: "★★★★★ 4.4 on Google · 100+ reviews" and "my child improved by 4 grades in GCSE Science in just 3 months!" Kiran Hayre, parent. Then move both parent reviews to the top of the wall, followed by Precious Chukwudi ("I joined Smarta achieving a grade 4 in my mocks ... my actual GCSE result was a grade 7."), which fits the mocks headline.
- Why: the buyer is the parent (profile). Playbook squeeze page: "short form, Google/Trustpilot reviews block". On phones the first review is about 1,650px down. All copy is already on the page.

**T5. VSL preview: still image to 10-second GIF (only if the VSL page wins on Oct 26)**
- Change: still image "If you're a Parent of year 10-11 student / GCSE maths / Science / English" with a play button.
- To: a 10-second GIF of Marta to camera from the same footage, same pop-up form on click.
- Why: playbook squeeze page elements: "VSL preview GIF (10-second clip in the Canva GIF frame...)". If the VSL page loses, skip T5 and test T4 earlier.

**Run plan:** about 1,026 clicks/week (about 73 per version a day). At 8 to 9% LPCR, 20 opt-ins per version needs about 230 visitors (about 3 days), but the client's rule is at least 7 days, so 7 days per test, tie at 14 days. Order: fixes now; VSL test ends Oct 26; T1 Oct 26 to Nov 2; T2 + T3 bundled (both small copy changes at the form); then T4; then T5. Clarity labels T1-A/B, T2-A/B (button + sub), T4-A/B, T5-A/B. Note that Pain 1 to 5 starting now changes the traffic mix mid-test; check results by utm_content.

## NEED FROM EMA
- **Which test is live:** confirm /optin-887216 (VSL preview pop-up) is the Oct 19 test, its start date, and whether the "✓ Takes 30 seconds" line was meant to be on it.
- **GHL page stats for 471135 vs 887216** (views and opt-ins since Oct 19, by device if possible), so the VSL test can be called on Oct 26.
- **GHL stats for the headline test** (471135 vs 325234), to log the winner properly.
- **What comes after opt-in:** VSL page or booking calendar. This sets the T2 button text.
- **How Lead reaches Meta** (CAPI workflow name) and why Meta shows 119 leads vs 92 in the sheet.
- **2 or 3 recent UK leads in GHL:** are phone numbers saved as +1?
- **Marta's written OK** for "Every single tutor is a qualified UK teacher and a current exam marker" (video claim, not in profile).
- **Pain 1 to 5 hooks:** scripts or captions, once they spend, so the page can be matched to them. I only saw one frame ("rereading notes").
- **Video audio:** I read on-screen captions only. Send the script if you want spoken lines quoted.
- **Real phone check** of both pages, since my phone checks are headless.

## Appendix: facts pulled
- **Sheet** "(ST) OLead - Business Reporting B2C", "Oct" tab, columns E "Link Clicks" and H "Lead". Filled through Oct 20.
  - Oct 14 to 20: 92 leads / 1,026 clicks = 9.0%. Spend 2,784.79 (column says USD, account is GBP), CPL 30.27, 23 calls booked.
  - Oct 18 to 20: 37 / 485 = 7.6%. Oct 19 to 20 (after the mobile fix and VSL test): 26 / 312 = 8.3%.
  - Oct 7 to 13: 61 / 816 = 7.5%.
  - Daily Oct 14 to 20: 7/129, 17/143, 14/140, 17/129, 11/173, 14/154, 12/158.
  - October to date: 205 / 2,542 = 8.1%.
  - Comments: Oct 14 "new LP A/B test", Oct 19 "new LP A/B test", Oct 21 "killed mocks, launching new adset".
- **Page files:** /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct21/smarta/ (v3-* = 471135, v4-* = 887216, v1-* = 325234 404, desktop and mobile, full-page, v4-mobile-afterclick.png = pop-up; page.json and page2.json raw data).
- **Profile (from Oct 19):** offer "We help ambitious Year 10 & 11 GCSE students improve by 2–4 grades in as little as 75 days"; proof "2000+ students served. 2-4 grade increase in 75 days"; no guarantee ("We don't have a guarantee or work with anyone for free"); buyer is the parent; CPL target £15.
