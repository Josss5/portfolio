"""Portfolio content for Josrel Enriquez Ombion.

Keep personal links as placeholders until you are ready to publish them. The
website reads all portfolio text and project case studies from this file.
"""

PROFILE = {
    "name": "Josrel",
    "full_name": "Josrel Enriquez Ombion",
    "title": "Portfolio",
    "email": "ombionjosrel@gmail.com",  # Replace before publishing.
    "github_url": "https://github.com/Josss5",  # Replace before publishing.
    "github_label": "https://github.com/Josss5",
    "linkedin_url": "",  # Add a full LinkedIn URL when available.
    "university": "Palawan State University – Rizal Campus",
    "resume_url": "",  # e.g. "/static/site/resume.pdf"
}

HERO = {
    "eyebrow": "Technology · Leadership · Innovation",
    "headline": "Building solutions through technology. Leading through service. Innovating for impact.",
    "intro": "I am a fourth-year Computer Science student who develops practical software, IoT systems, and innovation projects for real-world needs.",
    "stats": [("3 years", "University Student Government service"), ("2 projects", "Software and agri-innovation highlights"), ("2026", "YFC MIMAROPA Start-up Provincial Awardee")],
}

ABOUT = {
    "heading": "A student developer who builds with purpose.",
    "paragraphs": [
        "I am pursuing a Bachelor of Science in Computer Science at Palawan State University – Rizal Campus. My work brings together software development, system design, hardware-software integration, and project coordination.",
        "Whether I am developing an irrigation monitor, documenting service operations, or exploring agricultural automation, I begin with the people and processes a system needs to support. I aim for practical solutions that are clear, reliable, and ready to improve over time.",
    ],
    "focus": ["Software development", "IoT & automation", "Agricultural innovation", "Student leadership"],
    "facts": [("Education", "BSCS, 4th Year"), ("Campus", "Palawan State University – Rizal Campus"), ("Building", "Software, mobile, web, and IoT systems"), ("Leading", "University Student Government")],
}

SKILL_GROUPS = [
    {"name": "Programming & development", "items": ["Java", "C#", "Kotlin", "PHP", "C/C++ (Arduino)"]},
    {"name": "Web development", "items": ["Laravel", "HTML", "CSS", "JavaScript", "Tailwind CSS", "MySQL"]},
    {"name": "Mobile development", "items": ["Android Studio", "Kotlin", "Jetpack Compose", "Retrofit", "MVVM Architecture"]},
    {"name": "Hardware & IoT", "items": ["ESP32", "Arduino", "Sensor Integration", "Embedded Systems", "Automated Irrigation", "Hardware-Software Integration"]},
    {"name": "Design & tools", "items": ["Figma", "Git/GitHub", "Visual Studio Code", "Android Studio"]},
]

PROJECTS = [
    {
        "slug": "sibol", "number": "01", "name": "SIBOL", "subtitle": "ESP32-based farm monitoring and automatic irrigation for soil-bedded lettuce cultivation.",
        "description": "An agricultural technology system that connects environmental sensing, irrigation automation, and Android-based monitoring for lettuce cultivation.",
        "role": "System planning, hardware integration, firmware, Android development, architecture, and testing", "problem": "Lettuce cultivation needs timely awareness of soil and environmental conditions, while routine watering can be difficult to monitor and adjust consistently.",
        "solution": "SIBOL combines sensor monitoring with automatic, manual, and scheduled irrigation controls. An Android application provides real-time visibility, historical records, analytics, and watering prediction support.",
        "process": ["Plan the monitoring and irrigation workflow.", "Integrate ESP32 hardware, sensors, and local Wi-Fi communication.", "Develop the firmware and Android monitoring experience.", "Test irrigation controls, data logging, and system behavior."],
        "features": ["Soil moisture, temperature, and humidity monitoring", "Automatic, manual, and scheduled irrigation", "Configurable watering duration and soaking intervals", "Android monitoring, historical logs, analytics, and watering prediction"],
        "tech": ["ESP32", "Arduino/C++", "Kotlin", "Android Studio", "Jetpack Compose", "Retrofit", "SQLite/CSV"],
        "status": "Project development and testing", "accent": "green", "live_url": "", "repo_url": "",
    },
    {
        "slug": "motoshopgrid", "number": "02", "name": "MotoShopGrid", "subtitle": "Visual Inventory. Precision Service.",
        "description": "A motorcycle parts inventory and service shop management system for local repair and parts businesses.", "role": "Project developer",
        "problem": "Motorcycle shops need a clearer way to organize parts, confirm motorcycle compatibility, document service work, and maintain accurate operational records.",
        "solution": "MotoShopGrid organizes visual parts information, inventory, suppliers, work orders, service documentation, and reporting in one focused operational system. It is intentionally not a point-of-sale system.",
        "process": ["Define an inventory and service-focused workflow.", "Model parts, stock movements, suppliers, compatibility, and work orders.", "Build role-aware administration and operational views.", "Design documentation and backup features for day-to-day shop use."],
        "features": ["Visual parts catalogue and compatibility information", "Inventory, stock adjustments, restocking, and suppliers", "Work orders, service notes, and labor-cost documentation", "Role-based access, reporting, and backup management"],
        "tech": ["Laravel 13", "PHP 8.4+", "MySQL", "Blade", "Tailwind CSS 4", "Vite", "JavaScript"],
        "status": "In development", "accent": "orange", "live_url": "", "repo_url": "",
    },
]

LEADERSHIP = {
    "heading": "Leading through service and continuity.",
    "text": "My University Student Government journey has taught me to represent students responsibly, manage organizational work with care, and prepare the next group of leaders to continue the work.",
    "theme": "Continuing the Legacy, Empowering New Leaders.",
    "timeline": [("01", "Legislative Secretary", "Appointed", "Supported legislative work and organizational documentation."), ("02", "Student Government Senator", "Elected", "Represented student concerns through governance and policy work."), ("03", "USG President", "Elected", "Led student representation, programs, coordination, budget preparation, and organizational management.")],
    "responsibilities": ["Student representation and governance", "University activity planning and coordination", "Budget preparation and resource management", "Resolution and policy drafting and review", "Coordination with administrators, local officials, and external stakeholders", "Student development programs, assemblies, and campus events"],
}

ACHIEVEMENTS = [
    ("Leadership", "Three years in the University Student Government", "Appointed Legislative Secretary · Elected Senator · Elected President"),
    ("Innovation", "SIBOL agricultural IoT system", "Farm monitoring and irrigation automation for lettuce cultivation"),
    ("Development", "MotoShopGrid", "Inventory visibility and service-management system for motorcycle shops"),
]

CONTACT = {
    "heading": "Let’s connect and build something useful.",
    "text": "I welcome opportunities for internships, collaborations, project conversations, and technology initiatives.",
}
