# Sprint 2 — Capybara Mascot & Dashboard

**Sprint Dates:** 31 May – 3 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### Capybara Mascot ("Capy") — Canvas 2D Animation

The dashboard features a hand-drawn 2D capybara character rendered entirely in Canvas 2D.
No external images or sprite sheets are used — every part of Capy is drawn programmatically:

**Body parts drawn with Canvas arcs and bezier curves:**
- Rounded body (large ellipse with ear twitches)
- Animated legs (walking cycle using sine wave offsets)
- Tail wag
- Eye blink (random interval: 3–7 seconds)
- Eating animation (jaw movement)
- Wave animation (front leg raises)

**State machine:**
```
idle → walking → sitting → eating → waving → idle
```

Each state has a duration and transitions automatically after its animation completes.

**Click interaction:**
```javascript
canvas.addEventListener('click', () => {
  messageIndex = (messageIndex + 1) % MESSAGES.length;
  showMessage(MESSAGES[messageIndex]);
});
```
Clicking Capy cycles through 10 messages. Messages also auto-cycle every 5 seconds.

**The 10 Capy messages include:**
- Eco-themed tips ("Did you know? A 4-minute shower saves 30 litres!")
- Encouragement ("You're doing great! Keep earning points! 🌿")
- Game hints ("Unlock Memory Match by reaching 100 points!")

---

### `buzzxzone/templates/dashboard.html` — Game Hub

The dashboard template receives a `progress` dict from Flask:

```python
progress = get_user_progress(session["user_id"])
return render_template("dashboard.html", username=..., progress=progress)
```

The template uses this to:
1. Display the current high score in the nav and on the page.
2. Show a progress bar toward unlocking Memory Match.
3. Visually lock/unlock the Memory Match game card.

**Locked card with progress bar:**
```html
{% if not progress.memory_unlocked %}
<div class="lock-bar">
  <div class="lock-fill" style="width: {{ progress.progress_pct }}%"></div>
</div>
<p>{{ progress.high_score }} / {{ progress.threshold }} pts</p>
{% endif %}
```

**Session flash message** — if a user tries to access Memory Match while it's locked,
Flask redirects to dashboard with a message stored in `session["locked_msg"]`:
```python
session["locked_msg"] = f"🔒 Memory Match is locked. Reach {threshold} points to unlock it!"
return redirect("/dashboard")
```
The dashboard template reads and clears this message.

---

## Files Created/Modified This Sprint

| File | Change |
|------|--------|
| `templates/dashboard.html` | Game hub, Capy canvas, progress bar, game cards |
| `app.py` | `/dashboard` route, `get_user_progress()` helper |
| `static/style.css` | Dashboard-specific styles: game cards, lock overlay, progress bar |

---

## Animated Game Cards

Each game card on the dashboard has:
- A staggered entrance animation (CSS `animation-delay` increments).
- A bouncing icon on idle (`@keyframes bounce`).
- A glowing coloured top bar that slides in on hover.

The cards link to `/games/snake`, `/games/math`, `/games/cyber`, and `/games/memory`.
