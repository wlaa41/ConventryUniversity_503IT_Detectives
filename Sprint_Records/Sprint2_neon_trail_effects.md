# Sprint 2 — Neon Mouse Trail & Spark Effects

**Sprint Dates:** 31 May – 3 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### Neon Mouse Trail — `buzzxzone/templates/base.html`

Every page in buzzXzone has an animated neon glow trail that follows the cursor.
The trail is rendered on a full-screen fixed `<canvas>` element in `base.html`,
so it appears on every page that extends the base template.

#### How It Works

Mouse coordinates are tracked globally:

```javascript
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
document.addEventListener('mousemove', e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  addTrailPoint(mouseX, mouseY);
});
```

Trail points are stored in a fixed-size circular buffer. Each frame, older points
fade out by reducing their `alpha` value. The trail line is drawn by iterating the
buffer and stroking a path with a gradient width (thicker near the cursor, thinner
at the tail).

**Colour cycle:** particles cycle through `#00ffcc` (neon cyan), `#7fff00` (chartreuse),
and `#ffd700` (gold) over time using a hue rotation on the HSL model.

#### Particle Ring on Cursor

At the cursor tip, a pulsing ring is drawn:

```javascript
ctx.beginPath();
ctx.arc(mouseX, mouseY, pulseRadius, 0, Math.PI * 2);
ctx.strokeStyle = `rgba(0,255,204,${0.6 - pulseAlpha})`;
ctx.shadowBlur   = 20;
ctx.stroke();
```

`pulseRadius` grows from 4px to 18px then resets, creating a breathing ring effect.

---

### Spark Click Effect — `buzzxzone/templates/base.html`

Clicking anywhere spawns an explosion of 12 neon particles:

```javascript
document.addEventListener('click', e => {
  for (let i = 0; i < 12; i++) {
    sparks.push({
      x:   e.clientX,
      y:   e.clientY,
      vx:  (Math.random() - 0.5) * 8,
      vy:  (Math.random() - 0.5) * 8,
      life: 1.0,
      colour: SPARK_COLOURS[Math.floor(Math.random() * SPARK_COLOURS.length)]
    });
  }
});
```

Each spark has a random velocity vector. Every animation frame, velocity is applied and
`life` decreases. When `life` reaches 0 the spark is removed from the array.

Spark colours: `#00ffcc`, `#7fff00`, `#ffd700`, `#ff69b4`, `#c084fc`.

---

### `buzzxzone/static/style.css` — Global Styles

The stylesheet handles the eco forest theme across all pages:

| Class/Element | Style |
|---|---|
| `body` | Background `#0a1a0a`, text `#e0ffe0` |
| `.nav` | Dark glass effect with green glow border |
| `.ans-btn` | Dark green with neon hover glow |
| `.ans-btn.correct` | Bright green fill + shadow |
| `.ans-btn.wrong` | Red fill + shake animation |
| `.timer-bar` | Green → yellow → red based on remaining time |
| `.card` (memory) | 3D perspective flip with front/back faces |
| `@keyframes shake` | 3-cycle horizontal shake for wrong answers |
| `@keyframes bounce` | Dashboard icon bounce on idle |

---

## Files Modified This Sprint

| File | Change |
|------|--------|
| `templates/base.html` | Added neon trail canvas, spark effect JavaScript |
| `static/style.css` | Full eco-forest theme — all component styles |
| `static/logo.svg` | buzzXzone leaf logo — created as inline SVG |
