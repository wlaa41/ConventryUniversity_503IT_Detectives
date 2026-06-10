# Sprint 3 — Vercel Deployment & Environment Config

**Sprint Dates:** 7 June – 9 June 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/vercel.json` — Serverless Deployment Config

Vercel uses this file to determine how to build and route the Flask app:

```json
{
  "version": 2,
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    {
      "src": "/(.*)",
      "dest": "app.py",
      "headers": {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "strict-origin-when-cross-origin"
      }
    }
  ]
}
```

**Key decisions:**
- The static route is listed first so CSS/JS/SVG files are served directly by Vercel's CDN,
  not routed through Flask. This reduces cold-start latency for asset loads.
- Security headers are added at the routing level so they apply to every Flask response
  without needing to touch `app.py`.

### Database Path Switch

```python
DB_PATH = "/tmp/cyber.db" if os.environ.get("VERCEL") else os.path.join(BASE_DIR, "cyber.db")
```

Vercel's filesystem is read-only at `/var/task` (the app root). The only writable path is
`/tmp`. By checking for the `VERCEL` environment variable, the app uses the writable path
in production and a local file in development. Note: `/tmp` is ephemeral on Vercel — data
does not persist between cold starts. For persistent data the app uses Supabase (external DB).

### `buzzxzone/requirements.txt`

```
flask>=3.0.0
werkzeug>=3.0.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
```

`psycopg2-binary` is used instead of `psycopg2` to avoid the need to compile C extensions
on Vercel. The binary wheel includes the PostgreSQL client library.

---

## Deployment Checklist Verified

| Check | Result |
|-------|--------|
| `vercel.json` routes correct | ✓ |
| `DATABASE_URL` env var set in Vercel dashboard | ✓ |
| `FLASK_SECRET_KEY` env var set | ✓ |
| `GMAIL_USER` / `GMAIL_PASSWORD` set | ✓ |
| `/health` returns `{"status":"ok","database":"connected"}` | ✓ |
| All static assets loading (CSS, JS, logo) | ✓ |
| Registration and OTP flow working on live URL | ✓ |

---

## Local vs Production Differences

| Behaviour | Local (`python app.py`) | Production (Vercel) |
|-----------|------------------------|---------------------|
| Database | `buzzxzone/cyber.db` (persistent file) | `/tmp/cyber.db` (ephemeral) or external PostgreSQL |
| Session cookies | `Secure=False` (HTTP allowed) | `Secure=True` (HTTPS only) |
| Debug mode | `True` | `False` (Vercel production) |
| OTP | Printed to console if Gmail not configured | Sent via Gmail SMTP |

---

## Files Modified This Sprint

| File | Change |
|------|--------|
| `vercel.json` | Static route, security response headers |
| `app.py` | `SESSION_COOKIE_SECURE` toggle, `/health` endpoint |
| `requirements.txt` | Confirmed correct dependencies for Vercel |
