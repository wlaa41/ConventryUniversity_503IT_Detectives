# Meeting 3 — Minutes

## Meeting Details

| Field | Info |
|-------|------|
| **Date** | 3 June 2026 |
| **Time** | 2:00 PM – 3:30 PM |
| **Location** | Coventry University London Campus |
| **Chair** | Mohammad Zayed Alam |
| **Minute-Taker** | Shree Krishna Shrestha |

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

## Agenda

1. Sprint 2 demo — show working prototype to the team
2. Review all four mini-games
3. Identify bugs and missing content
4. Discuss Supabase integration progress
5. Plan Sprint 3 tasks

## Discussion Summary

Shree Krishna demonstrated the working prototype:
- Dashboard with Capybara mascot — functioning correctly
- Eco Snake Quiz — playable end-to-end, score saving working
- Math Quiz (Easy + Medium) — working, Hard tier questions incomplete
- Cyber Quiz (Easy) — working, Medium and Hard questions pending
- Memory Match — locked state with progress bar visible

**Issues raised during demo:**
- Math Hard tier questions not yet added
- Cyber Medium and Hard question banks incomplete
- Snake speed inconsistency observed on slower network connections

**Supabase Integration:**
Supabase PostgreSQL was successfully connected as the production database. The database
connection string uses the transaction pooler (port 6543) with `sslmode=require`.
The `users` table auto-creates on first startup.

A 3D game expansion idea was discussed (customisable characters, interactive 3D environment).
After evaluating time constraints and technical complexity, the team agreed not to pursue this
for the current submission and instead focus on completing and polishing the existing four games.

Peer review activity was completed — the team reviewed another group's presentation and
noted ideas to improve buzzXzone's own presentation structure.

## Decisions Made

- All question banks must be finalised by 5 June
- 3D expansion idea deferred to a future development cycle
- Pushparaj to run full manual test checklist before submission
- Presentation draft due 8 June

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Complete math hard questions | Aaryut | 5 June |
| Complete cyber medium + hard questions | Saif | 5 June |
| Fix snake speed bug | Shree Krishna | 5 June |
| Full manual test checklist | Pushparaj | 7 June |
| Presentation draft | Aaryut | 8 June |
| Supabase final verification | Shree Krishna | 6 June |

## Next Meeting

**Date:** 7 June 2026 — Final pre-submission review (remote, Teams).

## Evidence

See [Week 3 progress](Week%203%20progress/) for screenshots and activity records.
