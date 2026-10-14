# LPCR page review: Smarta Tutoring (Marta Bakowska-Mathews, UK, GBP), Oct 14 2026

**Verdict:** LPCR is 7.1% (7d) and 6.7% (3d), against a 20% goal and the sheet's own "> 25%" target. It has sat at about 7% since the OLead funnel launched on Sep 28. The main reason: the page asks a cold parent 6 questions, including a money question ("Which best describes you?"), under a headline that doesn't match the ad. Every live ad says "ATTENTION UK PARENTS WITH UPCOMING MOCKS" and "Book your free consultation today." The page never says "mocks" or "consultation", and the button just says "Submit". On top of that, there is still no Meta pixel on either opt-in, the phone field is still US format, and mobile visitors don't see the headline A/B test.

**What changed since the Oct 12 review**
- **New ads:** a new ad set "OLead – Mock Exams" (5 ads, "Mocks 1" to "Mocks 5") launched Oct 13. The sheet comment for Oct 13 is "launched L2 mocks ads". The ads had £0 spend in the last 7 days, but they are spending today (£62.58 so far on Oct 14 vs £142.71 for Wrong-tutor). They use the same primary text and headline as Wrong-tutor and the same link (/optin-here). Their on-screen text is "Parents of Year 10 & 11 GCSE Students" and "GCSE mocks are days away". This makes the "mocks" match on the page even more important.
- **Top ad:** still "Video - Wrong-tutor", with 97.7% of 7-day spend.
- **Page:** nothing changed on either variant. Same headlines, same 6-field form, same "+1 (555) 000-0000" placeholder, same footer, still no pixel.
- **Test bank:** the client's "AB LP test bank" tab now has stricter rules for calling a winner: 7+ days, about 20 opt-ins and 100+ visitors per variant, the winner about 30%+ better, and a fair test. It also lists a planned "prequalifier vs. none" test and a draft guarantee test (see Fix first #5).

**Funnel checked:** the ads go to `smartaeducation.co.uk/optin-here`. In 6 test loads it split 3/3 between `/optin-325234` and `/optin-745155-4725`.

**Screenshots** (in `oct14/st/`):
- `v1-desktop.png` / `v1-mobile.png`: /optin-325234
- `v2-desktop.png` / `v2-mobile.png`: /optin-745155-4725
- Full-page versions: `*-full.png`

---

## Live ads (account #1 597834280814934, last 7 days Oct 7 to 13, ACTIVE only)

All ads are in the campaign "OLead - GCSE - UK" and all link to /optin-here.

| Ad (ad set) | Spend | Link clicks | LPVs | Leads (Meta) | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| Video - Wrong-tutor (OLead) | £2,020.98 | 857 | 55 | 58 | 97.7% | 6.4% | 6.8% |
| Video - Wasted-spend (OLead) | £27.52 | 4 | 0 | 0 | 1.3% | 0% | 0% |
| Video ad style - Wrong-tutor (OLead) | £18.77 | 5 | 0 | 0 | 0.9% | 0% | 0% |
| Video Ad - Falling-behind (OLead) | £0.68 | 0 | 0 | 0 | 0.03% | n/a | n/a |
| Mocks 1 to 5 (OLead – Mock Exams) | £0.00 | 0 | 0 | 0 | 0% | n/a | n/a |
| **Total** | **£2,067.95** | **866** | **55** | **58** | 100% | **6.4%** | **6.7%** |

**Today so far (Oct 14):**
- Wrong-tutor: £142.71, 44 clicks.
- Mocks ads: £62.58 between them. Mocks 5 £19.24, Mocks 4 £17.97, Mocks 1 £14.85, Mocks 2 £7.01, Mocks 3 £3.51.

**What the numbers say**
- **Load rate is 6.4%, and that's a tracking problem.** Meta counts more leads (58) than landing page views (55), which can't happen when the pixel fires PageView. The cause is Fix first #1.
- **Meta and the sheet agree on leads:** Meta 58 vs sheet 58 (Oct 7 to 13). So there's no lead undercount, and Lead events reach Meta some other way (probably CAPI from GHL).
- **Clicks differ slightly:** Meta 866 link clicks vs sheet 816. The sheet probably logs unique link clicks. LPCR below uses the sheet numbers.

---

## Fix first (broken things, not tests)

1. **Still no Meta pixel on either opt-in variant.**
   - On both variants, desktop and mobile, there is no `fbq` code, no `fbevents.js` and no facebook.com/tr requests on load. That's why Meta reports 55 LPVs from 857 clicks.
   - Playbook: "GHL funnels: paste the full pixel in funnel **Settings → head tracking** so **PageView** fires on every page" and "Opt-in form (name, email, phone): form settings → pixel ID → on submission = **Lead**."
   - Confirm with whoever set up the CAPI workflow first, so Lead isn't double-counted.
2. **Phone field is US format.**
   - The placeholder is "+1 (555) 000-0000" on both variants, desktop and mobile.
   - There is no visible country picker or flag.
   - I typed "07123456789" and it was accepted as typed, with no +44 added. I didn't submit, so I can't confirm how GHL stores it (possibly as +1).
   - Fix: set the default country to United Kingdom (+44) and the placeholder to "07123 456789".
   - Check 2 or 3 recent leads in GHL to see whether their numbers were saved as +1.
3. **The Oct 9 headline A/B test only runs on desktop.**
   - On /optin-325234, desktop shows "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days".
   - Mobile visitors to the same URL see "Discover the Secret Smarta System That's Helped 2000+ Students / Score Grade 8/9s / in GCSE Maths, Science & English / (With a 89% success rate)". That's the same as variant 745155.
   - Most traffic is on phones, so most visitors see the same page on both variants, and the test can't find a winner.
   - Fix: make the GHL mobile headline element match desktop on each variant.
4. **There's no call-out line on mobile.**
   - Desktop shows "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY". Mobile on both variants starts straight with the headline.
   - Playbook: "Call-out line on the first 3 pages, kept to one line."
5. **Unproven stat on the page, and a draft guarantee in the test bank.**
   - The page says "(With a 89% success rate)" (variant 745155 and all mobile). The client profile has no 89% stat. The profile's stats are "2000+ students served. 2-4 grade increase in 75 days. top university attendance. grade 7-9".
   - The Wasted-spend ad says "95% of our students hit Grade 7+ in under 75 days". That conflicts with 89%. Confirm the source or remove it.
   - The test bank lists a test of "Don't see improvement after your first month? We'll coach for free until you do". The profile says: "We don't have a guarantee or work with anyone for free." Don't run that test unless Marta confirms in writing that she will offer it.
6. **The footer has no privacy policy link.**
   - It only shows "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS".
   - Playbook: "Terms and privacy policy links in every footer (required by Facebook...)". Also change 2025 to 2026.
7. **There's no Microsoft Clarity (or GTM) on the page.** None was found in the page code. Install Clarity in funnel head tracking before the tests, so the T1-A/T1-B labels have something to record.
8. **Page speed is worth a re-check.**
   - In this run (headless Chrome, not UK-based) the page took 2.8s to 13.6s to load, vs 1.1 to 1.6s on Oct 12.
   - That's probably network noise, but run Google PageSpeed on both variants once. The pixel gap (#1) hides any real load-rate problem.

---

## 5 A/B tests (biggest expected lift first)

### T1. Form: drop the money question and last name (6 inputs to 4)
- **Change:**
  - "First Name (Parent's ONLY) *"
  - "Last Name (Parent's ONLY)"
  - "Phone (Parent's ONLY) *"
  - "Email (Parent's ONLY) *"
  - "What year is your child in? *" (10 / 11)
  - "Which best describes you? *" with the options "I want the best outcome, and I'm ready to invest" / "I want good results, but price matters to me" / "I want the lowest-cost option available"
- **To:**
  - "First Name *" and "Phone *" side by side
  - "Email *" full width
  - "What year is your child in? *" with "Year 10" / "Year 11"
  - One line above the form: "For parents of Year 10 & 11 GCSE students."
- **Why:**
  - Playbook, Setting up your forms: "B2C: never mention money ('It is a complete drop off moment')".
  - It says pre-qualifiers are "not for competitive ones like college consulting, SAT/ACT". GCSE tutoring is crowded (MyEdSpace and others).
  - It also says "If CPL is already $45-50, don't". 7-day CPL is £35.58 against a £15 client max.
  - The playbook form is "first name + phone (two columns), email full width".
  - This is also the client's own planned "prequalifier vs. none" test.
  - The call-out line is taken from the Mocks ads' on-screen text ("Parents of Year 10 & 11 GCSE Students").

### T2. Headline: say "mocks" and the 2 to 4 grades, same on desktop and mobile
- **Change:**
  - Desktop on /optin-325234: "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days"
  - /optin-745155-4725 and all mobile: "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s (With a 89% success rate)"
  - Sub on both: "Enter your information below to learn how this system works:"
- **To:**
  - Call-out: "ATTENTION UK PARENTS WITH UPCOMING MOCKS"
  - Headline: "Help Your Child Improve by 2 to 4 GCSE Grades in as Little as 75 Days"
  - Sub: "I've helped 2,000+ students fix costly mistakes, gain confidence fast and perform better in mocks and finals, using smarter preparation focused on exam technique and how examiners actually mark."
- **Why:**
  - Every live ad opens with "ATTENTION UK PARENTS WITH UPCOMING MOCKS", and the new Mocks ads say "GCSE mocks are days away" on screen. The page never says "mocks".
  - The new copy is the ad's own words plus the profile offer ("improve by 2–4 grades in as little as 75 days").
  - Playbook: "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page", and "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad".
  - It drops "Secret", "Grade 8/9s" and "89%", which are not in the ad or the profile.
  - There's no guarantee line, because the profile says "We don't have a guarantee".

### T3. Button: say what they get
- **Change:** "Submit"
- **To:** "Show Me How It Works", with this line under the button: "✓ Takes 30 seconds · No payment required"
- **Why:**
  - The page promises "learn how this system works", and "Submit" names nothing.
  - Playbook form rule: the button is "Access" (names the reward).
  - The line under the button is already in the client's test bank.
  - If the page after opt-in is the booking calendar, use "Book My Free Consultation" instead. That matches the ad's "Book your free consultation today." (see Questions #1).

### T4. Parent proof next to the form, parents first
- **Change:**
  - No proof above or beside the form.
  - The review wall starts after "Submit". Its first card is "Matthias Amilegbe, Student". 7 of the 9 cards are students, and the 2 parent reviews (Kiran Hayre, Magdalena Manthey) are 4th and 8th.
- **To:**
  - A strip directly above the first field: "★★★★★ 4.4 on Google · 100+ reviews" and "My child improved by 4 grades in GCSE Science in just 3 months!" Kiran Hayre, parent.
  - Then reorder the wall so both parent reviews come first.
- **Why:**
  - The buyer is the parent (profile: "Parents - the students are below 18 years old").
  - Skill rule: "parent reviews first when parents are the buyer".
  - Playbook squeeze page: "short form, Google/Trustpilot reviews block".
  - On mobile, the first review shows at about 1,800px, after the Submit button at 1,322px.
  - The quote and the 4.4 rating are already on the page, so nothing is invented.

### T5. VSL preview above the form
- **Change:** no preview of what they get. Above the fold there's only the logo, headline and form. I found no video, GIF or iframe on either variant.
- **To:** a 10-second preview GIF of Marta's video between the headline and the form, with the overlay "Watch: how 2,000+ students improved by 2 to 4 GCSE grades". Clicking it opens the same 4-field form in a pop-up.
- **Why:**
  - Playbook squeeze page elements: "logo, call-out, headline, subheadline, **VSL preview GIF**..., short form, Google/Trustpilot reviews block". It's the only missing element.
  - The face in the ad (Marta at her desk, "over 2000" on screen) would then be on the page too.
  - Skip this test if the Oct 2 "new LP test: VSL preview with popup" clearly lost. Its result isn't logged in the sheet.

---

## How to run them

- **Traffic:** 816 link clicks in the last 7 days (sheet), about 117 a day. A 50/50 split gives each version about 58 visitors a day.
- **Time per test:**
  - About 150 visitors per version takes about 3 days.
  - But at a 7% LPCR, the client's rule of "about 20 opt-ins" per variant needs about 285 visitors per version (about 5 days).
  - Their rule also says "At least 7 days have passed". So plan **7 days per test**, and call a tie after 2 weeks.
- **Order:**
  - Day 0: Fix first #1 to #4 and #7 (pixel, +44, mobile headline, mobile call-out, Clarity). Stop the Oct 9 headline test: it's broken on mobile, and T2 replaces it. Log its result in "OLD TESTS WINNER vs LOSER".
  - Week 1: T1 (form).
  - Week 2: T2 (headline), on the winning form.
  - Week 3: T3 + T4 bundled into one B version (button + proof strip). Both are small changes near the form, and traffic is too low to give each its own week quickly.
  - Week 4: T5 (VSL preview).
- **Judge on sheet LPCR** (Lead ÷ Link Clicks, "Oct" tab) split by variant in GHL. Meta LPVs can't be used until the pixel is fixed.
- **Clarity labels:** T1-A / T1-B (form), T2-A / T2-B (headline), T3-A / T3-B (button + proof bundle; call it T3/4 if Ema prefers), T5-A / T5-B (VSL preview). Tag each GHL variant page.
- **Before each test starts,** check both variants on desktop AND phone. Fix first #3 shows mobile can drift from desktop.
- **Keep the ads the same during a test.** The Mocks ad set launched mid-week and sends new traffic to the same page. That's fine as long as both variants get it equally (the client's "test was fair" rule).

---

## Questions for Ema or the client

1. What happens after opt-in: a VSL/training page or straight to booking? The ad says "Book your free consultation today." and the page says "learn how this system works". The answer decides the T3 button text.
2. Where does "89% success rate" come from? The Wasted-spend ad says "95% of our students hit Grade 7+ in under 75 days. 75% exceed their school's predictions" and "Featured in The Guardian, BBC Radio". None of these are in the profile.
3. Has Marta approved "We'll coach for free until you do"? The profile says "We don't have a guarantee or work with anyone for free."
4. How is Meta getting Lead events with no pixel on the opt-in (GHL CAPI workflow)? Is the ad set optimising on that event?
5. Are phone numbers from UK parents being saved as +1 in GHL?
6. Who won the Oct 2 (VSL preview popup) and Oct 6 ("Your Child Already Has a Tutor. So Why Aren't Their Grades Moving?") tests? The Oct 6 headline matched the Wrong-tutor ad name.
7. The sheet header says "Adspend (USD)" but the account is GBP, and the numbers match Meta GBP. Rename the header?

---

## Appendix: Facts pulled

### LPCR (sheet "(ST) OLead - Business Reporting B2C", "Oct" and "Sep" tabs)
Columns used: "Link Clicks" (E) and "Lead" (H). LPCR = Lead ÷ Link Clicks. Oct 13 is filled in; Oct 14 is not yet.

**Last 7 days (Oct 7 to 13):** 58 leads / 816 clicks = **7.1%**.
- Spend £2,063.41, CPL £35.58.
- 11 calls booked, about £188 per booked call.

**Last 3 days (Oct 11 to 13):** 26 / 387 = **6.7%**. Spend £973.31, CPL £37.44.

**Daily (Oct):**
| Day | LPCR |
|---|---|
| 1 | 9.9% |
| 2 | 4.0% |
| 3 | 6.6% |
| 4 | 10.1% |
| 5 | 6.4% |
| 6 | 8.6% |
| 7 | 9.4% |
| 8 | 7.5% |
| 9 | 6.4% |
| 10 | 6.6% |
| 11 | 4.2% |
| 12 | 10.8% |
| 13 | 5.4% |

**Best month of 2026:**
- OLead: **October so far, 111 / 1,516 = 7.3%** (the Dash tab says 7.32%). September was 12 / 239 = 5.0% (only Sep 28 to 30).
- Background from the Oct 12 review: the OSchedule funnel (other sheet) had its best month in August at 9.6%. It fell from about 9 to 11% a week to 5.5% (Sep 14 to 20) and 3.0% (Sep 21 to 27).

**When it dropped:**
- OLead hasn't dropped. It has been flat at about 7% a week since launch: Sep 28 to Oct 4 6.7%, Oct 5 to 11 7.0%, Oct 7 to 13 7.1%.
- It was never at the 20% goal.

**Oct month to date:** CPL £33.98, 30 calls booked, 1 call taken.

**Sheet comments:**
- Sep 28 "launched"
- Sep 30 "increased budget to 200"
- Oct 2 "new LP test: VSL preview with popup"
- Oct 5 "budget to 300"
- Oct 6 "new A/B test running"
- Oct 9 "new LP test"
- Oct 11 "turned off OSchedule"
- Oct 13 "launched L2 mocks ads"

**KPI tab:** "Landing Page Conversion Rate > 25%", "Cost Per Lead Target: < $15 Max: $45".

**"AB LP test bank" tab:**
- Logged tests:
  - Oct 6 headline "Your Child Already Has a Tutor. So Why Aren't Their Grades Moving?"
  - Oct 9 "discover the secret smarta system vs. Learn How 2,000+ Students Have Jumped 2 to 4 GCSE Grades With Tutors Who Mark the Real Papers / Sub: with a 89% success rate vs. none"
- Planned tests:
  - VSL cover overlay
  - "✓ Takes 30 seconds · No payment required"
  - The "coach for free" line
  - "prequalifier vs. none"
- The "OLD TESTS WINNER vs LOSER" table is empty.
- Note: the live variant headlines don't match the Oct 9 wording in the test bank. The live desktop B is "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days".

### Ad copy (live)

**Video - Wrong-tutor** (97.7% of spend; creative 1866559821385323, video 2103420290534092, 68.6s)
- Headline (title): "Expert GCSE Tutors"
- Description: "UK's leading GCSE tutors"
- CTA: Learn More
- Primary text:
  > "ATTENTION UK PARENTS WITH UPCOMING MOCKS
  > Mock results shape confidence, placement, and future options.
  > I've helped 2,000+ students improve by 2–4 GCSE grades using smarter preparation focused on exam technique and how examiners actually mark.
  > I help students:
  > ✔️ Fix costly mistakes
  > ✔️ Gain confidence fast
  > ✔️ Perform better in mocks and finals
  > Book your free consultation today."
- On-screen (preview frame / thumbnail): Marta at her desk with laptops and books, caption "over 2000".
- Link: smartaeducation.co.uk/optin-here (display link from the ad preview).

**Mocks 1 to 5** (new ad set "OLead – Mock Exams", launched Oct 13)
- Same primary text and headline "Expert GCSE Tutors" as Wrong-tutor. Only Mocks 1 carries the description "UK's leading GCSE tutors".
- On screen (Mocks 1 and 5 previews): a top banner "Parents of Year 10 & 11 GCSE Students". The caption reads "GCSE mocks are days away" in Mocks 1 and "A lot" in Mocks 5. Marta speaks to camera in a white shirt.
- Link: /optin-here.

**Video - Wasted-spend**
- Headline: "Real Grade Transformation In A Few Weeks"
- Primary text includes:
  > "Grade 4 to Grade 8 in a few months?"
  > "95% of our students hit Grade 7+ in under 75 days. 75% exceed their school's predictions."
  > "Featured in The Guardian, BBC Radio. Trusted by elite schools across the UK."
  > "Book your free consultation now."

**Video ad style - Wrong-tutor:** same copy as Wrong-tutor.

### Page copy (both variants, checked Oct 14)

**/optin-325234, desktop:**
- Call-out: "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY"
- Headline: "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days"

**/optin-745155-4725, desktop:**
- Same call-out.
- Headline: "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s"
- Then: "(With a 89% success rate)"

**Mobile, both variants:**
- No call-out.
- Headline: "Discover the Secret Smarta System That's Helped 2000+ Students / Score Grade 8/9s / in GCSE Maths, Science & English / (With a 89% success rate)"

**Both variants:**
- Sub-line: "Enter your information below to learn how this system works:"
- Fields (labels show *):
  - "First Name (Parent's ONLY) *"
  - "Last Name (Parent's ONLY)"
  - "Phone (Parent's ONLY) *" (placeholder "+1 (555) 000-0000", no visible country picker)
  - "Email (Parent's ONLY) *"
  - "What year is your child in? *" (10 / 11)
  - "Which best describes you? *" (3 price options)
  - 4 hidden UTM fields
- No test data in the fields.
- Button: "Submit".
- After the form:
  - "What Parents & Students Are Saying / GOOGLE REVIEWS ★★★★★ 4.4 · 100+ reviews"
  - 9 review cards (7 students, 2 parents)
  - "UNIVERSITIES OUR STUDENTS ARE ACCEPTED INTO:"
  - Footer: "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS"
- No video, GIF or iframe. No pixel, Clarity or GTM.

**Positions:**
- Desktop: Submit at 987px (325234) and 1,069px (745155), on a 900px screen.
- Mobile: the first field starts at 582px and Submit is at 1,322px on an 844px screen. The form is **not** visible without scrolling; only the first name to phone fields are above the fold.

### Client profile facts
- **Offer:** "We help ambitious Year 10 & 11 GCSE students improve by 2–4 grades in as little as 75 days."
- **Programmes:** HONOURS / ADVANCESMARTA / GROWTH Academy.
- **Guarantee:** none. "We don't have a guarantee or work with anyone for free."
- **Proof:** "2000+ students served. 2-4 grade increase in 75 days. top university attendance. grade 7-9." The profile also says "helped over 1,000 students" and about 350 students last year. Testimonials are in a separate folder (not opened).
- **ICP:** parents of Year 10 and 11 students in England/UK who value education. The child can reach grades 7 to 9 but lacks confidence, revision strategy or exam technique. They want a structured long-term programme. Often private and grammar school families.
- **Qualified lead:**
  - Parent of a Year 10/11 student in England.
  - Wants GCSE Maths, Science or English.
  - Budget about £2,300 to £5,800+.
  - Wants to start now, and the student is motivated.
  - Both parents and the student attend the consultation.
  - Wants an ongoing programme.
- **Client targets:** max CPL £15, cost per booked call £50.

### Could not get, and why
- **Full video content of the ads:** Meta returns no download URL (download_hd_url is null) and only a 160px thumbnail. I read the on-screen text from ad preview frames only ("over 2000", "Parents of Year 10 & 11 GCSE Students", "GCSE mocks are days away", "A lot"). The spoken hook isn't quoted.
- **Pages after opt-in** (training, survey, booking): not loaded, to avoid submitting a fake lead. So I couldn't confirm how the phone number is stored or whether the hidden UTM fields fill on submit (they were empty on page load in this run).
- **GHL per-variant stats** (views → opt-ins for 325234 vs 745155): not pulled. The split is unknown, so the Oct 9 test can't be scored here.
- **Results of the Oct 2, 6 and 9 LP tests:** not logged in the sheet.
- **OSchedule sheet:** not re-pulled today. The August 9.6% figure comes from the Oct 12 review.
