# IPS · TextMagic + Zapier build steps

Goal: Zapier puts each lead on the right TextMagic list. TextMagic Flows send the texts and stop when someone replies.

Before you start, have open: TextMagic, Zapier, JotForm, Calendly.

---

## PART 1 · TextMagic lists (3 min)

Contacts → Lists → New list. Make these 4:

- [ ] IPS New Lead
- [ ] IPS Qualified
- [ ] IPS No Show
- [ ] IPS Booked

---

## PART 2 · Zapier (12 min)

### Zap A: Opt-in → IPS New Lead
Start from Violet's Zap "Meta Ads Jotform to Textmagic". **Delete "Delay Until" and "Send SMS".**

1. **Trigger:** JotForm, New Submission, form **262984250929368** (the /access opt-in)
2. **Filter** (add between 1 and 2), only continue if:
   - "Are you ready to invest in it?" **does not contain** "only looking for free info"
   - **AND** "When do you want to start…" **does not contain** "just exploring"
3. **Formatter → Text → Default value / compose phone:** `+1{{Area Code}}{{Phone Number}}` (no spaces or dashes)
4. **TextMagic → Create Contact**
   - Phone: the output of step 3
   - First name: First Name
   - Email: Email
   - List: **IPS New Lead**
5. Test with your own number, then turn it on.

### Zap B: Application → IPS Qualified
Copy Zap A (⋮ → Duplicate), then change:

1. **Trigger:** JotForm, New Submission, form **262803770587365** (the /training application)
2. **Filter:** only continue if the answers are **not** the disqualifying ones (match whatever is live on that form, e.g. "Things are really tight…" or "Under $2,000", and "never heard of a sleep consultant")
3. Phone formatter: same as Zap A (this form calls the field "Phone Number")
4. **TextMagic → Create Contact** (or **Update Contact** if they already exist from the opt-in)
   - List: **IPS Qualified**
   - If the action lets you replace lists, set it to IPS Qualified only, so they leave IPS New Lead

### Zap C: Booked → IPS Booked
1. **Trigger:** Calendly, Invitee Created, event "Free Career Call" (info-lniy)
2. Phone formatter if Calendly gives the number with spaces or dashes
3. **TextMagic → Update Contact** (find by phone)
   - List: **IPS Booked** (and take them off IPS New Lead and IPS Qualified if the action allows)

### Zap D: No-show → IPS No Show
1. **Trigger:** Calendly, Invitee No Show (if Zapier doesn't have it, use an ActiveCampaign tag "no-show" that Missy adds after the call)
2. **TextMagic → Update Contact**
   - List: **IPS No Show** (take them off IPS Booked)

---

## PART 3 · TextMagic Flows (12 min)

Automations/Flows → New flow. Same pattern for all 3:
**Trigger → Delay → SMS → Wait for reply & split.**
- **Path X, Any reply:** end the Flow (add "Notify" to Missy if it's offered)
- **Path Y, No reply:** next delay and SMS

Insert the name with **Insert tag → First name**, and check it shows as **[FirstName]**.

### Flow 1 · IPS New Lead
Trigger: Contact is added to a list → **IPS New Lead**

| Step | Wait | SMS |
|---|---|---|
| 1 | 5 min | Hey [FirstName]! Violet here from IPSP 👋 Saw you just grabbed The Sleep Consultant Career Breakdown. I'm curious, what got you interested in sleep consulting? |
| 2 | 1 hr, if no reply | I'd love to know a little about you! What does your work look like right now, and what would you change about it if you could? |
| 3 | Next morning, if no reply (about 16 hrs) | Hey [FirstName], just wanted to follow up... totally understand you're probably busy! No rush at all, I'd still love to hear from you whenever you get a minute 😊 |
| 4 | 1 day, if no reply | Quick one [FirstName] 😊 Finish this sentence for me: "I want to become a sleep consultant so I can ______" |

### Flow 2 · IPS Qualified
Trigger: Contact is added to a list → **IPS Qualified**

| Step | Wait | SMS |
|---|---|---|
| 1 | 2 min | Hi [FirstName]! It's Violet from IPSP 👋 I saw you wanted to chat. Here's my calendar so you can grab a time: https://violetsleepbabysleep.ac-page.com/slots |
| 2 | 2 hrs, if no reply | [FirstName], did the calendar link come through okay? Happy to find a time that works for you 😊 |
| 3 | 1 day | Hi [FirstName], it's Violet 😊 Do any times this week work for a quick chat? Here's the link again: https://violetsleepbabysleep.ac-page.com/slots |
| 4 | 1 day | [FirstName]? I just need a time from you and we're all set 😊 https://violetsleepbabysleep.ac-page.com/slots |
| 5 | 4 days | Hi [FirstName], I saved a little something for you: my Sleep Consultant Starter Kit 💙 https://instituteofpediatricsleep.com/wp-content/uploads/2026/05/Starter-Kit-2026.pdf And whenever you're ready to chat: https://violetsleepbabysleep.ac-page.com/slots |
| 6 | 3 days | [FirstName], do you still want to chat, or has the timing changed? Either way, just let me know 😊 https://violetsleepbabysleep.ac-page.com/slots |

### Flow 3 · IPS No Show
Trigger: Contact is added to a list → **IPS No Show**

| Step | Wait | SMS |
|---|---|---|
| 1 | 15 min | Hi [FirstName], it's Violet from IPSP 👋 Looks like we missed each other today. No worries at all! Here's the link to reschedule: https://violetsleepbabysleep.ac-page.com/slots |
| 2 | 2 days | Hi [FirstName], I just tried reaching you. If becoming a certified sleep consultant is still a priority, you can rebook here: https://violetsleepbabysleep.ac-page.com/slots |
| 3 | 2 days | Hi [FirstName], quick check. Are you still thinking about a real plan to become a sleep consultant? You can rebook here: https://violetsleepbabysleep.ac-page.com/slots |
| 4 | 10 days | Hi [FirstName], should I close your file for now? If you'd still like to explore a real plan to become a sleep consultant, here's the link: https://violetsleepbabysleep.ac-page.com/slots |

---

## PART 4 · Test (5 min)

- [ ] Opt in on /access with your phone → SMS 1 arrives in about 5 min
- [ ] Reply "hi" → you're moved to Path X, and **no** SMS 2 arrives
- [ ] Fill the /training application with a qualifying answer → Qualified SMS 1 arrives
- [ ] Book a test call → **check that no more Qualified texts arrive.** If they still come, add a condition before each SMS in Flow 2: "Contact is NOT in list IPS Booked" (if TextMagic has it), or tell me and we'll find another way
- [ ] Pick a disqualifying answer → no text at all
- [ ] Turn off the old ActiveCampaign SMS steps once all of this works

## Watch-outs

- **Phone format:** always +1 and the number with no spaces, or TextMagic may reject it.
- **Calendly reminders** stay in Calendly. Don't rebuild them here.
- **Replies:** they all land in the TextMagic inbox. Missy can answer from the TextMagic phone app.
