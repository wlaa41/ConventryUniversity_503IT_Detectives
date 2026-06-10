# Week 4 — Activities Completed

## Overview

Week 4 was the final sprint: all features completed, bugs resolved, Vercel deployment
verified, presentation delivered, and the project submitted.

## Activities

### Bug Resolution

All bugs identified during Week 3 testing were resolved:

| Bug | Fix Applied |
|-----|-------------|
| Snake speed inconsistency on slow connections | Rewrote movement loop using delta-time instead of fixed interval |
| OTP resend timer not resetting | Corrected `session["otp_expiry"]` reset logic on resend |
| Memory Match flip glitch on mobile | Accepted as low-priority; CSS `will-change: transform` applied as partial fix |

See evidence: [Internal_ERROR_FIXED.png](Internal_ERROR_FIXED.png) · [psycopg2.operationalERROR_FIXED.png](psycopg2.operationalERROR_FIXED.png)

### Vercel Deployment Finalised

The application was fully deployed and verified on Vercel:

- Environment variables set: `DATABASE_URL`, `FLASK_SECRET_KEY`, `GMAIL_USER`, `GMAIL_PASSWORD`
- `/health` endpoint confirmed: `{"status": "ok", "database": "connected", "version": "1.0.0"}`
- Static assets routing confirmed (CSS, JS, SVG served via CDN)

See evidence: [VERCEL_ENVIRONMENTAL_SETUP.png](VERCEL_ENVIRONMENTAL_SETUP.png) · [VERCEL_STATUS_ONLINE_HEALTHY.png](VERCEL_STATUS_ONLINE_HEALTHY.png) · [VERCEL_USER_CREDENTIALS.png](VERCEL_USER_CREDENTIALS.png)

### Login and Registration UI Verified

Both the login and registration pages were tested for correct form validation,
error message display, and OTP email delivery in the production environment.

See evidence: [Login_interface.png](Login_interface.png) · [Register_Interface.png](Register_Interface.png) · [Verification.png](Verification.png)

### Trello Final Update

All Trello tasks were marked as complete with descriptions, evidence screenshots, and
final status updates. The board was shared as evidence of Agile task management throughout
the project.

See evidence: [Trello_Board.png](Trello_Board.png)

### Presentation Delivery

The team presented buzzXzone to the class. Each member presented their assigned section.
The live demo covered all four mini-games. The presentation ran approximately 12 minutes —
within the 15-minute limit. Feedback from the audience and tutor was positive.

### Audio Features Added

Audio feedback (correct/incorrect answer sounds) and background ambient music were added
to improve the game experience, particularly for the target age group (6–12 years).

### Final README and Documentation

The README was completed with all sections: Features, Tech Stack, Project Structure,
Local Development, Vercel Deployment, Games, Question Format, Security, and Team Members.
