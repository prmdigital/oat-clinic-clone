# -*- coding: utf-8 -*-
"""Site-wide configuration, navigation and location records.

Everything a non-developer is likely to change lives in this package.
Edit here, run `python tools/build.py`, commit the generated HTML.
"""

SITE = {
    "name": "OAT Clinic",
    "legal_name": "OAT Clinic",
    "tagline": "Opioid agonist treatment across British Columbia",
    "description": (
        "Same day methadone and Suboxone treatment across five British Columbia "
        "clinics. In clinic, by telemedicine, or through your pharmacy. No referral."
    ),
    # Origin plus any sub path the site is served from. Drives canonical
    # URLs, Open Graph tags, the sitemap and the JSON-LD graph.
    #
    # GitHub Pages preview (current):
    "base_url": "https://prmdigital.github.io/oat-clinic-web-layout",
    # Production, once the domain is pointed at the host:
    #   "base_url": "https://www.oatclinic.ca",

    # Sub path the site lives under, no trailing slash. GitHub Pages project
    # sites serve from /<repo>/, so every internal link and asset needs the
    # prefix. Set to "" for a root domain.
    "base_path": "/oat-clinic-web-layout",

    # Preview builds are marked noindex so an unreviewed draft of clinical
    # content cannot turn up in search results. Set False at launch.
    "preview": True,
    "main_phone": "604-670-6580",
    "main_phone_href": "tel:+16046706580",
    "email": "info@oatclinic.ca",
    "hours_short": "Monday to Friday, 10:00 AM to 6:00 PM",
    "hours_note": "Closed weekends and statutory holidays. Requests left outside opening hours are reviewed the next business day.",
    "founded": "2019",
}

# Standard clinic hours. Overridden per location where they differ.
DEFAULT_HOURS = [
    ("Monday", "10:00 AM to 6:00 PM"),
    ("Tuesday", "10:00 AM to 6:00 PM"),
    ("Wednesday", "10:00 AM to 6:00 PM"),
    ("Thursday", "10:00 AM to 6:00 PM"),
    ("Friday", "10:00 AM to 6:00 PM"),
    ("Saturday", None),
    ("Sunday", None),
]

# Schema.org openingHours equivalent for the JSON-LD graph.
SCHEMA_HOURS = [
    {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
     "opens": "10:00", "closes": "18:00"},
]

LOCATIONS = [
    {
        "slug": "vancouver",
        "city": "Vancouver",
        "name": "OAT Clinic Vancouver",
        "street": "633 E Hastings St",
        "region": "BC",
        "postal": "V6A 2R2",
        "phone": "604-670-6580",
        "phone_href": "tel:+16046706580",
        "fax": "604-670-6581",
        "lat": "49.2812",
        "lng": "-123.0906",
        "neighbourhood": "Strathcona and the Downtown Eastside",
        "intro": (
            "Our Vancouver clinic sits on East Hastings between Princess and Heatley, "
            "in the part of the city where the need for accessible opioid agonist "
            "treatment is greatest. Walk in during opening hours and ask for an "
            "assessment. You do not need a referral, an appointment, or a family doctor."
        ),
        "transit": (
            "The 14 and 16 trolley buses stop on East Hastings within a block of the door. "
            "Main Street Science World station is roughly a fifteen minute walk south west."
        ),
        "parking": (
            "Metered street parking is available on East Hastings and on the side streets "
            "north of it. There is no dedicated patient lot."
        ),
        "access": (
            "Ground floor entry from the street with no steps. The washroom is wheelchair accessible."
        ),
        "highlights": [
            "Walk in assessment during all opening hours",
            "Same day methadone and Suboxone starts where clinically appropriate",
            "Direct coordination with nearby dispensing pharmacies",
            "Wound care referral and connection to outreach services",
        ],
        "faqs": [
            ("Can I walk in without calling first?",
             ["Yes. Vancouver is our walk in location. Arriving before 4:00 PM gives our "
              "team the best chance of completing an assessment and starting treatment the "
              "same day, because a first visit usually takes ninety minutes or more."]),
            ("What should I bring to a first visit?",
             ["A piece of photo identification and your BC Services Card if you have them. "
              "If you do not have identification, come anyway. We can begin an assessment "
              "and help you sort out coverage afterwards. It also helps to know the name "
              "and address of the pharmacy you would like to use."]),
            ("Do you take patients who are not from Vancouver?",
             ["Yes. Patients travel to us from across the region, and we regularly "
              "arrange for people assessed in Vancouver to have their medication dispensed "
              "at a pharmacy closer to home."]),
        ],
    },
    {
        "slug": "abbotsford",
        "city": "Abbotsford",
        "name": "OAT Clinic Abbotsford",
        "street": "2777 Gladwin Rd #108",
        "region": "BC",
        "postal": "V2T 4V1",
        "phone": "604-755-4408",
        "phone_href": "tel:+16047554408",
        "fax": "604-755-4378",
        "lat": "49.0431",
        "lng": "-122.3288",
        "neighbourhood": "central Abbotsford, near Abbotsford Regional Hospital",
        "intro": (
            "Our Abbotsford clinic serves the Fraser Valley from a ground floor unit on "
            "Gladwin Road, a short drive from Abbotsford Regional Hospital and Cancer Centre. "
            "It is the main access point for patients in Abbotsford, Mission and Aldergrove."
        ),
        "transit": (
            "Bus routes 2 and 12 stop on Gladwin Road within a short walk. "
            "The clinic is roughly ten minutes by car from Highway 1 at the Clearbrook exit."
        ),
        "parking": (
            "Free surface parking is available on site for patients and visitors."
        ),
        "access": (
            "Unit 108 is at ground level with step free access from the parking lot."
        ),
        "highlights": [
            "Fraser Valley base for methadone and Suboxone treatment",
            "Free on site parking",
            "Telemedicine follow up for patients in Mission and Aldergrove",
            "Coordination with Fraser Health community programs",
        ],
        "faqs": [
            ("Do I need an appointment in Abbotsford?",
             ["Calling ahead is best. Abbotsford runs on a booked schedule more than "
              "Vancouver does, and a call lets us hold time for a full assessment rather "
              "than fitting you in between follow ups."]),
            ("How far do patients usually travel to reach this clinic?",
             ["We see patients from across the eastern Fraser Valley, including Mission, "
              "Aldergrove and Langley. Once you are established on a stable dose, most "
              "follow up appointments can be done by telemedicine so the travel stops."]),
            ("Can my medication be dispensed closer to home?",
             ["Yes. You can be assessed in Abbotsford and have your prescription sent to a "
              "pharmacy near where you live or work. Tell us which pharmacy you prefer and "
              "we will coordinate directly with them."]),
        ],
    },
    {
        "slug": "chilliwack",
        "city": "Chilliwack",
        "name": "OAT Clinic Chilliwack",
        "street": "5625 Promontory Rd",
        "region": "BC",
        "postal": "V2R 0K5",
        "phone": "604-670-6580",
        "phone_href": "tel:+16046706580",
        "fax": None,
        "lat": "49.1188",
        "lng": "-121.9560",
        "neighbourhood": "Promontory, in the south of Chilliwack",
        "intro": (
            "Our Chilliwack location brings opioid agonist treatment into the eastern Fraser "
            "Valley, so patients in Chilliwack, Sardis and Hope no longer have to drive to "
            "Abbotsford or Surrey for routine care."
        ),
        "transit": (
            "Chilliwack transit route 5 serves Promontory Road. Most patients arrive by car."
        ),
        "parking": (
            "Free parking is available on site."
        ),
        "access": (
            "Ground floor access with parking directly outside the entrance."
        ),
        "highlights": [
            "Eastern Fraser Valley access without a drive to Abbotsford",
            "Free parking directly outside",
            "Telemedicine assessments for patients in Hope and Agassiz",
            "Prescriptions sent to the Chilliwack pharmacy you already use",
        ],
        "faqs": [
            ("What days is the Chilliwack clinic open?",
             ["Please call our main line at 604-670-6580 to confirm current clinic days in "
              "Chilliwack before travelling. Our smaller locations run on set days rather "
              "than a full weekly schedule."]),
            ("Can I start treatment here, or only continue it?",
             ["Both. New assessments and ongoing follow up are available. If a same day "
              "start is not possible in Chilliwack on the day you contact us, we will "
              "arrange a telemedicine assessment so treatment is not delayed."]),
        ],
    },
    {
        "slug": "surrey",
        "city": "Surrey",
        "name": "OAT Clinic Surrey",
        "street": "12818 72 Ave",
        "region": "BC",
        "postal": "V3W 2M9",
        "phone": "604-670-6580",
        "phone_href": "tel:+16046706580",
        "fax": None,
        "lat": "49.1350",
        "lng": "-122.8666",
        "neighbourhood": "West Newton, near King George Boulevard",
        "intro": (
            "Our Surrey clinic serves one of the fastest growing communities in British "
            "Columbia from 72 Avenue in West Newton, with straightforward access from King "
            "George Boulevard and Highway 10."
        ),
        "transit": (
            "The 314 and 316 bus routes serve 72 Avenue. Surrey Central SkyTrain station is "
            "about twenty minutes away by bus."
        ),
        "parking": (
            "Free parking is available on site."
        ),
        "access": (
            "Step free entry at ground level."
        ),
        "highlights": [
            "Serves Newton, Whalley, Cloverdale and North Delta",
            "Free on site parking",
            "Punjabi and Hindi language support available on request",
            "Same day telemedicine when in person slots are full",
        ],
        "faqs": [
            ("Is language support available?",
             ["Punjabi and Hindi speaking support can be arranged at the Surrey location. "
              "Please mention the language you prefer when you call so we can schedule "
              "accordingly. Interpretation in other languages can also be arranged."]),
            ("Which communities does the Surrey clinic serve?",
             ["Most patients come from Newton, Whalley, Guildford, Cloverdale and North "
              "Delta. Patients from Langley and White Rock are also welcome."]),
        ],
    },
    {
        "slug": "burnaby",
        "city": "Burnaby",
        "name": "OAT Clinic Burnaby",
        "street": "4676 Hastings St",
        "region": "BC",
        "postal": "V5C 2K5",
        "phone": "604-670-6580",
        "phone_href": "tel:+16046706580",
        "fax": None,
        "lat": "49.2806",
        "lng": "-122.9930",
        "neighbourhood": "Burnaby Heights",
        "intro": (
            "Our Burnaby clinic sits on Hastings Street in Burnaby Heights, close to the "
            "Vancouver boundary. It gives patients in North Burnaby, East Vancouver and "
            "the Tri Cities a quieter alternative to the Vancouver clinic."
        ),
        "transit": (
            "The 25 and 130 bus routes stop on Hastings Street nearby. Gilmore station on "
            "the Millennium Line is a short bus ride south."
        ),
        "parking": (
            "Street parking is available on Hastings Street and on the residential streets behind it."
        ),
        "access": (
            "Street level entry with no steps."
        ),
        "highlights": [
            "Quieter alternative to the Vancouver clinic",
            "Convenient for North Burnaby, East Vancouver and the Tri Cities",
            "Direct transfer of care from our Vancouver location",
            "Telemedicine follow up once your dose is stable",
        ],
        "faqs": [
            ("Can I transfer my care here from the Vancouver clinic?",
             ["Yes, and it is a common request. Because both clinics share one record "
              "system, a transfer usually needs nothing more than telling us at your next "
              "appointment. Your dose and your pharmacy do not have to change."]),
            ("Is this location easier to reach than the Vancouver clinic?",
             ["For patients coming from North Burnaby, the Tri Cities or the eastern edge "
              "of Vancouver, usually yes. Hastings Street parking is easier here than it is "
              "downtown, and the clinic is generally quieter."]),
        ],
    },
]

# Reasons a visitor might contact us, used in the callback form.
CALLBACK_REASONS = [
    "Starting treatment for the first time",
    "Restarting treatment after a break",
    "Transferring from another clinic",
    "Asking a question before I decide",
    "I am calling about someone else",
]

FOOTER_QUICK_LINKS = [
    ("What to expect", "/what-to-expect/"),
    ("For pharmacies", "/for-pharmacies/"),
    ("Blog", "/blog/"),
    ("Contact us", "/contact/"),
    ("Privacy policy", "/privacy/"),
    ("Accessibility", "/accessibility/"),
]
