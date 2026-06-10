# Sprint 2 — Quiz Engine (Math & Cyber)

**Sprint Dates:** 31 May – 3 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/static/quiz.js` — Shared Quiz Engine

A single JavaScript file powers both the Math Quiz and the Eco Cyber-Security Quiz.
The quiz type and difficulty are injected from Flask as JavaScript constants:

```html
<script>
  const QUESTIONS      = {{ questions_json | safe }};
  const QUIZ_CATEGORY  = "{{ category }}";
  const QUIZ_DIFFICULTY = "{{ difficulty }}";
  const QUESTION_TIME  = {{ question_time }};
  const POINTS_PER_Q   = {{ points_per_q }};
</script>
```

#### Tutorial Modal System

Before the quiz starts, a category/difficulty-specific tutorial overlay is shown.
The tutorial data is embedded directly in `quiz.js` as a nested object:

```javascript
const TUTORIAL_DATA = {
  math: {
    easy:   { icon, title, tips, example, trick },
    medium: { ... },
    hard:   { ... }
  },
  cyber: {
    easy:   { ... },
    medium: { ... },
    hard:   { ... }
  }
};
```

This approach keeps all tutorial content in one place without extra API calls.

#### Two-Attempt System

Math questions allow two attempts before the correct answer is revealed:

```javascript
if (wrongCount === 1) {
  elTryAgain.classList.remove('hidden');  // first wrong: show retry message
} else {
  // second wrong: reveal answer, show hint, advance
  answered = true;
  btns[q.correct].classList.add('correct');
  if (q.hint && QUIZ_CATEGORY === 'math') showHint(q.hint);
  setTimeout(() => { qIndex++; loadQuestion(); }, 2500);
}
```

The `hint` field is only shown for math questions (not cyber) since math hints contain
worked solutions, while cyber questions are knowledge-based.

#### Ripple Click Effect

Every answer button has a CSS ripple animation triggered on click:

```javascript
function addRipple(el, event) {
  const rect   = el.getBoundingClientRect();
  const ripple = document.createElement('span');
  ripple.className = 'ripple';
  ripple.style.cssText = `left:${x - size/2}px;top:${y - size/2}px;width:${size}px;height:${size}px;`;
  el.appendChild(ripple);
  ripple.addEventListener('animationend', () => ripple.remove());
}
```

The span is self-removing via `animationend` so no stale DOM elements accumulate.

---

## `buzzxzone/templates/difficulty.html` — Difficulty Picker

A single template used by both Math and Cyber, receiving `category`, `title`, and `icon`
from Flask. The three difficulty cards link to `/games/<category>/<difficulty>`.

## `buzzxzone/templates/quiz.html` — Quiz Page

Hosts the tutorial overlay and the quiz card. The quiz card is hidden initially and revealed
when the tutorial's "Start Quiz" button is clicked.

---

## Files Created/Modified This Sprint

| File | Change |
|------|--------|
| `static/quiz.js` | Full quiz engine with tutorial, two-attempt system, ripple — new file |
| `templates/quiz.html` | Quiz page layout with tutorial overlay |
| `templates/difficulty.html` | Difficulty picker (shared for math and cyber) |
| `app.py` | Added `/games/math`, `/games/cyber`, `/games/<category>/<difficulty>` routes |

---

## Question Bank Format

All question banks live in `buzzxzone/questions/*.json`:

```json
{
  "q": "Question text",
  "answers": ["Option A", "Option B", "Option C", "Option D"],
  "correct": 2,
  "hint": "Optional worked solution (math only)"
}
```

Seven JSON files cover all combinations: `snake.json`, `math_easy.json`,
`math_medium.json`, `math_hard.json`, `cyber_easy.json`, `cyber_medium.json`, `cyber_hard.json`.
