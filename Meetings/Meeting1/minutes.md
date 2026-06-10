# Meeting 1 — Minutes

## Meeting Details

| Field | Info |
|-------|------|
| **Date** | 27 May 2026 |
| **Time** | 2:00 PM – 3:00 PM |
| **Location** | Coventry University London Campus |
| **Chair** | Jina Giri |
| **Minute-Taker** | Mohammad Zayed Alam |

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

## Agenda

1. Introduce the project and review initial codebase
2. Assign team roles and responsibilities
3. Identify missing components and issues
4. Set up GitHub and Trello for collaboration
5. Plan Week 1 deliverables

## Discussion Summary

The team was introduced to the project structure under the group name **Cyber Detectives** (later rebranded to **buzzXzone**). The initial codebase from a previous prototype ("Pookie") was uploaded and reviewed — files included `app.py`, a database file, and `README.md`.

The project was identified as a Flask-based eco-themed educational quiz hub designed for children aged 6–12. The platform includes four mini-games: an auto-play Snake quiz, a Math quiz, a Cyber Security quiz, and a locked Memory Match game (unlocks at 100 points).

The authentication system was reviewed: user registration, login, OTP email verification, and password reset using SQLite for storage.

**Missing components identified:**
- `questions/` JSON files (quiz content)
- `static/` folder (CSS and JavaScript)
- `templates/` HTML files

**Security issue found:** Gmail address and app password were hard-coded in `app.py`. The team agreed to move credentials to environment variables.

The team learned basic GitHub workflow: committing changes, pushing updates, and pulling the latest version.

## Decisions Made

- Team name: **Cyber Detectives** (platform name: buzzXzone)
- Roles and responsibilities assigned to all six members
- Credentials must be moved to environment variables before next sprint
- Trello board set up for task tracking

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Move credentials to `.env` | Shree Krishna | Week 2 |
| Create question JSON files | Aaryut, Saif | Week 2 |
| Design dashboard wireframes | Jina | Week 2 |
| Set up Supabase database | Mohammad | Week 2 |
| Review and test auth flow | Pushparaj | Week 2 |

## Next Meeting

**Date:** 29 May 2026 — Review wireframes and plan Sprint 2.

## Evidence

See [Week 1 progress](Week%201%20progress/) for screenshots and activity records.
