# Sprint 2 — Memory Match Mini-Game

**Sprint Dates:** 31 May – 3 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/templates/memory.html` — Memory Match Game

Memory Match is a 4×4 card-flip game (16 cards, 8 emoji pairs) that is locked by default
and only accessible once the player's high score reaches 100 points.

#### Access Control (Server-Side)

The route checks the database before rendering the game:

```python
@app.route("/games/memory")
def memory():
    progress = get_user_progress(session["user_id"])
    if not progress["memory_unlocked"]:
        session["locked_msg"] = f"🔒 Memory Match is locked..."
        return redirect("/dashboard")
    return render_template("memory.html", username=...)
```

Even if a user manually navigates to `/games/memory`, the server redirects them away
if they have not met the unlock threshold. The lock cannot be bypassed client-side.

#### Game Board

The 8 emoji pairs used in Memory Match:

```javascript
const EMOJIS = ['🌿','🌊','☀️','🌱','🦋','🐝','🌍','♻️'];
const cards  = [...EMOJIS, ...EMOJIS];  // duplicate for pairs
shuffle(cards);
```

The emojis are all eco-themed to match the app's educational focus.

#### Card Flip Logic

```javascript
function flipCard(card) {
  if (flipped.length === 2 || card.classList.contains('matched')) return;
  card.classList.add('flipped');
  flipped.push(card);

  if (flipped.length === 2) {
    if (flipped[0].dataset.emoji === flipped[1].dataset.emoji) {
      flipped.forEach(c => c.classList.add('matched'));
      matched++;
      if (matched === EMOJIS.length) onComplete();
    } else {
      setTimeout(() => {
        flipped.forEach(c => c.classList.remove('flipped'));
      }, 1000);
    }
    flipped = [];
  }
}
```

Matched cards stay face-up and dim slightly. Unmatched cards flip back after 1 second.

#### CSS Flip Animation

Cards use CSS 3D transforms for the flip effect:

```css
.card-inner {
  transition: transform 0.5s;
  transform-style: preserve-3d;
}
.card.flipped .card-inner {
  transform: rotateY(180deg);
}
.card-front, .card-back {
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
```

#### Score on Completion

When all 8 pairs are matched, a bonus score is submitted:

```javascript
function onComplete() {
  fetch('/api/submit_score', {
    method: 'POST',
    body: JSON.stringify({ score: currentScore + 50, source: 'memory' }),
    ...
  });
}
```

---

## Files Created/Modified This Sprint

| File | Change |
|------|--------|
| `templates/memory.html` | Memory Match board, flip logic, completion handler |
| `app.py` | `/games/memory` route with server-side lock check |
| `static/style.css` | Card flip CSS (3D transform, face front/back) |
