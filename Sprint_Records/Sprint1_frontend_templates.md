# Sprint 1 — Frontend Templates & Base Layout

**Sprint Dates:** 27 May – 30 May 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/templates/base.html` — Shared Layout

All pages inherit from a single base template. This template includes:

- The neon mouse trail canvas (injected on every page via JavaScript).
- Spark click effect — a burst of neon particles on every mouse click.
- Navigation bar with the logo, username, and logout link.
- A Jinja2 `{% block content %}` slot that child templates fill in.

The trail and spark effects use a single persistent `<canvas id="trail-canvas">` element
positioned fixed behind all other content, so it does not interfere with layout.

### `buzzxzone/templates/login.html` and `register.html`

A minimal centred card layout on a dark background. The forms POST to Flask routes which
either redirect on success or re-render the template with an error message passed via Jinja2:

```html
{% if error %}
<p class="error-msg">{{ error }}</p>
{% endif %}
```

### `buzzxzone/templates/verify.html`

OTP verification page with a 6-character input field. Submitted OTP is compared server-side
against the session-stored OTP and its expiry timestamp.

### `buzzxzone/templates/forgot.html`, `reset_verify.html`, `new_password.html`

Three-step password reset flow. Each step stores state in the Flask session rather than the
database:
- `forgot.html` → collects email, generates OTP.
- `reset_verify.html` → checks OTP against `session["reset_otp"]`.
- `new_password.html` → updates password hash, clears session.

---

## Files Created This Sprint

| File | Purpose |
|------|---------|
| `templates/base.html` | Shared layout, neon trail, spark click, nav |
| `templates/login.html` | Login form with error display |
| `templates/register.html` | Registration form |
| `templates/verify.html` | OTP verification |
| `templates/forgot.html` | Forgot password entry |
| `templates/reset_verify.html` | Password reset OTP check |
| `templates/new_password.html` | New password form |

---

## Design Notes

The eco-forest colour palette was applied from the first template:
- Background: `#0a1a0a` (deep forest dark)
- Primary: `#2d7a2d` (leaf green)
- Accent: `#00ffcc` (neon cyan) for hover states and the mouse trail

All form inputs use a dark inset style with a glowing green border on focus.
