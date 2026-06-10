# Sprint 3 — Polish & UX Improvements

**Sprint Dates:** 7 June – 9 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Improved

### Keyboard Shortcuts — `buzzxzone/static/game.js` and `quiz.js`

Keyboard shortcuts (keys 1–4) were added to both game engines so players can answer
questions without reaching for the mouse:

**In `game.js`:**
```javascript
document.addEventListener('keydown', (e) => {
  if (!questionOpen) return;
  const map = {'1':0, '2':1, '3':2, '4':3};
  if (map[e.key] !== undefined) handleAnswer(map[e.key]);
});
```

**In `quiz.js`:**
```javascript
document.addEventListener('keydown', (e) => {
  if (answered) return;
  const map = {'1':0, '2':1, '3':2, '4':3};
  if (map[e.key] !== undefined) {
    const btns = elAnswers.querySelectorAll('.ans-btn');
    if (btns[map[e.key]] && !btns[map[e.key]].disabled) {
      handleAnswer(map[e.key], false);
    }
  }
});
```

The quiz.js version also checks that the target button is not already disabled
(i.e., not already answered this turn) before firing.

---

### Accuracy Display on Game Over / Quiz Completion

Both game engines now calculate and display accuracy percentage at the end:

**In `game.js` (snake game over screen):**
```javascript
const correct = Math.round(score / POINTS_PER_Q);
const pct     = QUESTIONS.length > 0 ? Math.round((correct / QUESTIONS.length) * 100) : 0;
overMessage.innerHTML = `...Correct: ${correct}/${QUESTIONS.length} | Accuracy: ${pct}%`;
```

**In `quiz.js` (quiz completion screen):**
```javascript
const pct = Math.round((correct / QUESTIONS.length) * 100);
elDoneMsg.innerHTML = `...${correct} of ${QUESTIONS.length} correct — ${pct}% accuracy.`;
```

---

### Play Again Button — `buzzxzone/static/quiz.js`

A "Play Again" link was added to the quiz completion screen. It reloads the same URL
(same category + difficulty) so the player can immediately retry with a freshly shuffled
question bank (questions are shuffled server-side on every page load):

```javascript
const playAgainBtn = document.createElement('a');
playAgainBtn.href      = window.location.href;
playAgainBtn.className = 'overlay-btn';
playAgainBtn.textContent = '🔄 Play Again';
elDoneMsg.appendChild(playAgainBtn);
```

---

### Eco Leaf Token — `buzzxzone/static/game.js`

The food token on the snake canvas was changed from `⚡` to `🌿` to reinforce the
eco theme throughout the game:

```javascript
ctx.fillText('🌿', leaf.x*CELL + CELL/2, leaf.y*CELL + CELL/2);
```

---

### Question Bank Expansion

| Bank | Questions Added |
|------|----------------|
| `questions/snake.json` | +5 (wind turbine, seed planting, conservation, rain barrel) |
| `questions/cyber_easy.json` | +5 (2FA, password reuse, hacked account, fake websites, phishing) |
| `questions/cyber_medium.json` | +3 (VPN, zero-day, social engineering) |
| `questions/math_hard.json` | +4 (polynomial expansion, linear equations, triangle area, factorial) |

---

## Files Modified This Sprint

| File | Change |
|------|--------|
| `static/game.js` | Keyboard shortcuts, accuracy display, leaf emoji token |
| `static/quiz.js` | Keyboard shortcuts, accuracy display, Play Again button |
| `questions/snake.json` | +5 questions |
| `questions/cyber_easy.json` | +5 questions |
| `questions/cyber_medium.json` | +3 questions |
| `questions/math_hard.json` | +4 questions |
