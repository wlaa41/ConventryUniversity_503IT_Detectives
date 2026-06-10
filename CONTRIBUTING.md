# Contributing to buzzXzone

## Branching

- All work goes into the `start` branch.
- For features: `git checkout -b feature/<short-name>`
- For bug fixes: `git checkout -b fix/<short-name>`

## Commit Style

Use short, imperative commit messages:

```
feat: add leaderboard page
fix: correct OTP expiry timestamp comparison
content: add 5 new eco snake questions
security: set SameSite flag on session cookie
style: update eco forest colour tokens
sprint: add Sprint 2 record for quiz engine
```

**Prefixes:**
| Prefix | Use for |
|--------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `content` | Question bank additions / text changes |
| `security` | Security improvements |
| `style` | CSS / visual-only changes |
| `sprint` | Sprint records and documentation |
| `docs` | README and other documentation |

## Pull Requests

- One logical change per PR.
- At least one team member approves before merging.
- Link the relevant Trello card in the PR description.

## Python Style

- Follow PEP 8.
- Max line length: 100 characters.
- Use `snake_case` for variables and functions.
- Use `UPPER_CASE` for module-level constants.

## JavaScript Style

- `const` / `let` only — no `var`.
- camelCase for variables and functions.
- Functions should do one thing; split large functions.

## Adding Questions

Question files live in `buzzxzone/questions/*.json`. Format:

```json
{
  "q": "Question text here?",
  "answers": ["Option A", "Option B", "Option C", "Option D"],
  "correct": 0,
  "hint": "Worked solution (math only)"
}
```

- `correct` is the 0-indexed position of the correct answer.
- `hint` is optional and only displayed for math questions.
- Shuffle the answer positions so the correct answer is not always in the same slot.
