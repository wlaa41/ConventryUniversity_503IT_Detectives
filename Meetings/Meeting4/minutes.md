# Meeting 4 — Minutes (Final Pre-Submission)

## Meeting Details

| Field | Info |
|-------|------|
| **Date** | 7 June 2026 |
| **Time** | 12:00 PM – 1:00 PM |
| **Location** | Microsoft Teams (remote) |
| **Chair** | Shree Krishna Shrestha |
| **Minute-Taker** | Jina Giri |

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato *(first full-team remote attendance)*

## Agenda

1. Final bug review from Pushparaj's test pass
2. Confirm all features working on Vercel
3. Review presentation slides
4. Assign presentation speaking roles
5. Submission checklist sign-off

## Discussion Summary

Pushparaj presented the results of the full manual test checklist. All critical items passed.

**Bugs resolved before this meeting:**
- Snake speed inconsistency — fixed with delta-time based movement
- OTP resend timer — corrected
- Memory Match flip animation glitch on mobile — accepted as low-priority for this submission

**Vercel Deployment Verified:**
The live application at `buzzxzone.vercel.app` was confirmed healthy:
- `/health` endpoint returns `{"status": "ok", "database": "connected", "version": "1.0.0"}`
- All environment variables confirmed set in the Vercel dashboard
- Static assets (CSS, JS, logo) loading via Vercel CDN

**Login and Register interfaces** were reviewed and approved by the full team.

**Presentation speaking roles assigned** — each member assigned specific slides covering
their area of contribution.

## Presentation Speaking Roles

| Section | Presenter |
|---------|-----------|
| Project intro & eco concept | Aaryut |
| Tech stack & architecture | Shree Krishna |
| Live demo — Snake Quiz | Shree Krishna |
| Live demo — Math & Cyber Quiz | Saif |
| Live demo — Memory Match | Jina |
| Agile process & sprints | Mohammad |
| Testing & QA results | Pushparaj |

## Submission Checklist — Sign-Off

| Item | Status |
|------|--------|
| Code pushed to GitHub (`start` branch) | ✅ |
| README complete | ✅ |
| Meeting minutes uploaded | ✅ |
| Presentation slides ready | ✅ |
| App live and healthy on Vercel | ✅ |

## Decisions Made

- No new features to be added after this meeting.
- `start` branch is the submission branch.
- Presentation rehearsal estimated at 12 minutes (within 15-minute limit).

## Meeting Closed

No further meetings scheduled. Submission date: 9 June 2026.

## Evidence

See [Week 4 progress](Week%204%20progress/) for screenshots and activity records.
