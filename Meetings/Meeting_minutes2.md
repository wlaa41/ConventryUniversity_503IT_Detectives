# Meeting Minutes — Meeting 2

**Project:** buzzXzone — Eco Learning Quiz Hub
**Date:** 29 May 2026
**Time:** 2:00 PM – 3:00 PM
**Location:** Coventry University London Campus
**Chair:** Shree Krishna Shrestha
**Minute-Taker:** Aaryut Chaudhary

---

## Attendees

- Shree Krishna Shrestha
- Jina Giri
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

---

## Objectives

1. Review wireframes from Sprint 1
2. Finalise tech stack
3. Agree GitHub branching strategy
4. Plan Sprint 2 backlog
5. Agree question bank format

---

## Discussion

Jina presented wireframes for the dashboard, quiz pages, and difficulty selector.
The team approved the designs with minor improvements to navigation flow.

**Tech stack confirmed:**
- Backend: Python 3 / Flask
- Database: SQLite (local) / Supabase PostgreSQL (production)
- Frontend: Vanilla HTML, CSS, Vanilla JavaScript
- Deployment: Vercel (free tier)
- Auth: Session + 6-digit OTP via Gmail SMTP

No React or Vue — the scope does not justify a frontend framework.
Questions will be stored as JSON files, not in the database, allowing parallel development
of question content and code.

The OTP verification system was tested live during the meeting — confirmed working for
both registration and password reset flows.

Score tracking and the Memory Match unlock at 100 points were tested and verified.

---

## Outcomes

- Tech stack confirmed for all layers
- `questions/*.json` format agreed for question banks
- Memory Match unlock threshold: 100 points (stored in `UNLOCK_THRESHOLD` constant)
- Single working branch (`start`) — no PR workflow for this team size

---

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Complete math question banks (all tiers) | Aaryut | 2 June |
| Complete cyber question banks (all tiers) | Saif | 3 June |
| Implement Snake quiz Canvas engine | Shree Krishna | 2 June |
| Build Memory Match game logic | Shree Krishna | 3 June |
| Dashboard CSS — eco-forest theme | Jina | 3 June |
| Test quiz difficulty and OTP in browser | Pushparaj | 4 June |

---

## Next Meeting

**Date:** 3 June 2026 — Sprint 2 review and Sprint 3 planning.
