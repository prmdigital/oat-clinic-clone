# -*- coding: utf-8 -*-
"""Blog posts.

To publish a new post, add a dict to the top of POSTS and run the build.
Newest first. `date` is ISO format and drives both the display date and the
Article JSON-LD. `body` is HTML that lands inside <div class="article-body">.
"""

AUTHORS = {
    "clinical": {
        "name": "OAT Clinic clinical team",
        "role": "Reviewed by our prescribing physicians",
        "initials": "OC",
    },
}

POSTS = [
    {
        "slug": "what-to-expect-first-week-methadone",
        "title": "What actually happens in your first week on methadone",
        "seo_title": "Your First Week on Methadone",
        "lede": (
            "The first week is the part nobody explains properly, and it is the week most "
            "people quit. Here is an honest account of what to expect, day by day, and why "
            "feeling rough on day three is not a sign that treatment is failing."
        ),
        "date": "2026-07-14",
        "updated": "2026-07-14",
        "category": "Starting treatment",
        "category_class": "",
        "read_time": "7 minute read",
        "author": "clinical",
        "meta_desc": (
            "An honest day by day account of the first week on methadone: what dosing feels "
            "like, why the dose starts low, and why day three is the hardest."
        ),
        "toc": [
            ("Day one", "day-one"),
            ("Days two and three", "days-two-three"),
            ("The rest of the first week", "rest-of-week"),
            ("What helps", "what-helps"),
            ("When to call us", "when-to-call"),
        ],
        "body": [
            "<p>Most written information about methadone describes how it works "
            "pharmacologically. Very little of it describes what the week feels like. That gap "
            "matters, because the most common reason people leave methadone treatment is not "
            "side effects or cost. It is quitting in the first ten days, convinced the "
            "medication is not working, when in fact it is working exactly as designed.</p>",

            "<h2 id=\"day-one\">Day one</h2>",
            "<p>Your first appointment takes longer than you expect, usually ninety minutes or "
            "more. There is a history to take, a physical assessment, a urine drug screen and a "
            "conversation about which pharmacy you want to use. Bring identification if you have "
            "it, and come anyway if you do not.</p>",
            "<p>Your first dose is deliberately low. Most people start somewhere in the range of "
            "ten to thirty milligrams, and if you have been using large amounts of fentanyl that "
            "number will sound absurd. Here is why it is not.</p>",
            "<p>Methadone has a long half life, which means it accumulates. The dose you take on "
            "Monday is still in your system on Thursday, adding to Tuesday and Wednesday doses. "
            "A dose that feels inadequate on day one can become dangerous by day four if it was "
            "set to feel adequate immediately. Every death in early methadone treatment comes "
            "from starting too high or going up too fast. So we start low, and we tell you in "
            "advance that it will feel low.</p>",
            "<p>That first dose usually takes the edge off within two to four hours. It will not "
            "hold you for a full day. Expect to feel some withdrawal by evening.</p>",

            "<h2 id=\"days-two-three\">Days two and three</h2>",
            "<p>This is the hard part, and it is where most people give up.</p>",
            "<p>You are attending the pharmacy daily for witnessed dosing. The dose is still "
            "building. You are probably still in some withdrawal for part of each day: restless "
            "legs at night, poor sleep, sweating, stomach trouble, and a low flat mood that is "
            "harder to describe than the physical symptoms and often worse.</p>",
            "<p>Day three is commonly the low point. Enough time has passed that the initial "
            "relief has worn off, but not enough for accumulation to have done its work. If you "
            "are also cutting down on other substances at the same time, it compounds.</p>",
            "<p>What we want you to know before you get there is that this is expected. It is "
            "not evidence that methadone does not work for you, that your dose is wrong for good, "
            "or that you have failed. It is the shape of the first week for almost everybody.</p>",

            "<h2 id=\"rest-of-week\">The rest of the first week</h2>",
            "<p>By days four and five, most people notice that the gaps are shortening. The dose "
            "holds a little longer. Sleep improves before mood does, which can be disorienting, "
            "since you may find yourself sleeping properly for the first time in months while "
            "still feeling emotionally flat.</p>",
            "<p>You will normally be reviewed around the end of the first week. The question we "
            "are asking is not whether you feel good. It is how many hours each dose holds you "
            "before withdrawal starts creeping back. If a dose covers you for sixteen hours, we "
            "need to go up. If it covers twenty four but leaves you sedated, we need to look at "
            "that too.</p>",
            "<p>Increases are usually small, commonly five to ten milligrams at a time, with "
            "several days between changes. Reaching a dose that holds you comfortably for a full "
            "day typically takes two to four weeks in total.</p>",

            "<h2 id=\"what-helps\">What helps during the first week</h2>",
            "<ul>"
            "<li><strong>Clear your schedule where you can.</strong> Treat this like recovering "
            "from an operation. If you can avoid a job interview or a court date in week one, do.</li>"
            "<li><strong>Ask about symptom medication.</strong> There are effective treatments "
            "for nausea, cramps, diarrhoea and sleeplessness during induction. Many people "
            "endure these unnecessarily because nobody mentioned they could be treated.</li>"
            "<li><strong>Eat and drink something, even without appetite.</strong> Dehydration "
            "makes every withdrawal symptom worse and is easy to overlook.</li>"
            "<li><strong>Have naloxone in the house.</strong> The first two weeks carry the "
            "highest risk, particularly if you use on top. This is precaution, not pessimism.</li>"
            "<li><strong>Tell one person what you are doing.</strong> Day three is much harder "
            "alone.</li>"
            "</ul>",

            "<h2 id=\"when-to-call\">When to call us rather than wait</h2>",
            "<p>Some things should not wait for your next scheduled appointment. Contact us the "
            "same day if you feel drowsy or find yourself nodding off after a dose, if you are "
            "still in significant withdrawal more than twelve hours after dosing, if you have "
            "missed two or more doses, or if you have been prescribed a new medication by anyone "
            "else.</p>",
            "<p>That last one catches people out. Methadone interacts with a long list of common "
            "medications, including some antibiotics and antidepressants. A prescription from a "
            "walk in clinic that nobody connected to your methadone is a genuine risk.</p>",
            "<p>If you are three days into treatment and thinking about stopping, please call us "
            "before you do. That conversation takes ten minutes and it changes outcomes more "
            "than almost anything else we do.</p>",
        ],
        "related_treatments": ["methadone", "suboxone"],
    },
    {
        "slug": "methadone-or-suboxone-how-to-choose",
        "title": "Methadone or Suboxone: how the choice actually gets made",
        "seo_title": "Methadone or Suboxone: How to Choose",
        "lede": (
            "Both are first line treatments and both work. The decision comes down to your "
            "tolerance, your schedule, and what you have already tried, rather than one being "
            "better than the other."
        ),
        "date": "2026-06-23",
        "updated": "2026-06-23",
        "category": "Choosing treatment",
        "category_class": "orange",
        "read_time": "6 minute read",
        "author": "clinical",
        "meta_desc": (
            "A practical comparison of methadone and Suboxone: tolerance, starting "
            "requirements, take home doses, and why switching between them is normal."
        ),
        "toc": [
            ("The question people actually ask", "the-question"),
            ("Where each one is stronger", "where-stronger"),
            ("The fentanyl problem", "fentanyl"),
            ("Practical differences", "practical"),
            ("Switching is normal", "switching"),
        ],
        "body": [
            "<h2 id=\"the-question\">The question people actually ask</h2>",
            "<p>Almost everyone arrives at a first appointment having already heard something "
            "definitive from someone else. Methadone is harder to get off. Suboxone does not work "
            "for fentanyl. Methadone rots your teeth. Suboxone puts you into instant withdrawal. "
            "Each of these contains a grain of truth wrapped in a lot of misunderstanding.</p>",
            "<p>Here is the framing we find more useful. Both medications are first line "
            "treatments recommended in British Columbia provincial guidance. Both dramatically "
            "reduce the risk of dying. The better medication for you is the one that keeps you in "
            "treatment, and that is a question about your life as much as your biology.</p>",

            "<h2 id=\"where-stronger\">Where each one is stronger</h2>",
            "<p><strong>Methadone tends to be more reliable at very high tolerance.</strong> As a "
            "full agonist it has no ceiling, so the dose can keep rising until it holds you. For "
            "someone using large daily quantities of fentanyl, this matters.</p>",
            "<p><strong>Methadone has no induction window.</strong> You do not need to be in "
            "withdrawal to start. If you are in crisis at four in the afternoon, this is a "
            "genuine practical advantage.</p>",
            "<p><strong>Suboxone has a much wider safety margin.</strong> The ceiling effect on "
            "breathing means overdose on buprenorphine alone is rare, which is why take home "
            "doses can be given far sooner. This is the difference between organising your week "
            "around a pharmacy and collecting once a week.</p>",
            "<p><strong>Suboxone blocks other opioids.</strong> Once established, using on top "
            "produces little effect. Many people describe this as what finally stopped the "
            "cycle of testing whether it would work.</p>",

            "<h2 id=\"fentanyl\">The fentanyl problem, honestly</h2>",
            "<p>The claim that Suboxone does not work for fentanyl is too strong, but it points "
            "at something real. Fentanyl accumulates in body fat and clears unpredictably, which "
            "makes the timing of a first Suboxone dose much harder than it was in the heroin era. "
            "Get it wrong and you get precipitated withdrawal, which is severe enough that people "
            "who experience it often refuse to try again.</p>",
            "<p>This is a solvable problem rather than a reason to rule Suboxone out. Low dose "
            "initiation, in which very small amounts of buprenorphine are introduced while you "
            "continue using your usual opioid and then built up over several days, has become "
            "common practice in British Columbia precisely because of fentanyl. It largely removes "
            "the risk and it removes the waiting.</p>",
            "<p>It does require planning, and it requires you to tell us honestly what you have "
            "been using and when. This is the single most useful piece of information you can "
            "bring to a first appointment.</p>",

            "<h2 id=\"practical\">The practical differences that decide it</h2>",
            "<p>In our experience the clinical factors narrow the field, and then ordinary life "
            "makes the choice. Worth thinking about before your appointment:</p>",
            "<ul>"
            "<li><strong>How soon do you need take home doses?</strong> If daily pharmacy visits "
            "would cost you a job, that weighs heavily toward Suboxone.</li>"
            "<li><strong>Can you tolerate a waiting period to start?</strong> If not, methadone "
            "starts today, or a low dose Suboxone initiation avoids the wait over several days.</li>"
            "<li><strong>What other medications are you on?</strong> Methadone interacts with a "
            "long list. Buprenorphine has fewer interactions.</li>"
            "<li><strong>What have you already tried?</strong> If Suboxone genuinely did not "
            "hold you at a full dose, that is meaningful information.</li>"
            "<li><strong>Would a monthly injection change things?</strong> Sublocade removes "
            "daily dosing entirely and is only available on the buprenorphine side.</li>"
            "</ul>",

            "<h2 id=\"switching\">Switching between them is normal</h2>",
            "<p>The decision you make at a first appointment is not permanent, and treating it as "
            "permanent leads people to stay on something that is not working.</p>",
            "<p>Moving from Suboxone to methadone is straightforward and can usually be done "
            "quickly. Moving from methadone to Suboxone takes more planning, because the methadone "
            "dose has to come down first and then clear sufficiently to avoid precipitated "
            "withdrawal, so it is planned over weeks.</p>",
            "<p>Either way, needing to switch is not a relapse and it is not a failure. It is a "
            "dose adjustment at a larger scale. If your current medication is not holding you, the "
            "worst option is to say nothing and drift out of treatment.</p>",
        ],
        "related_treatments": ["methadone", "suboxone"],
    },
    {
        "slug": "take-home-doses-carries-explained",
        "title": "Take home doses explained: how carries actually work in BC",
        "seo_title": "Take Home Doses (Carries) Explained",
        "lede": (
            "Carries are the point at which treatment stops running your week. Here is what "
            "decisions are based on, roughly how long it takes, and what causes them to be "
            "paused."
        ),
        "date": "2026-05-30",
        "updated": "2026-05-30",
        "category": "Living with treatment",
        "category_class": "sage",
        "read_time": "5 minute read",
        "author": "clinical",
        "meta_desc": (
            "How take home doses, known as carries, are decided in BC opioid agonist "
            "treatment. Criteria, timelines, safe storage, and why they get paused."
        ),
        "toc": [
            ("What carries are", "what-they-are"),
            ("What the decision is based on", "criteria"),
            ("How long it usually takes", "timeline"),
            ("Storing medication safely", "storage"),
            ("Why carries get paused", "paused"),
        ],
        "body": [
            "<h2 id=\"what-they-are\">What carries are</h2>",
            "<p>A carry is a dose you take home rather than take in front of a pharmacist. For "
            "most people they are the moment treatment stops being the organising fact of the "
            "week. Daily witnessed dosing means a pharmacy visit every single day, including "
            "the days you are ill, the days you are working and the days you are travelling. "
            "Carries end that.</p>",
            "<p>Because they matter so much, they generate more anxiety and more misinformation "
            "than any other part of treatment. The most common belief we encounter is that "
            "carries are a reward for good behaviour that clinics hand out grudgingly. That is "
            "not how the decision is framed.</p>",

            "<h2 id=\"criteria\">What the decision is actually based on</h2>",
            "<p>The question is whether a supply of medication at home is safe, for you and for "
            "the people around you. Provincial guidance sets out what to weigh, and clinicians "
            "apply it to your situation:</p>",
            "<ul>"
            "<li><strong>A settled dose.</strong> If your dose is still being adjusted, it is "
            "too early. This alone accounts for most of the wait.</li>"
            "<li><strong>Drug screens consistent with your plan.</strong> Not necessarily clean "
            "screens. Consistency with what you and your prescriber have agreed.</li>"
            "<li><strong>Reliable attendance.</strong> Regularly missed doses signal a risk of "
            "medication accumulating unused, which is a safety problem.</li>"
            "<li><strong>Somewhere safe to store it.</strong> A locked container and a stable "
            "place to keep it. This is often the practical sticking point.</li>"
            "<li><strong>Who else is in the home.</strong> Children, or another person with "
            "untreated substance use, changes the calculation. It rarely rules carries out, but "
            "it raises the bar on storage.</li>"
            "</ul>",
            "<p>Note that none of these is about deserving. Every one is about what happens to a "
            "bottle of methadone sitting in a kitchen.</p>",

            "<h2 id=\"timeline\">How long it usually takes</h2>",
            "<p>It depends heavily on the medication. With <strong>Suboxone</strong>, carries "
            "often begin within the first week or two, because the ceiling effect makes the risk "
            "profile very different. With <strong>methadone</strong>, expect longer. A common "
            "pattern is a first single carry once your dose has been stable for a period, then "
            "gradual expansion to two days, then a weekend, and onward.</p>",
            "<p>Nobody can give you a precise date at your first appointment, and you should be "
            "cautious of anyone who does. What we can tell you is what specifically is standing "
            "between you and the next step, and that is a fair question to ask at every "
            "appointment.</p>",

            "<h2 id=\"storage\">Storing medication safely</h2>",
            "<p>This is the part patients underestimate and it is the part that most often "
            "delays approval.</p>",
            "<p>A single carry of methadone is enough to kill a child or an adult with no "
            "opioid tolerance. It needs to be locked, out of sight and out of reach, and it "
            "needs to stay in the pharmacy bottle with the label intact. A small lockbox costs "
            "very little and resolves the issue entirely. Ask us and we can often help you get "
            "one.</p>",
            "<p>Never store it in a fridge door, a bedside drawer or a bag left in a shared "
            "space. Never move it into a different container. If a carry is lost or stolen, tell "
            "us immediately rather than waiting for the next appointment, because replacing a "
            "dose safely requires a conversation and quietly going without is dangerous.</p>",

            "<h2 id=\"paused\">Why carries get paused</h2>",
            "<p>Carries are reviewed continuously, not granted permanently, and they can be "
            "scaled back. This is not intended as punishment, though we recognise it can feel "
            "that way. Common reasons include a period of instability, drug screens that suggest "
            "the current plan is not holding, a change in living situation, several missed "
            "appointments, or a lost or diverted dose.</p>",
            "<p>If your carries are reduced, ask two questions: what specifically prompted it, "
            "and what needs to happen to restore them. Both should have clear answers. A "
            "reduction is usually temporary, and it is far better to work through it than to "
            "disappear from treatment over it.</p>",
        ],
        "related_treatments": ["methadone", "suboxone"],
    },
    {
        "slug": "helping-someone-not-ready-for-treatment",
        "title": "How to help someone who is not ready for treatment yet",
        "seo_title": "Helping Someone Not Ready for Treatment",
        "lede": (
            "The hardest position is caring about someone who has not decided to change. What "
            "the evidence says about what helps, what makes things worse, and how to stay in "
            "contact without losing yourself."
        ),
        "date": "2026-05-08",
        "updated": "2026-05-08",
        "category": "For families",
        "category_class": "",
        "read_time": "6 minute read",
        "author": "clinical",
        "meta_desc": (
            "Guidance for families supporting someone with opioid use disorder who is not "
            "ready for treatment, including what the evidence says about ultimatums."
        ),
        "toc": [
            ("Start with the survival facts", "survival"),
            ("What the evidence says about pressure", "pressure"),
            ("Staying in contact", "contact"),
            ("Being ready for the window", "window"),
            ("Looking after yourself", "yourself"),
        ],
        "body": [
            "<p>A significant share of the calls our clinic receives are not from people seeking "
            "treatment. They are from a parent, a partner, an adult child or a friend, asking "
            "some version of the same question: what do I do when they will not go?</p>",
            "<p>There is no method that reliably makes another adult accept treatment. What "
            "there is, is a set of things that keep someone alive and connected until they "
            "decide, and a set of things that reliably make matters worse.</p>",

            "<h2 id=\"survival\">Start with the survival facts</h2>",
            "<p>Before anything about motivation, three practical things reduce the chance of "
            "the worst outcome, and none of them require the person to want treatment.</p>",
            "<ul>"
            "<li><strong>Get naloxone and learn to use it.</strong> Free take home kits are "
            "available across British Columbia at pharmacies and health units. Have one where "
            "the person actually is.</li>"
            "<li><strong>Ask them not to use alone.</strong> Most fatal overdoses happen alone "
            "behind a closed door. Overdose prevention sites and the Lifeguard app both exist "
            "for this. If they will not use either, ask them to leave the door unlocked and to "
            "tell someone.</li>"
            "<li><strong>Know that calling for help is protected.</strong> The Good Samaritan "
            "Drug Overdose Act protects people at the scene of an overdose from charges for "
            "simple possession. Fear of police stops people calling, and that fear is worth "
            "addressing directly.</li>"
            "</ul>",

            "<h2 id=\"pressure\">What the evidence says about pressure</h2>",
            "<p>The confrontational intervention familiar from television performs poorly in "
            "research. It has low uptake and a real risk of rupturing the relationship, which "
            "removes the very connection that later makes treatment possible.</p>",
            "<p>Ultimatums are a mixed picture. A boundary you will genuinely keep can be "
            "useful and is sometimes necessary for your own sake. A boundary announced in anger "
            "and abandoned a week later teaches that your words do not mean much. If you are "
            "going to draw a line, draw one you can hold.</p>",
            "<p>What performs better is unglamorous. Approaches built on listening rather than "
            "arguing, on asking what they want rather than telling them what they need, and on "
            "keeping the door open, consistently outperform confrontation. The aim is not to win "
            "the argument today. It is to be the person they call when something shifts.</p>",

            "<h2 id=\"contact\">Staying in contact without endorsing the situation</h2>",
            "<p>People worry that staying connected amounts to approval. In practice, isolation "
            "is what makes drug use more dangerous, not less. You can decline to give money, "
            "decline to lie for someone, and still answer the phone.</p>",
            "<p>A few things that tend to help:</p>",
            "<ul>"
            "<li>Separate the person from the use in how you talk. Words like addict and clean "
            "carry judgement that closes conversations.</li>"
            "<li>Ask questions rather than issuing statements. What would have to change for "
            "you to consider it opens more than you should get help.</li>"
            "<li>Offer specific, small help. A lift to an appointment is easier to accept than "
            "an offer to fix everything.</li>"
            "<li>Do not make your affection conditional on progress. That is the single thing "
            "most likely to end contact.</li>"
            "</ul>",

            "<h2 id=\"window\">Being ready for the window</h2>",
            "<p>Willingness is rarely a permanent state that arrives and stays. It tends to come "
            "in windows, sometimes only hours long, often after something frightening. The "
            "difference between a window that leads to treatment and one that closes is usually "
            "how much friction is in the way.</p>",
            "<p>So do the preparation in advance. Know which clinic they could attend and its "
            "hours. Know that no referral is required in British Columbia. Know that a same day "
            "assessment is possible. Have the number saved. When someone says maybe, the answer "
            "you want to have ready is that they are open now and I will drive you, not that you "
            "will look into it.</p>",
            "<p>You can also call a clinic yourself, before that moment, and ask what would "
            "happen if they walked in. We take those calls regularly and we are happy to take "
            "yours. We cannot discuss another adult medical information with you, but we can "
            "tell you exactly how the process works.</p>",

            "<h2 id=\"yourself\">Looking after yourself is not optional</h2>",
            "<p>People in this position frequently arrive exhausted, financially strained and "
            "carrying a guilt that does not belong to them. It is worth saying plainly that you "
            "did not cause this and you cannot control it.</p>",
            "<p>Support for families exists across British Columbia, and using it makes you "
            "better at this rather than worse. Al Anon, Nar Anon and family support programmes "
            "through regional health authorities all provide it. If the strain is affecting your "
            "own health, that is a reason to see your own doctor, not a sign of weakness.</p>",
            "<p>The most useful thing you can be, over a long period, is still there and still "
            "standing. That is easier to sustain if you are not doing it alone.</p>",
        ],
        "related_treatments": ["methadone", "suboxone", "substance-use-treatment"],
    },
]
