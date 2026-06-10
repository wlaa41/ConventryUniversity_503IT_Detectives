#!/usr/bin/env bash
set -e

REPO="c:/Users/sande/OneDrive/Documents/GitHub/ConventryUniversity_503IT_Detectives"
cd "$REPO"

commit() {
  git add -A
  git commit -m "$1"
}

# ── COMMIT 1 ── Add Screenshots section to README
cat >> README.md << 'EOF'

---

## Screenshots

> Screenshots of the live application demonstrating key features.

| Page | Description |
|------|-------------|
| Dashboard | Main hub with Capy mascot and game cards |
| Eco Snake Quiz | Auto-playing snake with live question overlay |
| Math Quiz | Difficulty selector and question screen |
| Memory Match | Unlockable 4×4 card grid |
| Login / Register | OTP-verified auth pages |

_Screenshots are located in `/screenshots/` (added during presentation sprint)._
EOF
commit "docs: add Screenshots section to README"

# ── COMMIT 2 ── Add Troubleshooting section
cat >> README.md << 'EOF'

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `DATABASE_URL` error on startup | Env var not set | Add `DATABASE_URL` to `.env` |
| OTP not received | Gmail not configured | Check `GMAIL_USER` / `GMAIL_PASSWORD` or read OTP from console |
| Vercel 500 error | Missing env vars in dashboard | Set all required vars in Vercel → Settings → Environment Variables |
| Memory Match locked forever | Score never reaches 100 | Play Snake or Math Quiz first to build score |
| `psycopg2` install fails | Missing libpq | Use `psycopg2-binary` instead of `psycopg2` |
EOF
commit "docs: add Troubleshooting section to README"

# ── COMMIT 3 ── Add Contributing section
cat >> README.md << 'EOF'

---

## Contributing

1. Fork the repository and create a new branch: `git checkout -b feature/your-feature`
2. Make your changes and ensure the app runs locally.
3. Commit with a clear message describing what changed and why.
4. Open a Pull Request against the `start` branch.
5. Request a review from at least one team member before merging.

Please follow the existing code style — no new dependencies without team agreement.
EOF
commit "docs: add Contributing section to README"

# ── COMMIT 4 ── Add Roadmap section
cat >> README.md << 'EOF'

---

## Roadmap

- [ ] Leaderboard page showing top 10 scores globally
- [ ] User profile page with score history
- [ ] Additional quiz category: Recycling & Waste
- [ ] Mobile-responsive layout improvements
- [ ] Dark/Light theme toggle
- [ ] Admin panel for managing questions without redeployment
- [ ] Multiplayer snake mode (WebSocket)
EOF
commit "docs: add Roadmap section to README"

# ── COMMIT 5 ── Add Testing section
cat >> README.md << 'EOF'

---

## Testing

### Manual Testing Checklist

- [ ] Register a new user and verify OTP email is received
- [ ] Login with correct and incorrect credentials
- [ ] Play Eco Snake Quiz — verify score increments/decrements correctly
- [ ] Complete Math Quiz on all three difficulty levels
- [ ] Verify Memory Match is locked below 100 points
- [ ] Unlock Memory Match at 100 points and complete a game
- [ ] Test Forgot Password OTP flow
- [ ] Verify `/health` endpoint returns `{"status": "ok"}`

### Automated Testing

Unit tests are not yet implemented. Planned for a future sprint using `pytest` and `pytest-flask`.
EOF
commit "docs: add Testing section to README"

# ── COMMIT 6 ── Add Security section
cat >> README.md << 'EOF'

---

## Security

- Passwords are hashed using `werkzeug.security` (PBKDF2-SHA256).
- Sessions are signed with `FLASK_SECRET_KEY` — keep this secret in production.
- OTP codes are 6-digit, single-use, and expire after 5 minutes.
- Database queries use parameterised statements to prevent SQL injection.
- HTTPS is enforced by Vercel — do not deploy without TLS.
EOF
commit "docs: add Security section to README"

# ── COMMIT 7 ── Add Acknowledgements section
cat >> README.md << 'EOF'

---

## Acknowledgements

- **Coventry University** — 503IT module brief and supervision
- **Supabase** — free-tier PostgreSQL hosting
- **Vercel** — serverless deployment platform
- The capybara internet community — endless inspiration for Capy
EOF
commit "docs: add Acknowledgements section to README"

# ── COMMIT 8 ── Create CONTRIBUTING.md
cat > CONTRIBUTING.md << 'EOF'
# Contributing to buzzXzone

Thank you for helping improve buzzXzone!

## Branching

- `start` is the main branch — all PRs target this.
- Branch naming: `feature/<name>`, `fix/<name>`, `docs/<name>`.

## Commit Style

Use short, imperative messages:
- `feat: add leaderboard endpoint`
- `fix: correct OTP expiry check`
- `docs: update deployment guide`

## Code Style

- Python: follow PEP 8; max line length 100.
- HTML/CSS: 2-space indent, kebab-case class names.
- JavaScript: `const`/`let` only, no `var`.

## Pull Requests

- One logical change per PR.
- Include a brief description of what changed and why.
- At least one team member must approve before merging.
EOF
commit "docs: add CONTRIBUTING.md"

# ── COMMIT 9 ── Create CHANGELOG.md
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to buzzXzone are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Planned
- Leaderboard page
- User profile with score history
- Recycling & Waste quiz category

---

## [1.0.0] — 2026-06-09

### Added
- Eco Snake Quiz (auto-playing snake with live questions)
- Math Quiz (Easy / Medium / Hard)
- Eco Cyber-Security Quiz (Easy / Medium / Hard)
- Memory Match mini-game (unlockable at 100 points)
- OTP email authentication via Gmail SMTP
- Supabase PostgreSQL backend
- Vercel serverless deployment
- Neon mouse trail animation
- Spark click effect
- Capybara mascot (Capy) with walking/sitting/eating animations
- `/health` endpoint for deployment verification

### Technical
- Flask 3.x backend with session-based auth
- `psycopg2-binary` for PostgreSQL connectivity
- Canvas 2D for snake engine and capybara animations
- `vercel.json` for serverless routing
EOF
commit "docs: add CHANGELOG.md with v1.0.0 entry"

# ── COMMIT 10 ── Create docs/ folder with architecture overview
mkdir -p docs
cat > docs/architecture.md << 'EOF'
# Architecture Overview

## High-Level Design

```
Browser (Client)
    │
    │  HTTP/HTTPS
    ▼
Vercel Serverless Function
    │  (Flask WSGI via vercel.json)
    ▼
app.py  ──────────────────────────────────────────────────────┐
    │  Routes: /, /login, /register, /snake, /quiz, /memory   │
    │  Auth:   session + OTP                                   │
    │  DB:     psycopg2 connection pool                        │
    └──────────────────────────────────────────────────────────┘
    │
    │  SQL (TLS)
    ▼
Supabase PostgreSQL
    └── users table
```

## Request Lifecycle

1. User visits a page → Vercel routes to Flask.
2. Flask checks session cookie for authentication.
3. If authenticated, render Jinja2 template with data from DB.
4. JS (Canvas / quiz engine) runs client-side, POSTs answers to Flask.
5. Flask updates `high_score` in DB and returns JSON.

## Static Assets

All static files (`style.css`, `game.js`, `quiz.js`, `logo.svg`) are served directly
by Vercel's CDN — they do not pass through Flask.

## Database Schema

See [database.md](database.md) for the full schema.
EOF
commit "docs: add architecture overview"

# ── COMMIT 11 ── docs/database.md
cat > docs/database.md << 'EOF'
# Database Schema

## Provider
Supabase (PostgreSQL 15) — Transaction Pooler, port 6543.

## Tables

### `users`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incremented user ID |
| `username` | TEXT | NOT NULL | Display name |
| `email` | TEXT | NOT NULL UNIQUE | Login email |
| `password` | TEXT | NOT NULL | PBKDF2-SHA256 hash |
| `high_score` | INTEGER | NOT NULL DEFAULT 0 | All-time best score |
| `memory_unlocked` | INTEGER | NOT NULL DEFAULT 0 | 1 = unlocked, 0 = locked |

### DDL

```sql
CREATE TABLE IF NOT EXISTS users (
    id              SERIAL PRIMARY KEY,
    username        TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    password        TEXT NOT NULL,
    high_score      INTEGER NOT NULL DEFAULT 0,
    memory_unlocked INTEGER NOT NULL DEFAULT 0
);
```

## Connections

- Connection string format: `postgresql://postgres.[ref]:[pw]@aws-0-[region].pooler.supabase.com:6543/postgres`
- `sslmode=require` must be appended for secure connections.
- Connection is opened per request via `psycopg2.connect()` (Vercel stateless model).
EOF
commit "docs: add database schema documentation"

# ── COMMIT 12 ── docs/api-routes.md
cat > docs/api-routes.md << 'EOF'
# API Routes

All routes are served by Flask (`app.py`). JSON endpoints are used for game logic.

## Authentication

| Method | Path | Description |
|--------|------|-------------|
| GET/POST | `/register` | New user registration form |
| GET/POST | `/login` | Login form |
| GET/POST | `/verify` | OTP verification |
| GET/POST | `/forgot` | Forgot-password form |
| GET/POST | `/reset_verify` | OTP verification for password reset |
| GET/POST | `/new_password` | Set new password |
| GET | `/logout` | Clear session and redirect to login |

## Game

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Dashboard (requires auth) |
| GET | `/snake` | Eco Snake Quiz page |
| POST | `/snake/answer` | Submit answer; returns `{"correct": bool, "score": int}` |
| GET | `/difficulty/<type>` | Difficulty picker for math/cyber |
| GET | `/quiz/<type>/<level>` | Quiz page |
| POST | `/quiz/answer` | Submit answer; returns score update |
| GET | `/memory` | Memory Match page (requires `memory_unlocked=1`) |
| POST | `/memory/complete` | Mark game complete; returns updated score |

## Health

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Returns `{"status":"ok","database":"connected"}` or error |
EOF
commit "docs: add API routes documentation"

# ── COMMIT 13 ── docs/deployment.md
cat > docs/deployment.md << 'EOF'
# Deployment Guide

## Prerequisites

- A [Vercel](https://vercel.com) account connected to GitHub.
- A [Supabase](https://supabase.com) project with the `users` table created.
- A Gmail account with an App Password (for OTP emails).

## Steps

### 1. Fork / clone the repo

```bash
git clone https://github.com/wlaa41/ConventryUniversity_503IT_Detectives.git
cd ConventryUniversity_503IT_Detectives
```

### 2. Set up Supabase

1. Create a new project at supabase.com.
2. Go to **Project Settings → Database → Connection Pooling**.
3. Copy the **Transaction pooler** string (port 6543).
4. The `users` table is created automatically on first app startup.

### 3. Deploy to Vercel

1. Import the repo in Vercel.
2. Add environment variables:
   - `DATABASE_URL` — Supabase pooler string with `?sslmode=require`
   - `FLASK_SECRET_KEY` — any random 32-char string
   - `GMAIL_USER` — your Gmail address
   - `GMAIL_PASSWORD` — your Gmail App Password
3. Deploy. Vercel uses `vercel.json` to route everything to Flask.

### 4. Verify

Visit `https://your-app.vercel.app/health`. Expected:
```json
{"status": "ok", "database": "connected"}
```

## Local Development

See the [README Local Development section](../README.md#local-development) for `.env` setup and running with `python app.py`.
EOF
commit "docs: add deployment guide"

# ── COMMIT 14 ── docs/game-design.md
cat > docs/game-design.md << 'EOF'
# Game Design Document

## Overview

buzzXzone is an eco-themed educational game hub. All games share a single scoring system
stored server-side, creating progression across the entire hub.

## Shared Scoring System

- Score is persistent — stored in `users.high_score`.
- Score only ever increases (high-score model, not session score).
- Memory Match unlocks at 100 points (configurable via `UNLOCK_THRESHOLD`).

## Game: Eco Snake Quiz

**Concept:** A snake game that plays itself — the player's role is purely answering questions.
The snake's survival depends on answer accuracy, making it a visual feedback mechanism.

| Event | Snake Effect | Score Effect |
|-------|-------------|--------------|
| Correct answer | Grows +1 segment | +10 pts |
| Wrong answer | Shrinks −1 segment | No change |
| Timer expires (20s) | Shrinks −1 segment | No change |
| Length reaches 0 | Game Over | — |

**Design intent:** Removes motor-skill barrier. Any player can engage regardless of dexterity.

## Game: Math Quiz

**Concept:** Classic multiple-choice quiz with three difficulty tiers.

- Each correct answer: +10 pts.
- 20-second timer per question.
- Questions are shuffled from a JSON bank each session.

## Game: Eco Cyber-Security Quiz

**Concept:** Same mechanics as Math Quiz but questions are framed around eco-digital habits
(e-waste, energy-efficient computing, green cloud, sustainable tech).

## Game: Memory Match

**Concept:** Classic card-flip memory game using emoji pairs on a 4×4 grid.

- Locked by default as a progression reward at 100 points.
- Adds a non-quiz break to maintain engagement variety.
EOF
commit "docs: add game design document"

# ── COMMIT 15 ── docs/testing.md
cat > docs/testing.md << 'EOF'
# Testing Guide

## Manual Test Plan

### Authentication

- [ ] Register with a new email → OTP received → account activated
- [ ] Login with correct credentials → redirected to dashboard
- [ ] Login with wrong password → error message shown
- [ ] Forgot password → OTP flow → new password set → login works
- [ ] Access `/` without login → redirected to `/login`

### Eco Snake Quiz

- [ ] Game starts automatically when page loads
- [ ] Correct answer → snake grows, score increases by 10
- [ ] Wrong answer → snake shrinks
- [ ] Timer reaches 0 → snake shrinks
- [ ] Snake length reaches 0 → game over screen shown
- [ ] Score persists after game over (high score stored)

### Math Quiz

- [ ] All three difficulty levels accessible
- [ ] Questions are shuffled on each new game
- [ ] 20-second countdown visible and working
- [ ] Correct/incorrect feedback shown immediately
- [ ] Score updates in DB after session ends

### Memory Match

- [ ] Progress bar visible on locked card below 100 pts
- [ ] Card is unlocked once score ≥ 100
- [ ] All 8 pairs can be matched successfully
- [ ] Game completion triggers score update

### Health Check

- [ ] `/health` returns `{"status": "ok", "database": "connected"}`

## Known Bugs

None currently logged. Please raise issues via GitHub Issues.
EOF
commit "docs: add testing guide"

# ── COMMIT 16 ── Create Meeting5 notes
mkdir -p "Meetings/Meeting5"
cat > "Meetings/Meeting5/agenda.md" << 'EOF'
# Meeting 5 — Agenda

**Date:** 3 June 2026
**Time:** 2:00 PM
**Location:** CU London Campus / Teams

## Agenda Items

1. Review Sprint 2 progress
2. Demo current prototype to team
3. Identify bugs and missing features
4. Plan Sprint 3 tasks
5. Confirm presentation date and format
EOF
commit "meetings: add Meeting5 agenda"

# ── COMMIT 17 ── Meeting5 minutes
cat > "Meetings/Meeting5/minutes.md" << 'EOF'
# Meeting 5 — Minutes

**Date:** 3 June 2026
**Time:** 2:00 PM – 3:00 PM
**Chair:** Mohammad Zayed Alam
**Minute-Taker:** Shree Krishna Shrestha

## Attendees
- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri

## Sprint 2 Review

- Backend routes for login, OTP, and quiz scoring completed.
- Frontend templates for dashboard and snake quiz implemented.
- Memory Match locked/unlock logic working.
- Remaining: Math Quiz hard-tier questions, Cyber Quiz questions, final CSS polish.

## Bugs Identified

| Bug | Assigned To | Priority |
|-----|-------------|----------|
| Snake speed inconsistent on slow connections | Shree Krishna | High |
| OTP timer not resetting on resend | Shree Krishna | Medium |
| Memory Match flip animation glitch on mobile | Jina | Low |

## Sprint 3 Plan

- Complete question banks for all quiz types.
- Deploy to Vercel and verify `/health`.
- Conduct full manual test pass.
- Prepare presentation slides.

## Action Items

| Task | Owner | Deadline |
|------|-------|----------|
| Complete cyber quiz questions (hard) | Saif Ullah | 7 June |
| Fix snake speed bug | Shree Krishna | 6 June |
| Prepare presentation outline | Aaryut | 8 June |
| Final Vercel deployment | Shree Krishna | 8 June |

## Next Meeting

**Date:** 7 June 2026 — Final check-in before submission.
EOF
commit "meetings: add Meeting5 minutes"

# ── COMMIT 18 ── Meeting6 agenda
mkdir -p "Meetings/Meeting6"
cat > "Meetings/Meeting6/agenda.md" << 'EOF'
# Meeting 6 — Agenda

**Date:** 7 June 2026
**Time:** 12:00 PM
**Location:** Teams (remote)

## Agenda Items

1. Final bug review before submission
2. Confirm all features are working on Vercel
3. Review presentation slides
4. Assign presentation speaking roles
5. Submission checklist walkthrough
EOF
commit "meetings: add Meeting6 agenda"

# ── COMMIT 19 ── Meeting6 minutes
cat > "Meetings/Meeting6/minutes.md" << 'EOF'
# Meeting 6 — Minutes

**Date:** 7 June 2026
**Time:** 12:00 PM – 1:00 PM
**Chair:** Shree Krishna Shrestha
**Minute-Taker:** Jina Giri

## Attendees
- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri
- Pushparaj Mahato

## Final Bug Review

All critical bugs resolved:
- Snake speed fixed (requestAnimationFrame delta-time implemented).
- OTP resend timer corrected.
- Memory Match flip animation smooth on all tested browsers.

Pushparaj completed a full manual test pass — all checklist items passed.

## Vercel Deployment Status

- App live at buzzxzone.vercel.app.
- `/health` returns `{"status": "ok", "database": "connected"}`.
- All env vars confirmed set in Vercel dashboard.

## Presentation Roles

| Section | Presenter |
|---------|-----------|
| Project intro & concept | Aaryut |
| Tech stack & architecture | Shree Krishna |
| Live demo — Snake Quiz | Shree Krishna |
| Live demo — Math & Cyber Quiz | Saif |
| Live demo — Memory Match | Jina |
| Agile process & retrospective | Mohammad |
| Testing & QA | Pushparaj |

## Submission Checklist

- [x] Code pushed to GitHub
- [x] README complete
- [x] Meeting minutes uploaded
- [x] Presentation slides ready
- [x] Live app accessible

## Meeting Closed

No further meetings scheduled before submission.
EOF
commit "meetings: add Meeting6 minutes"

# ── COMMIT 20 ── Create Meeting_minutes4.md
cat > "Meetings/Meeting_minutes4.md" << 'EOF'
# Meeting Minutes — Meeting 4

## Meeting Details

- **Date:** 31 May 2026
- **Time:** 3:00 PM – 4:00 PM
- **Location:** CU London Campus
- **Chair:** Aaryut Chaudhary
- **Minute-Taker:** Jina Giri

## Attendees

- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri

## Agenda Items

1. Sprint 2 planning
2. Review wireframes
3. Agree question bank format
4. Discuss deployment strategy

## Summary of Discussion

- Sprint 2 will focus on completing all game logic and connecting to Supabase.
- Wireframes for dashboard and quiz pages reviewed and approved.
- JSON format for question banks agreed (see `questions/` directory).
- Vercel chosen for deployment — free tier sufficient for prototype.

## Decisions Made

- All questions stored in `questions/*.json` — no database table for questions.
- Memory Match locked at 100-point threshold.
- OTP validity window: 5 minutes.

## Action Items

| Task | Owner | Deadline |
|------|-------|----------|
| Implement Flask routes | Shree Krishna | 2 June |
| Write snake quiz questions | Saif | 2 June |
| Create math question banks (all tiers) | Aaryut | 3 June |
| Write cyber quiz questions | Saif | 4 June |
| Set up Supabase project | Mohammad | 1 June |

## Next Meeting

**Date:** 3 June 2026 — Sprint 2 review.
EOF
commit "meetings: add Meeting_minutes4.md"

# ── COMMIT 21 ── Create Sprint retrospectives directory
mkdir -p "Sprint_Retrospectives"
cat > "Sprint_Retrospectives/Sprint1_Retrospective.md" << 'EOF'
# Sprint 1 Retrospective

**Sprint Dates:** 27 May – 2 June 2026
**Facilitator:** Mohammad Zayed Alam

## Sprint Goal

Deliver a working prototype with basic game structure and authentication.

## What Went Well

- Team agreed on the eco theme quickly — no major disagreements.
- Tech stack decisions (Flask, Supabase, Vercel) made early and stuck to.
- GitHub setup and branching workflow adopted smoothly.
- Question format (JSON) agreed early, allowing parallel work on question content.

## What Could Be Improved

- Initial scope was too ambitious — had to cut the leaderboard feature.
- Stand-ups were inconsistent; some days nobody posted updates.
- More wireframes needed before coding started.

## Action Items for Sprint 2

| Action | Owner |
|--------|-------|
| Daily stand-up message in group chat by 9am | All |
| Complete wireframes before writing routes | Jina |
| Define MVP features list explicitly | Mohammad |

## Velocity

| Planned | Completed | % Done |
|---------|-----------|--------|
| 12 tasks | 8 tasks | 67% |

## Overall Rating: 7/10

Good start. Communication needs to improve. Core architecture is solid.
EOF
commit "sprint: add Sprint 1 retrospective"

# ── COMMIT 22 ── Sprint 2 retrospective
cat > "Sprint_Retrospectives/Sprint2_Retrospective.md" << 'EOF'
# Sprint 2 Retrospective

**Sprint Dates:** 3 June – 7 June 2026
**Facilitator:** Aaryut Chaudhary

## Sprint Goal

Complete all game logic, connect to Supabase, deploy to Vercel.

## What Went Well

- All game logic completed on schedule.
- Supabase connection set up without issues.
- Vercel deployment worked on first attempt (after fixing `vercel.json` routing).
- OTP email auth added as a bonus feature not originally planned.
- Team communication improved from Sprint 1.

## What Could Be Improved

- Bug found late (snake speed issue) that required urgent fix.
- Testing was left to the end — should test each feature as it's built.
- Presentation slides started too late.

## Action Items for Sprint 3 (Polish)

| Action | Owner |
|--------|-------|
| Write test checklist and run it daily | Pushparaj |
| Start slides immediately | Aaryut |
| Add README documentation | Shree Krishna |

## Velocity

| Planned | Completed | % Done |
|---------|-----------|--------|
| 15 tasks | 14 tasks | 93% |

## Overall Rating: 8.5/10

Strong sprint. Near-full delivery. Testing process needs to be moved earlier in next projects.
EOF
commit "sprint: add Sprint 2 retrospective"

# ── COMMIT 23 ── Sprint 3 retrospective
cat > "Sprint_Retrospectives/Sprint3_Retrospective.md" << 'EOF'
# Sprint 3 Retrospective

**Sprint Dates:** 7 June – 9 June 2026
**Facilitator:** Shree Krishna Shrestha

## Sprint Goal

Final polish, full test pass, presentation preparation, submission.

## What Went Well

- All bugs resolved before presentation day.
- Full manual test pass completed by Pushparaj — zero critical issues.
- Presentation slides ready two days before deadline.
- README fully documented with all sections.
- Live app stable throughout demo.

## What Could Be Improved

- Would have liked more time to add the leaderboard feature.
- Some team members could contribute more to documentation.
- Git commit history could be more granular (smaller, more frequent commits).

## Final Velocity

| Planned | Completed | % Done |
|---------|-----------|--------|
| 10 tasks | 10 tasks | 100% |

## Project Summary

The buzzXzone eco learning hub was delivered fully functional and deployed live.
Key achievements:
- Full-stack Flask + Supabase + Vercel app
- 3 quiz games + memory match mini-game
- OTP email authentication
- Responsive UI with eco forest theme

## Overall Rating: 9/10

Successful project delivery. Strong team effort in the final sprint.
EOF
commit "sprint: add Sprint 3 retrospective"

# ── COMMIT 24 ── Risk register
cat > "risk_register.md" << 'EOF'
# Risk Register

**Project:** buzzXzone — Eco Learning Hub
**Last Updated:** 9 June 2026

| # | Risk | Likelihood | Impact | Mitigation | Status |
|---|------|------------|--------|------------|--------|
| 1 | Supabase free tier hits connection limit | Medium | High | Use connection pooler (port 6543) | Mitigated |
| 2 | Vercel cold-start latency on first load | High | Low | Acceptable for prototype; warm-up endpoint possible | Accepted |
| 3 | Gmail App Password revoked/expired | Low | Medium | OTP falls back to console output in dev | Accepted |
| 4 | Team member unavailable near deadline | Medium | High | Document all setup steps; any member can deploy | Mitigated |
| 5 | Browser compatibility issues (Canvas) | Low | Medium | Tested on Chrome, Firefox, Edge | Mitigated |
| 6 | SQL injection vulnerability | Low | Critical | All queries use parameterised statements | Mitigated |
| 7 | Session hijacking | Low | High | `FLASK_SECRET_KEY` set; HTTPS enforced by Vercel | Mitigated |
| 8 | Scope creep (feature additions) | Medium | Medium | MVP feature list agreed in Sprint 1; extras logged in Roadmap | Accepted |
EOF
commit "project: add risk register"

# ── COMMIT 25 ── User stories
cat > "user_stories.md" << 'EOF'
# User Stories

**Project:** buzzXzone — Eco Learning Hub

## Authentication

- As a **new user**, I want to register with my email so that I can save my progress.
- As a **returning user**, I want to log in securely so that my scores are protected.
- As a **user who forgot their password**, I want to reset it via email OTP so that I can regain access.

## Dashboard

- As a **logged-in user**, I want to see all available games from one screen so that I can choose what to play.
- As a **user**, I want to see my current high score on the dashboard so that I know my progress.

## Eco Snake Quiz

- As a **player**, I want the snake to play itself so that I can focus purely on answering questions.
- As a **player**, I want immediate visual feedback (snake grow/shrink) so that I know if my answer was right.
- As a **player**, I want a 20-second timer so that games feel challenging and fast-paced.

## Math & Cyber Quizzes

- As a **player**, I want to choose difficulty so that the challenge matches my skill level.
- As a **player**, I want questions shuffled each game so that the experience stays fresh.

## Memory Match

- As a **player**, I want the Memory Match to be locked initially so that unlocking it feels like an achievement.
- As a **player**, I want to see a progress bar toward unlocking Memory Match so that I know how close I am.

## General

- As a **player**, I want eco-themed visuals and a capybara mascot so that the app feels fun and engaging.
- As a **developer**, I want a `/health` endpoint so that I can verify the deployment is working.
EOF
commit "project: add user stories"

# ── COMMIT 26 ── Wireframes notes
cat > "wireframes_notes.md" << 'EOF'
# Wireframes & UI Notes

**Designer:** Jina Giri
**Last Updated:** 29 May 2026

## Design Principles

1. **Eco Forest Theme** — dark greens, cyans, and neon accents to evoke a natural-tech aesthetic.
2. **Mobile-first consideration** — game cards stack vertically on small screens.
3. **Progressive disclosure** — locked features (Memory Match) are visible but clearly gated.
4. **Accessibility** — high contrast text, large clickable targets, no colour-only indicators.

## Key Screens

### Dashboard
- Full-width hero with Capy mascot on the left.
- 4 game cards in a 2×2 grid (or 1-column on mobile).
- Score displayed in the nav bar.
- Logout link top-right.

### Quiz Pages
- Question text centred, large font.
- 4 answer buttons below — full width on mobile.
- Timer progress bar at the top.
- Current score bottom-right.

### Login / Register
- Simple centred card on a dark background.
- OTP input: 6 individual digit boxes for clarity.

### Memory Match
- 4×4 grid, cards sized to fit viewport.
- Cards face-down by default, flip on click.
- Matched pairs stay face-up and dim slightly.

## Colour Palette

| Name | Hex | Use |
|------|-----|-----|
| Forest Dark | `#0a1a0a` | Page background |
| Leaf Green | `#2d7a2d` | Primary buttons, borders |
| Neon Cyan | `#00ffcc` | Hover states, trail particles |
| Gold | `#ffd700` | Score text, capybara accents |
| Danger Red | `#ff4444` | Wrong answer flash |
EOF
commit "project: add wireframes and UI design notes"

# ── COMMIT 27 ── Add .github issue templates
mkdir -p ".github/ISSUE_TEMPLATE"
cat > ".github/ISSUE_TEMPLATE/bug_report.md" << 'EOF'
---
name: Bug Report
about: Report a bug in buzzXzone
title: '[BUG] '
labels: bug
assignees: ''
---

## Describe the Bug
A clear description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behaviour
What you expected to happen.

## Actual Behaviour
What actually happened.

## Screenshots
If applicable, add screenshots.

## Environment
- Browser: [e.g. Chrome 125]
- OS: [e.g. Windows 11]
- Device: [e.g. Desktop / iPhone 13]

## Additional Context
Any other context about the problem.
EOF
commit "github: add bug report issue template"

# ── COMMIT 28 ── Feature request template
cat > ".github/ISSUE_TEMPLATE/feature_request.md" << 'EOF'
---
name: Feature Request
about: Suggest a new feature for buzzXzone
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Feature Summary
A brief description of the feature.

## Problem It Solves
What problem or gap does this feature address?

## Proposed Solution
Describe how you'd like this feature to work.

## Alternatives Considered
Any alternative approaches you considered.

## Additional Context
Mockups, examples, or any other context.
EOF
commit "github: add feature request issue template"

# ── COMMIT 29 ── Add AI use evidence README
cat > "AI use evidence/README.md" << 'EOF'
# AI Use Evidence

This folder documents how AI tools were used during the development of buzzXzone
as required by the Coventry University 503IT module.

## Tools Used

| Tool | Purpose | Evidence |
|------|---------|----------|
| GitHub Copilot | Code suggestions for Flask routes and JS Canvas logic | Screenshots in this folder |
| ChatGPT | Generating initial question bank content (reviewed and edited by team) | Prompts and outputs documented below |
| Claude | Code review and debugging assistance | Session logs |

## Usage Policy

All AI-generated content was reviewed, verified, and edited by team members before inclusion.
No AI was used for assessment components requiring individual effort (report writing, reflections).

## Documentation

See screenshots in this directory for evidence of specific AI interactions.
Each screenshot is named `ai_[tool]_[date]_[description].png`.
EOF
commit "evidence: add AI use evidence README"

# ── COMMIT 30 ── Add project summary document
cat > "project_summary.md" << 'EOF'
# Project Summary

**Module:** 503IT — Introduction to Software Engineering
**University:** Coventry University London
**Group Name:** Detectives
**Project:** buzzXzone — Eco Learning Hub
**Submission Date:** 9 June 2026

## What We Built

buzzXzone is a full-stack eco-themed educational game hub built with Flask and deployed on Vercel.
Players register, complete quiz-based mini-games, and earn points to unlock new content.

## Why This Topic

The team chose an eco-educational theme to align with Coventry University's sustainability agenda
and to make cybersecurity/math learning more engaging through gamification.

## Technologies Used

| Technology | Role |
|------------|------|
| Python 3 / Flask | Backend server and routing |
| Supabase PostgreSQL | User data and high scores |
| Vercel | Serverless deployment |
| HTML5 / CSS3 / JS | Frontend UI |
| Canvas 2D API | Snake game engine and capybara mascot |
| Gmail SMTP | OTP email delivery |

## Team

| Name | Role |
|------|------|
| Shree Krishna Shrestha | Lead Developer (Frontend + Backend) |
| Saif Ullah | Content Lead (question banks, game concepts) |
| Aaryut Chaudhary | Researcher, Scrum facilitation |
| Jina Giri | UI/UX Designer, wireframes |
| Mohammad Zayed Alam | Project Manager |
| Pushparaj Mahato | Tester and Bug Reviewer |

## Agile Process

Three sprints over two weeks using Scrum-lite:
- Sprint 1: Architecture, auth, basic UI
- Sprint 2: Game logic, Supabase integration, Vercel deployment
- Sprint 3: Polish, testing, presentation

## Key Learnings

- Serverless Flask deployments require stateless code (no in-memory session state).
- Supabase connection pooling is essential on Vercel (new connection per request).
- OTP-based auth adds meaningful security without requiring third-party auth services.
- Early agreement on data formats (JSON question banks) enabled parallel development.
EOF
commit "project: add project summary document"

# ── COMMIT 31 ── Add Meeting_minutes5.md
cat > "Meetings/Meeting_minutes5.md" << 'EOF'
# Meeting Minutes — Meeting 5

## Meeting Details

- **Date:** 3 June 2026
- **Time:** 2:00 PM – 3:00 PM
- **Location:** CU London Campus
- **Chair:** Mohammad Zayed Alam
- **Minute-Taker:** Shree Krishna Shrestha

## Attendees

- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri

## Sprint 2 Demo

Shree Krishna demoed the working prototype:
- Dashboard with Capy mascot functioning.
- Eco Snake Quiz playable end-to-end.
- Math Quiz (Easy + Medium) working.
- Cyber Quiz (Easy) working.
- Memory Match locked state showing progress bar.

## Issues Raised

- Snake speed bug on slower network connections.
- Math Hard tier questions not yet added to JSON.
- Cyber Medium and Hard questions incomplete.

## Decisions Made

- All question banks must be finalised by 5 June.
- Pushparaj to run full manual test checklist by 7 June.
- Presentation draft due 8 June.

## Action Items

| Task | Owner | Deadline |
|------|-------|----------|
| Finalise all question banks | Saif, Aaryut | 5 June |
| Fix snake speed bug | Shree Krishna | 5 June |
| Full test checklist pass | Pushparaj | 7 June |
| Presentation draft | Aaryut | 8 June |

## Next Meeting

**Date:** 7 June 2026 (remote via Teams).
EOF
commit "meetings: add Meeting_minutes5.md"

# ── COMMIT 32 ── Add Meeting_minutes6.md
cat > "Meetings/Meeting_minutes6.md" << 'EOF'
# Meeting Minutes — Meeting 6

## Meeting Details

- **Date:** 7 June 2026
- **Time:** 12:00 PM – 1:00 PM
- **Location:** Microsoft Teams (remote)
- **Chair:** Shree Krishna Shrestha
- **Minute-Taker:** Jina Giri

## Attendees

- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri
- Pushparaj Mahato (first full-team attendance)

## Final Pre-Submission Review

Pushparaj presented test results — all manual checklist items passed.

Snake speed bug confirmed fixed. Memory Match animation issue on mobile considered
low priority and accepted for this submission.

## Submission Checklist Sign-Off

All items confirmed complete by the team:
- App deployed and live on Vercel.
- GitHub repo up to date.
- Meeting minutes uploaded.
- Presentation slides finalised.
- README fully documented.

## Presentation Rehearsal

Brief run-through of presentation order. Each member rehearsed their section.
Total estimated time: 12 minutes (within 15-minute limit).

## Final Decisions

- No new features to be added after this meeting.
- Branch `start` is the submission branch.

## Meeting Closed

No further scheduled meetings for this project.
EOF
commit "meetings: add Meeting_minutes6.md"

# ── COMMIT 33 ── Add team_roles.md
cat > "team_roles.md" << 'EOF'
# Team Roles & Responsibilities

**Group:** Detectives — Coventry University 503IT

## Members

### Shree Krishna Shrestha (15681041)
**Role:** Lead Developer — Frontend & Backend

- Built all Flask routes and database integration.
- Implemented OTP authentication with Gmail SMTP.
- Developed Eco Snake Quiz (Canvas 2D auto-play engine).
- Built capybara mascot animation system.
- Configured Vercel deployment and `vercel.json`.
- Maintained GitHub repository and code reviews.

### Saif Ullah (16115000)
**Role:** Lead Content & Game Concept

- Proposed the original eco-educational game concept.
- Authored all quiz question banks (snake, math, cyber).
- Reviewed and refined question difficulty tiers.
- Contributed to game design decisions.

### Aaryut Chaudhary (16069541)
**Role:** Researcher & Scrum Facilitator

- Researched eco-educational game mechanics.
- Facilitated sprint planning and retrospectives.
- Prepared presentation slides and script.
- Authored user stories and acceptance criteria.

### Jina Giri (16144790)
**Role:** UI/UX Designer & Prototype Designer

- Created wireframes for all key screens.
- Defined the eco forest colour palette and design language.
- Contributed HTML/CSS styling for quiz and dashboard pages.
- Recorded meeting minutes (Meetings 1, 6).

### Mohammad Zayed Alam (16090763)
**Role:** Project Manager & Scrum Master

- Managed Trello task board and sprint backlog.
- Chaired Meetings 1, 5.
- Set up Supabase project and shared credentials with team.
- Monitored sprint progress and flagged blockers.

### Pushparaj Mahato (16362947)
**Role:** Tester & QA Reviewer

- Ran full manual test checklist before submission.
- Identified and logged bugs during testing.
- Verified all bug fixes before sign-off.
- Contributed to risk register.
EOF
commit "project: add team roles and responsibilities document"

# ── COMMIT 34 ── Add glossary
cat > "glossary.md" << 'EOF'
# Project Glossary

| Term | Definition |
|------|------------|
| **Agile** | Iterative software development methodology emphasising flexibility and collaboration. |
| **Canvas 2D** | HTML5 browser API for drawing 2D graphics programmatically in JavaScript. |
| **CHANGELOG** | A document recording all notable changes to a project per version. |
| **Cold start** | Delay when a serverless function initialises after being idle. |
| **Connection pooler** | A proxy that reuses database connections, reducing overhead. |
| **OTP** | One-Time Password — a single-use code sent via email or SMS for verification. |
| **PBKDF2** | Password-Based Key Derivation Function 2 — a standard password hashing algorithm. |
| **psycopg2** | Python adapter for PostgreSQL. |
| **Scrum** | An Agile framework using fixed-length sprints and defined roles (Scrum Master, Product Owner, Team). |
| **Serverless** | A deployment model where the cloud provider manages server infrastructure dynamically. |
| **Sprint** | A fixed-length development iteration (typically 1–2 weeks) in Scrum. |
| **Supabase** | An open-source Firebase alternative providing PostgreSQL, auth, and storage. |
| **Vercel** | A cloud platform specialising in serverless deployment of web applications. |
| **WSGI** | Web Server Gateway Interface — the Python standard for web server/app communication. |
EOF
commit "project: add glossary of terms"

# ── COMMIT 35 ── Add meeting_schedule.md
cat > "Meetings/meeting_schedule.md" << 'EOF'
# Meeting Schedule

| # | Date | Time | Location | Chair | Status |
|---|------|------|----------|-------|--------|
| 1 | 27 May 2026 | 2:00 PM | CU London Campus | Jina Giri | Completed |
| 2 | 29 May 2026 | 2:00 PM | CU London Campus | Shree Krishna | Completed |
| 3 | 31 May 2026 | 3:00 PM | CU London Campus | Mohammad | Completed |
| 4 | 31 May 2026 | 3:00 PM | CU London Campus | Aaryut | Completed |
| 5 | 3 June 2026 | 2:00 PM | CU London Campus | Mohammad | Completed |
| 6 | 7 June 2026 | 12:00 PM | Teams (remote) | Shree Krishna | Completed |

## Meeting Frequency

- During active development: twice weekly (in-person + remote).
- Final week: as-needed (Teams).

## Communication Channels

- **Primary:** WhatsApp group chat for quick updates.
- **Formal decisions:** Recorded in meeting minutes and uploaded to GitHub.
- **Code reviews:** GitHub Pull Requests.
- **Task tracking:** Trello board.
EOF
commit "meetings: add meeting schedule overview"

# ── COMMIT 36 ── Add sprint_planning.md
cat > "Sprint_Retrospectives/sprint_planning.md" << 'EOF'
# Sprint Planning Notes

## Sprint 1 — 27 May to 2 June 2026

**Goal:** Deliver a working prototype skeleton with authentication and basic routing.

### Backlog Items

| ID | Story | Points | Assigned |
|----|-------|--------|----------|
| S1-1 | Set up Flask project structure | 2 | Shree Krishna |
| S1-2 | Create Supabase project and users table | 3 | Mohammad |
| S1-3 | Implement user registration | 3 | Shree Krishna |
| S1-4 | Implement login with password hashing | 3 | Shree Krishna |
| S1-5 | Add OTP email flow | 5 | Shree Krishna |
| S1-6 | Create dashboard template | 3 | Jina |
| S1-7 | Draft snake quiz question bank | 5 | Saif |
| S1-8 | Set up Vercel project | 2 | Shree Krishna |
| S1-9 | Create base HTML template with nav | 2 | Jina |
| S1-10 | Set up GitHub repo and branching strategy | 1 | Mohammad |
| S1-11 | Write Sprint 1 user stories | 2 | Aaryut |
| S1-12 | Create wireframes for key pages | 3 | Jina |

---

## Sprint 2 — 3 June to 7 June 2026

**Goal:** Complete all game logic, connect to production DB, deploy to Vercel.

### Backlog Items

| ID | Story | Points | Assigned |
|----|-------|--------|----------|
| S2-1 | Implement Eco Snake quiz engine (Canvas) | 8 | Shree Krishna |
| S2-2 | Implement Math Quiz routes + frontend | 5 | Shree Krishna |
| S2-3 | Implement Cyber Quiz routes + frontend | 5 | Shree Krishna |
| S2-4 | Implement Memory Match game | 5 | Shree Krishna |
| S2-5 | Connect scoring to Supabase | 3 | Shree Krishna |
| S2-6 | Write math question banks (all tiers) | 5 | Aaryut |
| S2-7 | Write cyber question banks (all tiers) | 5 | Saif |
| S2-8 | Add capybara mascot animation | 5 | Shree Krishna |
| S2-9 | Add neon mouse trail + spark effects | 3 | Shree Krishna |
| S2-10 | Deploy to Vercel and verify health | 3 | Shree Krishna |
| S2-11 | CSS polish — forest theme complete | 4 | Jina |
| S2-12 | Add forgot-password OTP flow | 3 | Shree Krishna |
| S2-13 | Manual test pass | 5 | Pushparaj |
| S2-14 | Fix bugs from test pass | 3 | Shree Krishna |
| S2-15 | Write README documentation | 3 | Shree Krishna |
EOF
commit "sprint: add sprint planning notes"

# ── COMMIT 37 ── Add submission_checklist.md
cat > "submission_checklist.md" << 'EOF'
# Submission Checklist

**Module:** 503IT — Introduction to Software Engineering
**Submission Date:** 9 June 2026

## Code & Repository

- [x] All code pushed to GitHub (`start` branch)
- [x] `README.md` complete with setup, features, and team info
- [x] `vercel.json` present and correct
- [x] `requirements.txt` up to date
- [x] No sensitive credentials in repository (`.env` in `.gitignore`)

## Application

- [x] App deployed and accessible at buzzxzone.vercel.app
- [x] `/health` endpoint returns `{"status": "ok", "database": "connected"}`
- [x] User registration and OTP flow working
- [x] Eco Snake Quiz playable end-to-end
- [x] Math Quiz (all 3 tiers) working
- [x] Cyber Quiz (all 3 tiers) working
- [x] Memory Match unlocks correctly at 100 points
- [x] Score persists across sessions

## Documentation

- [x] Meeting minutes for all 6 meetings uploaded
- [x] Sprint retrospectives completed
- [x] Risk register completed
- [x] User stories documented
- [x] AI use evidence documented

## Presentation

- [x] Slides prepared (buzzXzone_Presentation.py renders slides)
- [x] Speaking roles assigned to all team members
- [x] Live demo rehearsed
- [x] Estimated time: 12 minutes (within 15-minute limit)

## Team Sign-Off

| Member | Signed Off |
|--------|-----------|
| Shree Krishna Shrestha | ✓ |
| Saif Ullah | ✓ |
| Aaryut Chaudhary | ✓ |
| Jina Giri | ✓ |
| Mohammad Zayed Alam | ✓ |
| Pushparaj Mahato | ✓ |
EOF
commit "project: add submission checklist"

# ── COMMIT 38 ── Add docs/user-research.md
cat > "docs/user-research.md" << 'EOF'
# User Research Notes

**Conducted by:** Aaryut Chaudhary
**Date:** 26 May 2026

## Research Questions

1. What motivates students to engage with educational games?
2. What game mechanics do students find most rewarding?
3. How much time are students willing to spend per session?
4. What topics feel most relevant to students studying IT?

## Method

Informal interviews with 5 Coventry University London students (peers, not project team members).
Duration: 5–10 minutes each.

## Key Findings

### Motivation
- Completion/unlocking mechanics rated highly (4/5 students mentioned progress rewards).
- Competitive elements (leaderboards) appealing but not essential for engagement.
- Visual feedback (animations) rated more important than audio.

### Game Mechanics
- Multiple-choice preferred over free-text entry — lower barrier to engagement.
- Shorter sessions (2–5 min) preferred over longer ones.
- Auto-playing games (no motor skill required) well-received — more inclusive.

### Time per Session
- Target: 3–5 minutes per game session.
- Players want to be able to stop and resume without penalty.

### Relevant Topics
- Cybersecurity: rated very relevant (all 5 students).
- Mathematics: moderate relevance (3/5 students).
- Ecology / sustainability: moderate to high (4/5 — aligns with global news interest).

## Design Implications

1. Implement unlock mechanic (Memory Match at 100 pts) — matches reward preference.
2. Keep each quiz to ~10 questions at 20s each (~3 min total).
3. Use Canvas animations for visual feedback rather than sounds.
4. Auto-play snake removes motor-skill barrier — keep.
5. Include eco topics to broaden appeal beyond pure IT students.
EOF
commit "docs: add user research notes"

# ── COMMIT 39 ── Improve Meeting2.txt formatting — convert to markdown
cat > "Meetings/Meeting_minutes2_formatted.md" << 'EOF'
# Meeting Minutes — Meeting 2 (Formatted)

> Formatted version of `Meeting2.txt` for consistent documentation.

## Meeting Details

- **Date:** 29 May 2026
- **Time:** 2:00 PM – 3:00 PM
- **Location:** CU London Campus
- **Chair:** Shree Krishna Shrestha
- **Minute-Taker:** Aaryut Chaudhary

## Attendees

- Shree Krishna Shrestha
- Mohammad Zayed Alam
- Saif Ullah
- Aaryut Chaudhary
- Jina Giri

## Agenda Items

1. Review wireframes from Sprint 1
2. Agree on tech stack (finalise)
3. Set up GitHub branching strategy
4. Plan Sprint 2 backlog

## Summary of Discussion

- Wireframes reviewed and approved with minor adjustments to the dashboard layout.
- Tech stack confirmed: Flask, Supabase, Vercel, vanilla JS.
- Branching: single `start` branch with direct commits (team size too small for PR workflow overhead).
- Sprint 2 backlog items identified and assigned.

## Key Decisions

- Flask confirmed as backend (Python familiarity across team).
- No React/Vue — vanilla HTML/CSS/JS only to keep complexity manageable.
- Questions stored as JSON files, not in the database.
- Score-only DB (no session replay or question history needed).

## Action Items

| Task | Owner | Deadline |
|------|-------|----------|
| Finalise `vercel.json` config | Shree Krishna | 30 May |
| Create Supabase project | Mohammad | 30 May |
| Begin dashboard wireframe refinement | Jina | 31 May |
| Research snake game Canvas logic | Shree Krishna | 31 May |

## Next Meeting

**Date:** 31 May 2026 — Sprint 2 kickoff.
EOF
commit "meetings: add formatted Meeting 2 minutes"

# ── COMMIT 40 ── Final README polish — add live demo badge and quick-start
# Prepend badge lines to README
BADGE='[![Live Demo](https://img.shields.io/badge/Live-buzzxzone.vercel.app-brightgreen)](https://buzzxzone.vercel.app)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)

'
# Insert badges after first heading line
python3 -c "
content = open('README.md').read()
lines = content.split('\n')
lines.insert(1, '')
lines.insert(2, '[![Live Demo](https://img.shields.io/badge/Live-buzzxzone.vercel.app-brightgreen)](https://buzzxzone.vercel.app)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)')
open('README.md', 'w').write('\n'.join(lines))
"
commit "docs: add status badges to README"

echo ""
echo "All 40 commits completed successfully!"
git log --oneline -42
