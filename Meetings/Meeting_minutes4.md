# Meeting Minutes — Meeting 4

**Project:** buzzXzone — Eco Learning Quiz Hub
**Date:** 3 June 2026
**Time:** 2:00 PM – 3:30 PM
**Location:** Coventry University London Campus
**Chair:** Mohammad Zayed Alam
**Minute-Taker:** Shree Krishna Shrestha

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

1. Sprint 2 demo — show working prototype
2. Review all four mini-games
3. Identify bugs and incomplete areas
4. Discuss Supabase integration
5. Plan Sprint 3 tasks

---

## Discussion

Shree Krishna demoed the working prototype:

| Feature | Status |
|---------|--------|
| Dashboard with Capybara mascot | ✅ Working |
| Eco Snake Quiz (end-to-end) | ✅ Working |
| Math Quiz (Easy + Medium) | ✅ Working |
| Math Quiz (Hard tier) | ⚠️ Questions incomplete |
| Cyber Quiz (Easy) | ✅ Working |
| Cyber Quiz (Medium + Hard) | ⚠️ Questions incomplete |
| Memory Match (locked state) | ✅ Working |

**Bugs identified:**

| Bug | Severity | Assigned To |
|-----|----------|-------------|
| Snake speed inconsistency on slow networks | High | Shree Krishna |
| OTP resend timer not resetting | Medium | Shree Krishna |
| Memory Match flip glitch on mobile | Low | Accepted for now |

**Supabase update:** Production database connected and verified. Transaction pooler
(port 6543) with `sslmode=require` confirmed working on Vercel.

**3D expansion idea** proposed and discussed. Agreed not to pursue for this submission
due to time constraints. Logged in backlog for future consideration.

---

## Outcomes

- All question banks must be finalised by 5 June
- Bug fixes assigned with 5 June deadline
- 3D expansion deferred
- Presentation draft due 8 June
- Full manual test checklist by Pushparaj due 7 June

---

## Action Items

| Task | Assigned To | Deadline |
|------|-------------|----------|
| Finalise all question banks | Aaryut, Saif | 5 June |
| Fix snake speed bug | Shree Krishna | 5 June |
| Fix OTP resend timer | Shree Krishna | 5 June |
| Full manual test pass | Pushparaj | 7 June |
| Presentation draft | Aaryut | 8 June |
| Verify Vercel `/health` endpoint | Shree Krishna | 6 June |

---

## Next Meeting

**Date:** 7 June 2026 — Final pre-submission review (remote, Teams).
