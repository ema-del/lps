# IPS · Moving all SMS from ActiveCampaign to TextMagic

**Moving:** New lead, Qualified lead and No Show texts (14 messages).
**Not moving:** Calendly reminders (Calendly sends those) and Long Term.

Time: about 1 to 1.5 hours, one time.

---

## How it works (the simple version)

TextMagic can't run timed sequences on its own. So:

- **ActiveCampaign keeps doing the timing.** The automations, waits and "stop if they booked" rules all stay as they are.
- **Each "Send SMS" step in ActiveCampaign becomes an "Add tag" step.** For example, the tag `sms-newlead-1`.
- **One Zap in Zapier sends the text.** When a contact gets any tag starting with `sms-`, Zapier looks up the message for that tag and sends it from TextMagic.
- **A second Zap stops texting people who reply.** A reply in TextMagic adds the tag `sms-replied` in ActiveCampaign, and every SMS step checks for that tag first.

You build 2 Zaps total. No per-message Zaps.

---

## Step by step

### A. TextMagic (10 min)
1. Make sure the sending number is the one Violet's leads already know.
2. In Settings, find the API key. Zapier asks for it once when you connect TextMagic.

### B. Zap 1: Send the texts (20 min)
1. **Trigger:** ActiveCampaign, "Tag added to contact" (the exact name in Zapier may differ slightly).
2. **Filter:** only continue if the tag name **starts with** `sms-` and is **not** `sms-replied`.
3. **Formatter → Utilities → Lookup Table:**
   - Lookup key: the tag name
   - Table: paste the 14 rows from the table below (tag → message)
4. **Formatter → Text → Replace:** replace `%FIRSTNAME%` with the contact's first name.
5. **TextMagic → Send SMS:**
   - Phone: the contact's phone
   - Text: the output of step 4

### C. Zap 2: Stop when they reply (10 min)
1. **Trigger:** TextMagic, "New inbound message".
2. **ActiveCampaign → Find contact** by phone.
3. **ActiveCampaign → Add tag** `sms-replied`.
4. Optional: **Slack or email Missy** "New SMS reply from [name]" so the team answers fast.

### D. ActiveCampaign (30 min)
In the **New lead**, **Qualified lead** and **No Show** automations, for each "Send SMS" step:
1. Add an **If/Else** before it: "Has tag `sms-replied`?" If yes, skip the SMS.
2. Replace the SMS step with **Add tag** (the tag from the table below).
3. Keep all the waits exactly as they are.

### E. Test (10 min)
1. Opt in on /access with your own phone, using a test email.
2. Check the first text arrives within 5 minutes.
3. Reply to it, and check `sms-replied` gets added and the next text doesn't come.
4. Turn off ActiveCampaign SMS (and its billing) once it works.

---

## The 14 messages

Merge field: `%FIRSTNAME%` (Zap 1 swaps it in).
Booking link updated to https.

### New lead (after opt-in on /access)

| Tag | When | Message |
|---|---|---|
| sms-newlead-1 | 5 min after opt-in | Hey %FIRSTNAME%! Violet here from IPSP 👋 Saw you just grabbed The Sleep Consultant Career Breakdown. I'm curious, what got you interested in sleep consulting? |
| sms-newlead-2 | 1 hr later | I'd love to know a little about you! What does your work look like right now, and what would you change about it if you could? |
| sms-newlead-3 | Next morning | Hey %FIRSTNAME%, just wanted to follow up... totally understand you're probably busy! No rush at all, I'd still love to hear from you whenever you get a minute 😊 |
| sms-newlead-4 | Day 1 | Quick one %FIRSTNAME% 😊 Finish this sentence for me: "I want to become a sleep consultant so I can ______" |

### Qualified lead (passed the application, hasn't booked)

| Tag | When | Message |
|---|---|---|
| sms-qual-1 | Within minutes | Hi %FIRSTNAME%! It's Violet from IPSP 👋 I saw you were looking for a time to chat. Here's my calendar so you can grab a slot: https://violetsleepbabysleep.ac-page.com/slots |
| sms-qual-2 | 2 hrs later | %FIRSTNAME%, did the calendar link come through okay? Happy to find a time that works for you 😊 |
| sms-qual-3 | Day 1 | Hi %FIRSTNAME%, it's Violet 😊 Do any times this week work for a quick chat? Here's the link again: https://violetsleepbabysleep.ac-page.com/slots |
| sms-qual-4 | Day 2 | %FIRSTNAME%? I just need a time from you and we're all set 😊 https://violetsleepbabysleep.ac-page.com/slots |
| sms-qual-5 | Day 6 | Hi %FIRSTNAME%, my calendar's filling up this month. Want me to hold a spot for you? https://violetsleepbabysleep.ac-page.com/slots |
| sms-qual-6 | Day 9 | %FIRSTNAME%, do you still want to chat, or has the timing changed? Either way, just let me know 😊 https://violetsleepbabysleep.ac-page.com/slots |

### No Show (missed the Career Call)

| Tag | When | Message |
|---|---|---|
| sms-noshow-1 | Same day | Hi %FIRSTNAME%, it's Missy from IPSP 👋 Looks like we missed each other today. No worries at all! Here's the link to reschedule: https://violetsleepbabysleep.ac-page.com/slots |
| sms-noshow-2 | Day 2 | Hi %FIRSTNAME%, I just tried reaching you. If becoming a certified sleep consultant is still a priority, you can rebook here: https://violetsleepbabysleep.ac-page.com/slots |
| sms-noshow-3 | Day 4 | Hi %FIRSTNAME%, quick check. Are you still thinking about a real plan to become a sleep consultant? You can rebook here: https://violetsleepbabysleep.ac-page.com/slots |
| sms-noshow-4 | Day 14 | Hi %FIRSTNAME%, should I close your file for now? If you'd still like to explore a real plan to become a sleep consultant, here's the link: https://violetsleepbabysleep.ac-page.com/slots |

---

## Things to check

- **Opt-out:** TextMagic handles STOP replies, but make sure STOP also tags the contact in ActiveCampaign, or Zap 1 keeps trying to send them texts.
- **Sender:** the New lead and Qualified texts come from "Violet", the No Show texts from "Missy". Make sure whoever answers the TextMagic inbox knows that.
- **Qualified Day 6:** I softened "one of the last spots" to "a spot", unless her calendar really is nearly full.
- **Zapier plan:** Zap 1 has 5 steps, so it needs a paid Zapier plan (multi-step Zaps). Make.com works the same way and is cheaper, if Pacow already has it.
