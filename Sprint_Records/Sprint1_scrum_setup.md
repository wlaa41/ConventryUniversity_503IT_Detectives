# Sprint 1 — Project & Scrum Setup

**Sprint Dates:** 27 May – 30 May 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## Repository Setup

The GitHub repository was initialised at the start of Sprint 1 with the following structure:

```
ConventryUniversity_503IT_Detectives/
├── buzzxzone/           ← Main Flask application
│   ├── app.py
│   ├── requirements.txt
│   ├── vercel.json
│   ├── questions/       ← Question bank JSON files
│   ├── static/          ← CSS, JS, SVG
│   └── templates/       ← Jinja2 HTML templates
├── Meetings/            ← Meeting minutes
├── Sprint_Records/      ← Technical sprint documentation
└── README.md
```

The `start` branch was used as the main working branch throughout the project.

---

## Agile Process

The team adopted a lightweight Scrum process:

- **Sprint length:** 3–5 days per sprint (adjusted for the 2-week project timeline).
- **Daily stand-up:** WhatsApp group messages — what was done, what is next, any blockers.
- **Sprint planning:** Conducted at each meeting, outcomes recorded in meeting minutes.
- **Sprint review:** Live demo to the team at each meeting.
- **Sprint retrospective:** Written up after each sprint (see Sprint Retrospectives).
- **Backlog tracking:** Trello board with cards per task.

---

## Tech Stack Decision (Sprint 1)

The tech stack was agreed in Meeting 2 and has been unchanged since:

| Layer | Choice | Reason |
|-------|--------|--------|
| Backend | Python / Flask | Team familiar with Python; Flask is lightweight for a small app |
| DB | SQLite (local) / Supabase PostgreSQL (production) | SQLite for simplicity; Supabase for free hosted PostgreSQL |
| Frontend | Vanilla HTML/CSS/JS | No framework needed at this scale; reduces complexity |
| Deployment | Vercel | Free tier, Git integration, zero-config for Flask via `@vercel/python` |
| Auth | Session + OTP | Simple to implement, adds real security value |

The decision to avoid React or Vue was deliberate — the extra framework complexity was not
justified for a four-page game hub. Vanilla Canvas 2D proved sufficient for all visual features.

---

## Initial Files Created This Sprint

| File | Description |
|------|-------------|
| `buzzxzone/app.py` | Flask application skeleton with config and DB init |
| `buzzxzone/requirements.txt` | Flask, Werkzeug, psycopg2-binary, python-dotenv |
| `buzzxzone/vercel.json` | Initial Vercel deployment config |
| `README.md` | Project overview with tech stack and team information |
| `.gitignore` | Python, .env, .db, IDE files excluded from version control |
