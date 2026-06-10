# Meeting 1 — Agenda & Summary

**Date:** 27 May 2026
**Group:** Cyber Detectives (buzzXzone)

---

## Agenda

1. Introduce the project and review initial codebase
2. Assign team roles and responsibilities
3. Identify missing components and security issues
4. Set up GitHub and Trello
5. Plan Week 1 deliverables

---

## Meeting Summary

The team (six members, group name **Cyber Detectives**) was formed and roles were assigned.

The initial project files from a previous prototype were reviewed:
- `app.py` — Flask application with routes and database setup
- Database file — SQLite user store
- `README.md` — project overview

The platform was confirmed as a Flask-based eco-themed educational quiz hub for children
aged 6–12, featuring four mini-games: auto-play Snake quiz, Math quiz, Eco Cyber-Security
quiz, and a locked Memory Match (unlocks at 100 points).

**Authentication flow reviewed:**
- Register with email + password
- Login with OTP email verification (6-digit, 5-minute expiry)
- Forgot-password OTP reset flow
- SQLite database for user storage

**Missing components identified:**
- `questions/` JSON files — quiz content
- `static/` folder — CSS and JavaScript
- `templates/` HTML files — the app will not render without these

**Security issue raised:**
Gmail credentials were hard-coded in `app.py`. The team agreed to move all sensitive
credentials to a `.env` file excluded from version control.

**GitHub workflow learned:**
- `git commit` — save changes with a message
- `git push` — upload to the shared repository
- `git pull` — download the latest version from the remote

---

## Outcomes

- Team formed with six members and clear role assignments
- Project scope confirmed: eco educational quiz hub, four mini-games
- Security fix agreed: credentials → environment variables
- GitHub and Trello set up for collaboration
