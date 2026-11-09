"""
Everything written on the portfolio lives here. Edit the text, no HTML needed.

Projects can ALSO be managed from the Django admin (/admin/ -> Projects).
If the database has any projects, they replace the PROJECTS list below.

Images live in pages/static/site/img/. To use your own hobby photos, save them with
the same names (hobby-boxing.png, hobby-badminton.png, hobby-gym.png). Transparent
PNG cut-outs look best because the three photos overlap each other.
"""

PROFILE = {
    "name": "Francis",
    "full_name": "Francis G. Poliran",
    "title": "Portfolio",
    "email": "francispoliran437@gmail.com",
    "github_url": "https://github.com/renceCoding/portfolio-project.git",
    "github_label": "github.com/renceCoding",
    "university": "Palawan State University",
    "resume_url": "",   # e.g. "/static/site/resume.pdf" once you add the file
}

HERO = {
    "headline": ["Designing the web,", "simply beautiful."],
    "intro": "Hi, I'm Francis, a website and UI designer who also writes the code.",
    "card_left": {
        "title": "User-friendly by default",
        "text": "Clean, visually appealing websites that are easy to use.",
    },
    "card_right": {
        "title": "Design and code",
        "text": "Figma and Photoshop for the look, Django and JavaScript for the build.",
    },
    "badge": "design \u00b7 develop \u00b7 deliver \u00b7 ",
}

ABOUT = {
    "heading": "Hi, I'm Francis.",
    "paragraphs": [
        "I am a designer, proficient in Figma and Photoshop, and also skilled in video editing. "
        "In addition to my design skills, I am a passionate developer with a strong commitment to continuous learning.",
        "I strive to create user-friendly and visually appealing websites. My goal is to collaborate with "
        "clients to bring their visions to life and deliver exceptional digital solutions.",
    ],
    "chips": ["Website designer", "UI designer", "Developer"],
    # (label, value); a value starting with "mailto:" or "http" becomes a link in the template
    "facts": [
        ("Studying at", "Palawan State University"),
        ("Focus", "Website and UI design"),
        ("Design tools", "Figma, Photoshop, video editing"),
        ("Build with", "Django, JavaScript, HTML, CSS"),
    ],
}

HOBBIES = {
    "heading": "Away from the screen",
    "text": "When I'm not designing or coding, you'll find me boxing, playing badminton or training at the gym.",
    "items": [
        {"id": "boxing", "label": "Boxing", "image": "site/img/hobby-boxing.png"},
        {"id": "badminton", "label": "Badminton", "image": "site/img/hobby-badminton.png"},
        {"id": "gym", "label": "Gym", "image": "site/img/hobby-gym.png"},
    ],
}

# Glossy 3D tiles (hero + toolkit). `glyph` picks the drawing in the template.
TOOLS = [
    {"id": "figma", "label": "Figma", "group": "Design", "glyph": "figma"},
    {"id": "photoshop", "label": "Photoshop", "group": "Design", "glyph": "ps"},
    {"id": "django", "label": "Django", "group": "Build", "glyph": "dj"},
    {"id": "js", "label": "JavaScript", "group": "Build", "glyph": "js"},
    {"id": "web", "label": "HTML and CSS", "group": "Build", "glyph": "code"},
    {"id": "video", "label": "Video editing", "group": "Creative", "glyph": "play"},
]

TOOLKIT = {
    "heading": "Tools I work with",
    "groups": [
        {"name": "Design", "items": ["Figma", "Photoshop", "UI design"]},
        {"name": "Build", "items": ["Django", "JavaScript", "HTML", "CSS"]},
        {"name": "Creative", "items": ["Video editing"]},
    ],
}

PROJECTS = [
    {
        "name": "FITPLAN",
        "description": "This is my recent work for my database class project about HRM or Human Resources Management.",
        "role": "Database class project",
        "tech": ["Database design", "HRM"],
        "image": "site/img/fitplan.webp",
        "live_url": "", "repo_url": "",
    },
    {
        "name": "PALCONNECT",
        "description": "I created this design using the Figma application and it's one of my favorite web designs for a landing page.",
        "role": "UI designer",
        "tech": ["Figma", "Landing page"],
        "image": "site/img/palconnect.webp",
        "live_url": "", "repo_url": "",
    },
    {
        "name": "PSU FOOD RESERVATION APP",
        "description": "An application to reserve food only at Palawan State University. I designed this for my Proposal project.",
        "role": "UI designer",
        "tech": ["Figma", "App design"],
        "image": "site/img/psu-food.webp",
        "live_url": "", "repo_url": "",
    },
]

CONTACT = {
    "heading": "Let's build something remarkable together.",
    "text": "Tell me about your idea, your project or your team. I read every message.",
}
