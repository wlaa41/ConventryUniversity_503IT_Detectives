# Sprint 3 — Scoring System & API Endpoints

**Sprint Dates:** 3 June – 7 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### Score Persistence System — `buzzxzone/app.py`

The scoring system stores only the all-time high score, not individual session scores.
This design decision (made in Sprint 2 planning) keeps the database simple and prevents
the need for a session-history table.

#### `update_high_score()` Helper

```python
def update_high_score(user_id, new_score):
    row  = cur.execute(
        "SELECT high_score, memory_unlocked FROM users WHERE id=?", (user_id,)
    ).fetchone()

    best     = max(row["high_score"], int(new_score))
    unlocked = 1 if (best >= UNLOCK_THRESHOLD or row["memory_unlocked"]) else 0

    cur.execute(
        "UPDATE users SET high_score=?, memory_unlocked=? WHERE id=?",
        (best, unlocked, user_id),
    )
```

The `max()` call ensures the score never decreases — if a user scores 80 then 40 in the
next game, their stored score stays at 80. The Memory Match unlock (`memory_unlocked=1`)
is also set permanently once the threshold is reached, even if the user's score later
drops below 100 in a new game (it cannot, since score is monotonically non-decreasing).

#### `get_user_progress()` Helper

Returns a dict used both by template rendering and the `/api/progress` JSON endpoint:

```python
return {
    "high_score":      row["high_score"],
    "memory_unlocked": bool(row["memory_unlocked"]),
    "threshold":       UNLOCK_THRESHOLD,
    "progress_pct":    pct,
}
```

`progress_pct` is capped at 100 so the progress bar never overflows:
```python
pct = min(100, int(row["high_score"] * 100 / UNLOCK_THRESHOLD))
```

---

### `/api/submit_score` — Score POST Endpoint

All games (snake, math, cyber, memory) submit scores to a single unified endpoint:

```python
@app.route("/api/submit_score", methods=["POST"])
def submit_score():
    data       = request.get_json(silent=True) or {}
    score      = int(data.get("score", 0))
    source     = data.get("source", "unknown")
    best, unlocked = update_high_score(session["user_id"], score)
    return jsonify({
        "ok":              True,
        "submitted":       score,
        "high_score":      best,
        "memory_unlocked": unlocked,
        "threshold":       UNLOCK_THRESHOLD,
    })
```

The `source` field (snake / math / cyber / memory) is logged for debugging.
The response tells the client whether Memory Match was just unlocked, so the game
can show an unlock notification without a page reload.

---

### `/api/leaderboard` — Top 10 Scores

Added in Sprint 3 polish to support a future leaderboard page:

```python
rows = conn.execute(
    "SELECT username, high_score FROM users ORDER BY high_score DESC LIMIT 10"
).fetchall()
return jsonify({
    "ok": True,
    "leaderboard": [{"rank": i+1, "username": r["username"], "score": r["high_score"]}
                    for i, r in enumerate(rows)]
})
```

---

### `/health` — Deployment Verification Endpoint

Added to verify Vercel deployment health:

```python
@app.route("/health")
def health():
    conn.execute("SELECT 1").fetchone()
    return jsonify({"status": "ok", "database": "connected", "version": "1.0.0"})
```

---

## Security Improvements This Sprint

| Improvement | Implementation |
|-------------|----------------|
| HttpOnly session cookie | `SESSION_COOKIE_HTTPONLY = True` |
| SameSite cookie flag | `SESSION_COOKIE_SAMESITE = "Lax"` |
| Secure cookie on Vercel | `SESSION_COOKIE_SECURE = True` (Vercel only) |
| Security response headers | `X-Content-Type-Options`, `X-Frame-Options` in `vercel.json` |

---

## Files Modified This Sprint

| File | Change |
|------|--------|
| `app.py` | Score helpers, API endpoints, security config, health check |
| `vercel.json` | Security headers, static file routing |
