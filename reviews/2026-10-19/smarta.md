# Smarta Tutoring: LPCR deep dive, Oct 19 2026

**Smarta**: LPCR 7d 9.0% (88/981), 3d 9.5% (42/442), prior week 7.5% (61/816). It moved up about 1.5 points since the mocks headline went live on Oct 14, but it is still well under 15%. Main reason: phone visitors (most of the traffic) never see the winning headline. Mobile still shows the old "Secret Smarta System ... (With a 89% success rate)" headline on both URLs, under a 6-field form that asks about money and ends in "Submit".

Note: Ema confirmed the headline test winner (call-out "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY" + "Jump 2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks."). It is the new control. No headline test below.

## Changed since Oct 14
- DONE: a mocks headline went live on desktop at a new URL, /optin-471135 ("Jump 2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks."). It won against /optin-325234.
- DONE: the old variant /optin-745155-4725 is out of the split. It now returns 404 (14 test loads of /optin-here: 6 went to 325234, 8 to 471135, none to 745155).
- PARTLY DONE: the phone field now shows a flag picker, but it still defaults to "United States: +1", with placeholder "+1 (555) 000-0000".
- NOT DONE: Meta pixel. Still no fbq/fbevents and no facebook.com/tr requests on either page, desktop or phone.
- NOT DONE: mobile headline. Both URLs on a 390px phone still show "Discover the Secret Smarta System That's Helped 2000+ Students / Score Grade 8/9s / in GCSE Maths, Science & English / (With a 89% success rate)".
- NOT DONE: mobile call-out. It is still missing on both URLs.
- NOT DONE: unproven "89% success rate". It is still on mobile.
- NOT DONE: form. It still has 6 inputs: Last Name and the money question "Which best describes you?" are still there.
- NOT DONE: button. It still says "Submit".
- NOT DONE: proof near the form. Reviews still start after Submit, and the first card is still a student (Matthias Amilegbe).
- NOT DONE: footer. It still reads "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS", with no privacy policy link.
- NOT DONE: Clarity / GTM. Neither is installed.
- NOT DONE: VSL preview. There is still no video, GIF or iframe.

## Live ads (account 597834280814934, Oct 12 to 18, ACTIVE only, all link to /optin-here)

| Ad (ad set) | Spend | Link clicks | LPVs | Leads (Meta) | Share | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| Video - Wrong-tutor (OLead) | £2,095.72 | 882 | 95 | 99 | 90.5% | 10.8% | 11.2% |
| Mocks 1 (OLead – Mock Exams) | £76.76 | 20 | 0 | 0 | 3.3% | 0% | 0% |
| Mocks 2 | £51.94 | 13 | 1 | 1 | 2.2% | 7.7% | 7.7% |
| Mocks 3 | £44.83 | 17 | 1 | 1 | 1.9% | 5.9% | 5.9% |
| Mocks 4 | £39.77 | 8 | 0 | 0 | 1.7% | 0% | 0% |
| Video ad style - Wrong-tutor | £5.58 | 3 | 0 | 0 | 0.2% | 0% | 0% |
| Video Ad - Falling-behind | £1.65 | 1 | 0 | 0 | 0.1% | 0% | 0% |
| **Total** | **£2,316.25** | **944** | **97** | **101** | 100% | **10.3%** | **10.7%** |

- **Video - Wrong-tutor, 90.5% of spend.**
  - Headline "Expert GCSE Tutors".
  - Primary text opens "ATTENTION UK PARENTS WITH UPCOMING MOCKS" and ends "Book your free consultation today."
  - Video hook, from on-screen captions: "What if your child's tutor was also the person who marks the exam?"
  - Other captions:
    - "knows exactly what the mark scheme says"
    - "Every single tutor is a qualified UK teacher and a current exam marker. They mark real GCSE papers every summer."
    - "over 2000 have jumped 2 to 4 grades"
    - "live classes, 24/7 support and unlimited exam practice marked by examiners"
    - "Give your child the one advantage most students never get."
    - "Book your free consultation"
  - The video itself never says "mocks". Only the primary text does.
- **Mocks 1 to 4, 9.2% combined (each under 5%).**
  - Same primary text and headline as Wrong-tutor.
  - On screen: banner "Parents of Year 10 & 11 GCSE Students", hook "GCSE mocks are days away".
  - Mocks 1 then says, in captions: "Your child can be confident explaining at home ... Then freeze when real exam pressure hits", "Every tutor is a qualified teacher and GCSE examiner", "2,000 have jumped 2 to 4 grades", "click below ... and book [a] consultation".
- **Launched since Oct 14:** none. Mocks 1 to 5 launched Oct 13. Mocks 5 and Video - Wasted-spend are no longer in the ACTIVE list.

## Health checks
- **Load rate is 10.3%.** Meta logs more leads (101) than landing page views (97). That can't happen with a working pixel, so the PageView pixel is missing (confirmed in page code).
- **Leads, Meta vs sheet:** Meta 101 vs sheet 88 (Oct 12 to 18). Meta is now higher, so Lead may be counted twice (CAPI plus something else), or the 7-day click window is pulling in later leads. Judge on sheet numbers.
- **Clicks:** Meta 944 link clicks (851 unique) vs sheet 981. The sheet also includes spend from ads that are paused now (sheet spend £2,645.82 vs £2,316.25 for active ads).
- **Phone field:**
  - It defaults to the US flag "+1" on desktop and phone.
  - I typed "07123456789" and it was accepted as typed, with no +44 added. I did not submit.
- **Form renders on both URLs**, desktop and phone. Submit is enabled and nothing covers it. There is no test data in the fields. The 4 hidden UTM fields are empty on load.
- **Mobile, above the fold:**
  - The first field starts at about 580px, and Submit is at about 1,320px on an 844px screen.
  - Only First Name to Phone are visible without scrolling.
  - The first review is at about 1,760px.
- **Speed:** it loads in 0.9s to 1.5s (headless Chrome, not from the UK). That's fine.
- **Dead URL:** /optin-745155-4725 is 404. It's harmless as long as nothing links to it.
- **The split is still live:** /optin-here still sends some traffic to the losing page /optin-325234.

## A. FIXES (do now, not tests)
1. **Show the winning headline on phones (both pages).**
   - Change (mobile): "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s in GCSE Maths, Science & English (With a 89% success rate)"
   - To: "Jump 2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks."
   - Also add the mobile call-out "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY".
   - This also removes the unproven "89%". The profile only has "2000+ students served. 2-4 grade increase in 75 days."
   - Note: phone visitors saw the same headline on both pages, so the win was decided by desktop traffic.
2. **End the old split.** Point /optin-here 100% to /optin-471135 (the winner) until T1 starts, and log the result in "OLD TESTS WINNER vs LOSER".
3. **Add the Meta pixel** in funnel Settings, head tracking, so PageView fires.
   - Playbook: "GHL funnels: paste the full pixel in funnel Settings → head tracking so PageView fires on every page."
   - Before adding Lead on the form, check the CAPI workflow. Meta already shows more leads than the sheet, so a second Lead could double count.
4. **Set the phone field to UK.**
   - Change: default country "United States: +1" and placeholder "+1 (555) 000-0000"
   - To: default "United Kingdom: +44" and placeholder "07123 456789".
5. **Fix the footer.**
   - Change: "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS"
   - To: "COPYRIGHT 2026 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS | PRIVACY POLICY" (linked).
   - Playbook: "Terms and privacy policy links in every footer (required by Facebook...)".
6. **Install Microsoft Clarity** in head tracking before T1, so the T1-A/T1-B labels have something to record.

## B. A/B TESTS (control = winning headline page, biggest lift first)

**T1. Form: cut the money question and Last Name (6 inputs to 4)**
- Change:
  - "Last Name (Parent's ONLY)"
  - "Which best describes you? *", with the options "I want the best outcome, and I'm ready to invest" / "I want good results, but price matters to me" / "I want the lowest-cost option available"
  - Layout: First/Last on row 1, Phone/Email on row 2
- To:
  - Remove both fields.
  - Row 1: "First Name (Parent's ONLY) *" + "Phone (Parent's ONLY) *". Row 2: "Email (Parent's ONLY) *" full width.
  - Keep "What year is your child in? *" with the options "Year 10" / "Year 11".
- Why:
  - Playbook: "B2C: never mention money ('It is a complete drop off moment')".
  - The playbook says pre-qualifiers are "not for competitive ones" and "If CPL is already $45-50, don't". 7-day CPL is £30.07 (about $40) against a £15 client max.
  - It's also the client's own planned "prequalifier vs. none" test.
  - Watch calls booked per lead, since the money question was filtering.

**T2. Button: say what they get**
- Change: "Submit"
- To: "Show Me How It Works", with "✓ Takes 30 seconds · No payment required" directly under it.
- Why:
  - The page promises "learn how this system works", and "Submit" names nothing. Playbook form rule: the button says "Access" (names the reward).
  - The line under the button is already in the client's AB LP test bank.
  - If the page after opt-in is the booking calendar, use "Book My Free Consultation" instead. That matches the ad's "Book your free consultation today."

**T3. Subheadline: name the method the ad sells**
- Change: "Enter your information below to learn how this system works:"
- To: "Smarter preparation focused on exam technique and how examiners actually mark. Enter your details to see how it works:"
- Why:
  - "This system" is never explained on the page. The new line is word for word from the primary text ("smarter preparation focused on exam technique and how examiners actually mark").
  - It also matches the video hook ("What if your child's tutor was also the person who marks the exam?").
  - Once Marta confirms the video claim in writing, a stronger version is: "Every Smarta tutor is a qualified UK teacher and a current GCSE exam marker. Enter your details to see how it works:" I left it out until then because it isn't in the profile.

**T4. Parent proof above the form, parents first**
- Change:
  - No proof above Submit.
  - The review wall starts after Submit, with "Matthias Amilegbe, Student". The 2 parent reviews are 4th (Kiran Hayre) and 8th (Magdalena Manthey).
- To:
  - A strip directly above the first field: "★★★★★ 4.4 on Google · 100+ reviews" and "my child improved by 4 grades in GCSE Science in just 3 months!" Kiran Hayre, parent.
  - Move both parent reviews to the top of the wall, then "I joined Smarta achieving a grade 4 in my mocks ... my actual GCSE result was a grade 7." Precious Chukwudi. That review fits the mocks headline.
- Why:
  - The buyer is the parent (profile: "Parents - the students are below 18 years old").
  - Playbook squeeze page: "short form, Google/Trustpilot reviews block".
  - On phones, proof currently starts about 1,760px down. All copy is already on the page, so nothing is invented.

**T5. VSL preview above the form**
- Change: nothing between the headline and the form. There is no video, GIF or iframe on the page.
- To: a 10-second GIF of Marta to camera (from the Mocks footage), with the overlay "Watch: how 2,000+ students jumped 2 to 4 grades". Clicking it opens the same form in a pop-up.
- Why:
  - Playbook squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block". It's the only element missing.
  - Skip this test if the Oct 2 "VSL preview with popup" test clearly lost. Its result isn't logged.

**Run plan:**
- Traffic: 981 clicks/week on the sheet (about 140 a day, about 70 per version a day).
- At 9% LPCR, the client's "about 20 opt-ins per variant" rule needs about 220 visitors per version (about 3 days), but their rule also says at least 7 days. So run 7 days per test, and call a tie at 14 days.
- Order:
  - Day 0: Fixes 1 to 6.
  - Week 1: T1.
  - Week 2: T2 + T3 bundled. Both are small copy changes at the form, and traffic is too low to split them.
  - Week 3: T4.
  - Week 4: T5.
- Clarity labels: T1-A/B, T2-A/B (button + sub bundle), T4-A/B, T5-A/B.
- Check both versions on a real phone before each test starts.

## NEED FROM EMA
- **A real phone check of /optin-471135.** Open it on your own phone and screenshot it. My headless iPhone (390px) showed the old "Secret Smarta System ... 89%" headline on both URLs, and your screenshot A looks like that mobile view.
- **GHL per-page stats for the headline test** (page views and opt-ins for 471135 vs 325234, split by device if possible), so we know the winner held on phones.
- **Marta's written OK for the video claim** "Every single tutor is a qualified UK teacher and a current exam marker", plus the source for "89% success rate". Neither is in her profile.
- **What comes after opt-in:** VSL page or booking calendar? This decides the T2 button text.
- **2 or 3 recent UK leads in GHL:** are their phone numbers saved as +1?
- **How Lead reaches Meta** (CAPI workflow name), and why Meta shows 101 leads vs 88 in the sheet for Oct 12 to 18.
- **Video audio:** I read the on-screen captions only (the full 68s Wrong-tutor and 39s Mocks 1 videos, 1 frame per second). If you want exact spoken lines, send the script or a transcript.
- **Results of the Oct 2 (VSL preview popup) and Oct 6 tests**, for the test bank.

## Appendix: facts pulled
- **Sheet** "(ST) OLead - Business Reporting B2C", "Oct" tab. Columns E "Link Clicks" and H "Lead".
  - Oct 18 is filled in. Oct 19 has 10 leads already but no clicks, so the Dash "Oct" LPCR of 8.48% is inflated. The real October to date is 179/2,230 = 8.0%.
  - Oct 12 to 18: spend £2,645.82, CPL £30.07, 15 calls booked.
  - Oct 7 to 13: CPL £34.15, 11 booked. (The sheet now shows 61 leads for that week. It showed 58 on Oct 14.)
  - Oct 14 to 18: 66/714 = 9.2%.
  - Best month of 2026: October so far (8.0%). September was 5.9%.
  - Sheet comments: Oct 14 "new LP A/B test". The test bank lists "test: '2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks.'"
- **Page, desktop, /optin-471135:**
  - Logo
  - "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY"
  - "Jump 2 to 4 GCSE Grades Higher in 75 Days. Start Before the Mocks."
  - "Enter your information below to learn how this system works:"
  - Form fields: "First Name (Parent's ONLY) *", "Last Name (Parent's ONLY)", "Phone (Parent's ONLY) *", "Email (Parent's ONLY) *", "What year is your child in? *" (10/11), "Which best describes you? *" (3 price options). None of them use the HTML required attribute; GHL validates the * fields.
  - "Submit"
  - "What Parents & Students Are Saying / GOOGLE REVIEWS ★★★★★ 4.4 · 100+ reviews": 9 cards (7 students, 2 parents)
  - "Real Google Reviews from SmartaTutoring parents and students"
  - "UNIVERSITIES OUR STUDENTS ARE ACCEPTED INTO:"
  - Footer as above.
  - No guarantee anywhere. That's correct: the profile says "We don't have a guarantee or work with anyone for free."
- **Page, desktop, /optin-325234:** the same, with the headline "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days".
- **Profile:**
  - Offer: "We help ambitious Year 10 & 11 GCSE students improve by 2–4 grades in as little as 75 days."
  - Proof: "2000+ students served. 2-4 grade increase in 75 days. top university attendance. grade 7-9."
  - Buyer: the parents.
  - Qualified lead: Y10/11 in England, budget about £2,300 to £5,800+, wants to start now.
  - Targets: CPL £15, cost per booked call £50.
- **Files** (folder /tmp/claude-0/-home-user-lps/164f61e1-fdee-53bc-873d-634ac5aa1b31/scratchpad/oct19/smarta/):
  - Screenshots: v1-* (325234), v3-* (471135) and v2-* (the 404), each desktop and mobile, plus full-page versions.
  - Video frame sheets: vid/sheet_1..5.png (Wrong-tutor) and vid/m1_1..3.png (Mocks 1).
  - Raw data: page.json and page3.json.
