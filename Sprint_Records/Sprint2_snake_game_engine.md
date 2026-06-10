# Sprint 2 — Eco Snake Quiz Game Engine

**Sprint Dates:** 31 May – 3 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/static/game.js` — Auto-Play Snake Engine (Canvas 2D)

The Eco Snake Quiz is the centrepiece of the app. Unlike a traditional snake game, the snake
plays itself — the player's only role is answering questions. This design removes any motor-skill
barrier and makes the game accessible to all users.

#### Auto-Pilot Algorithm

```javascript
function chooseDirection() {
  const head = snake[0];
  const candidates = [
    {x: 1, y: 0}, {x: -1, y: 0}, {x: 0, y: 1}, {x: 0, y: -1},
  ].filter(d => !(d.x === -dir.x && d.y === -dir.y));  // no 180° turn

  const safe = candidates.filter(d => {
    const nx = head.x + d.x, ny = head.y + d.y;
    if (nx < 0 || nx >= COLS || ny < 0 || ny >= ROWS) return false;
    return !snake.slice(0, -1).some(s => s.x === nx && s.y === ny);
  });

  safe.sort((a, b) => {
    const da = Math.abs(head.x + a.x - leaf.x) + Math.abs(head.y + a.y - leaf.y);
    const db = Math.abs(head.x + b.x - leaf.x) + Math.abs(head.y + b.y - leaf.y);
    return da - db;
  });
  return safe[0];
}
```

The snake filters out unsafe moves (walls, self-collision) then picks the direction with the
lowest Manhattan distance to the leaf token. This gives it a natural-looking pathfinding
without the complexity of A*.

#### Score Submission with `keepalive`

```javascript
fetch('/api/submit_score', {
  method:    'POST',
  keepalive: true,
  ...
})
```

The `keepalive: true` flag ensures the score POST survives page navigation and tab close.
Without it, navigating away before the fetch completes would silently drop the score update.

#### Game Loop

Two `setInterval` loops run simultaneously:
- `gameLoopId` (110ms tick) — moves the snake one cell and redraws the canvas.
- `timerLoopId` (1000ms tick) — counts down the question timer.

Both are stored and cleared on game end to prevent them accumulating across restarts.

---

## `buzzxzone/templates/snake.html` — Snake Page

The template injects server-side data into JavaScript constants at the top of the page:

```html
<script>
  const QUESTIONS     = {{ questions_json | safe }};
  const QUESTION_TIME = {{ question_time }};
  const POINTS_PER_Q  = {{ points_per_q }};
</script>
```

This pattern passes the shuffled question bank (loaded and randomised in Python) into the
client-side game engine without any additional API calls during gameplay.

---

## Files Created/Modified This Sprint

| File | Change |
|------|--------|
| `static/game.js` | Full auto-play snake engine — new file |
| `templates/snake.html` | Snake page with Canvas element and HUD |
| `app.py` | Added `/games/snake` route and `/api/submit_score` endpoint |

---

## Canvas Grid Dimensions

| Property | Value |
|----------|-------|
| Canvas size | 500 × 500 px |
| Cell size | 20 px |
| Grid | 25 × 25 cells |
| Snake start length | 3 segments |
| Auto-move tick | 110 ms |
