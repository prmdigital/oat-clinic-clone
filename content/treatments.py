# -*- coding: utf-8 -*-
"""Treatment programme pages.

Each entry becomes /treatments/<slug>/. Clinical copy here is written for a
general audience and is deliberately non prescriptive: it explains how care
usually works rather than telling anyone what to take. Every page carries the
"not medical advice" disclaimer from the base template.

Sections are (anchor_id, heading, [html_block, ...]).
FAQs are (question, [answer_html_block, ...]) and are emitted as FAQPage JSON-LD.
"""

# NOTE ON THE STATISTICS BELOW
# Every `stats` entry carries its source, and nothing here is invented. The
# mortality figure is the Sordo et al. BMJ 2017 meta-analysis of opioid agonist
# treatment, which is the standard citation for it. Entries sourced to "OAT
# Clinic practice" or "OAT Clinic policy" are claims about how this clinic
# works, and must be confirmed by the clinic. Every figure on these pages
# should be signed off by a prescribing physician before launch.

TREATMENTS = [
    # ----------------------------------------------------------------- #
    {
        "slug": "methadone",
        "name": "Methadone treatment",
        "nav_name": "Methadone",
        "nav_desc": "Long acting daily liquid, the most established option",
        "tag": "Opioid agonist",
        "h1": "Methadone treatment",
        "lede": (
            "Methadone is the longest established opioid agonist treatment in Canada. "
            "Taken once a day as a liquid, it holds withdrawal and craving steady for a "
            "full twenty four hours so that the rest of your life has room to restart."
        ),
        "meta_desc": (
            "Methadone treatment across five BC clinics. How dosing works, what the first "
            "week is like, take home doses, and PharmaCare coverage."
        ),
    "stats": [
        ('~50%', 'Lower risk of death while in treatment',
         'Sordo et al., BMJ 2017'),
        ('60+ yrs', 'In clinical use, the most studied option',
         'WHO Essential Medicines List'),
        ('$0', 'To see our physicians with MSP coverage',
         'BC Medical Services Plan'),
    ],
        "summary": (
        'A daily liquid that holds withdrawal and craving steady for a full twenty four hours.'
    ),
    "cards": [
        ('pharmacy', 'What it is',
         'A long acting opioid agonist, taken by mouth as a measured liquid. It occupies the same receptors as fentanyl, but releases slowly, so there is no rush and no crash.'),
        ('clock', 'How you take it',
         'Once a day, at a pharmacy while a pharmacist watches. Take home doses begin once your dose is settled, usually starting with one day a week.'),
        ('route', 'What to expect',
         'Your dose starts low and rises slowly. Reaching a dose that holds you for a full day commonly takes two to four weeks. The first week is the hardest part.'),
    ],
    "facts": [
        ('Form', 'Liquid, taken by mouth'),
        ('Dosing', 'Once daily'),
        ('Starting', 'No withdrawal needed first'),
        ('Take home doses', 'After your dose is stable'),
        ('Cost in BC', 'Covered by PharmaCare'),
    ],
    "pullquote": (
        'Every death in early methadone treatment comes from starting too high or going up too fast. So we start low, and we tell you in advance that it will feel low.'
    ),
    "sections": [
            ("how-it-works", "How methadone works", [
                "<p>Methadone is a full opioid agonist. It occupies the same receptors that "
                "fentanyl, heroin or prescription opioids act on, which is why it stops "
                "withdrawal. The difference is speed. Methadone is absorbed slowly and "
                "leaves the body slowly, so instead of the sharp rise and fall that drives "
                "the cycle of using, the level in your blood stays flat.</p>",
                "<p>That flatness is the entire point. At a dose that suits you, there is no "
                "rush and no crash. Cravings quieten. Withdrawal does not arrive in the "
                "afternoon. Most people describe it not as feeling medicated but as finally "
                "feeling normal, sometimes for the first time in years.</p>",
                "<p>Because methadone is long acting, it also gives a measure of protection "
                "against overdose. Tolerance is held at a steady level rather than dropping "
                "between uses, which is when the risk of a fatal overdose is highest.</p>",
            ]),
            ("first-week", "What the first two weeks look like", [
                "<p>Methadone is started low and raised slowly. This is not caution for its "
                "own sake. Methadone accumulates in the body over the first several days, so "
                "the dose you take on day one is still building on day four. Raising too "
                "quickly is the single greatest risk in early treatment, and every "
                "responsible programme in Canada works the same way.</p>",
                "<p>A typical pattern looks like this:</p>",
                "<ul>"
                "<li><strong>Day one.</strong> Assessment, a urine drug screen, and a first "
                "dose taken under observation at your pharmacy. You will be asked to stay "
                "reachable that day.</li>"
                "<li><strong>Days two to five.</strong> Daily witnessed dosing. Expect to "
                "still feel some withdrawal. This is normal and is not a sign the medication "
                "is failing.</li>"
                "<li><strong>Week one review.</strong> We check how long each dose is holding "
                "you and adjust upward, usually in small increments.</li>"
                "<li><strong>Weeks two and three.</strong> Further adjustments until a dose "
                "holds you comfortably for a full twenty four hours.</li>"
                "</ul>",
                "<p>Reaching a comfortable dose commonly takes two to four weeks. The waiting "
                "is the hardest part of methadone, and it is worth knowing about in advance "
                "so that a difficult third day does not read as failure.</p>",
            ]),
            ("dosing", "Dosing, carries and daily life", [
                "<p>At the start, methadone is taken at a pharmacy while a pharmacist "
                "watches. This is called witnessed dosing. It sounds intrusive, and for the "
                "first weeks it genuinely is inconvenient, but it exists because the early "
                "period is when the risk is real.</p>",
                "<p>Take home doses, known as carries, are the standard next step. Eligibility "
                "in British Columbia depends on clinical stability rather than on time served: "
                "a settled dose, drug screens consistent with your treatment plan, somewhere "
                "safe to store the medication, and reliable attendance. Carries usually begin "
                "with one day a week and expand from there.</p>",
                "<p>Once you hold carries, methadone stops organising your week. People work "
                "full time on methadone, travel, study and raise children on it. Getting to "
                "that point is the aim of the first few months.</p>",
            ]),
            ("safety", "Safety and interactions", [
                "<p>Two things matter more than anything else. The first is that methadone "
                "and benzodiazepines, alcohol, or other sedatives together are the main cause "
                "of overdose in people on treatment. If you use any of these, tell us. We can "
                "work with it. We cannot work around what we do not know.</p>",
                "<p>The second is that methadone interacts with a long list of ordinary "
                "medications, including some antibiotics, antifungals, HIV medications and "
                "antidepressants. Some raise your methadone level, some lower it. Always tell "
                "any prescriber that you are on methadone, and tell us about anything new you "
                "have been prescribed.</p>",
                "<p>We recommend every patient keep a take home naloxone kit, and we can tell "
                "you where to get one at no cost. Having one is not an admission that "
                "treatment is going badly. It is the same logic as a smoke alarm.</p>",
            ]),
        ],
        "balance": {
            "good_title": "Where methadone is strongest",
            "good": [
                "Works reliably at high opioid tolerance, including long term fentanyl use",
                "No induction window, so you do not need to be in withdrawal to start",
                "The most studied opioid agonist treatment, with sixty years of evidence",
                "Often effective for people for whom Suboxone did not hold",
                "Liquid dosing allows very fine adjustment",
            ],
            "note_title": "What to weigh up",
            "note": [
                "Daily pharmacy visits at first, which takes real organising",
                "Reaching a comfortable dose usually takes two to four weeks",
                "Interacts with many common medications, so tell every prescriber",
                "Stopping abruptly causes prolonged withdrawal, so any taper is planned slowly",
                "Dangerous in combination with benzodiazepines or alcohol",
            ],
        },
        "faqs": [
            ("How quickly will methadone stop my withdrawal?",
             ["<p>The first dose usually takes the edge off within two to four hours, but it "
              "will not hold you for a full day. That is expected. Because methadone builds "
              "up gradually, most people need two to four weeks of small increases before a "
              "dose covers twenty four hours comfortably.</p>",
              "<p>The most common reason people leave methadone treatment is quitting during "
              "this window, believing it is not working. If day three is hard, tell us rather "
              "than deciding on your own. We can adjust supportive medication for symptoms "
              "while the main dose catches up.</p>"]),
            ("Will methadone make me feel high or sedated?",
             ["<p>At the right dose, no. What people describe is the absence of something: no "
              "withdrawal, no clock watching, no craving in the background. That flatness can "
              "feel strange at first if the rhythm of using has structured your day for years.</p>",
              "<p>Feeling drowsy, nodding off, or slurring speech means the dose is too high "
              "or something is interacting with it. That is a reason to contact us the same "
              "day, not to wait for your next appointment.</p>"]),
            ("Do I have to go to the pharmacy every single day?",
             ["<p>At the beginning, yes. Witnessed daily dosing is standard while your dose is "
              "being established, because that is the period when the risk of overdose is "
              "highest.</p>",
              "<p>Take home doses are the goal, not a reward we withhold. Once your dose is "
              "stable, your drug screens match your treatment plan, and you have somewhere "
              "safe to store medication, carries usually start with a single day and build "
              "from there. Many long term patients collect once or twice a week.</p>"]),
            ("Can I drive while taking methadone?",
             ["<p>Once you are on a stable dose and not sedated, yes. Being on methadone does "
              "not by itself prevent you from holding a driver licence in British Columbia.</p>",
              "<p>During the first weeks, while your dose is still being adjusted, be careful. "
              "Do not drive if you feel drowsy, and never drive after combining methadone with "
              "alcohol, benzodiazepines or other sedating drugs. Commercial licence holders "
              "should raise it with us directly, because different rules apply.</p>"]),
            ("What happens if I miss doses?",
             ["<p>Tell us and tell your pharmacy. Tolerance to methadone falls faster than most "
              "people expect. After three consecutive missed days, your previous dose may no "
              "longer be safe, and we will need to restart at a lower amount and build back up.</p>",
              "<p>This is a safety measure rather than a penalty. Taking a full previous dose "
              "after a gap is a genuine cause of fatal overdose. Missing doses does not put "
              "you out of the programme, and it is not something to hide from us.</p>"]),
            ("Does methadone damage your teeth or your bones?",
             ["<p>Methadone does not dissolve teeth. What it does is reduce saliva, and a dry "
              "mouth over years allows decay that would otherwise not happen. The liquid is "
              "also sweetened. Rinsing with water after each dose, not brushing immediately "
              "afterwards, and regular dental care make a large difference.</p>",
              "<p>Long term opioid use of any kind can lower sex hormone levels, which over "
              "many years can affect bone density. It is worth mentioning to us if you have "
              "other risk factors, because it is measurable and treatable.</p>"]),
            ("How long will I need to stay on methadone?",
             ["<p>There is no fixed course. Opioid use disorder behaves like other long term "
              "conditions, and the evidence is consistent: the longer someone stays in "
              "treatment, the better the outcome. Many people remain on methadone for years, "
              "and some stay on it indefinitely, in the same way someone might stay on blood "
              "pressure medication.</p>",
              "<p>If you decide you want to come off, that is your call, and we will support "
              "it. A planned taper is gradual, often over many months, and can be paused or "
              "reversed at any point. Nobody is discharged for changing their mind.</p>"]),
            ("What does methadone treatment cost in British Columbia?",
             ["<p>Appointments with our physicians are billed to the Medical Services Plan, so "
              "there is no fee for the visit if you have active MSP coverage. The medication "
              "itself is covered by BC PharmaCare for most residents, and people receiving "
              "income assistance or disability assistance are generally covered in full "
              "including dispensing fees.</p>",
              "<p>Exact coverage depends on which PharmaCare plan you fall under and whether "
              "your deductible is met. Our team checks this with you at your first visit. If "
              "you have no coverage at all, say so early, because it can usually be arranged.</p>"]),
        ],
        "related": ["suboxone", "substance-use-treatment", "benzodiazepine-support"],
    },
    # ----------------------------------------------------------------- #
    {
        "slug": "suboxone",
        "name": "Suboxone treatment",
        "nav_name": "Suboxone",
        "nav_desc": "Buprenorphine and naloxone, with earlier take home doses",
        "tag": "Opioid agonist",
        "h1": "Suboxone treatment",
        "lede": (
            "Suboxone combines buprenorphine with naloxone in a tablet or film that dissolves "
            "under the tongue. It has a wider safety margin than methadone and take home doses "
            "usually start much sooner, which is why it is often the first option offered."
        ),
        "meta_desc": (
            "Suboxone treatment in BC. How buprenorphine works, avoiding precipitated "
            "withdrawal when starting from fentanyl, take home doses and Sublocade."
        ),
    "stats": [
        ('~50%', 'Lower risk of death while in treatment',
         'Sordo et al., BMJ 2017'),
        ('1 to 2 wks', 'Typical wait for take home doses',
         'OAT Clinic practice'),
        ('1 / month', 'Injections on Sublocade, instead of daily dosing',
         'BC PharmaCare special authority'),
    ],
        "summary": (
        'A daily tablet that stops withdrawal, blocks other opioids, and allows take home doses sooner.'
    ),
    "cards": [
        ('pharmacy', 'What it is',
         'Buprenorphine with naloxone, dissolved under the tongue. It binds tightly but only partly activates, which gives it a ceiling effect on breathing.'),
        ('clock', 'How you take it',
         'Once daily under the tongue, never swallowed. Or once a month as a Sublocade injection, which removes daily dosing entirely.'),
        ('route', 'What to expect',
         'You need to be in mild withdrawal before the first dose, or use a low dose start. Getting that timing right is the one thing worth planning carefully.'),
    ],
    "facts": [
        ('Form', 'Tablet or film, under the tongue'),
        ('Dosing', 'Once daily, or monthly injection'),
        ('Starting', 'Mild withdrawal required first'),
        ('Take home doses', 'Often within one to two weeks'),
        ('Cost in BC', 'Covered by PharmaCare'),
    ],
    "pullquote": (
        'If you stop Suboxone, the blockade lifts while your tolerance is now much lower. This is the most dangerous moment in the whole course of treatment.'
    ),
    "sections": [
            ("how-it-works", "How Suboxone works", [
                "<p>Buprenorphine, the active ingredient, is a partial opioid agonist. It binds "
                "to opioid receptors very tightly but activates them only partly. Two "
                "consequences follow, and both are clinically useful.</p>",
                "<p>The first is a ceiling effect. Past a certain dose, buprenorphine stops "
                "suppressing breathing further. This is why overdose on buprenorphine alone is "
                "rare, and it is the main reason take home doses can be given earlier than with "
                "methadone.</p>",
                "<p>The second is that its tight binding displaces other opioids from the "
                "receptor and blocks them from attaching. Using fentanyl on top of an "
                "established Suboxone dose generally produces little effect. Many patients "
                "describe this as the thing that finally broke the habit of trying.</p>",
                "<p>The naloxone in the combination is there to deter injection. Taken as "
                "directed under the tongue, almost none of it is absorbed and it does nothing "
                "at all.</p>",
            ]),
            ("starting", "Starting Suboxone, and why timing matters", [
                "<p>Suboxone has one genuine complication, and being warned about it in advance "
                "makes all the difference. Because buprenorphine pushes other opioids off the "
                "receptor, taking a first dose while other opioids are still active can trigger "
                "sudden, severe withdrawal. This is called precipitated withdrawal.</p>",
                "<p>The way to avoid it is to already be in mild to moderate withdrawal before "
                "the first dose. We assess this with you using a standard symptom scale rather "
                "than guesswork, and we will tell you what to look for.</p>",
                "<p>Fentanyl makes this harder than it used to be. Fentanyl stores in body fat "
                "and clears unpredictably, so the older waiting rules are unreliable. Two "
                "approaches are now common in British Columbia:</p>",
                "<ul>"
                "<li><strong>Low dose initiation.</strong> Very small amounts of buprenorphine "
                "are introduced while you continue your usual opioid, then increased over "
                "several days. Precipitated withdrawal is largely avoided and you do not have "
                "to sit in withdrawal first.</li>"
                "<li><strong>Standard initiation.</strong> You wait until clear withdrawal has "
                "set in, then take a first dose under guidance. Faster, but it requires an "
                "uncomfortable wait.</li>"
                "</ul>",
                "<p>Which route suits you depends on what you have been using and how much "
                "structure your week allows. This is a conversation, not a rule we apply.</p>",
            ]),
            ("sublocade", "Sublocade, the monthly injection", [
                "<p>Sublocade is an extended release buprenorphine injection given once a month "
                "into the abdomen. It releases medication steadily for four weeks, which removes "
                "daily dosing, pharmacy visits and the question of storing medication at home "
                "entirely.</p>",
                "<p>It suits people who are stable on daily Suboxone and want their treatment to "
                "stop being a daily event, people whose work or travel makes daily dosing "
                "impractical, and people for whom keeping opioid medication at home is a risk. "
                "You normally need to be tolerating daily buprenorphine for about a week before "
                "the first injection.</p>",
                "<p>Ask us about it if daily dosing is the part of treatment you find hardest. "
                "It is covered under BC PharmaCare special authority for eligible patients.</p>",
            ]),
            ("daily-life", "Take home doses and daily life", [
                "<p>Because the safety margin is wider, carries with Suboxone often begin within "
                "the first week or two rather than after months. Many patients settle quickly "
                "into collecting a week or more at a time.</p>",
                "<p>The tablet or film must dissolve fully under the tongue, which takes several "
                "minutes. Swallowing it wastes the dose, since buprenorphine is poorly absorbed "
                "from the stomach. Avoid eating or drinking for about fifteen minutes "
                "beforehand, and do not talk while it dissolves.</p>",
                "<p>Most people take Suboxone in the morning. If it makes you drowsy, evening "
                "dosing works equally well. Because it is long acting, the exact hour matters "
                "less than it does with shorter acting medication.</p>",
            ]),
        ],
        "balance": {
            "good_title": "Where Suboxone is strongest",
            "good": [
                "Ceiling effect on breathing makes overdose on Suboxone alone far less likely",
                "Take home doses usually start within the first week or two",
                "Blocks the effect of other opioids, which removes the incentive to test it",
                "Fewer interactions with other medications than methadone",
                "Available as a monthly injection for people who want to stop daily dosing",
            ],
            "note_title": "What to weigh up",
            "note": [
                "Starting requires being in withdrawal first, unless a low dose start is used",
                "Precipitated withdrawal is a real risk if the timing is wrong",
                "Some people with very high fentanyl tolerance are not adequately held by it",
                "The tablet takes several minutes to dissolve and cannot be swallowed",
                "Starting from fentanyl needs more planning than it once did",
            ],
        },
        "faqs": [
            ("What is precipitated withdrawal, and how likely is it?",
             ["<p>It is sudden, intense withdrawal that can begin within an hour of a first "
              "Suboxone dose, caused by buprenorphine displacing other opioids from the "
              "receptor faster than your body can adjust. It is deeply unpleasant, though not "
              "dangerous in itself, and it usually settles within a day.</p>",
              "<p>It is also largely preventable. It happens when a first dose is taken too "
              "soon. With a properly timed start, or with a low dose initiation, the risk is "
              "low. This is the single most important reason not to start Suboxone from "
              "someone else supply without guidance.</p>"]),
            ("How long do I have to wait after using fentanyl before my first dose?",
             ["<p>There is no reliable fixed number any more, and anyone who gives you one is "
              "oversimplifying. Fentanyl accumulates in body fat and clears at very different "
              "rates depending on how long and how heavily it has been used. Waits that worked "
              "for heroin are frequently too short for fentanyl.</p>",
              "<p>This is exactly why low dose initiation has become common in British Columbia. "
              "It lets you begin buprenorphine while still using your usual opioid, building up "
              "over several days, so the waiting problem largely disappears. Talk to us before "
              "you start rather than after a bad experience.</p>"]),
            ("Should I choose Suboxone or methadone?",
             ["<p>Both are first line treatments and both work. Broadly, Suboxone is often "
              "offered first because of its safety profile and earlier take home doses. "
              "Methadone tends to be more reliable at very high opioid tolerance, and it has no "
              "induction window, so it can be started without waiting for withdrawal.</p>",
              "<p>The honest answer is that the better medication is whichever one keeps you in "
              "treatment. Switching between them is normal and is not a setback. What matters "
              "at the assessment is your history, your tolerance, your schedule and what you "
              "have already tried.</p>"]),
            ("Can I switch from methadone to Suboxone, or the other way?",
             ["<p>Yes, both directions are done regularly. Moving from methadone to Suboxone "
              "needs care, because methadone must be reduced to a lower dose first and then "
              "cleared enough to avoid precipitated withdrawal. It is planned over weeks, not "
              "days.</p>",
              "<p>Moving from Suboxone to methadone is simpler and can usually be done quickly. "
              "If your current medication is not holding you, raise it with us. Switching is a "
              "normal clinical adjustment.</p>"]),
            ("Will Suboxone block pain medication if I am injured or need surgery?",
             ["<p>It complicates it, but pain can still be treated. Buprenorphine occupies "
              "receptors tightly, so standard doses of other opioids may have reduced effect. "
              "Non opioid pain control is often more effective than expected, and for severe "
              "pain there are established approaches your treating team can use.</p>",
              "<p>Tell any hospital or surgical team that you are on Suboxone, and contact us "
              "as early as you can before planned surgery so we can coordinate. Do not stop "
              "your Suboxone on your own before a procedure.</p>"]),
            ("Can I still feel the effect of other opioids while on Suboxone?",
             ["<p>Generally very little, once you are on a full dose. That blocking effect is "
              "part of how Suboxone helps, because it removes the point of using on top.</p>",
              "<p>There is an important safety consequence. If you stop Suboxone, the blockade "
              "lifts while your tolerance is now much lower than it was, and returning to a "
              "previous amount can be fatal. This is the most dangerous moment in the whole "
              "course of treatment. If you are thinking about stopping, talk to us first.</p>"]),
            ("How soon can I get take home doses?",
             ["<p>Often within the first week or two, which is considerably sooner than with "
              "methadone. Because buprenorphine has a ceiling effect, the risk that makes early "
              "carries unwise with methadone is much smaller here.</p>",
              "<p>We still need to see that your dose is settled, that you have somewhere safe "
              "to store the medication, and that you are attending as arranged. Carries are "
              "reviewed continuously rather than granted once and forgotten.</p>"]),
            ("Is Suboxone covered by PharmaCare in British Columbia?",
             ["<p>Yes. Suboxone is covered for eligible British Columbia residents, and people "
              "on income assistance or disability assistance are generally covered in full "
              "including dispensing fees. Appointments with our physicians are billed to MSP.</p>",
              "<p>Sublocade, the monthly injection, requires special authority approval, which "
              "we submit on your behalf. Bring your BC Services Card if you have one, and tell "
              "us early if you have no coverage so we can sort it out before it becomes a "
              "barrier.</p>"]),
        ],
        "related": ["methadone", "substance-use-treatment", "benzodiazepine-support"],
    },
    # ----------------------------------------------------------------- #
    {
        "slug": "substance-use-treatment",
        "name": "Substance use treatment",
        "nav_name": "Substance use care",
        "nav_desc": "Stimulants, alcohol and support beyond opioid medication",
        "tag": None,
        "h1": "Substance use treatment",
        "lede": (
            "Opioids are rarely the whole picture. Stimulants, alcohol and other substances "
            "often sit alongside them, and treating only one leaves the rest to undo the work. "
            "This is the part of our practice that deals with everything else."
        ),
        "meta_desc": (
            "Substance use treatment in BC covering stimulants, alcohol and mental health "
            "support alongside opioid agonist treatment."
        ),
    "stats": [
        ('$0', 'To see our physicians with MSP coverage',
         'BC Medical Services Plan'),
        ('Same day', 'Assessment covering every substance you use',
         'OAT Clinic practice'),
        ('0', 'Patients discharged for continued substance use',
         'OAT Clinic policy'),
    ],
        "summary": (
        'Care for the stimulants, alcohol and other substances that sit alongside opioid use.'
    ),
    "cards": [
        ('users', 'Who it is for',
         'Anyone whose use goes beyond opioids. Stimulants, alcohol and benzodiazepines are common alongside opioid use, and treating one while ignoring the rest rarely holds.'),
        ('shield', 'What we can treat',
         'Medication for alcohol use disorder, structured support for stimulant use, and concurrent mental health assessment and prescribing.'),
        ('route', 'What we refer for',
         'Counselling, housing and income support, and hepatitis C or HIV care. We refer, then follow up on whether the referral actually went anywhere.'),
    ],
    "facts": [
        ('Covers', 'Stimulants, alcohol, concurrent care'),
        ('Medication', 'Available for alcohol use disorder'),
        ('Stimulants', 'Structured support, no proven drug yet'),
        ('Counselling', 'By referral, not in house'),
        ('Cost in BC', 'Appointments billed to MSP'),
    ],
    "pullquote": (
        'Alcohol withdrawal, unlike opioid withdrawal, can be fatal. If you drink heavily every day, do not stop abruptly on your own.'
    ),
    "sections": [
            ("stimulants", "Stimulant use", [
                "<p>Methamphetamine and cocaine use alongside opioid treatment is extremely "
                "common in British Columbia. There is currently no medication for stimulant use "
                "disorder with anything like the evidence base that methadone and Suboxone have "
                "for opioids, and it would be dishonest to suggest otherwise.</p>",
                "<p>What does help is structure. Contingency management, which links concrete "
                "rewards to verified periods of non use, has the strongest evidence of any "
                "approach to stimulant use. Regular contact, sleep repair and treating "
                "underlying mental health conditions all move the needle.</p>",
                "<p>Some medications show promise for specific patterns of use, and we will "
                "discuss the evidence honestly with you rather than promising more than it "
                "supports. What matters most is that stimulant use is not a reason to be turned "
                "away from opioid treatment. Being on OAT while still using stimulants is far "
                "safer than being on neither.</p>",
            ]),
            ("alcohol", "Alcohol use", [
                "<p>Alcohol is the substance most often left out of the conversation, and it is "
                "the one that most reliably makes opioid treatment dangerous. Alcohol and "
                "methadone both suppress breathing, and together they account for a large share "
                "of overdose deaths among people who are otherwise stable in treatment.</p>",
                "<p>There are effective medications for alcohol use disorder, and they are "
                "consistently underused. Naltrexone reduces the reward from drinking, though it "
                "cannot be combined with opioid agonist treatment. Acamprosate helps maintain "
                "abstinence and is compatible with OAT. Both are available in British Columbia.</p>",
                "<p>One warning matters more than the rest. Alcohol withdrawal, unlike opioid "
                "withdrawal, can be fatal. If you drink heavily every day, do not stop abruptly "
                "on your own. Tell us, and we will arrange a safe withdrawal plan.</p>",
            ]),
            ("mental-health", "Mental health alongside substance use", [
                "<p>Depression, anxiety, post traumatic stress and ADHD appear far more often in "
                "people with substance use disorders than in the general population. The old "
                "argument about which came first has largely been abandoned, because in practice "
                "treating them separately works badly and treating them together works.</p>",
                "<p>We assess mental health as part of your care rather than treating it as "
                "someone else problem, and we prescribe for common conditions where that is "
                "appropriate. Where you need more than we can provide, we refer, and we follow "
                "up on whether the referral actually went anywhere.</p>",
            ]),
            ("beyond", "Support beyond the prescription", [
                "<p>A prescription does not fix housing, income, a criminal matter or the loss "
                "of a relationship, and pretending otherwise wastes everyone time. What we can "
                "do is connect you to the services that handle those things and stay involved.</p>",
                "<ul>"
                "<li>Referral to counselling and structured treatment programmes</li>"
                "<li>Connection to housing and income assistance workers</li>"
                "<li>Testing and treatment referral for hepatitis C and HIV</li>"
                "<li>Take home naloxone and overdose prevention information</li>"
                "<li>Documentation for court, employers or income assistance where you ask for it</li>"
                "</ul>",
                "<p>You are not obliged to take any of it. Some people want only the medication, "
                "and that is a legitimate way to use this clinic.</p>",
            ]),
        ],
        "balance": {
            "good_title": "What this covers",
            "good": [
                "Assessment of all substance use, not opioids in isolation",
                "Medication for alcohol use disorder where appropriate",
                "Structured support and close follow up for stimulant use",
                "Concurrent mental health assessment and prescribing",
                "Referral to counselling, housing and community services",
            ],
            "note_title": "Being straight with you",
            "note": [
                "No medication yet matches OAT for stimulant use disorder",
                "Counselling is by referral, since we do not provide therapy in house",
                "Heavy daily drinking needs a planned withdrawal, never an abrupt stop",
                "We do not provide inpatient detox or residential treatment directly",
                "Progress here is usually gradual rather than dramatic",
            ],
        },
        "faqs": [
            ("Will I be refused opioid treatment if I am still using other drugs?",
             ["<p>No. This is the single most common fear people bring to a first appointment, "
              "and it keeps people away for years.</p>",
              "<p>Continued substance use is information about how well your treatment plan is "
              "working, not grounds for discharge. It may change practical details, such as how "
              "quickly take home doses are offered, because those decisions are about safety. It "
              "does not change whether you are welcome here.</p>"]),
            ("Is it safe to drink alcohol while on methadone or Suboxone?",
             ["<p>Alcohol with methadone is genuinely dangerous. Both suppress breathing, and "
              "the combination is a leading cause of overdose in people who are otherwise doing "
              "well in treatment. The risk with Suboxone is lower because of its ceiling effect, "
              "but it is not absent.</p>",
              "<p>If you drink, tell us how much, honestly. We would far rather adjust your care "
              "around real drinking than plan around a number you thought we wanted to hear.</p>"]),
            ("Can you help me stop drinking?",
             ["<p>Yes. Medication for alcohol use disorder is effective and underused. "
              "Acamprosate can be combined with opioid agonist treatment. Naltrexone works well "
              "for alcohol but cannot be used alongside methadone or Suboxone, so it is an "
              "option only in specific circumstances.</p>",
              "<p>If you drink heavily every day, the first step is a safe withdrawal plan "
              "rather than medication. Alcohol withdrawal can cause seizures and can be fatal, "
              "which is not true of opioid withdrawal. Do not stop suddenly on your own.</p>"]),
            ("Is there a medication for methamphetamine or cocaine use?",
             ["<p>Not one with the evidence behind it that methadone and Suboxone have for "
              "opioids. Some medications show modest benefit for particular patterns of use, and "
              "we will go through what the research actually shows if you want that "
              "conversation.</p>",
              "<p>The strongest evidence for stimulant use is behavioural. Contingency "
              "management, which provides tangible incentives for verified periods of non use, "
              "outperforms everything else currently available. Regular contact, sleep and "
              "treating underlying mental health conditions all help meaningfully.</p>"]),
            ("Do you provide counselling at the clinic?",
             ["<p>Not in house. We are a medical clinic, and our physicians provide assessment, "
              "prescribing and follow up rather than therapy.</p>",
              "<p>What we do is refer, and then check that the referral led somewhere. Many "
              "patients combine our medical care with counselling elsewhere, and the two work "
              "considerably better together than either does alone.</p>"]),
            ("What if my main problem is benzodiazepines rather than opioids?",
             ["<p>Then start with our <a href=\"/treatments/benzodiazepine-support/\">"
              "benzodiazepine support</a> page. Benzodiazepine dependence needs a different "
              "approach from opioid dependence, and stopping abruptly is genuinely dangerous.</p>",
              "<p>Many patients need both, since benzodiazepines are increasingly present in the "
              "unregulated drug supply. We treat them together rather than asking you to solve "
              "one before we address the other.</p>"]),
            ("Will what I tell you be shared with police, my employer or child services?",
             ["<p>Your medical record is confidential and protected under British Columbia "
              "health privacy law. We do not report drug use to police or to employers.</p>",
              "<p>There are narrow legal exceptions that apply to all health professionals in "
              "the province, principally an immediate risk to your life or someone else, or a "
              "duty to report a child at risk of harm. These are legal obligations rather than "
              "clinic policy, and we will tell you plainly if one applies.</p>"]),
        ],
        "related": ["methadone", "suboxone", "benzodiazepine-support"],
    },
    # ----------------------------------------------------------------- #
    {
        "slug": "benzodiazepine-support",
        "name": "Benzodiazepine support",
        "nav_name": "Benzodiazepines",
        "nav_desc": "Planned tapering, and the risks of stopping suddenly",
        "tag": "Taper based",
        "h1": "Benzodiazepine support",
        "lede": (
            "Benzodiazepines now appear throughout the unregulated opioid supply in British "
            "Columbia, which means many people are dependent on them without ever having chosen "
            "to be. Coming off requires a slow, planned taper, never an abrupt stop."
        ),
        "meta_desc": (
            "Benzodiazepine support in BC. Why stopping abruptly is dangerous, how a taper "
            "is planned, and managing dependence alongside opioid treatment."
        ),
    "stats": [
        ('5 to 10%', 'Typical dose reduction per step',
         'Standard tapering practice'),
        ('1 to 4 wks', 'Between reduction steps, paused whenever needed',
         'Standard tapering practice'),
        ('0', 'Doses you should ever stop abruptly',
         'Withdrawal can cause seizures'),
    ],
        "summary": (
        'A planned, gradual taper. Stopping benzodiazepines suddenly can cause seizures.'
    ),
    "cards": [
        ('alert', 'Why it matters',
         'Benzodiazepines now appear throughout the unregulated opioid supply, so many people are dependent without ever having chosen to be.'),
        ('route', 'How the taper works',
         'Usually a switch to a long acting benzodiazepine, then small reductions at intervals of weeks. The pace is set by how you feel, not by a schedule.'),
        ('shield', 'Alongside opioid treatment',
         'We treat both at the same time. Withholding opioid treatment until someone stops benzodiazepines pushes them back to a supply that contains both.'),
    ],
    "facts": [
        ('Approach', 'Structured, gradual taper'),
        ('Typical length', 'Months, sometimes over a year'),
        ('Never', 'Stop abruptly, withdrawal can cause seizures'),
        ('Alongside OAT', 'Yes, treated at the same time'),
        ('Naloxone', 'Does not reverse benzodiazepines'),
    ],
    "pullquote": (
        'Opioid withdrawal is miserable but rarely dangerous. Benzodiazepine withdrawal is the opposite. It can cause seizures, delirium and, in severe cases, death.'
    ),
    "sections": [
            ("in-the-supply", "Benzodiazepines in the unregulated supply", [
                "<p>Since around 2019, benzodiazepines such as etizolam and bromazolam have been "
                "found in a large share of the unregulated opioid supply in British Columbia. "
                "This has changed what overdose looks like on the street. Naloxone reverses the "
                "opioid but does nothing to the benzodiazepine, so people wake up and then go "
                "back under, and sedation outlasts the reversal.</p>",
                "<p>It has also created a population of people who are physically dependent on "
                "benzodiazepines without ever having taken one knowingly. If you have been using "
                "street fentanyl regularly, you may be in this position. Symptoms that point to "
                "it include blackouts, missing hours you cannot account for, severe anxiety and "
                "insomnia between uses, and withdrawal that continues after your opioid "
                "treatment is well established.</p>",
                "<p>If you start opioid agonist treatment and still feel dreadful once your dose "
                "is clearly adequate, untreated benzodiazepine withdrawal is one of the first "
                "things we look for. It is missed often, and it is treatable.</p>",
            ]),
            ("why-slow", "Why the taper has to be slow", [
                "<p>Opioid withdrawal is miserable but rarely dangerous. Benzodiazepine "
                "withdrawal is the opposite. It can cause seizures, delirium and, in severe "
                "cases, death. This difference governs everything about how it is treated.</p>",
                "<p>A benzodiazepine taper typically involves switching to a long acting "
                "benzodiazepine such as diazepam, which smooths out the peaks and troughs, then "
                "reducing by small percentages at intervals of weeks. Total time is usually "
                "measured in months. For someone who has used heavily for years, a year or more "
                "is not unusual.</p>",
                "<p>The pace is set by how you actually feel, not by a schedule printed at the "
                "start. If a reduction is difficult, we hold at that level until it settles. "
                "Pausing is not failure, and holding a dose for a while is a normal part of "
                "almost every successful taper.</p>",
            ]),
            ("with-oat", "Managing this alongside opioid treatment", [
                "<p>The combination of benzodiazepines and opioids is the single most common "
                "contributor to overdose deaths among people receiving opioid agonist treatment. "
                "That fact shapes how we approach it, but it does not mean we withhold "
                "treatment.</p>",
                "<p>Being on methadone or Suboxone while also dependent on benzodiazepines is "
                "considerably safer than being on neither. Refusing opioid treatment until "
                "someone stops benzodiazepines pushes them back to the unregulated supply, which "
                "contains both. So we treat them together.</p>",
                "<p>In practice that means being candid with each other about use, closer "
                "follow up early on, a more careful approach to take home doses, and naloxone in "
                "the house. It does not mean choosing between the two.</p>",
            ]),
        ],
        "balance": {
            "good_title": "What we can do",
            "good": [
                "Identify benzodiazepine dependence that arrived through the drug supply",
                "Plan and prescribe a structured taper at a pace you can sustain",
                "Substitute to a long acting benzodiazepine to smooth withdrawal",
                "Treat this at the same time as opioid agonist treatment",
                "Adjust or pause the plan whenever a step proves too hard",
            ],
            "note_title": "Important cautions",
            "note": [
                "Never stop benzodiazepines abruptly, since withdrawal can cause seizures",
                "Tapering takes months, and sometimes longer than a year",
                "Symptoms can persist for a while after the last dose",
                "Combining benzodiazepines with opioids or alcohol carries serious overdose risk",
                "Naloxone reverses opioids only, and does nothing to benzodiazepines",
            ],
        },
        "faqs": [
            ("Why can I not just stop taking them?",
             ["<p>Because unlike opioid withdrawal, benzodiazepine withdrawal can kill you. "
              "Abrupt cessation after regular use can cause seizures, severe confusion and "
              "delirium requiring hospital care.</p>",
              "<p>This is the one part of substance use treatment where doing it yourself, "
              "quickly, is genuinely dangerous rather than merely unpleasant. If you have been "
              "using benzodiazepines regularly and want to stop, please talk to us before you "
              "reduce anything.</p>"]),
            ("How would I know if there are benzodiazepines in what I have been using?",
             ["<p>You often cannot tell from the drug itself, but the pattern gives it away. "
              "Blackouts, hours you cannot account for, coming round confused after an overdose "
              "reversal, and severe anxiety or insomnia between uses all point toward it.</p>",
              "<p>The clearest sign shows up once opioid treatment is working. If your methadone "
              "or Suboxone dose is clearly adequate and you still feel awful, benzodiazepine "
              "withdrawal is a likely explanation. Drug checking services in British Columbia can "
              "test a sample, and a urine screen at the clinic can confirm it.</p>"]),
            ("How long does a benzodiazepine taper take?",
             ["<p>Months, usually. A common approach reduces by roughly five to ten percent of "
              "the current dose every one to four weeks, which for someone on a substantial dose "
              "means six months to a year or more.</p>",
              "<p>It sounds slow, and it is. It is also the approach with the best chance of "
              "working, because fast tapers overwhelmingly end in a return to use. The taper is "
              "yours to pace, and we would far rather take eighteen months and succeed than six "
              "months and start again.</p>"]),
            ("Can I be on methadone or Suboxone and still be prescribed benzodiazepines?",
             ["<p>Sometimes, in the context of a structured taper and with clear monitoring. It "
              "is not something we do casually, because the combination carries real overdose "
              "risk.</p>",
              "<p>The alternative is usually worse. Someone dependent on benzodiazepines who "
              "cannot get a prescribed, measured supply returns to a street supply of unknown "
              "strength. A supervised taper is safer than that, and we make the decision case by "
              "case rather than by blanket policy.</p>"]),
            ("Will withdrawal symptoms continue after I finish the taper?",
             ["<p>For some people, yes. A minority experience lingering anxiety, sleep "
              "disturbance and sensory sensitivity for weeks or months after the last dose. It "
              "is recognised, it is not imagined, and it does resolve.</p>",
              "<p>Knowing it can happen matters, because people who are not warned often assume "
              "something is permanently wrong and go back to using. Stay in contact with us "
              "through that period rather than disappearing at the end of the taper.</p>"]),
            ("Does naloxone work on a benzodiazepine overdose?",
             ["<p>No. Naloxone reverses opioids only. It has no effect on benzodiazepines.</p>",
              "<p>This matters a great deal with today drug supply. When someone overdoses on a "
              "mixture, naloxone will restore their breathing but they may remain heavily "
              "sedated and can deteriorate again. Always call 911, always stay with the person, "
              "and be ready to give further doses. The Good Samaritan Drug Overdose Act gives "
              "legal protection from simple drug possession charges to people who call for help "
              "at an overdose.</p>"]),
            ("I was prescribed benzodiazepines by a doctor years ago. Is this the same thing?",
             ["<p>The dependence is the same, and so is the taper. What differs is the "
              "circumstances, and it is worth saying plainly that long term prescribed "
              "benzodiazepine dependence is not a moral failure. It was standard practice for "
              "decades.</p>",
              "<p>People who came to it through a prescription often taper more predictably, "
              "because the dose is known and consistent. The principles are unchanged: slowly, "
              "with support, at a pace you set.</p>"]),
        ],
        "related": ["methadone", "suboxone", "substance-use-treatment"],
    },
    # ----------------------------------------------------------------- #
    {
        "slug": "nicotine-cessation",
        "name": "Nicotine and tobacco cessation",
        "nav_name": "Nicotine",
        "nav_desc": "Free provincial coverage for cessation medication",
        "tag": None,
        "h1": "Nicotine and tobacco cessation",
        "lede": (
            "Smoking rates among people in opioid treatment are several times higher than in the "
            "general population, and tobacco ends up killing more of our patients than opioids "
            "do. British Columbia covers the medication that helps. Most people do not know it."
        ),
        "meta_desc": (
            "Nicotine and tobacco cessation in BC. Free nicotine replacement and cessation "
            "medication through the provincial programme, alongside opioid treatment."
        ),
    "stats": [
        ('~80%', 'Of people in opioid treatment smoke, against roughly 10% of BC adults',
         'Addiction medicine literature'),
        ('$0', 'Cost of nicotine replacement in British Columbia',
         'BC Smoking Cessation Program'),
        ('0', 'Prescriptions needed for patches, gum or lozenges',
         'BC Smoking Cessation Program'),
    ],
        "summary": (
        'Free provincial coverage for the medication that actually helps you stop smoking.'
    ),
    "cards": [
        ('shield', 'What is covered',
         'Patches, gum, lozenges and inhalers, plus varenicline and bupropion. British Columbia covers all of it for eligible residents.'),
        ('clinic', 'How to get it',
         'Ask any BC pharmacy to register you with your BC Services Card, or raise it at your next appointment and we will sort it out while you are here.'),
        ('route', 'What actually works',
         'A patch alone is the most common approach and the least effective. A patch plus a fast acting product works considerably better, and it is covered.'),
    ],
    "facts": [
        ('Options', 'Patches, gum, varenicline, bupropion'),
        ('Cost in BC', 'Free through the provincial programme'),
        ('Prescription', 'Not needed for nicotine replacement'),
        ('Best results', 'A patch plus a fast acting product'),
        ('Alongside OAT', 'Yes, and outcomes tend to improve'),
    ],
    "pullquote": (
        'Around eighty percent of people in opioid agonist treatment smoke, against roughly ten percent of adults in British Columbia. Over a full life, tobacco kills more people in this group than overdose does.'
    ),
    "sections": [
            ("why-now", "Why this matters in an opioid clinic", [
                "<p>It is a strange thing to raise with someone whose life is being organised "
                "around fentanyl, and we understand why it lands low on the list. The numbers "
                "are still worth stating. Around eighty percent of people in opioid agonist "
                "treatment smoke, against roughly ten percent of adults in British Columbia. "
                "Over a full life, tobacco kills more people in this group than overdose does.</p>",
                "<p>There is a persistent belief that quitting smoking will destabilise recovery "
                "from other substances. Research points the other way. People who address tobacco "
                "during substance use treatment tend to do slightly better on the substance they "
                "came in for, not worse.</p>",
                "<p>None of this is a condition of your care. We will raise it once, tell you "
                "what is available, and leave it with you.</p>",
            ]),
            ("whats-covered", "What British Columbia covers", [
                "<p>The BC Smoking Cessation Program is one of the more generous in Canada and "
                "one of the least used. It covers, for eligible residents:</p>",
                "<ul>"
                "<li><strong>Nicotine replacement therapy.</strong> Patches, gum, lozenges and "
                "inhalers, available from a pharmacy without a prescription. You register once "
                "with your BC Services Card.</li>"
                "<li><strong>Prescription cessation medication.</strong> Varenicline and "
                "bupropion, covered through PharmaCare with the usual plan rules.</li>"
                "<li><strong>QuitNow.</strong> Free coaching by phone, text and web, available "
                "in multiple languages.</li>"
                "</ul>",
                "<p>Ask your pharmacist to register you for the nicotine replacement benefit, or "
                "raise it at your next appointment with us and we will sort it out while you are "
                "here.</p>",
            ]),
            ("what-works", "What actually works", [
                "<p>A patch on its own is the most common approach and the least effective. The "
                "patch delivers a steady background level but does nothing for the sudden urge "
                "that follows a coffee or a stressful phone call.</p>",
                "<p>Combination therapy works better: a patch for the baseline, plus gum, a "
                "lozenge or an inhaler for the peaks. This is well supported by evidence, it is "
                "covered, and it is underused because nobody explains it.</p>",
                "<p>Two other points are worth knowing. Most people underdose nicotine "
                "replacement, stop too early, then conclude it does not work. And most successful "
                "quits follow several unsuccessful ones. A relapse is a data point about what to "
                "change, not evidence that you cannot do it.</p>",
            ]),
        ],
        "balance": {
            "good_title": "What is available",
            "good": [
                "Free nicotine patches, gum, lozenges and inhalers through the provincial programme",
                "Varenicline and bupropion covered through PharmaCare",
                "Free QuitNow coaching by phone, text and web",
                "Prescribing and follow up during appointments you already attend",
                "No prescription needed for the nicotine replacement benefit",
            ],
            "note_title": "Worth knowing",
            "note": [
                "The provincial nicotine replacement benefit covers a set period each calendar year",
                "A patch alone is far less effective than a patch with a fast acting product",
                "Most people underdose nicotine replacement and stop it too early",
                "Several attempts are normal, and each one improves the odds of the next",
                "Vaping is less harmful than smoking but is not covered by the programme",
            ],
        },
        "faqs": [
            ("Should I really try to quit smoking while I am dealing with opioids?",
             ["<p>Only if you want to. It is never a condition of your opioid treatment and we "
              "will not keep bringing it up.</p>",
              "<p>The evidence does contradict the common assumption. People who address tobacco "
              "during substance use treatment tend to do slightly better with the substance they "
              "came in for. The idea that quitting smoking uses up willpower needed elsewhere is "
              "intuitive but not supported.</p>"]),
            ("How do I get the free nicotine patches or gum?",
             ["<p>Go to any pharmacy in British Columbia with your BC Services Card and ask to "
              "register for the smoking cessation programme. No prescription and no appointment "
              "is needed for nicotine replacement therapy.</p>",
              "<p>The benefit covers a continuous period of treatment each calendar year, so it "
              "is worth starting when you are reasonably ready rather than trying it for three "
              "days. We can also register you during a clinic appointment.</p>"]),
            ("Is varenicline safe for someone in opioid treatment?",
             ["<p>Generally yes. Varenicline is among the most effective cessation medications "
              "and does not interact with methadone or buprenorphine.</p>",
              "<p>Older warnings about serious mood effects were reviewed in large trials and "
              "largely withdrawn. That said, if you have significant depression or a history of "
              "suicidal thoughts, tell us so we can follow up more closely. Nausea is the most "
              "common side effect and usually settles.</p>"]),
            ("Does smoking affect my methadone dose?",
             ["<p>It can. Tobacco smoke induces liver enzymes that metabolise a number of "
              "medications, and some people find their methadone clears faster while they are "
              "smoking heavily.</p>",
              "<p>The practical consequence is that quitting can occasionally make an existing "
              "dose feel stronger. It is not a reason to keep smoking. It is a reason to tell us "
              "when you quit, so we can watch for it and adjust if needed. This effect comes from "
              "the smoke rather than the nicotine, so patches and gum do not cause it.</p>"]),
            ("Is vaping a reasonable way to stop smoking?",
             ["<p>It is considerably less harmful than smoking, and for some people it works "
              "when nothing else has. It is not harmless, and the long term effects are still "
              "being studied.</p>",
              "<p>It is not covered by the provincial programme, so you pay for it yourself, "
              "which for many patients is the deciding factor. If vaping has got you off "
              "cigarettes, that is real progress. Talk to us about a plan to come off nicotine "
              "entirely when you are ready.</p>"]),
            ("I have tried to quit before and failed. Is there any point trying again?",
             ["<p>Yes, and the statistics are genuinely on your side. Most people who quit "
              "permanently did so after several earlier attempts. Each attempt teaches you "
              "something about which situations undo you.</p>",
              "<p>What usually changes on a successful attempt is method rather than "
              "willpower: combination nicotine replacement instead of a patch alone, an adequate "
              "dose, a longer course, and coaching alongside it. If previous attempts were "
              "unaided, you have not really tested what the treatments can do.</p>"]),
        ],
        "related": ["methadone", "suboxone", "substance-use-treatment"],
    },
]
