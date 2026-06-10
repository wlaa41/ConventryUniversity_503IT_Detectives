# Meeting Minutes — Meeting 5 (Final Pre-Submission)

**Project:** buzzXzone — Eco Learning Quiz Hub
**Date:** 7 June 2026
**Time:** 12:00 PM – 1:00 PM
**Location:** Microsoft Teams (remote)
**Chair:** Shree Krishna Shrestha
**Minute-Taker:** Jina Giri

---

## Attendees

- Jina Giri
- Shree Krishna Shrestha
- Aaryut Chaudhary
- Saif Ullah
- Mohammad Zayed Alam
- Pushparaj Mahato

---

## Objectives

1. Final bug review from Pushparaj's test pass
2. Confirm all features live on Vercel
3. Review and finalise presentation slides
4. Assign presentation speaking roles
5. Submission checklist sign-off

---

## Discussion

Pushparaj presented the full manual test results — all critical items passed.

**Bugs resolved since Meeting 4:**

| Bug | Fix |
|-----|-----|
| Snake speed inconsistency | Delta-time movement implemented |
| OTP resend timer not resetting | Session expiry recalculated on resend |

Memory Match mobile flip glitch: accepted as a low-priority cosmetic issue.
`will-change: transform` CSS applied as a partial fix.

**Vercel deployment confirmed live:**
- App URL: buzzxzone.vercel.app
- `/health` response: `{"status": "ok", "database": "connected", "version": "1.0.0"}`
- All environment variables verified in Vercel dashboard
- Static assets (CSS, JS, logo) loading correctly

**Presentation rehearsal completed** — all sections delivered in approximately 12 minutes.

---

## Presentation Roles Assigned

| Section | Presenter |
|---------|-----------|
| Project intro & eco concept | Aaryut Chaudhary |
| Tech stack & architecture | Shree Krishna Shrestha |
| Live demo — Snake Quiz | Shree Krishna Shrestha |
| Live demo — Math & Cyber Quiz | Saif Ullah |
| Live demo — Memory Match | Jina Giri |
| Agile process & sprints | Mohammad Zayed Alam |
| Testing & QA results | Pushparaj Mahato |

---

## Submission Checklist — Final Sign-Off

| Item | Status |
|------|--------|
| Code pushed to GitHub (`start` branch) | ✅ |
| README complete with all sections | ✅ |
| All meeting minutes uploaded | ✅ |
| Sprint records documented | ✅ |
| Presentation slides ready | ✅ |
| App live and `/health` healthy | ✅ |
| Evidence screenshots uploaded | ✅ |

---

## Decisions Made

- No new features or changes after this meeting
- `start` branch confirmed as the submission branch
- Submission deadline: 9 June 2026

---

## Meeting Closed

No further meetings scheduled. All team members signed off on the submission.
