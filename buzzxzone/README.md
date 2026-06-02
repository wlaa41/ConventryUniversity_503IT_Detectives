# 🌿 pooki — Eco Learning Quiz Hub

A Flask web app featuring **pooki**: an eco-themed learning hub for ages 6–12 with an auto-playing snake quiz, a math quiz, an eco-friendly cyber-security quiz, and an unlockable memory-match mini-game.

Deployable locally **or** on [Vercel](https://vercel.com) via `vercel.json`.

---

## Project Structure

```
buzzxzone/
│
├── app.py              ← Flask routes, SQLite, scoring, OTP email
├── cyber.db            ← SQLite database (auto-created on first run)
├── requirements.txt    ← Python dependencies (flask, werkzeug)
├── vercel.json         ← Vercel deployment config
├── .gitignore
│
├── questions/          ← All question banks (separate JSON files)
│   ├── math_easy.json
│   ├── math_medium.json
│   ├── math_hard.json
│   ├── cyber_easy.json
│   ├── cyber_medium.json
│   ├── cyber_hard.json
│   └── snake.json
│
├── static/
│   ├── style.css       ← All visual styles
│   ├── game.js         ← Auto-play snake engine
│   └── quiz.js         ← Shared quiz engine (math + cyber)
│
└── templates/
    ├── base.html           ← Shared layout (leaf background)
        ├── login.html / register.html / verify.html
            ├── forgot.html / reset_verify.html / new_password.html
                ├── dashboard.html      ← Game hub (4 cards, memory locked by default)
                    ├── snake.html          ← Auto-play snake page
                        ├── difficulty.html     ← Easy / Medium / Hard picker (math + cyber)
                            ├── quiz.html           ← Generic quiz page (math + cyber)
                                └── memory.html         ← Memory Match (only reachable when unlocked)
                                ```

                                ---

                                ## How to Run

                                ### 1. Install dependencies

                                ```bash
                                pip install flask werkzeug
                                ```

                                Or via requirements file:

                                ```bash
                                pip install -r requirements.txt
                                ```

                                ### 2. Database

                                pooki uses **SQLite** (`cyber.db`) — Python's built-in `sqlite3` module.  
                                No external database server, no schema setup, no credentials.  
                                The DB file is created automatically on first run.

                                ### 3. (Optional) Email credentials

                                If you want OTP emails to send, set these environment variables:

                                ```
                                GMAIL_USER=your@gmail.com
                                GMAIL_PASSWORD=your-app-password
                                ```

                                If email isn't configured, the OTP is printed to the server console so you can still log in.

                                ### 4. Start the server

                                ```bash
                                python app.py
                                ```

                                Visit **http://localhost:5000**

                                ---

                                ## Deploying to Vercel

                                The repo includes a `vercel.json` that routes all traffic through `app.py` via `@vercel/python`.

                                > **Note:** Vercel's filesystem is read-only except `/tmp`, so `cyber.db` is stored at `/tmp/cyber.db` on Vercel and **will not persist between cold starts**. For persistent storage, connect an external database.

                                ```bash
                                vercel deploy
                                ```

                                ---

                                ## Key Constants (in `app.py`)

                                | Constant | Default | Meaning |
                                |---|---|---|
                                | `QUESTION_TIME_SEC` | `20` | Seconds allowed per question (hard cap) |
                                | `POINTS_PER_Q` | `10` | Points awarded per correct answer |
                                | `UNLOCK_THRESHOLD` | `100` | High score needed to unlock Memory Match |

                                ---

                                ## Game Features

                                ### 🐍 Auto-Play Eco Snake Quiz

                                The snake slithers autonomously — the player only answers the on-screen question.

                                | Feature | Detail |
                                |---|---|
                                | Mode | Fully auto-play animation — no keyboard controls |
                                | Timer | **20 seconds** per question (hard cap) |
                                | Correct answer | Snake grows by 1 segment, +10 points |
                                | Wrong / time-out | Snake shrinks by 1 segment |
                                | Game over | Snake shrinks below its minimum length |
                                | Question pool | `questions/snake.json` (eco-themed, shuffled each game) |

                                ---

                                ### 🧮 Math Quiz (Easy / Medium / Hard)

                                Player picks a difficulty, then answers a randomised pool from that tier.

                                - **Easy:** single-digit add/sub, simple multiplication  
                                - **Medium:** two-digit arithmetic, multiplication tables, division  
                                - **Hard:** BIDMAS, fractions, percentages, powers, simple algebra  
                                - 20 seconds per question, 10 points per correct answer  
                                - Question banks: `questions/math_easy.json`, `math_medium.json`, `math_hard.json`

                                ---

                                ### 🛡️ Eco-Friendly Cyber-Security Quiz (Easy / Medium / Hard)

                                Cyber-security questions framed around eco-friendly digital habits.

                                - **Easy:** phishing basics, password basics, safe device habits  
                                - **Medium:** 2FA, fake eco-deals, HTTPS, e-waste data wiping  
                                - **Hard:** social engineering, supply-chain attacks, ransomware, encryption  
                                - 20 seconds per question, 10 points per correct answer  
                                - Question banks: `questions/cyber_easy.json`, `cyber_medium.json`, `cyber_hard.json`

                                ---

                                ### 🧩 Memory Match — 🔒 LOCKED by default

                                - Unlocks once the player's highest score reaches **100 points** (configurable via `UNLOCK_THRESHOLD`)  
                                - Dashboard shows a 🔒 card with a progress bar toward the unlock  
                                - Once unlocked: 4×4 grid of 16 cards (8 emoji pairs), with moves + time tracking

                                ---

                                ## Auth Flow

                                | Route | Purpose |
                                |---|---|
                                | `/register` | Create account (username, email, password) |
                                | `/login` | Email + password → OTP sent via Gmail |
                                | `/verify` | Enter 6-digit OTP (expires in 5 minutes) |
                                | `/forgot` | Request password reset OTP |
                                | `/reset_verify` | Verify reset OTP |
                                | `/new_password` | Set new password |
                                | `/logout` | Clear session |

                                ---

                                ## API Endpoints

                                | Endpoint | Method | Description |
                                |---|---|---|
                                | `/api/submit_score` | POST | Submit game score, updates high score + unlock status |
                                | `/api/progress` | GET | Returns current high score, unlock status, progress % |

                                ---

                                ## Adding / Editing Questions

                                Every question lives in its own JSON file under `questions/`. Format:

                                ```json
                                [
                                  {
                                      "q": "What is 7 + 5?",
                                          "answers": ["10", "11", "12", "13"],
                                              "correct": 2
                                                }
                                                ]
                                                ```

                                                - `answers` must be exactly 4 strings  
                                                - `correct` is the 0-indexed position of the right answer (0 = first)  
                                                - Add as many questions per file as you like — they are shuffled per session

                                                ---

                                                ## File Responsibilities

                                                | File | Owns |
                                                |---|---|
                                                | `app.py` | Routes, SQLite, question loading, scoring, OTP, unlock logic |
                                                | `questions/*.json` | All question banks (math/cyber easy–medium–hard, snake) |
                                                | `static/style.css` | CSS variables, layout, card/button styles, locked-card + difficulty UI |
                                                | `static/game.js` | Auto-play snake engine, per-question 20-second timer, grow/shrink logic |
                                                | `static/quiz.js` | Shared math/cyber quiz engine, timer, score submission |
                                                | `templates/base.html` | Shared layout, leaf background |
                                                | `templates/dashboard.html` | Game hub (4 cards, memory locked card with progress bar) |
                                                | `templates/snake.html` | Snake canvas + HUD, injects QUESTIONS JSON |
                                                | `templates/difficulty.html` | Easy/Medium/Hard picker (used by both math and cyber) |
                                                | `templates/quiz.html` | Generic quiz page used by math + cyber |
                                                | `templates/memory.html` | Memory board (only reachable when unlocked) |
                                                | Auth templates | login, register, verify, forgot, reset_verify, new_password |
