# Meeting 2 — Minutes

## Meeting Details

| Field | Info |
|-------|------|
| **Date** | 29 May 2026 |
| **Time** | 2:00 PM – 3:00 PM |
| **Location** | Coventry University London Campus |
| **Chair** | Shree Krishna Shrestha |
| **Minute-Taker** | Aaryut Chaudhary |

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

## Agenda

1. Review wireframes from Sprint 1
2. Confirm tech stack
3. Set up GitHub branching strategy
4. Plan Sprint 2 backlog
5. Discuss quiz question format and content

## Discussion Summary

Jina presented initial wireframe sketches for the dashboard, quiz pages, and difficulty
selector. The team reviewed the designs and approved them with minor feedback on navigation flow.

**Tech stack confirmed:**
- Backend: Python 3 / Flask (team familiarity)
- Database: SQLite (local) / Supabase PostgreSQL (production)
- Frontend: Vanilla HTML, CSS, JavaScript — no framework (scope too small to justify React/Vue)
- Deployment: Vercel (free tier, zero-config for Flask)
- Authentication: Session-based + 6-digit OTP via Gmail SMTP

The team agreed to work on the `start` branch directly (small team — PR workflow overhead not
justified). The question bank format was agreed: JSON files in `questions/`, one file per
quiz type and difficulty.

**Math and Cyber quiz question banks** were begun by Aaryut and Saif during this sprint.
Each bank targets beginner-friendly concepts with clear multiple-choice options.

The OTP email verification system was tested during this meeting — working correctly for
both registration and password reset flows.

Score tracking and Memory Match unlock logic were reviewed and confirmed working at the
100-point threshold.

## Decisions Made

- Vanilla HTML/CSS/JS confirmed — no React or Vue
- Questions stored as JSON, not in the database
- Memory Match locked until `high_score >= 100`
- OTP validity: 5 minutes

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Complete math question banks (all tiers) | Aaryut | 2 June |
| Complete cyber question banks (all tiers) | Saif | 3 June |
| Implement Snake quiz Canvas engine | Shree Krishna | 2 June |
| Connect scoring to Supabase | Shree Krishna | 3 June |
| Complete dashboard CSS polish | Jina | 3 June |
| Test quiz difficulty levels | Pushparaj | 4 June |

## Next Meeting

**Date:** 1 June 2026 — Sprint 2 progress review.

## Evidence

See [Week 2 progress](Week%202%20progress/) for screenshots and activity records.
