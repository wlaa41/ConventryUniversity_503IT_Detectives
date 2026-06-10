# Week 1 — Activities Completed

## Overview

Week 1 focused on understanding the project structure, assigning roles, identifying missing
components, improving security awareness, and setting up collaboration tools.

## Activities

### Project Introduction & Role Assignment

The team (six members, group name: **Cyber Detectives**) was introduced to the project.
Roles were assigned according to each member's strengths to ensure clear responsibilities
and efficient workflow.

The initial project files from the previous prototype ("Pookie") were uploaded and reviewed:
`app.py`, the database file, and `README.md`. The project was confirmed as a Flask-based
eco-themed learning quiz hub designed for children aged 6–12, featuring four mini-games:
auto-play Snake quiz, Math quiz, Eco Cyber-Security quiz, and a locked Memory Match.

See evidence: [Roles assigned.png](Roles%20assigned.png)

### Authentication System Review

The authentication flow was reviewed in full:
- User registration with email uniqueness enforcement
- Login with password hash verification
- 6-digit OTP email verification with 5-minute expiry
- Password reset via OTP flow
- SQLite database for user and game data

### Missing Components Identified

The following required files were found missing from the initial upload:

| Missing Component | Impact |
|-------------------|--------|
| `questions/*.json` | No quiz content — game cannot start |
| `static/` (CSS + JS) | No styling or game logic |
| `templates/*.html` | No pages to render |

### Security Issue Identified

Pushparaj identified that sensitive credentials (Gmail address and app password) were
hard-coded inside `app.py`. The team agreed to move these to environment variables
(`.env` file, excluded from version control) as an immediate security improvement.

### Database Setup

Flask database initialisation was reviewed. The `init_db()` function creates the `users`
table automatically on first startup and handles schema migrations.

See evidence: [FLASK_DB_SETUP.png](FLASK_DB_SETUP.png)

### GitHub Workflow

The team learned and practised:
- Making commits with descriptive messages
- Pushing updates to the shared repository
- Pulling the latest version from the remote
- Understanding branch structure

### Trello Setup

Each team member created task cards on the shared Trello board, assigned themselves to their
responsibilities, and moved cards between To-Do, In Progress, and Done columns throughout the week.
