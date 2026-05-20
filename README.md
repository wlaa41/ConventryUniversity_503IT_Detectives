

> **A child-friendly, eco-themed cyber-security and maths learning game for ages 6–15**
> Developed as part of Coventry University | Module: 503IT Communication and Collaboration

---
# Teacher Will is the very best 

## 📖 Project Overview

**pooki** is an interactive, browser-based educational game built with Flask (Python). It targets students aged **6–15** and combines eco/nature theming with four engaging mini-games designed to teach *.*cyber-security awareness**, **digital safety**, and **mathematics** in a fun, age-appropriate way.

The project responds directly to the module client brief: *Cyber-Smart Gaming for Education* — producing a fully testable prototype that meets the accessibility, educational value, and replayability requirements set out by the client.

---

## 🎮 The Games

### 1. 🐍 Auto-Play Eco Snake Quiz

The snake moves automatically — no keyboard control needed, keeping it accessible for young learners. Players focus entirely on answering **eco-themed maths questions**.

- ✅ Correct answer → snake grows +1 segment, +10 points
- ❌ Wrong or timed-out answer → snake shrinks
- ☠️ Game over when the snake shrinks below minimum length
- ⏱️ 1-minute timer per question

---

### 2. ➗ Math Quiz

A classic maths challenge with three difficulty levels:

| Level | Content |
|-------|---------|
| **Easy** | Single-digit arithmetic |
| **Medium** | Two-digit sums, multiplication tables, division |
| **Hard** | BIDMAS, fractions, percentages, powers, simple algebra |

- 10 points per correct answer
- 1-minute timer per question

---

### 3. 🔐 Eco-Friendly Cyber-Security Quiz

Cyber-security knowledge presented through an eco-digital lens. Same Easy / Medium / Hard structure covering topics such as:

- Password hygiene and 2FA
- Recognising phishing and "green deal" scams
- Safe device recycling and e-waste
- Ransomware, encryption, and online privacy
- Energy-efficient digital habits

---

### 4. 🧩 Memory Match *(Unlockable)*

A **4×4 emoji-pair matching game** (8 pairs). Locked by default to encourage progression.

- 🔒 Unlocks once the player's **best score reaches 100 points** (configurable via `UNLOCK_THRESHOLD` in `app.py`)
- Dashboard shows a 🔒 card with a progress bar until unlocked

---

## 🔐 Authentication & Security

- User registration with **email OTP verification** (Gmail SMTP)
- Secure login flow
- Full **forgot-password / OTP-reset** flow
- Local **SQLite** database (`pooki.db`) — no external database required

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3 / Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (via SQLAlchemy or raw sqlite3) |
| Email | Gmail SMTP (OTP delivery) |
| Version Control | Git / GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/wlaa41/ConventryUniversity_503IT_Detectives.git
cd ConventryUniversity_503IT_Detectives

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Create a .env file with:
# MAIL_USERNAME=your_gmail@gmail.com
# MAIL_PASSWORD=your_app_password
# SECRET_KEY=your_secret_key

# 5. Run the app
flask run
```

Open your browser at `http://127.0.0.1:5000`

---

## 📁 Repository Structure

```
ConventryUniversity_503IT_Detectives/
├── app.py                  # Main Flask application & config
├── pooki.db                # SQLite database (auto-created)
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates (Jinja2)
│   ├── index.html
│   ├── dashboard.html
│   ├── snake_quiz.html
│   ├── math_quiz.html
│   ├── cyber_quiz.html
│   └── memory_match.html
├── static/                 # CSS, JS, images & assets
│   ├── css/
│   ├── js/
│   └── images/
└── README.md
```

---

## 👥 Team — The Detectives

| Role | Name | Student ID |
|------|------|-----------|
| 📝 **Content Lead** | Saif Ullah | 116115000 |
| 🔍 **Researcher** | Aaryut Chaudhary | 16069541 |
| 🎨 **Designer & Coder** | Shree Krishna Shrestha | 15681041 |
| 📋 **Project Manager** | Mohammad Zayed Alam | 16090763 |
| 🖼️ **Prototype Designer** | Jina Giri | 16144790 |
| 🧪 **Tester** | Pushparaj Mahato | 16362947 |

### Role Descriptions

**📝 Content Lead — Saif Ullah**
Responsible for writing and structuring all project content, leading report writing and documentation quality, ensuring clarity and academic tone in written work, and supporting presentation script development.

**🔍 Researcher — Aaryut Chaudhary**
Conducts cybersecurity research covering threats, risks, and tools; gathers credible sources and references; supports content development with accurate information; and maintains research documentation.

**🎨 Designer & Coder — Shree Krishna Shrestha**
Designs project structure and visual elements, handles GitHub repository setup and formatting, supports technical organisation of files and assets, and improves presentation and report layout design.

**📋 Project Manager — Mohammad Zayed Alam**
Oversees project progress and deadlines, coordinates team communication and task distribution, ensures tasks are completed on time, and monitors overall workflow and quality control.

**🖼️ Prototype Designer — Jina Giri**
Designs diagrams, visuals, and conceptual models; supports presentation design and layout; creates visual explanations of cybersecurity concepts; and assists in UI/UX style representation of ideas.

**🧪 Tester — Pushparaj Mahato**
Reviews project content for errors and consistency, checks report accuracy and formatting, tests presentation flow and clarity, and ensures final submission quality.

---

## 🎯 Educational Design Rationale

**Target Audience:** Students aged 6–15 (adjustable difficulty accommodates the full range)

**Cyber-security concepts covered:**
- Password hygiene and multi-factor authentication
- Phishing recognition and scam awareness
- Online privacy and personal data management
- Safe device disposal and digital sustainability
- Ransomware, encryption basics

**Accessibility considerations:**
- Auto-play snake removes motor-skill barriers
- Difficulty levels cater to different age groups within the range
- Emoji-based memory game is intuitive for younger players
- Clean, eco-friendly visual design avoids sensory overload

**Replayability:**
- Randomised question pools
- Score-based unlock mechanic encourages return visits
- Multiple difficulty tiers provide a progression path

---

## 📚 Module Context

- **University:** Coventry University Group
- **Module:** 503IT — Communication and Collaboration
- **Assignment:** Collaborative Solution Development and Professional Reflection
- **Submission Deadline:** 12th June 2026 at 18:00 hrs
- **Assessment Type:** Composite (Group Presentation + Individual Portfolio)

---

## ⚠️ Disclaimer

This project was developed solely for academic assessment purposes at Coventry University. All game content is age-appropriate and safe for children aged 6–15. No harmful, violent, or adult content is included at any level.

---

*Made with 💚 by The Detectives — Coventry University 503IT*
