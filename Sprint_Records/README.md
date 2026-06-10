# Sprint Records — buzzXzone

This folder documents the technical work completed across each sprint by Shree Krishna Shrestha (15681041).

Each record covers the specific code files implemented, design decisions made, and code snippets
from the actual implementation to show depth of technical contribution.

## Sprint Overview

| Sprint | Dates | Focus | Records |
|--------|-------|-------|---------|
| Sprint 1 | 27–30 May 2026 | Backend setup, authentication, base templates | [Backend Setup](Sprint1_backend_setup.md) · [Frontend Templates](Sprint1_frontend_templates.md) |
| Sprint 2 | 31 May – 3 Jun | Game engines, Capybara mascot, visual effects | [Snake Engine](Sprint2_snake_game_engine.md) · [Quiz Engine](Sprint2_quiz_engine.md) · [Capybara & Dashboard](Sprint2_capybara_mascot.md) · [Memory Match](Sprint2_memory_match.md) · [Neon Trail & CSS](Sprint2_neon_trail_effects.md) |
| Sprint 3 | 3–9 Jun 2026 | Scoring system, APIs, deployment, polish | [Scoring & APIs](Sprint3_scoring_system.md) · [Deployment](Sprint3_deployment.md) · [Polish & UX](Sprint3_polish_improvements.md) |

## Key Technical Achievements

### Backend (`buzzxzone/app.py`)
- Full Flask app with 15+ routes: auth, games, API endpoints, health check
- SQLite database with auto-init and live schema migration
- OTP email authentication with 5-minute expiry (Gmail SMTP)
- Score persistence with monotonically non-decreasing high score
- Memory Match unlock logic tied to score threshold
- Session security: HttpOnly, SameSite, Secure cookie flags

### Frontend (`buzzxzone/static/`, `buzzxzone/templates/`)
- Auto-playing snake game engine built with Canvas 2D (`game.js`) — 356 lines
- Shared quiz engine with tutorial modal and 2-attempt system (`quiz.js`) — 334 lines
- 11 Jinja2 HTML templates (login, register, OTP, dashboard, games)
- Neon mouse trail + spark click effect (Canvas 2D, no libraries)
- Capybara mascot with walking/sitting/eating/waving animations
- Eco forest theme CSS with hover glows, shake animations, 3D card flips

### Question Banks (`buzzxzone/questions/`)
- 7 JSON question banks: snake (25), math ×3 (15–20 each), cyber ×3 (15–20 each)
- Math questions include worked solution hints
- All questions reviewed for accuracy and eco-educational relevance

### Deployment (`buzzxzone/vercel.json`, environment config)
- Vercel serverless configuration with static asset CDN routing
- Security response headers (X-Content-Type-Options, X-Frame-Options)
- Environment variable pattern for local vs. production database path

## Lines of Code Summary

| File | Lines | Purpose |
|------|-------|---------|
| `app.py` | ~430 | Flask routes, DB, auth, scoring |
| `static/game.js` | ~370 | Canvas snake engine |
| `static/quiz.js` | ~350 | Quiz engine with tutorial |
| `static/style.css` | ~600+ | Full eco-forest theme |
| `templates/*.html` | ~800+ | 11 Jinja2 page templates |
