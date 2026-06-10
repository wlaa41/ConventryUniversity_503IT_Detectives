# Week 3 — Activities Completed

## Overview

Week 3 focused on completing all four mini-games, integrating Supabase as the production
database, expanding question banks, and beginning intensive testing.

## Activities

### All Four Mini-Games Implemented

All four games were fully implemented and functional by the end of Week 3:

| Game | Status | Notes |
|------|--------|-------|
| Eco Snake Quiz | ✅ Complete | Auto-play engine, score saving, game over screen |
| Math Quiz | ✅ Complete | Easy, Medium, Hard tiers with hints |
| Eco Cyber-Security Quiz | ✅ Complete | Easy, Medium, Hard tiers |
| Memory Match | ✅ Complete | Locked at < 100 pts, unlocks permanently at threshold |

### Supabase Integration

Supabase PostgreSQL was integrated as the production database backend. The database path
was configured to switch automatically:
- **Local development:** `buzzxzone/cyber.db` (SQLite)
- **Vercel production:** Supabase PostgreSQL via environment variable `DATABASE_URL`

The `users` table structure remained identical in both environments, making the transition seamless.

See evidence: [Supabase_db.png](Supabase_db.png)

### Question Bank Refinement

All question banks were reviewed and updated to ensure educational accuracy and
age-appropriate difficulty. Questions across Easy, Medium, and Hard levels were
verified for content quality and correctness.

See evidence: [Updated_QN_QUIZ.png](Updated_QN_QUIZ.png)

### Testing Phase Begins

Intensive testing was conducted across all four mini-games:
- Quiz accuracy (correct/incorrect marking, score increments)
- Score tracking persistence across sessions
- Memory Match unlock at exactly 100 points
- OTP email delivery and expiry
- Gameplay animations and visual feedback

### Peer Review Activity

The team reviewed another group's project presentation and documented improvement ideas
for buzzXzone's own presentation structure and content delivery.

### 3D Expansion Discussion

A brief discussion on adding 3D game elements (customisable characters, interactive
environments) concluded that the scope was too large for the current timeline.
The idea was logged in the project backlog for a future development cycle.
