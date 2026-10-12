# LPCR page review: Smarta Tutoring (Marta Bakowska-Mathews, UK, GBP)

**Verdict:** LPCR is 7.0% (7d) and 5.7% (3d), far under the 20% goal. The main reason is a long form with a money question ("Which best describes you?") on a page that doesn't match the live ad (the ad says "mocks" and "Book your free consultation", the page says neither, and the button just says "Submit"). On top of that, the opt-in page has no Meta pixel, the phone field defaults to the US (+1), and the headline A/B test only runs on desktop.

Funnel checked: the live ads all go to one opt-in, `smartaeducation.co.uk/optin-here`. It splits visitors between `/optin-325234` and `/optin-745155-4725` (GHL funnel "NEW OPT-IN FUNNEL 2026/2027"). This is the OLead funnel. OSchedule was turned off on Oct 11 (sheet comment), and ad accounts #2, #3 and #5 have no active ads.

Screenshots: `smarta-desktop.png` (1440x900) and `smarta-mobile.png` (390x844), both of /optin-325234.

---

## Live ads (account #1 597834280814934, last 14 days, ACTIVE only)

Campaign "OLead - GCSE - UK", ad set "OLead". All four ads link to /optin-here.

| Ad | Spend | Link clicks | LPVs | Leads (Meta) | Share of spend | Load rate | LPCR (Meta) |
|---|---|---|---|---|---|---|---|
| Video - Wrong-tutor | £3,113.63 | 1,357 | 85 | 91 | 96.9% | 6.3% | 6.7% |
| Video - Wasted-spend | £55.13 | 14 | 1 | 1 | 1.7% | 7.1% | 7.1% |
| Video ad style - Wrong-tutor | £41.77 | 18 | 0 | 0 | 1.3% | 0% | 0% |
| Video Ad - Falling-behind | £3.82 | 0 | 0 | 0 | 0.1% | n/a | n/a |
| **Total** | **£3,214.35** | **1,389** | **86** | **92** | 100% | **6.2%** | **6.6%** |

- One ad (Wrong-tutor) gets 97% of spend, so the page has to match that ad.
- **Load rate of 6% is a tracking problem, not a slow page.** Meta counts more leads (92) than landing page views (86), which can't happen if tracking works. The page loaded in about 1.1 to 1.6 seconds in my test. The cause is below in Fix first #1.
- Meta leads (92) vs sheet leads (102, Sep 28 to Oct 11): close enough. No lead undercount to flag, but the sheet is still the source of truth.

---

## Fix first (broken things, not tests)

1. **No Meta pixel on either opt-in variant.** In the GHL page data for /optin-325234 and /optin-745155-4725, the head tracking, body tracking, global tracking code and form `fbPixelId` are all empty, and `pixelToInit` is `[]`. No Facebook requests fired when I loaded the page. That's why Meta sees 86 page views from 1,389 clicks. Playbook: "GHL funnels: paste the full pixel in funnel Settings → head tracking so PageView fires on every page" and "Opt-in form ... pixel ID with Lead on submission." The form's event is set to "SubmitApplication". Meta still records Leads, probably through CAPI. Confirm with whoever set up tracking before changing anything.
2. **Phone field defaults to United States (+1).** The flag is "United States: +1" and the placeholder is "+1 (555) 000-0000" on both variants, desktop and mobile. UK parents typing 07... get a US-format number or an error. Set the default to United Kingdom (+44) and the placeholder to "07123 456789".
3. **The headline A/B test doesn't run on mobile.** On /optin-325234 the desktop headline is "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days", but mobile visitors to the same URL see "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s ... (With a 89% success rate)", which is the same headline as the other variant. Most traffic is on phones, so the Oct 9 headline test is measuring desktop only. GHL has a separate mobile element. Make mobile match desktop on each variant.
4. **Mobile has no call-out line.** Desktop shows "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY", but it's hidden on mobile for both variants. Playbook: "Call-out line on the first 3 pages, kept to one line."
5. **Unverified stats.**
   - "(With a 89% success rate)" is on the page.
   - The Wasted-spend ad says "95% of our students hit Grade 7+ in under 75 days. 75% exceed their school's predictions" and "Featured in The Guardian, BBC Radio".
   - None of these are in the client profile. The profile's stats are "2000+ students served. 2-4 grade increase in 75 days. top university attendance. grade 7-9".
   - The page's 89% and the ad's 95% also contradict each other. Confirm the source or remove them.
6. **Footer has no privacy policy link.** It only shows "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS". Playbook: "Terms and privacy policy links in every footer (required by Facebook ...)". Also update 2025 to 2026.
7. **Microsoft Clarity isn't in the page code.** I found no Clarity or GTM script in the page source. Install it (funnel head tracking) before starting the tests below, or the T1-A/T1-B labels have nothing to record.
8. **Finish or stop the current headline test (started Oct 9).** The "OLD TESTS WINNER vs LOSER" table in the "A/B LP test bank" tab is empty, so earlier results (Oct 2 VSL preview popup, Oct 6 "Your Child Already Has a Tutor" headline) aren't logged.

---

## 5 A/B tests (biggest expected lift first)

### T1. Remove the money question and the last name field
- **A (now), 6 inputs:**
  - "First Name (Parent's ONLY) *"
  - "Last Name (Parent's ONLY)"
  - "Phone (Parent's ONLY) *"
  - "Email (Parent's ONLY) *"
  - "What year is your child in? *" (10 / 11)
  - "Which best describes you? *" with the options "I want the best outcome, and I'm ready to invest" / "I want good results, but price matters to me" / "I want the lowest-cost option available"
- **B, 4 inputs:**
  - "First Name *" and "Phone *" side by side
  - "Email *" full width
  - "What year is your child in? *" (Year 10 / Year 11)
  - Keep one small line above the form: "For parents only."
- **Why:**
  - The playbook says "B2C: never mention money ('It is a complete drop off moment')".
  - It also says pre-qualifiers are "not for competitive ones like college consulting, SAT/ACT". GCSE tutoring is crowded (MyEdSpace and others).
  - It says "If CPL is already $45-50, don't". CPL is £37.08 for the last 7 days and £45.48 for the last 3 days, against the client's max of £15.
  - The playbook form is "first name + phone (two columns), email full width".
  - The money question already sends low-budget parents a signal on a cold page. Qualification belongs in the survey after opt-in.

### T2. Make the headline match the live ad (mocks + 2 to 4 grades), same on desktop and mobile
- **A (now):**
  - Variant 325234 on desktop: "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days"
  - Variant 745155 everywhere, and all mobile: "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s (With a 89% success rate)"
  - Sub-line on both: "Enter your information below to learn how this system works:"
- **B:**
  - Call-out: "FOR UK PARENTS OF YEAR 10 & 11 STUDENTS WITH MOCKS COMING UP"
  - Headline: "Help Your Child Jump 2 to 4 GCSE Grades in as Little as 75 Days"
  - Sub: "See how 2,000+ students fixed costly exam mistakes and gained confidence before their mocks and finals."
- **Why:**
  - The ad with 97% of spend opens with "ATTENTION UK PARENTS WITH UPCOMING MOCKS" and promises "I've helped 2,000+ students improve by 2–4 GCSE grades" so students can "Fix costly mistakes ✔️ Gain confidence fast ✔️ Perform better in mocks and finals". The page never says "mocks".
  - Playbook: "Headline = the offer ('Get X in X time, or guarantee') and it must be the same on every page", and "Landing page conversion (clicks → leads) < 25% → headline/offer must match the ad".
  - The B headline is the client's own offer line ("improve by 2–4 grades in as little as 75 days").
  - There is no guarantee line because the profile says "We don't have a guarantee".

### T3. Button says what they get
- **A (now):** "Submit"
- **B:** "Show Me How It Works", with a line under the button: "Takes 30 seconds. No payment required."
- **Why:**
  - The page promises "learn how this system works" and the button doesn't repeat it.
  - Playbook: the opt-in button is "Access" (it names the action and the reward). "Submit" names neither.
  - The line under the button is already in the client's test bank ("✓ Takes 30 seconds · No payment required").
  - If the next step is the consultation booking, use "Book My Free Consultation" instead so it matches the ad's "Book your free consultation today." (see Questions).

### T4. Parent proof next to the form, parents first
- **A (now):** the reviews start under the form. 7 of the 9 cards are from students. The first card is "Matthias Amilegbe, Student". The two parent reviews (Kiran Hayre, Magdalena Manthey) are 4th and 8th.
- **B:** add a strip directly above the first form field: "★★★★★ 4.4 on Google (100+ reviews)" plus one quote: "my child improved by 4 grades in GCSE Science in just 3 months!" Kiran Hayre, parent. Then reorder the review wall so the two parent reviews come first.
- **Why:**
  - Parents are the buyer (profile: "Parents - the students are below 18 years old").
  - The skill rule is "parent reviews first when parents are the buyer". Playbook squeeze page: "short form, Google/Trustpilot reviews block".
  - On mobile, no proof shows until after the form (reviews start at about 1,400px).

### T5. VSL preview image above the form
- **A (now):** no preview of what they get. Both variants have only the logo, headline and form above the fold.
- **B:** a 10-second VSL preview GIF between the headline and the form, with the overlay "Watch: how Smarta students jump 2 to 4 GCSE grades". Clicking it opens the same 4-field form in a pop-up.
- **Why:**
  - Playbook squeeze page elements: "logo, call-out, headline, subheadline, VSL preview GIF ..., short form, Google/Trustpilot reviews block". It's the only missing element.
  - The sheet shows this was tried ("new LP test: VSL preview with popup", Oct 2, and Sep 24 "a/b tested without VSL preview"). Skip this test if that one clearly lost. If it wasn't logged, re-run it on the shorter form.

---

## How to run them

- **Traffic:** 818 link clicks in the last 7 days (sheet), about 117 a day. A 50/50 split gives each version about 58 visitors a day.
- **Time per test:** about 150 visitors per version takes about 3 days. Run each test 3 to 4 days, and up to 7 if the gap is under 3 points. That matches the client's own rule in the test bank: "at about 150+ visits per version, if one version is ahead by 3+ percentage points ... If it's closer than that, keep it running another week."
- **Order:**
  - Day 0: Fix first #1 to #4 (pixel, +44, mobile headline, mobile call-out) and install Clarity.
  - Then T1 → T2 → T3 → T4 → T5, one at a time. The winner of each becomes A for the next.
- **Bundling:** traffic is enough to test one thing at a time. If Ema wants faster results, T3 (button) and T4 (proof strip) are both small and can go into one B version.
- **Judge on sheet LPCR** (Lead ÷ Link Clicks in the OLead tab). Meta LPVs aren't usable until the pixel is fixed.
- **Clarity labels:** T1-A / T1-B (money question), T2-A / T2-B (headline), T3-A / T3-B (button), T4-A / T4-B (proof strip), T5-A / T5-B (VSL preview). Tag each GHL variant page with its label.
- **Check both devices** on every variant before starting (Fix first #3 shows mobile can drift from desktop).

---

## Questions for Ema or the client

1. What happens after opt-in: a training/VSL page, or straight to booking? The ad says "Book your free consultation today." and the page says "learn how this system works". The answer decides the T3 button text.
2. Was "Which best describes you?" (the price question) on the OSchedule opt-in too? If yes, when was it added? OSchedule LPCR fell from 9.3% (Sep 7 to 13) to 5.5% (Sep 14 to 20) and 3.0% (Sep 21 to 27). The sheet comments for that period are "launched new ads" (Sep 16) and "a/b tested without VSL preview" (Sep 24).
3. Where do "89% success rate", "95% of our students hit Grade 7+", "75% exceed their school's predictions" and "Featured in The Guardian, BBC Radio" come from? The profile lists "2000+ students served" and also "over 1,000 students".
4. Who won the Oct 2 VSL preview popup test and the Oct 6 "Your Child Already Has a Tutor. So Why Aren't Their Grades Moving?" headline test? That headline matched the Wrong-tutor ad.
5. With no pixel on the opt-in, how is Meta getting Lead events (CAPI from GHL)? Does the Wrong-tutor ad set optimise on that event?
6. The sheet header says "Adspend (USD)" but the ad account is GBP. Are the numbers GBP? They match the Meta GBP spend.

---

## Appendix: Facts pulled

### LPCR (sheet "(ST) OLead - Business Reporting B2C", monthly tabs Sep/Oct, columns "Link Clicks" (E) and "Lead" (H); LPCR = Lead ÷ Link Clicks)
- **Last 7 days (Oct 5 to 11):** 57 leads / 818 clicks = **7.0%**. Spend £2,113.61, CPL £37.08, 5 calls booked.
- **Last 3 days (Oct 9 to 11):** 19 / 336 = **5.7%**. CPL £45.48. Daily: Oct 9 6.4%, Oct 10 6.6%, Oct 11 4.2%.
- **Best month of 2026:**
  - OLead funnel: October so far, 90 / 1,249 = **7.2%**. It launched Sep 28, so September is only 3 days (12 / 239 = 5.0%).
  - Account-wide: August on the OSchedule funnel, 160 / 1,672 = **9.6%** (Dash tab, OSchedule sheet).
- **When it dropped:**
  - OSchedule held 9.2% to 10.8% a week from Aug 17 to Sep 13, then fell to 5.5% (Sep 14 to 20) and 3.0% (Sep 21 to 27).
  - OLead has never been above about 7% a week (6.7% Sep 28 to Oct 4, 7.0% Oct 5 to 11).
  - The best OLead days were Oct 1 (9.9%), Oct 4 (10.1%) and Oct 7 (9.4%).
- **Sheet comments (OLead):** Sep 28 "launched", Sep 30 "increased budget to 200", Oct 2 "new LP test: VSL preview with popup", Oct 5 "budget to 300", Oct 6 "new A/B test running", Oct 9 "new LP test", Oct 11 "turned off OSchedule".
- **Sheet KPI tab:** "Landing Page Conversion Rate > 25%".

### Ad copy (live, spending)
- **Wrong-tutor** (97% of spend). Headline "Expert GCSE Tutors", description "UK's leading GCSE tutors", CTA Learn More. Primary text:
  > "ATTENTION UK PARENTS WITH UPCOMING MOCKS / Mock results shape confidence, placement, and future options. / I've helped 2,000+ students improve by 2–4 GCSE grades using smarter preparation focused on exam technique and how examiners actually mark. / I help students: ✔️ Fix costly mistakes ✔️ Gain confidence fast ✔️ Perform better in mocks and finals / Book your free consultation today."
- **Wasted-spend.** Headline "Real Grade Transformation In A Few Weeks". Primary text opens:
  > "Grade 4 to Grade 8 in a few months? ... 95% of our students hit Grade 7+ in under 75 days. 75% exceed their school's predictions. ... Featured in The Guardian, BBC Radio. Trusted by elite schools across the UK. ... Book your free consultation now."
- **Link:** smartaeducation.co.uk/optin-here?utm_source=meta&utm_medium=paid_social&utm_campaign=pcw_leads&utm_content=wrongtutorvideoad (wastedspendvideoad for the second ad).

### Page copy (both variants)
- **Variant /optin-325234, desktop:**
  - Call-out: "FOR PARENTS OF MOTIVATED YEAR 10 & 11 STUDENTS ONLY"
  - Headline: "Discover How 2,000+ Students Jumped 2 to 4 Grades in Their GCSEs in Under 75 Days"
- **Variant /optin-745155-4725, and all mobile:** "Discover the Secret Smarta System That's Helped 2000+ Students Score Grade 8/9s" / "in GCSE Maths, Science & English" (mobile) / "(With a 89% success rate)". There is no call-out on mobile.
- **Both:**
  - Sub-line: "Enter your information below to learn how this system works:"
  - Fields: First Name (Parent's ONLY) *, Last Name (Parent's ONLY) (optional), Phone (Parent's ONLY) * (default US +1, placeholder "+1 (555) 000-0000"), Email (Parent's ONLY) *, "What year is your child in? *" (10 / 11), "Which best describes you? *" (3 price options, quoted in T1).
  - Hidden UTM fields work (source, medium, campaign, content are filled). No test data in the fields. Cloudflare Turnstile (invisible) is on the form.
  - Button: "Submit".
  - Then: "What Parents & Students Are Saying / GOOGLE REVIEWS ★★★★★ 4.4 · 100+ reviews". 9 review cards (7 students, 2 parents), a university logos strip, and the footer "COPYRIGHTS 2025 | SMARTAEDUCATION.CO.UK | TERMS & CONDITIONS".
- **No VSL preview, video or GIF** on either variant.
- **Page position:**
  - Desktop: Submit at 987px (325234) and 1,069px (745155), below the 900px fold.
  - Mobile: the first field starts at 578px and Submit is at 1,318px on an 844px screen, so the form is **not** fully visible without scrolling.
- **Load time** in a headless test: about 1.1s (mobile) and 1.6s (desktop) to page load.

### Client profile facts
- **Offer:** "We help ambitious Year 10 & 11 GCSE students improve by 2–4 grades in as little as 75 days." Programmes: HONOURS / ADVANCESMARTA / GROWTH Academy, 9 months £2,250 to £12,000.
- **Guarantee:** none. "We don't have a guarantee or work with anyone for free."
- **Proof:** "2000+ students served. 2-4 grade increase in 75 days. top university attendance. grade 7-9." The profile also says "helped over 1,000 students". About 350 students last year. Testimonials are in a separate folder (not opened).
- **ICP:** parents of Year 10 and 11 students in England/UK. They value education, the child can reach 7 to 9, they want a structured long-term programme, often private and grammar school families.
- **Qualified lead:** parent of a Year 10/11 student in England, wants GCSE Maths/Science/English, budget about £2,300 to £5,800+, wants to start now, motivated student, both parents and the student attend the consultation, wants an ongoing programme.
- **Client targets:** max CPL £15, cost per booked call £50.

### Could not get, and why
- **Video content of the ads:** I only saw a preview frame (Marta at her desk, "over 2000" caption; Wasted-spend: UCL building, "or UCL"). I couldn't watch the full video, so the Wrong-tutor spoken hook isn't quoted.
- **Next steps after opt-in** (training page, survey, booking): not loaded, to avoid submitting a fake lead.
- **Results of earlier LP tests** (Oct 2, Oct 6, Oct 9): not logged in the sheet's winner/loser table.
- **GHL funnel stats** (page views → opt-ins per variant): not pulled. I skipped HighLevel to save time, so the per-variant split is unknown.
- **Sheet lead source** (GHL or Meta): not labelled in the sheet. Pre-qualified and qualified columns are empty for Sep and Oct.
- **Whether OSchedule used the same opt-in page:** not confirmed.
- **Meta link_url:** not returned by ads_get_creatives. I took it from the ad preview's destination link instead.
