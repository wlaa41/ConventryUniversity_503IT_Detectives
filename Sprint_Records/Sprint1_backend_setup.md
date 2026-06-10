# Sprint 1 — Backend Setup & Authentication

**Sprint Dates:** 27 May – 30 May 2026
**Developer:** Shree Krishna Shrestha (15681041)

---

## What Was Built

### `buzzxzone/app.py` — Flask Application Core

The main backend file was written from scratch using Python 3 and Flask.

**Key sections implemented in this sprint:**

#### Database Setup
```python
DB_PATH = "/tmp/cyber.db" if os.environ.get("VERCEL") else os.path.join(BASE_DIR, "cyber.db")
```
The database path switches to `/tmp/` automatically when deployed on Vercel, since Vercel's
filesystem is read-only except for that directory. This prevents a FileNotFoundError on deployment.

#### User Table + Schema Migration
```python
def init_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            username        TEXT NOT NULL,
            email           TEXT NOT NULL UNIQUE,
            password        TEXT NOT NULL,
            high_score      INTEGER NOT NULL DEFAULT 0,
            memory_unlocked INTEGER NOT NULL DEFAULT 0
        )
    """)
```
The `init_db()` function also handles live schema migrations — it checks for missing columns
and adds them with `ALTER TABLE` rather than dropping the table, so existing user data is preserved.

#### Registration Route
```python
@app.route("/register", methods=["GET", "POST"])
def register():
```
Passwords are hashed with `werkzeug.security.generate_password_hash` (PBKDF2-SHA256) before
being stored. Email uniqueness is enforced at the database level with a `UNIQUE` constraint.

#### Login with OTP
```python
otp = str(random.randint(100000, 999999))
session["otp"]        = otp
session["otp_expiry"] = (datetime.now() + timedelta(minutes=5)).isoformat()
```
After credential verification, a 6-digit OTP is generated and emailed. The OTP and its
5-minute expiry are stored in the Flask session, not the database, to avoid needing a
separate `otp_tokens` table.

---

## Files Created This Sprint

| File | Description |
|------|-------------|
| `buzzxzone/app.py` | Flask routes, DB init, OTP auth, score logic |
| `buzzxzone/requirements.txt` | Python dependencies |
| `buzzxzone/vercel.json` | Vercel serverless deployment configuration |

---

## Screenshot Evidence

> See `AI use evidence/` folder for screenshots of early development and testing.
