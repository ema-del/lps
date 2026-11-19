from _common import *
P=lambda *xs:''.join(f'<p>{x}</p>' for x in xs)
INTRO=lambda who,repl: P(f'<b>For:</b> {who}', f'<b>Replaces:</b> {repl}',
 '<b>Voice:</b> rewritten to sound like Violet, using her own Starter Kit emails and resources (her sneak peek video, Starter Kit, student stories, free Facebook group, her book).',
 '<b>SMS tokens:</b> SMS go out through TextMagic, so the first name tag is <b>[FirstName]</b>. Emails stay in ActiveCampaign with <b>%FIRSTNAME%</b>.')

# ---------- NEW LEAD ----------
nl=[]
nl.append(email('DAY 0 · Right after opt-in','Your Sleep Consultant Career Breakdown, %FIRSTNAME% 💙','Plus one quick favor before you watch',P(
 'Hi %FIRSTNAME%,','Violet Giannone here. I\'m a Registered Nurse and the founder of IPSP&reg;.',
 'Thank you for trusting me with your email. I know a lot of people grab your address and then bury you in emails you never asked for. I promise these will be worth opening.',
 'Here\'s your free video:', '👉 '+a(TRAIN,'Watch The Sleep Consultant Career Breakdown'),
 'In it, I walk you through how moms, nurses, nannies and teachers become certified pediatric sleep consultants and build a business they run from home, on their own schedule.',
 'Nap time is a great time to watch it 😉',
 'One favor before you go. Can you hit reply and tell me the #1 thing holding you back from a career you love right now? One sentence is perfect. I read every answer.')+V+P('P.S. Questions while you watch? Reply here or call/text me at (833) 600-6292.')))
nl.append(sms('5 min after opt-in','Hey [FirstName]! Violet here from IPSP 👋 Saw you just grabbed The Sleep Consultant Career Breakdown. I\'m curious, what got you interested in sleep consulting?'))
nl.append(sms('1 hr later, if no reply','I\'d love to know a little about you! What does your work look like right now, and what would you change about it if you could?'))
nl.append(sms('Next morning, if no reply','Hey [FirstName], just wanted to follow up... totally understand you\'re probably busy! No rush at all, I\'d still love to hear from you whenever you get a minute 😊'))
nl.append(email('DAY 1 · Did you watch?','Did the video come through okay?','Most of our students start exactly where you are',P(
 'Hi %FIRSTNAME%,','Just checking that your Career Breakdown came through.',
 'If you\'re here because you\'re quietly wondering whether sleep consulting could be your next step, I want you to know that\'s how most of our students start.',
 'Not fully decided.<br>Not totally sure.<br>Just wanting to learn more before taking a big step.','And honestly? That\'s exactly how it should be.',
 '👉 '+a(TRAIN,'Here\'s the video again'),
 'Watching doesn\'t commit you to anything. My goal is simply for you to feel informed and confident about what might be next for you.')+V))
nl.append(sms('Day 1','Quick one [FirstName] 😊 Finish this sentence for me: "I want to become a sleep consultant so I can ______"'))
nl.append(email('DAY 2 · The gap','Why so many women stay stuck at "someday"','It has nothing to do with being capable',P(
 'Hi %FIRSTNAME%,','Almost no one struggles in this field because they aren\'t capable.','They struggle because of what I call the gap.',
 'The gap between getting certified and knowing how to turn that certificate into a real business.','Here\'s what it looks like in real life.',
 'You finish a program.<br>You feel excited.<br>You\'re ready to begin.','Then the questions start.',
 'How do I get clients?<br>Where do they come from?<br>What do I do first?',
 'Most programs teach the material and stop there. Getting your first family is a completely different skill, and nobody teaches it.',
 'That\'s why IPSP includes a full module on getting clients and 6 months of 1:1 mentorship after you certify.',
 'I show you how we close the gap in the video:','👉 '+a(TRAIN,'Watch the Career Breakdown'))+V+P('P.S. If you\'re feeling unsure right now, that\'s not a red flag. It usually means you\'re taking this seriously.')))
nl.append(email('DAY 3 · Offer the call','Can I look at your situation with you?','30 minutes, free, and honest',P(
 'Hi %FIRSTNAME%,','Every woman who comes to IPSP starts from a different place.',
 'Some are nurses, OTs and doulas who still love caring for families but can\'t keep doing it on someone else\'s schedule. Some are moms who want to work from home and be there for the little moments. Some have already helped friends get their babies sleeping and think, "could I actually do this?"',
 'So if you\'d like, let\'s hop on a free Career Call. It\'s 30 minutes with our team. We\'ll look at where you\'re starting from and give you an honest read on whether IPSP is the right fit.',
 '👉 '+a(TRAIN,'Book your free Career Call'),'No pressure. Just clarity.','And if this path isn\'t right for you, that\'s okay too.')+V))
nl.append(email('DAY 5 · Andria\'s story','"I wanted it to be part time"','She now leads her own team of consultants',P(
 'Hi %FIRSTNAME%,','I want to tell you about Andria.','She wanted sleep consulting to be part time. Something on the side that fit around her life.',
 'She got certified with IPSP, followed the steps and showed up to mentorship.',
 'Today, Andria (Have Baby Must Sleep) leads her own team of sleep consultants serving families all over the world.',
 'She didn\'t start with confidence or certainty. She started by closing the gap.',
 'And she\'s one of many. Shannon (Calm &amp; Sleepy) got fully booked while raising two little ones. Melissa (Rested Little Nest) had 16 clients in her second month.',
 'These aren\'t special unicorns 🦄 They\'re women who followed the IPSP process with heart, consistency and support.',
 '👉 '+a(REVIEWS,'Read their stories (screenshots included)'),'👉 '+a(TRAIN,'Book your free Career Call'))+V))
nl.append(email('DAY 7 · "What if I\'m not successful?"','"What if I never get a single client?"','I hear this from almost everyone',P(
 'Hi %FIRSTNAME%,','I already know what might be circling in your mind.',
 '"Okay Violet, it sounds amazing. But what if I\'m not successful? What if I never get a single client?"',
 'Almost every woman who\'s joined IPSP said those exact words at the start.',
 'They worried it wouldn\'t work. That they weren\'t cut out for it. That this would be one more thing they spent money on that didn\'t go anywhere.',
 'So here\'s my promise to you.',
 'Go through the training, do the work, show up to mentorship and follow the steps. If you don\'t land any clients at all, I\'ll keep mentoring you until you do. At no additional cost.',
 '👉 '+a(TRAIN,'Book your free Career Call'),'You\'re investing your time, energy and heart into your future. We take that seriously.')+V))
nl.append(email('DAY 10 · Which programs can you trust?','How to spot a fake sleep consultant program','Yes, that\'s a thing now',P(
 'Hi %FIRSTNAME%,','There are a lot of sleep consultant programs out there that look great on the outside.',
 'Many students tell me they didn\'t understand what they were really getting until after they\'d invested thousands of dollars.','I never want that to be your experience.',
 'Before you choose any program, ask 3 questions:',
 '1. Who actually teaches it? Look for credentialed instructors who stay with you, not a lineup of guest speakers.<br>2. Does it teach you how to get clients, or does it stop at the certificate?<br>3. What support do you get after you certify?',
 'I started IPSP in 2014 because so many programs were taught by people with no medical background. Ours is taught by Registered Nurses and credentialed instructors, and it\'s science-backed so families can trust you.',
 'Want to see how we teach? Here\'s a short '+a(PEEK,'sneak peek inside the program')+'.',
 '👉 '+a(TRAIN,'Book your free Career Call')+' and ask us anything.')+V))
nl.append(email('DAY 14 · Last check-in','Should I stop reaching out, %FIRSTNAME%?','No hard feelings either way',P(
 'Hi %FIRSTNAME%,','I don\'t want to clutter your inbox if the timing\'s off. Life with little ones is full enough.',
 'But if you still love helping families and you\'re ready for a career that fits your life, let\'s talk:',
 '👉 '+a(TRAIN,'Book your free Career Call'),
 'Either way, I\'m so glad you\'re here. You can always reply to this email or call/text me at (833) 600-6292.')+V+P('<i>After Day 14: move to Long Term nurture (not changed).</i>')))
open('new-lead.html','w').write(page('(IPS) New lead · Violet\'s voice',INTRO('everyone who opts in on /access','"(IPS) New lead" in ActiveCampaign'),nl,[
 'Andria: Violet\'s email says "a global team of eight", her DM says "a team of 9". I wrote "her own team" so it\'s true either way.',
 'I removed the old "confirming spots for this cycle" email. Add it back only if there\'s a real deadline.',
 'Stop all SMS as soon as they reply, so the team takes over the conversation.']))

# ---------- QUALIFIED ----------
q=[]
q.append(email('DAY 0 · Right after they pass the application','Here\'s my calendar, %FIRSTNAME% 💙','Pick any time that works',P(
 'Hi %FIRSTNAME%,','Violet here. I saw you\'re interested in a Career Call, and I love that!',
 'Here\'s my calendar so you can grab a time that works for you:','👉 '+a(SLOTS,'Book your free Career Call'),
 'It\'s 30 minutes. We\'ll look at where you\'re starting from and give you an honest read on whether IPSP is the right fit.',
 'Talk soon!')+V+P('P.S. Questions before you book? Reply here or call/text me at (833) 600-6292. I\'m usually available the same day.')))
q.append(sms('Within minutes','Hi [FirstName]! It\'s Violet from IPSP 👋 I saw you wanted to chat. Here\'s my calendar so you can grab a time: '+SLOTS))
q.append(sms('2 hrs later, if no booking','[FirstName], did the calendar link come through okay? Happy to find a time that works for you 😊'))
q.append(email('DAY 1 · A look inside first','Want to see how we teach before your call?','A short sneak peek inside IPSP',P(
 'Hi %FIRSTNAME%,','Before you ever consider enrolling in a certification program, I believe you deserve to see how you\'d be taught.',
 'So here\'s a short sneak peek inside the IPSP Sleep Consultant Certification. Full transparency.',
 '👉 '+a(PEEK,'Watch the IPSP sneak peek'),
 'You\'ll see our course dashboard, how the lessons are structured, the business training, and the credentialed instructors who teach inside the program.',
 'Then, if you\'d like to talk it through, grab a time here:','👉 '+a(SLOTS,'Book your free Career Call'))+V))
q.append(sms('Day 1','Hi [FirstName], it\'s Violet 😊 Do any times this week work for a quick chat? Here\'s the link again: '+SLOTS))
q.append(email('DAY 2 · Nothing to prepare','Takes 30 seconds to book','No prep needed',P(
 'Hi %FIRSTNAME%,','No prep needed on your end. Just pick a time and show up as you are.','Nap time works. So does after bedtime 😉',
 'On the call, we\'ll look at where you are right now and build a real plan to get certified and land your first clients.','That\'s it.',
 '👉 '+a(SLOTS,'Pick your time'))+V))
q.append(sms('Day 2','[FirstName]? I just need a time from you and we\'re all set 😊 '+SLOTS))
q.append(email('DAY 4 · Katie\'s story','"From unprepared to fully booked"','She didn\'t feel ready either',P(
 'Hi %FIRSTNAME%,','I want to tell you about Katie.','She was right where you are. Unsure if she was ready. Not sure where to even start.','Sound familiar?',
 'Before IPSP, Katie was an elementary teacher dealing with major burnout. She got certified, followed the plan step by step, and showed up to mentorship.',
 'Today she works from home, spends time with her daughter, and runs a fully booked practice.',
 'She didn\'t start out feeling ready. She started with one call.',
 '👉 '+a(REVIEWS,'Read more stories like Katie\'s'),'👉 '+a(SLOTS,'Book your Career Call'))+V))
q.append(email('DAY 6 · A gift while you decide','Your Sleep Consultant Starter Kit','Everything you need to know about this career',P(
 'Hi %FIRSTNAME%,','While you think about your call, I want you to have this.',
 'My Sleep Consultant Starter Kit walks you through everything you need to know about becoming a sleep consultant: what the work looks like, how sleep consultants get clients, and what to look for in a certification.',
 '👉 '+a(KIT,'Download your Starter Kit'),
 'And when you\'re ready to talk about your own path, my calendar is here:','👉 '+a(SLOTS,'Book your Career Call'))+V))
q.append(sms('Day 6','Hi [FirstName], I saved a little something for you: my Sleep Consultant Starter Kit 💙 '+KIT+' And whenever you\'re ready to chat: '+SLOTS))
q.append(email('DAY 9 · Did the timing change?','Did the timing change, %FIRSTNAME%?','Totally okay if it did',P(
 'Hi %FIRSTNAME%,','You took the time to fill out the application, so I know becoming a certified sleep consultant matters to you.',
 'If the timing shifted, that\'s okay. Life with little ones has a way of doing that. Just hit reply and let me know.',
 'But if you\'re still in, here\'s my calendar one more time:','👉 '+a(SLOTS,'Book your Career Call'))+V))
q.append(sms('Day 9','[FirstName], do you still want to chat, or has the timing changed? Either way, just let me know 😊 '+SLOTS))
q.append(email('DAY 12 · Last nudge','Last one from me 💙','Plus a place to keep learning',P(
 'Hi %FIRSTNAME%,','This is my last nudge, I promise.','The call is free. There\'s no commitment. And you\'re already qualified. The only thing left is picking a time.',
 '👉 '+a(SLOTS,'Book your Career Call'),
 'And if now isn\'t the right time, come hang out in our '+a(FB,'free Facebook group')+'. It\'s the perfect place to get your questions answered and connect with others who share your passion for sleep consulting.',
 'I\'m so glad you\'re here, either way.')+V+P('<i>After Day 12: move to Long Term nurture (not changed).</i>')))
open('qualified-lead.html','w').write(page('(IPS) Qualified lead · Violet\'s voice',INTRO('people who passed the application but haven\'t booked a call','"(IPS) Qualified lead" in ActiveCampaign'),q,[
 'Removed "my calendar is filling up / one of the last spots" (Day 6). Add it back only if her calendar really is nearly full.',
 'Katie\'s details come from her review on the site (former elementary teacher with burnout, now works from home). Double check Violet is happy using her name.',
 'Stop all emails and SMS as soon as they book.']))

# ---------- NO SHOW ----------
n=[]
n.append(email('DAY 0 · Same day','Missed you today, let\'s reschedule','No worries at all',P(
 'Hi %FIRSTNAME%,','We missed you on your Career Call today. Totally understandable. Schedules get busy, especially with little ones at home 💙',
 'Let\'s find a time that works better for you:','👉 '+a(SLOTS,'Rebook your Career Call'),
 'On the call, we\'ll look at where you are right now, what\'s standing between you and becoming a certified sleep consultant, and whether IPSP is the right fit.')+M))
n.append(sms('Same day','Hi [FirstName], it\'s Missy from IPSP 👋 Looks like we missed each other today. No worries at all! Here\'s the link to reschedule: '+SLOTS))
n.append(email('DAY 2 · A look inside','Here\'s what you missed','A short look inside IPSP',P(
 'Hi %FIRSTNAME%,','Since we didn\'t get to talk, I wanted to share something Violet always says: before you ever consider a certification program, you deserve to see how you\'d be taught.',
 'So here\'s a short sneak peek inside the program:','👉 '+a(PEEK,'Watch the IPSP sneak peek'),
 'If it sparks questions, let\'s talk them through:','👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(sms('Day 2','Hi [FirstName], I just tried reaching you. If becoming a certified sleep consultant is still a priority, you can rebook here: '+SLOTS))
n.append(email('DAY 3 · "Someday"','Before "someday" turns into next year','The women who did it started before they felt ready',P(
 'Hi %FIRSTNAME%,','Here\'s something most moms and caregivers underestimate.','"Someday" has a way of turning into next year.',
 'The women you see succeeding today didn\'t wait until everything felt perfect. They started before they felt ready, and they had support while they took each step.',
 '👉 '+a(REVIEWS,'See what happened when they started'),'If you want to see where you stand, here\'s the link:','👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(email('DAY 4 · Your plan','Still thinking about becoming a sleep consultant?','A plan built around your life',P(
 'Hi %FIRSTNAME%,','Just checking in again 💙',
 'Free info online can only take you so far. On the call, we look at exactly what\'s missing for you and build a plan around your life. Your schedule. Your family. Your goals.',
 '👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(sms('Day 4','Hi [FirstName], quick check. Are you still thinking about a real plan to become a sleep consultant? You can rebook here: '+SLOTS))
n.append(email('DAY 5 · Pause your file?','Should I pause your file?','Totally okay either way',P(
 'Hi %FIRSTNAME%,','I haven\'t heard back, so I wanted to check once more before I pause your file.',
 'If becoming a certified sleep consultant is still something you\'d like to explore, I\'d be happy to reconnect. And if now isn\'t the time, that\'s okay.',
 '👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(email('DAY 8 · Keep learning','Something to keep you going','Violet\'s free Starter Kit',P(
 'Hi %FIRSTNAME%,','Whether or not now is the right time, I want you to have Violet\'s Sleep Consultant Starter Kit. It covers everything you need to know about becoming a sleep consultant.',
 '👉 '+a(KIT,'Download the Starter Kit'),
 'You\'re also welcome in our '+a(FB,'free Facebook group')+', where you can ask questions and get a feel for what this career could look like for you.',
 'When you\'re ready, we\'re here:','👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(email('DAY 14 · Close your file?','Should I close your file?','Last check from me',P(
 'Hi %FIRSTNAME%,','I\'ve reached out a few times, and I don\'t want to crowd your inbox.',
 'If becoming a certified sleep consultant is still a priority, I\'m happy to keep your file open. If not, I\'ll close it for now.',
 '👉 '+a(SLOTS,'Rebook your Career Call'))+M))
n.append(sms('Day 14','Hi [FirstName], should I close your file for now? If you\'d still like to explore a real plan to become a sleep consultant, here\'s the link: '+SLOTS))
n.append(email('DAY 30 · Final note','A final note from us','Wishing you clarity either way',P(
 'Hi %FIRSTNAME%,','This is my final note.',
 'The women who become certified, booked sleep consultants didn\'t wait for the perfect moment. It rarely comes.',
 'If you still want clarity on this, now\'s a good time to reconnect:','👉 '+a(SLOTS,'Rebook your Career Call'),
 'And if this isn\'t your season, that\'s okay. You can always reply here or call/text Violet at (833) 600-6292. We\'re so glad you\'re here either way 💙')+M+P('<i>After Day 30: move to Long Term nurture (not changed).</i>')))
open('no-show.html','w').write(page('(IPS) No Show · Violet\'s voice',INTRO('people who booked a Career Call and didn\'t show','"(IPS) No Show" in ActiveCampaign'),n,[
 'Signed by Missy (she runs the calls), but now shares Violet\'s resources: sneak peek video, student stories, Starter Kit, Facebook group.',
 'Removed "spots are limited" and "regret" language. It read pushier than Violet\'s own emails.',
 'Stop everything as soon as they rebook.']))

# ---------- REMINDERS ----------
r=[]
r.append(P('<b>Important:</b> these are sent by <b>Calendly</b> (it knows the call time). Calendly tokens stay as they are: {{invitee_first_name}}, {{event_date}}, {{event_time}}, {{location}}.'))
r.append(email('IMMEDIATELY AFTER BOOKING · Confirmation','You\'re booked, {{invitee_first_name}}! 🎉','{{event_date}} at {{event_time}}',P(
 'Hi {{invitee_first_name}},','You\'re all set! Your free Career Call is confirmed for {{event_date}} at {{event_time}} 💙',
 'We just texted you too. If you saw this first, just reply YES to lock it in.',
 'On the call, we\'ll look at where you are right now, what\'s standing between you and becoming a certified sleep consultant, and whether IPSP is the right fit for you.',
 'No prep needed. Just show up as you are.','Join here: {{location}}',
 'While you wait, Violet put together a short sneak peek inside the program, so you can see exactly how you\'d be taught:',
 '👉 '+a(PEEK,'Watch the IPSP sneak peek'))+M))
r.append(sms('Confirmation','Hi {{invitee_first_name}}! It\'s Missy from IPSP 👋 Your free Career Call is set for {{event_date}} at {{event_time}}. Reply YES to confirm.','Calendly'))
r.append(email('14 HOURS AFTER BOOKING · Meet our grads','A few stories to read before your call','They started exactly where you are',P(
 'Hi {{invitee_first_name}},','Before your call on {{event_date}}, I want you to meet a few of our graduates. They came to us unsure, just like you might feel right now:',
 '• Andria wanted sleep consulting to be part time. Today she leads her own team of sleep consultants.<br>• Shannon got fully booked while raising two little ones.<br>• Katie left a burned-out teaching job and now works from home around her daughter.',
 'These aren\'t special unicorns 🦄 They\'re women who followed the IPSP process with heart, consistency and support.',
 '👉 '+a(REVIEWS,'Read their stories (screenshots included)'))+M))
r.append(sms('14 hrs after booking','Hi {{invitee_first_name}}, Missy here from IPSP! Before your call, see what our grads have to say 💙 '+REVIEWS,'Calendly'))
r.append(email('48 HOURS BEFORE · Only if booked 3+ days out','Get to know Violet before your call','The Christmas Day that started IPSP',P(
 'Hi {{invitee_first_name}},','Your call is coming up on {{event_date}}, so I wanted you to get to know the woman behind IPSP.',
 'On Christmas Day 2005, Violet\'s boss told her that if she left her nursing shift, she wouldn\'t have a job to come back to.',
 'For over a decade as a Registered Nurse, she kept choosing between her career and her kids. So she built a business she could run from home, and in 2014 she founded IPSP so other women could do the same.',
 'She\'s also the author of '+a(BOOK,'Baby Sleep Training in 7 Days')+', and you can follow along with her on '+a(IG,'Instagram')+'.',
 'See you on {{event_date}}!')+M))
r.append(email('24 HOURS BEFORE · Personal video','Your call\'s tomorrow at {{event_time}}','Watch this quick video first',P(
 'Hi {{invitee_first_name}},','Quick reminder. Your Career Call is tomorrow, {{event_date}} at {{event_time}}.',
 'Violet recorded a short video for you to watch before we connect:','👉 '+a(CONF,'Watch Violet\'s video'),
 'It\'ll help you get the most out of our time together. Reply DONE once you\'ve watched it so I know you\'re all set.',
 'Want to connect with others on the same path? Join our '+a(FB,'free Facebook group')+'.','Join the call here: {{location}}')+M))
r.append(sms('24 hrs before','Hi {{invitee_first_name}}! Your call is tomorrow at {{event_time}} 💙 Violet made a quick video for you to watch before we meet: '+CONF,'Calendly'))
r.append(email('1 HOUR BEFORE','Starting in 1 hour, here\'s your link','Bring your questions',P(
 'Hi {{invitee_first_name}},','Your Career Call starts in one hour, at {{event_time}}.',
 'Grab a coffee, find a quiet spot, and bring any questions you have. Nothing is off limits.','Join here: {{location}}')+M))
r.append(sms('1 hr before','Hi {{invitee_first_name}}! We\'re on in 1 hour. See you at {{event_time}} 💙 Link: {{location}}','Calendly'))
r.append(email('10 MINUTES BEFORE','10 minutes, join here','See you soon',P(
 'Hi {{invitee_first_name}},','We\'re starting in 10 minutes!','Join here: {{location}}','See you in there 💙')+M))
r.append(sms('10 min before','Hi {{invitee_first_name}}! See you in 10 minutes 💙 Link: {{location}}','Calendly'))
open('reminders.html','w').write(page('(IPS) Reminders · Violet\'s voice',INTRO('everyone who books a Career Call','"(IPS) Reminders" (Calendly workflows)'),r,[
 'These SMS stay in Calendly, because TextMagic doesn\'t know the call time. If you want them in TextMagic too, they need a Zap from Calendly with the time passed in.',
 'The 48-hours-before email is new. In Calendly, set it to only send when the call is 3+ days after booking (or skip it).',
 'The old confirmation SMS said Google Meet and the email said Zoom. I removed both and used {{location}} so it\'s always right.',
 'Calendly shows {{invitee_first_name}} as the first name. If a lead typed their full name in one box, it may show the full name.']))
print('built')
