# Meeting Minutes — Meeting 1

**Project:** buzzXzone — Eco Learning Quiz Hub
**Date:** 27 May 2026
**Time:** 2:00 PM – 3:00 PM
**Location:** Coventry University London Campus
**Chair:** Jina Giri
**Minute-Taker:** Mohammad Zayed Alam

---

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

---

## Agenda Items

1. Review initial project codebase
2. Discuss platform features and game design
3. Assign team roles and responsibilities
4. Plan Agile development process
5. Set up GitHub and Trello

---

## Summary of Discussion

The team reviewed the initial project files (Flask application, database, README) uploaded from
the prototype. The platform was identified as a Flask-based eco-themed educational quiz hub
for children aged 6–12.

**Features agreed for development:**
- Auto-play Eco Snake Quiz (no motor-skill barrier)
- Math Quiz (Easy / Medium / Hard)
- Eco Cyber-Security Quiz (Easy / Medium / Hard)
- Memory Match mini-game (locked, unlocks at 100 points)
- OTP email authentication
- Score tracking with persistent high score

Agile Scrum methodology was chosen. Weekly sprints were planned. GitHub is used for version
control and Trello for task tracking.

**Security issue raised:** Gmail credentials were found hard-coded in `app.py`. The team
agreed to move all sensitive credentials to environment variables immediately.

---

## Decisions Made

- Platform concept approved — eco educational quiz hub
- All six roles assigned (Developer, Designer, PM, Content Lead, Researcher, Tester)
- Prototype to be submission-ready within 2 weeks
- Credentials to be moved to `.env` before any code sharing

---

## Role Assignments

| Member | Role |
|--------|------|
| Shree Krishna Shrestha | Lead Developer (Frontend + Backend) |
| Saif Ullah | Content Lead (questions, game concept) |
| Aaryut Chaudhary | Researcher & Scrum Facilitator |
| Jina Giri | UI/UX Designer |
| Mohammad Zayed Alam | Project Manager |
| Pushparaj Mahato | Tester & QA Reviewer |

---

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Move credentials to `.env` | Shree Krishna | Week 2 |
| Create question JSON files (initial) | Aaryut, Saif | Week 2 |
| Design dashboard wireframes | Jina | Week 2 |
| Set up Trello task board | Mohammad | Week 1 |
| Test auth flow end-to-end | Pushparaj | Week 2 |

---

## Next Meeting

**Date:** 29 May 2026 — Review wireframes and plan Sprint 2.
