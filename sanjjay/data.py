"""Static profile data used by the CLI dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Project:
    name: str
    description: str
    stack: str
    github: str
    demo: str


PROFILE = {
    "name": "Sanjjay",
    "role": "Developer / Cybersecurity Enthusiast",
    "bio": (
        "I build secure and beautiful developer experiences, blending software "
        "engineering with practical cybersecurity workflows. I enjoy shipping "
        "tools that feel fast, polished, and memorable."
    ),
    "hostname": "sanjjay@scorpion",
    "os": "Kali Linux",
    "terminal": "sanjjay-shell v1.0",
    "contact": {
        "phone": "(+91) 8608948946",
        "email": "sanjjay@example.com",
        "location": "India",
    },
    "socials": {
        "github": "https://github.com/sanjjaystars",
        "linkedin": "https://www.linkedin.com/in/sanjjay-aroumougam-43a919382/",
        "instagram": "https://www.instagram.com/blaze._xr/",
        "resume": "https://example.com/sanjjay-resume.pdf",
    },
    "skills": {
        "Programming": ["Python", "JavaScript", "Bash", "SQL"],
        "Cybersecurity": ["Threat Modeling", "OSINT", "Vulnerability Assessment", "SIEM"],
        "DevOps & Cloud": ["Docker", "GitHub Actions", "Linux", "CI/CD"],
        "Frameworks": ["FastAPI", "Flask", "Rich", "React"],
    },
    "certifications": [
        "CompTIA Security+ (Placeholder)",
        "Google Cybersecurity Professional Certificate (Placeholder)",
    ],
    "education": [
        "B.E. in Computer Science (Placeholder University)",
    ],
}


PROJECTS: List[Project] = [
    Project(
        name="SentinelScan",
        description="Automated recon and vulnerability triage toolkit for security teams.",
        stack="Python, Nmap, OWASP ZAP, SQLite",
        github="https://github.com/sanjjaystars/sentinelscan",
        demo="https://example.com/sentinelscan-demo",
    ),
    Project(
        name="DarkTrace CLI",
        description="A terminal-first log intelligence assistant with threat tagging.",
        stack="Python, Rich, Elastic, Regex",
        github="https://github.com/sanjjaystars/darktrace-cli",
        demo="https://example.com/darktrace-cli",
    ),
    Project(
        name="GhostPort",
        description="Stealth portfolio terminal inspired by eDEX-UI aesthetics.",
        stack="Python, Rich, Packaging",
        github="https://github.com/sanjjaystars/ghostport",
        demo="https://example.com/ghostport",
    ),
]

COMMAND_DESCRIPTIONS = {
    "help": "Show all available commands.",
    "about": "Display a short intro/profile summary.",
    "skills": "Show technical skills grouped by category.",
    "projects": "List featured projects with stack and links.",
    "github": "Show GitHub profile link.",
    "linkedin": "Show LinkedIn profile link.",
    "contact": "Display contact details.",
    "resume": "Show resume link placeholder.",
    "clear": "Clear the terminal and redraw dashboard header.",
    "whoami": "Display terminal identity and mission info.",
    "socials": "Show all social links in one table.",
    "banner": "Redraw the ASCII brand banner.",
    "system": "Show fake system status and runtime metrics.",
    "exit": "Exit gracefully.",
}
