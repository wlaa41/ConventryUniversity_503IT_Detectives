#!/usr/bin/env python3
"""
buzzXzone – Eco Learning Hub
Professional 18-Slide Presentation with Morph Transitions
Team Detectives | 503IT | Coventry University | 2026

Run:  python buzzXzone_Presentation.py
Out:  buzzXzone_Presentation.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_CONNECTOR_TYPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import qn

# ─── COLOUR PALETTE ──────────────────────────────────────────────────────────
BG   = RGBColor(0x05, 0x10, 0x08)   # deep forest black
CARD = RGBColor(0x0C, 0x22, 0x12)   # card surface
MID  = RGBColor(0x11, 0x2C, 0x17)   # mid-tone
GRN  = RGBColor(0x00, 0xE5, 0x7A)   # spring-green (primary accent)
CYN  = RGBColor(0x00, 0xD4, 0xFF)   # electric cyan
GLD  = RGBColor(0xFF, 0xC4, 0x00)   # amber gold
LIM  = RGBColor(0x7F, 0xFF, 0x00)   # chartreuse
ORN  = RGBColor(0xFF, 0x80, 0x00)   # orange
PRP  = RGBColor(0xBB, 0x00, 0xFF)   # violet
RED  = RGBColor(0xFF, 0x44, 0x44)   # alert red
WHT  = RGBColor(0xFF, 0xFF, 0xFF)   # white
LGT  = RGBColor(0xBB, 0xF0, 0xCC)   # mint text
DIM  = RGBColor(0x55, 0x88, 0x66)   # muted text

W = Inches(13.33)
H = Inches(7.50)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
BLANK = prs.slide_layouts[6]   # blank – no placeholders


# ─── DRAWING PRIMITIVES ──────────────────────────────────────────────────────

def _new():
    return prs.slides.add_slide(BLANK)


def bg(s, c=BG):
    sh = s.shapes.add_shape(1, 0, 0, W, H)
    sh.fill.solid(); sh.fill.fore_color.rgb = c; sh.line.fill.background()


def rect(s, x, y, w, h, fill, brd=None, bw=Pt(1.2)):
    sh = s.shapes.add_shape(1, x, y, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if brd: sh.line.color.rgb = brd; sh.line.width = bw
    else:   sh.line.fill.background()
    return sh


def ln(s, x1, y1, x2, y2, c=GRN, w=Pt(1.5)):
    conn = s.shapes.add_connector(MSO_CONNECTOR_TYPE.STRAIGHT, x1, y1, x2, y2)
    conn.line.color.rgb = c; conn.line.width = w
    return conn


def txt(s, text, x, y, w, h, sz=18, b=False, c=WHT,
        al=PP_ALIGN.LEFT, it=False, fnt="Calibri"):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = al
    run = p.add_run()
    run.text = text; run.font.size = Pt(sz); run.font.bold = b
    run.font.italic = it; run.font.color.rgb = c; run.font.name = fnt
    return tb


def mtxt(s, lines, x, y, w, h, sz=16, b=False, c=WHT,
         al=PP_ALIGN.LEFT, sp=1.15, szs=None, cs=None, bs=None, fnt="Calibri"):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, line_text in enumerate(lines):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.alignment = al; p.line_spacing = sp
        run = p.add_run(); run.text = line_text
        run.font.size    = Pt(szs[i] if szs and i < len(szs) else sz)
        run.font.bold    = bs[i]  if bs  and i < len(bs)  else b
        run.font.color.rgb = cs[i] if cs  and i < len(cs)  else c
        run.font.name = fnt
    return tb


def morph(s):
    """Inject PowerPoint Morph slide transition."""
    NS_P  = "http://schemas.openxmlformats.org/presentationml/2006/main"
    NS_14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
    el = s._element
    for t in el.findall(qn('p:transition')):
        el.remove(t)
    el.append(parse_xml(
        f'<p:transition xmlns:p="{NS_P}" xmlns:p14="{NS_14}" spd="slow" smthBld="1">'
        f'<p14:morph dur="500" dir="n" useObjAnim="0"/>'
        f'</p:transition>'
    ))


# ─── LAYOUT HELPERS ──────────────────────────────────────────────────────────

def hdr(s, title, sub=None):
    """Top bar + title + optional subtitle + divider. Returns content-y."""
    rect(s, 0, 0, W, Inches(0.07), GRN)
    txt(s, title, Inches(0.5), Inches(0.1), Inches(12.3), Inches(0.85),
        sz=40, b=True, c=WHT)
    y = Inches(0.97)
    if sub:
        txt(s, sub, Inches(0.5), y, Inches(12.3), Inches(0.44), sz=20, c=GRN)
        y += Inches(0.44)
    ln(s, Inches(0.5), y + Inches(0.05), Inches(12.83), y + Inches(0.05), GRN, Pt(0.9))
    return y + Inches(0.18)


def stat_box(s, x, y, w, h, number, label, nc=GRN, lc=LGT):
    rect(s, x, y, w, h, CARD, brd=GRN, bw=Pt(1.2))
    txt(s, number, x, y + Inches(0.08), w, Inches(0.8),
        sz=42, b=True, c=nc, al=PP_ALIGN.CENTER)
    txt(s, label,  x, y + Inches(0.85), w, Inches(0.6),
        sz=13, c=lc, al=PP_ALIGN.CENTER)


def card(s, x, y, w, h, title, bullets, tc=GRN, bc=LGT, brd=GRN, sz=14, tsz=17):
    rect(s, x, y, w, h, CARD, brd=brd, bw=Pt(1.0))
    rect(s, x, y, w, Inches(0.055), brd)
    txt(s, title, x + Inches(0.15), y + Inches(0.10), w - Inches(0.3), Inches(0.45),
        sz=tsz, b=True, c=tc)
    ln(s, x + Inches(0.15), y + Inches(0.56),
       x + w  - Inches(0.15), y + Inches(0.56), brd, Pt(0.7))
    items = ["  • " + b for b in bullets]
    mtxt(s, items, x + Inches(0.15), y + Inches(0.65),
         w - Inches(0.3), h - Inches(0.75), sz=sz, c=bc)


def flow_box(s, x, y, w, h, label, sub=None, fill=MID, brd=GRN, tsz=15):
    rect(s, x, y, w, h, fill, brd=brd, bw=Pt(1.2))
    ty = y + Inches(0.12) if sub else y + Inches(0.18)
    txt(s, label, x + Inches(0.08), ty, w - Inches(0.16), Inches(0.5),
        sz=tsz, b=True, c=WHT, al=PP_ALIGN.CENTER)
    if sub:
        txt(s, sub, x + Inches(0.08), ty + Inches(0.5), w - Inches(0.16), Inches(0.55),
            sz=11, c=LGT, al=PP_ALIGN.CENTER)


def arr(s, x, y, c=GRN):
    ln(s, x, y, x + Inches(0.3), y, c, Pt(2.0))
    txt(s, "▶", x + Inches(0.17), y - Inches(0.15), Inches(0.25), Inches(0.3),
        sz=8, c=c, al=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 1 — TITLE / HERO
# ══════════════════════════════════════════════════════════════════════════════
def s01():
    s = _new(); bg(s)
    rect(s, 0, 0, W, Inches(3.62), RGBColor(0x07, 0x14, 0x0B))
    rect(s, 0, Inches(3.62), W, Inches(0.08), GRN)

    # Logo box
    rect(s, Inches(0.8), Inches(0.52), Inches(1.5), Inches(1.5), MID, brd=GRN, bw=Pt(2.5))
    txt(s, "BZ", Inches(0.8), Inches(0.65), Inches(1.5), Inches(1.2),
        sz=58, b=True, c=GRN, al=PP_ALIGN.CENTER)

    # Title
    txt(s, "buzzXzone", Inches(2.7), Inches(0.38), Inches(10.0), Inches(1.65),
        sz=76, b=True, c=GRN)
    txt(s, "Eco Learning Hub  —  Interactive Web Application",
        Inches(2.7), Inches(1.95), Inches(10.0), Inches(0.62), sz=26, c=LGT)
    txt(s, "Gamifying Digital Ecology  ·  Cybersecurity  ·  Mathematics  ·  Ages 10–18",
        Inches(2.7), Inches(2.57), Inches(10.0), Inches(0.5), sz=17, c=DIM)

    # Stat boxes
    for i, (n, l) in enumerate([("4", "Interactive\nGames"), ("6", "Team\nMembers"),
                                  ("3", "Difficulty\nLevels"), ("100%", "Serverless\nCloud")]):
        stat_box(s, Inches(1.0 + i * 2.9), Inches(3.88), Inches(2.5), Inches(1.5), n, l)

    # Footer
    rect(s, 0, Inches(5.75), W, Inches(1.75), RGBColor(0x03, 0x09, 0x05))
    txt(s, "TEAM DETECTIVES  |  503IT  |  COVENTRY UNIVERSITY  |  2026",
        0, Inches(5.95), W, Inches(0.5), sz=15, b=True, c=GRN, al=PP_ALIGN.CENTER)
    txt(s, "Shree Krishna Shrestha  ·  Saif Ullah  ·  Aaryut Chaudhary  "
           "·  Jina Giri  ·  Mohammad Zayed Alam  ·  Pushparaj Mahato",
        0, Inches(6.5), W, Inches(0.5), sz=13, c=DIM, al=PP_ALIGN.CENTER)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 2 — MEET THE TEAM
# ══════════════════════════════════════════════════════════════════════════════
TEAM = [
    ("Shree Krishna\nShrestha", "15681041", "Full-Stack Developer\nFrontend & Backend\nVercel Deployment", GRN),
    ("Saif Ullah",              "16115000", "Lead Content Creator\nGame & Quiz Design\nQuestion Architecture", CYN),
    ("Aaryut Chaudhary",        "16069541", "Researcher & Scrum Lead\nAgile Methodology\nTrello Coordinator", GLD),
    ("Jina Giri",               "16144790", "UI/UX Designer\nPrototype & Wireframes\nDocumentation", LIM),
    ("Mohammad Zayed Alam",     "16090763", "Project Manager\nBackend Auth & Routes\nTask Tracking", ORN),
    ("Pushparaj Mahato",        "16362947", "QA Tester & Reviewer\nBug Detection\nScore System Audit", PRP),
]

def s02():
    s = _new(); bg(s)
    cy = hdr(s, "Meet the Detectives", "503IT — Six Specialists, One Mission")
    CW, CH = Inches(4.1), Inches(2.3)
    GX, GY = Inches(0.265), Inches(0.2)
    SX, SY = Inches(0.25), cy + Inches(0.1)
    for i, (name, sid, role, acc) in enumerate(TEAM):
        col = i % 3; row = i // 3
        x = SX + col * (CW + GX)
        y = SY + row * (CH + GY)
        rect(s, x, y, CW, CH, CARD, brd=acc, bw=Pt(1.5))
        rect(s, x, y, CW, Inches(0.055), acc)
        txt(s, name,   x + Inches(0.15), y + Inches(0.1),  CW - Inches(0.3), Inches(0.7),
            sz=17, b=True, c=WHT)
        txt(s, f"#{sid}", x + Inches(0.15), y + Inches(0.78), CW - Inches(0.3), Inches(0.3),
            sz=12, c=acc)
        mtxt(s, role.split('\n'),
             x + Inches(0.15), y + Inches(1.06), CW - Inches(0.3), Inches(0.95),
             sz=13, c=LGT)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 3 — PROJECT OVERVIEW & VISION
# ══════════════════════════════════════════════════════════════════════════════
def s03():
    s = _new(); bg(s)
    cy = hdr(s, "Project Overview & Vision", "What We Built and Why It Matters")

    # Left column – mission
    LW = Inches(5.8)
    rect(s, Inches(0.5), cy, LW, Inches(5.5), CARD, brd=GRN, bw=Pt(1.0))
    rect(s, Inches(0.5), cy, LW, Inches(0.055), GRN)
    txt(s, "Our Mission", Inches(0.65), cy + Inches(0.12), LW - Inches(0.3), Inches(0.45),
        sz=20, b=True, c=GRN)
    ln(s, Inches(0.65), cy + Inches(0.6), Inches(6.15), cy + Inches(0.6), GRN, Pt(0.7))
    mission_lines = [
        "buzzXzone is a full-stack web application built to",
        "make learning fun, interactive, and meaningful for",
        "the next generation of digital citizens.",
        "",
        "We combine eco-education, mathematics, and",
        "cybersecurity awareness into four engaging games,",
        "delivered through a beautifully designed interface",
        "powered by modern cloud technology.",
        "",
        "Live at:  buzzxzone.vercel.app",
    ]
    mtxt(s, mission_lines, Inches(0.65), cy + Inches(0.7),
         LW - Inches(0.3), Inches(4.5), sz=15, c=LGT,
         cs=[LGT]*8 + [GLD, GRN])

    # Right column – 3 highlight cards
    RX = Inches(6.65)
    highlights = [
        ("Target Audience",  CYN, ["Students aged 10–18", "Beginners in cyber & eco-education",
                                    "Classroom and self-study use"]),
        ("Technology Stack", GLD, ["Python Flask · Supabase PostgreSQL",
                                    "Vanilla JS · CSS3 · Canvas 2D",
                                    "Deployed on Vercel (serverless)"]),
        ("Key Outcomes",     GRN, ["4 interactive learning games", "OTP-authenticated user accounts",
                                    "Gamified score & unlock system"]),
    ]
    for i, (title, acc, items) in enumerate(highlights):
        y = cy + Inches(0.05) + i * Inches(1.77)
        card(s, RX, y, Inches(6.18), Inches(1.68), title, items, tc=acc, brd=acc, sz=13, tsz=16)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 4 — PROBLEM STATEMENT
# ══════════════════════════════════════════════════════════════════════════════
def s04():
    s = _new(); bg(s)
    cy = hdr(s, "Problem Statement", "The Educational Gap We Are Closing")

    problems = [
        ("Low Engagement",       RED,  ["Traditional quizzes feel passive",
                                         "Students disengage within minutes",
                                         "No reward loop to motivate learning"]),
        ("Fragmented Knowledge", ORN,  ["Eco-education is rarely digital",
                                         "Cyber safety taught in isolation",
                                         "Math practice lacks real context"]),
        ("Accessibility Gap",    GLD,  ["Premium tools behind paywalls",
                                         "Complex UI alienates young users",
                                         "No unified multi-subject platform"]),
        ("Our Solution",         GRN,  ["buzzXzone: free, gamified, multi-subject",
                                         "Progressive difficulty keeps users engaged",
                                         "OTP-secured accounts + score rewards"]),
    ]
    CW, CH = Inches(5.9), Inches(2.65)
    for i, (title, acc, bullets) in enumerate(problems):
        col = i % 2; row = i // 2
        x = Inches(0.5) + col * (CW + Inches(0.53))
        y = cy + Inches(0.1) + row * (CH + Inches(0.35))
        card(s, x, y, CW, CH, title, bullets, tc=acc, brd=acc, sz=14, tsz=18)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 5 — AGILE SCRUM METHODOLOGY
# ══════════════════════════════════════════════════════════════════════════════
def s05():
    s = _new(); bg(s)
    cy = hdr(s, "Agile Scrum Methodology", "Our Development Framework")

    # Why Agile box
    rect(s, Inches(0.5), cy, Inches(4.0), Inches(5.55), CARD, brd=GRN, bw=Pt(1.0))
    rect(s, Inches(0.5), cy, Inches(4.0), Inches(0.055), GRN)
    txt(s, "Why We Chose Scrum", Inches(0.65), cy + Inches(0.1), Inches(3.7), Inches(0.45),
        sz=17, b=True, c=GRN)
    ln(s, Inches(0.65), cy + Inches(0.58), Inches(4.35), cy + Inches(0.58), GRN, Pt(0.7))
    why = [
        "  ✓  Iterative delivery in weekly sprints",
        "  ✓  Continuous feedback after each sprint",
        "  ✓  Flexible to changing requirements",
        "  ✓  Transparent team accountability",
        "  ✓  Risk management via retrospectives",
        "  ✓  Daily stand-ups on WhatsApp",
        "  ✓  GitHub for version control",
        "  ✓  Trello for task management",
    ]
    mtxt(s, why, Inches(0.65), cy + Inches(0.66), Inches(3.7), Inches(4.6),
         sz=14, c=LGT)

    # Scrum cycle diagram
    DX = Inches(5.0)
    txt(s, "Scrum Sprint Cycle", DX, cy + Inches(0.05), Inches(7.8), Inches(0.45),
        sz=18, b=True, c=GRN)

    scrum_items = [
        (DX + Inches(0.0), cy + Inches(0.7), "Product\nBacklog",     GRN),
        (DX + Inches(1.9), cy + Inches(0.7), "Sprint\nPlanning",     CYN),
        (DX + Inches(3.8), cy + Inches(0.7), "Sprint\nExecution",    GLD),
        (DX + Inches(5.7), cy + Inches(0.7), "Sprint\nReview",       ORN),
        (DX + Inches(2.8), cy + Inches(2.5), "Sprint\nRetrospective", PRP),
        (DX + Inches(0.9), cy + Inches(2.5), "Product\nIncrement",   GRN),
    ]
    for (bx, by, label, acc) in scrum_items:
        flow_box(s, bx, by, Inches(1.7), Inches(1.1), label, fill=MID, brd=acc, tsz=14)

    # Arrows
    for ax in [DX + Inches(1.72), DX + Inches(3.62), DX + Inches(5.52)]:
        arr(s, ax, cy + Inches(1.25), GRN)

    # Feedback loop label
    txt(s, "Continuous\nFeedback Loop", DX + Inches(1.5), cy + Inches(4.3),
        Inches(4.8), Inches(0.8), sz=13, c=DIM, al=PP_ALIGN.CENTER, it=True)

    # Sprint info cards (row of 4)
    sprint_info = [("Week 1", "Prototype\nDesign"), ("Week 2", "Core\nDevelopment"),
                   ("Week 3", "Integration\nTesting"), ("Week 4", "Deployment\nReview")]
    for i, (wk, act) in enumerate(sprint_info):
        sx = DX + i * Inches(1.95)
        rect(s, sx, cy + Inches(3.7), Inches(1.8), Inches(1.6), CARD, brd=GRN, bw=Pt(0.8))
        txt(s, wk,  sx + Inches(0.1), cy + Inches(3.78), Inches(1.6), Inches(0.38),
            sz=14, b=True, c=GRN, al=PP_ALIGN.CENTER)
        txt(s, act, sx + Inches(0.1), cy + Inches(4.14), Inches(1.6), Inches(0.8),
            sz=12, c=LGT, al=PP_ALIGN.CENTER)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 6 — SPRINT TIMELINE & ROADMAP
# ══════════════════════════════════════════════════════════════════════════════
def s06():
    s = _new(); bg(s)
    cy = hdr(s, "Sprint Timeline & Roadmap", "4-Week Agile Development Plan")

    sprints = [
        ("SPRINT 1", "Design & Setup",          GRN,
         ["Team roles assigned", "Wireframes & mockups created",
          "GitHub repository setup", "Trello board configured",
          "Tech stack finalized"]),
        ("SPRINT 2", "Core Development",         CYN,
         ["Flask app scaffolding", "Snake quiz engine built",
          "Math quiz (3 tiers) implemented", "OTP authentication system",
          "PostgreSQL schema designed"]),
        ("SPRINT 3", "Integration & Features",   GLD,
         ["Cyber security quiz added", "Memory Match mini-game",
          "Score & unlock system wired", "Supabase migration from SQLite",
          "UI polished with animations"]),
        ("SPRINT 4", "Testing & Deployment",     ORN,
         ["Full QA testing pass", "Bug fixes from Pushparaj",
          "Vercel deployment live", "Domain configured",
          "Final review & sign-off"]),
    ]
    CW = Inches(3.0)
    SX = Inches(0.42)

    # Timeline bar
    rect(s, SX, cy + Inches(0.48), W - Inches(0.84), Inches(0.04), GRN)

    for i, (sp, title, acc, tasks) in enumerate(sprints):
        x = SX + i * (CW + Inches(0.12))

        # Connector dot on timeline
        rect(s, x + CW / 2 - Inches(0.08), cy + Inches(0.38), Inches(0.16), Inches(0.16), acc)

        # Card
        rect(s, x, cy + Inches(0.7), CW, Inches(5.5), CARD, brd=acc, bw=Pt(1.3))
        rect(s, x, cy + Inches(0.7), CW, Inches(0.055), acc)

        # Sprint badge
        rect(s, x + Inches(0.15), cy + Inches(0.8), CW - Inches(0.3), Inches(0.38), MID, brd=acc, bw=Pt(0.8))
        txt(s, sp, x + Inches(0.15), cy + Inches(0.8), CW - Inches(0.3), Inches(0.38),
            sz=13, b=True, c=acc, al=PP_ALIGN.CENTER)
        txt(s, title, x + Inches(0.15), cy + Inches(1.22), CW - Inches(0.3), Inches(0.44),
            sz=16, b=True, c=WHT, al=PP_ALIGN.CENTER)
        ln(s, x + Inches(0.15), cy + Inches(1.7), x + CW - Inches(0.15), cy + Inches(1.7), acc, Pt(0.7))

        task_lines = ["  ✓ " + t for t in tasks]
        mtxt(s, task_lines, x + Inches(0.15), cy + Inches(1.8),
             CW - Inches(0.3), Inches(4.0), sz=13, c=LGT)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 7 — PRODUCT BACKLOG & USER STORIES
# ══════════════════════════════════════════════════════════════════════════════
def s07():
    s = _new(); bg(s)
    cy = hdr(s, "Product Backlog & User Stories", "Epics, Features, and Acceptance Criteria")

    epics = [
        ("EPIC 1: Authentication", GRN,
         "As a user, I want secure login so my progress is saved.",
         ["Register with username, email & password",
          "Login triggers 6-digit OTP to registered email",
          "OTP expires in 5 minutes for security",
          "Forgot password via same OTP mechanism",
          "Session persists until explicit logout"]),
        ("EPIC 2: Learning Games", CYN,
         "As a student, I want interactive games that teach me.",
         ["Auto-play Eco Snake Quiz with eco questions",
          "Math Quiz with Easy / Medium / Hard tiers",
          "Eco Cyber-Security Quiz (phishing to encryption)",
          "Memory Match unlocks at 100 points",
          "20-second timer per question enforced"]),
        ("EPIC 3: Scoring & Rewards", GLD,
         "As a player, I want to be rewarded for learning.",
         ["10 points per correct answer across all games",
          "High score persists in database per user",
          "Progress bar shows path to Memory Match unlock",
          "Dashboard reflects live high-score status",
          "Score submitted via secure API endpoint"]),
    ]
    EW = Inches(4.0)
    for i, (title, acc, story, tasks) in enumerate(epics):
        x = Inches(0.42) + i * (EW + Inches(0.24))
        CH = Inches(5.7)
        rect(s, x, cy + Inches(0.05), EW, CH, CARD, brd=acc, bw=Pt(1.2))
        rect(s, x, cy + Inches(0.05), EW, Inches(0.055), acc)
        txt(s, title, x + Inches(0.15), cy + Inches(0.12), EW - Inches(0.3), Inches(0.46),
            sz=16, b=True, c=acc)
        ln(s, x + Inches(0.15), cy + Inches(0.62), x + EW - Inches(0.15), cy + Inches(0.62), acc, Pt(0.7))
        txt(s, story, x + Inches(0.15), cy + Inches(0.7), EW - Inches(0.3), Inches(0.75),
            sz=13, c=LGT, it=True)
        ln(s, x + Inches(0.15), cy + Inches(1.5), x + EW - Inches(0.15), cy + Inches(1.5), DIM, Pt(0.5))
        txt(s, "Acceptance Criteria:", x + Inches(0.15), cy + Inches(1.58),
            EW - Inches(0.3), Inches(0.38), sz=13, b=True, c=GRN)
        items = ["✓ " + t for t in tasks]
        mtxt(s, items, x + Inches(0.15), cy + Inches(1.98),
             EW - Inches(0.3), Inches(3.4), sz=13, c=LGT)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 8 — SYSTEM ARCHITECTURE
# ══════════════════════════════════════════════════════════════════════════════
def s08():
    s = _new(); bg(s)
    cy = hdr(s, "System Architecture", "Full-Stack Serverless Web Application")

    layers = [
        ("PRESENTATION LAYER",  CYN, Inches(0.7),
         ["HTML5 templates (Jinja2)", "CSS3 — Dark forest theme + animations",
          "Vanilla JavaScript", "Canvas 2D — Snake engine"]),
        ("APPLICATION LAYER",   GRN, Inches(2.75),
         ["Python 3 + Flask framework", "Jinja2 template rendering",
          "Session-based auth + OTP logic", "REST API endpoints"]),
        ("DATA LAYER",          GLD, Inches(4.8),
         ["Supabase PostgreSQL (cloud)", "psycopg2 driver", "Connection pooler port 6543",
          "users table with high_score & unlock"]),
        ("DEPLOYMENT LAYER",    ORN, Inches(6.85),
         ["Vercel serverless platform", "vercel.json routing config",
          "GitHub CI/CD pipeline", "SSL/HTTPS enforced"]),
    ]
    LW = Inches(12.33)
    for i, (label, acc, y, desc) in enumerate(layers):
        lh = Inches(1.52)
        rect(s, Inches(0.5), cy + y, LW, lh, CARD, brd=acc, bw=Pt(1.1))
        rect(s, Inches(0.5), cy + y, Inches(0.055), lh, acc)
        txt(s, label, Inches(0.65), cy + y + Inches(0.08),
            Inches(2.5), Inches(0.4), sz=14, b=True, c=acc)
        line_items = ["▶  " + d for d in desc]
        mtxt(s, line_items, Inches(3.3), cy + y + Inches(0.1),
             Inches(9.35), lh - Inches(0.2), sz=13, c=LGT)
        if i < 3:
            arr(s, Inches(6.2), cy + y + lh, acc)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 9 — APPLICATION FEATURES OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
def s09():
    s = _new(); bg(s)
    cy = hdr(s, "Application Features Overview", "Four Games + Visual Extras + Secure Auth")

    features = [
        ("Eco Snake Quiz",        GRN,  ["Auto-playing snake animation",
                                          "Eco-themed question bank (JSON)",
                                          "Grow on correct, shrink on wrong",
                                          "20s timer per question  |  +10 pts"]),
        ("Math Quiz",             CYN,  ["3 difficulty tiers (Easy / Med / Hard)",
                                          "Topics: arithmetic to algebra & BIDMAS",
                                          "Shuffled question pool per session",
                                          "20s timer  |  +10 pts per correct"]),
        ("Eco Cyber Quiz",        GLD,  ["3 tiers: phishing to supply-chain attacks",
                                          "Eco-digital framing (e-waste, HTTPS)",
                                          "Same engine as Math Quiz (quiz.js)",
                                          "20s timer  |  +10 pts per correct"]),
        ("Memory Match",          ORN,  ["4×4 grid of 16 emoji-pair cards",
                                          "Locked until high score reaches 100 pts",
                                          "Dashboard shows unlock progress bar",
                                          "Tracks moves + elapsed time"]),
        ("Visual Extras",         LIM,  ["Neon mouse trail (greens, cyans, golds)",
                                          "Spark click explosion effect",
                                          "Animated capybara mascot on dashboard",
                                          "Staggered card entrance animations"]),
        ("OTP Authentication",    PRP,  ["Register → Login → OTP email sent",
                                          "6-digit code expires in 5 minutes",
                                          "Gmail SMTP or console fallback",
                                          "Forgot password via same OTP flow"]),
    ]
    CW, CH = Inches(4.0), Inches(2.4)
    GXG, GYG = Inches(0.24), Inches(0.2)
    SX, SY = Inches(0.42), cy + Inches(0.1)
    for i, (title, acc, items) in enumerate(features):
        col = i % 3; row = i // 3
        x = SX + col * (CW + GXG)
        y = SY + row * (CH + GYG)
        card(s, x, y, CW, CH, title, items, tc=acc, brd=acc, sz=13, tsz=17)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 10 — ECO SNAKE QUIZ (DEEP DIVE)
# ══════════════════════════════════════════════════════════════════════════════
def s10():
    s = _new(); bg(s)
    cy = hdr(s, "Eco Snake Quiz — Deep Dive", "Auto-Play Learning Engine")

    # Left: mechanics
    card(s, Inches(0.5), cy, Inches(5.8), Inches(5.6), "Game Mechanics",
         ["Snake moves autonomously — player never touches keyboard",
          "Eco-themed question appears at top of screen",
          "4 multiple-choice answers with 20-second countdown",
          "CORRECT: snake grows by +1 segment  |  +10 pts",
          "WRONG / TIMEOUT: snake shrinks by −1 segment",
          "GAME OVER: snake shrinks below minimum length",
          "Questions loaded from questions/snake.json",
          "Pool shuffled on every new session"],
         tc=GRN, brd=GRN, sz=14, tsz=18)

    # Right top: flow
    RX = Inches(6.65)
    rect(s, RX, cy, Inches(6.18), Inches(2.75), CARD, brd=CYN, bw=Pt(1.0))
    rect(s, RX, cy, Inches(6.18), Inches(0.055), CYN)
    txt(s, "Question Flow", RX + Inches(0.15), cy + Inches(0.1), Inches(5.88), Inches(0.45),
        sz=17, b=True, c=CYN)
    ln(s, RX + Inches(0.15), cy + Inches(0.58), RX + Inches(6.03), cy + Inches(0.58), CYN, Pt(0.7))

    flow_steps = ["Load & shuffle snake.json", "Display question + 4 answers",
                  "Start 20s countdown timer", "User selects answer",
                  "Evaluate: correct or wrong?", "Update snake & score  →  loop"]
    for j, step in enumerate(flow_steps):
        fx = RX + Inches(0.15) + (j % 2) * Inches(3.0)
        fy = cy + Inches(0.68) + (j // 2) * Inches(0.62)
        rect(s, fx, fy, Inches(2.7), Inches(0.52), MID, brd=CYN, bw=Pt(0.7))
        txt(s, f"{j+1}. {step}", fx + Inches(0.1), fy + Inches(0.06),
            Inches(2.5), Inches(0.4), sz=12, c=LGT)

    # Right bottom: scoring table
    rect(s, RX, cy + Inches(2.9), Inches(6.18), Inches(2.75), CARD, brd=GLD, bw=Pt(1.0))
    rect(s, RX, cy + Inches(2.9), Inches(6.18), Inches(0.055), GLD)
    txt(s, "Scoring & Constants", RX + Inches(0.15), cy + Inches(3.0),
        Inches(5.88), Inches(0.45), sz=17, b=True, c=GLD)
    ln(s, RX + Inches(0.15), cy + Inches(3.48), RX + Inches(6.03), cy + Inches(3.48), GLD, Pt(0.7))
    rows = [("QUESTION_TIME_SEC", "20", "Seconds allowed per question"),
            ("POINTS_PER_Q",      "10", "Points awarded per correct answer"),
            ("UNLOCK_THRESHOLD",  "100", "Score needed to unlock Memory Match")]
    for j, (const, val, desc) in enumerate(rows):
        ry = cy + Inches(3.58) + j * Inches(0.64)
        rect(s, RX + Inches(0.15), ry, Inches(5.88), Inches(0.55), MID)
        txt(s, const, RX + Inches(0.25), ry + Inches(0.07), Inches(2.4), Inches(0.4),
            sz=13, b=True, c=GRN)
        txt(s, val,   RX + Inches(2.7),  ry + Inches(0.07), Inches(0.7), Inches(0.4),
            sz=13, b=True, c=GLD)
        txt(s, desc,  RX + Inches(3.45), ry + Inches(0.07), Inches(2.5), Inches(0.4),
            sz=12, c=LGT)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 11 — MATH QUIZ & ECO CYBER QUIZ
# ══════════════════════════════════════════════════════════════════════════════
def s11():
    s = _new(); bg(s)
    cy = hdr(s, "Math Quiz & Eco Cyber-Security Quiz", "Dual-Subject Adaptive Learning")

    # Math Quiz
    card(s, Inches(0.5), cy, Inches(6.0), Inches(5.6), "Math Quiz",
         [], tc=CYN, brd=CYN, tsz=20)
    tiers_math = [
        ("Easy", GRN,   ["Single-digit add / subtract", "Simple multiplication & division"]),
        ("Medium", GLD, ["Two-digit arithmetic", "Multiplication tables & long division"]),
        ("Hard", RED,   ["BIDMAS / BODMAS rules", "Fractions, %, powers & simple algebra"]),
    ]
    for j, (tier, acc, items) in enumerate(tiers_math):
        ty = cy + Inches(0.7) + j * Inches(1.55)
        rect(s, Inches(0.65), ty, Inches(5.7), Inches(1.44), MID, brd=acc, bw=Pt(0.9))
        txt(s, tier, Inches(0.8), ty + Inches(0.1), Inches(1.2), Inches(0.38),
            sz=15, b=True, c=acc)
        items_t = ["• " + it for it in items]
        mtxt(s, items_t, Inches(2.1), ty + Inches(0.1),
             Inches(4.1), Inches(1.2), sz=13, c=LGT)

    # Cyber Quiz
    card(s, Inches(6.83), cy, Inches(6.0), Inches(5.6), "Eco Cyber-Security Quiz",
         [], tc=GLD, brd=GLD, tsz=20)
    tiers_cyber = [
        ("Easy", GRN,   ["Phishing basics & safe browsing", "Password hygiene & device safety"]),
        ("Medium", GLD, ["2FA, HTTPS, fake eco-deals", "E-waste data wiping practices"]),
        ("Hard", RED,   ["Social engineering & ransomware", "Supply-chain attacks & encryption"]),
    ]
    for j, (tier, acc, items) in enumerate(tiers_cyber):
        ty = cy + Inches(0.7) + j * Inches(1.55)
        rect(s, Inches(6.98), ty, Inches(5.7), Inches(1.44), MID, brd=acc, bw=Pt(0.9))
        txt(s, tier, Inches(7.13), ty + Inches(0.1), Inches(1.2), Inches(0.38),
            sz=15, b=True, c=acc)
        items_c = ["• " + it for it in items]
        mtxt(s, items_c, Inches(8.43), ty + Inches(0.1),
             Inches(4.1), Inches(1.2), sz=13, c=LGT)

    # Shared engine note
    rect(s, Inches(0.5), cy + Inches(5.7), Inches(12.33), Inches(0.58), MID, brd=DIM, bw=Pt(0.6))
    txt(s, "Both quizzes share the same quiz.js engine and quiz.html template — only the question bank changes.",
        Inches(0.7), cy + Inches(5.76), Inches(11.93), Inches(0.45),
        sz=14, c=DIM, it=True)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 12 — MEMORY MATCH & AUTHENTICATION FLOW
# ══════════════════════════════════════════════════════════════════════════════
def s12():
    s = _new(); bg(s)
    cy = hdr(s, "Memory Match & Authentication", "Reward System + Secure Access Flow")

    # Memory Match
    card(s, Inches(0.5), cy, Inches(5.8), Inches(5.6), "Memory Match Mini-Game",
         ["Locked by default on the dashboard",
          "Progress bar shows % toward 100-point unlock",
          "Unlocks permanently once threshold is reached",
          "4×4 grid — 16 cards, 8 emoji pairs",
          "Tracks total moves and elapsed time",
          "UNLOCK_THRESHOLD constant in app.py (default: 100)",
          "All game cards have staggered entrance animation"],
         tc=ORN, brd=ORN, sz=14, tsz=18)

    # Auth flow
    RX = Inches(6.65)
    rect(s, RX, cy, Inches(6.18), Inches(5.6), CARD, brd=PRP, bw=Pt(1.0))
    rect(s, RX, cy, Inches(6.18), Inches(0.055), PRP)
    txt(s, "OTP Authentication Flow", RX + Inches(0.15), cy + Inches(0.1),
        Inches(5.88), Inches(0.45), sz=18, b=True, c=PRP)
    ln(s, RX + Inches(0.15), cy + Inches(0.58), RX + Inches(6.03), cy + Inches(0.58), PRP, Pt(0.7))

    steps = [("Register",      "Username, email, password hashed with Werkzeug"),
             ("Login",         "Email + password verified against database"),
             ("OTP Sent",      "6-digit code sent via Gmail SMTP (or console)"),
             ("Verify OTP",    "User enters code — expires in 5 minutes"),
             ("Dashboard",     "Session created  |  progress restored"),
             ("Forgot PW",     "Same OTP flow resets password securely"),
             ("Logout",        "Session cleared  |  redirect to login")]
    for j, (step, desc) in enumerate(steps):
        sy = cy + Inches(0.7) + j * Inches(0.68)
        rect(s, RX + Inches(0.15), sy, Inches(5.88), Inches(0.6), MID, brd=PRP, bw=Pt(0.6))
        txt(s, f"{j+1:02d}  {step}", RX + Inches(0.28), sy + Inches(0.08),
            Inches(1.8), Inches(0.44), sz=14, b=True, c=PRP)
        txt(s, desc, RX + Inches(2.1), sy + Inches(0.1),
            Inches(3.75), Inches(0.4), sz=12, c=LGT)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 13 — UI/UX DESIGN SYSTEM
# ══════════════════════════════════════════════════════════════════════════════
def s13():
    s = _new(); bg(s)
    cy = hdr(s, "UI/UX Design System", "Dark Forest Theme — Visual Identity")

    # Colour swatches
    txt(s, "Brand Colour Palette", Inches(0.5), cy + Inches(0.05),
        Inches(4.5), Inches(0.42), sz=17, b=True, c=GRN)
    swatches = [
        (GRN,  "#00E57A  Spring Green",  "Primary accent"),
        (CYN,  "#00D4FF  Electric Cyan", "Secondary accent"),
        (GLD,  "#FFC400  Amber Gold",    "Highlight"),
        (LIM,  "#7FFF00  Chartreuse",    "Hover state"),
        (BG,   "#051008  Forest Black",  "Background"),
        (CARD, "#0C2212  Card Surface",  "Card bg"),
    ]
    for j, (col, name, desc) in enumerate(swatches):
        row = j // 2; c2 = j % 2
        sx = Inches(0.5) + c2 * Inches(3.2)
        sy = cy + Inches(0.55) + row * Inches(0.72)
        rect(s, sx, sy, Inches(0.52), Inches(0.52), col, brd=DIM, bw=Pt(0.5))
        txt(s, name, sx + Inches(0.6), sy + Inches(0.04), Inches(2.4), Inches(0.26),
            sz=13, b=True, c=WHT)
        txt(s, desc, sx + Inches(0.6), sy + Inches(0.28), Inches(2.4), Inches(0.22),
            sz=11, c=DIM)

    # Typography
    TX = Inches(6.83)
    rect(s, TX, cy, Inches(6.0), Inches(3.4), CARD, brd=CYN, bw=Pt(1.0))
    rect(s, TX, cy, Inches(6.0), Inches(0.055), CYN)
    txt(s, "Typography & Sizing", TX + Inches(0.15), cy + Inches(0.1),
        Inches(5.7), Inches(0.45), sz=17, b=True, c=CYN)
    type_rows = [("Slide Title",    "Calibri Bold 40pt",     WHT),
                 ("Section Header", "Calibri Bold 18–20pt", GRN),
                 ("Body Text",      "Calibri Regular 14–16pt", LGT),
                 ("Dim / Labels",   "Calibri Regular 12–13pt", DIM),
                 ("Stat Numbers",   "Calibri Bold 42pt",     GRN)]
    for j, (typ, spec, c) in enumerate(type_rows):
        ty = cy + Inches(0.65) + j * Inches(0.54)
        txt(s, typ,  TX + Inches(0.2),  ty, Inches(2.4), Inches(0.44), sz=13, c=WHT)
        txt(s, spec, TX + Inches(2.65), ty, Inches(3.1), Inches(0.44), sz=13, c=c)

    # Animations
    rect(s, TX, cy + Inches(3.5), Inches(6.0), Inches(2.15), CARD, brd=GLD, bw=Pt(1.0))
    rect(s, TX, cy + Inches(3.5), Inches(6.0), Inches(0.055), GLD)
    txt(s, "Animations & Visual Effects", TX + Inches(0.15), cy + Inches(3.6),
        Inches(5.7), Inches(0.45), sz=17, b=True, c=GLD)
    anim = ["Neon mouse trail — particles cycle greens, cyans, golds",
            "Spark click explosion on every tap / click",
            "Capybara mascot: walk, sit, eat, wave, blink, ear-twitch",
            "Dashboard cards: staggered entrance + hover glow bar"]
    for j, a in enumerate(anim):
        txt(s, "⚡ " + a, TX + Inches(0.2), cy + Inches(4.1) + j * Inches(0.36),
            Inches(5.7), Inches(0.34), sz=12, c=LGT)

    # Key file note
    rect(s, Inches(0.5), cy + Inches(5.7), Inches(6.0), Inches(0.58), MID, brd=GRN, bw=Pt(0.6))
    txt(s, "Key files:  static/style.css  ·  base.html  ·  dashboard.html  ·  game.js",
        Inches(0.65), cy + Inches(5.78), Inches(5.7), Inches(0.4), sz=13, c=GRN)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 14 — DATABASE DESIGN
# ══════════════════════════════════════════════════════════════════════════════
def s14():
    s = _new(); bg(s)
    cy = hdr(s, "Database Design", "Supabase PostgreSQL — Cloud-Native Storage")

    # Schema table
    rect(s, Inches(0.5), cy, Inches(7.8), Inches(5.7), CARD, brd=GRN, bw=Pt(1.2))
    rect(s, Inches(0.5), cy, Inches(7.8), Inches(0.055), GRN)
    txt(s, "Table: users", Inches(0.65), cy + Inches(0.1), Inches(7.5), Inches(0.45),
        sz=20, b=True, c=GRN)
    ln(s, Inches(0.65), cy + Inches(0.58), Inches(8.15), cy + Inches(0.58), GRN, Pt(0.7))

    # Column headers
    headers = [("Column", Inches(0.65)), ("Type", Inches(2.65)), ("Default", Inches(4.45)),
               ("Notes", Inches(5.7))]
    HY = cy + Inches(0.66)
    rect(s, Inches(0.5), HY, Inches(7.8), Inches(0.44), MID)
    for hname, hx in headers:
        txt(s, hname, hx, HY + Inches(0.06), Inches(1.8), Inches(0.34),
            sz=13, b=True, c=GLD)

    cols_data = [
        ("id",               "SERIAL",  "—",         "PRIMARY KEY auto-increment"),
        ("username",         "TEXT",    "NOT NULL",   "Player display name"),
        ("email",            "TEXT",    "NOT NULL",   "Unique email (login key)"),
        ("password",         "TEXT",    "NOT NULL",   "Werkzeug hashed password"),
        ("high_score",       "INTEGER", "0",          "All-time highest score"),
        ("memory_unlocked",  "INTEGER", "0",          "1 = Memory Match accessible"),
    ]
    for j, (col, typ, default, note) in enumerate(cols_data):
        ry = HY + Inches(0.44) + j * Inches(0.7)
        bg_c = CARD if j % 2 == 0 else MID
        rect(s, Inches(0.5), ry, Inches(7.8), Inches(0.65), bg_c)
        txt(s, col,     Inches(0.65), ry + Inches(0.12), Inches(1.9), Inches(0.4),
            sz=14, b=True, c=CYN)
        txt(s, typ,     Inches(2.65), ry + Inches(0.12), Inches(1.7), Inches(0.4),
            sz=13, c=GRN)
        txt(s, default, Inches(4.45), ry + Inches(0.12), Inches(1.2), Inches(0.4),
            sz=13, c=GLD)
        txt(s, note,    Inches(5.7),  ry + Inches(0.12), Inches(2.45), Inches(0.4),
            sz=12, c=LGT)

    # Right panel
    RX = Inches(8.75)
    panels = [
        ("Connection Config",  GLD,
         ["Provider: Supabase (cloud PostgreSQL)",
          "Driver: psycopg2-binary",
          "Mode: Transaction pooler (port 6543)",
          "sslmode=require enforced",
          "Credentials stored in Vercel env vars"]),
        ("Auto-Creation SQL",  CYN,
         ["CREATE TABLE IF NOT EXISTS users (",
          "  id   SERIAL PRIMARY KEY,",
          "  email TEXT NOT NULL UNIQUE,",
          "  high_score INTEGER DEFAULT 0,",
          "  memory_unlocked INTEGER DEFAULT 0",
          ");"]),
        ("API Endpoints",      GRN,
         ["POST /api/submit_score",
          "  → Updates high_score & unlock status",
          "GET /api/progress",
          "  → Returns score, unlock, progress %"]),
    ]
    PH = [Inches(2.0), Inches(2.4), Inches(1.8)]
    py = cy + Inches(0.0)
    for i, (title, acc, items) in enumerate(panels):
        card(s, RX, py, Inches(4.08), PH[i], title, items, tc=acc, brd=acc, sz=12, tsz=15)
        py += PH[i] + Inches(0.18)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 15 — SECURITY IMPLEMENTATION
# ══════════════════════════════════════════════════════════════════════════════
def s15():
    s = _new(); bg(s)
    cy = hdr(s, "Security Implementation", "Defence-in-Depth Across All Layers")

    sec_items = [
        ("Password Security",       GRN,
         ["Passwords hashed with Werkzeug (PBKDF2-SHA256)",
          "Plain-text passwords never stored",
          "Hash verified on every login attempt",
          "Minimum-length enforcement on registration"]),
        ("OTP Authentication",      CYN,
         ["6-digit one-time password per login",
          "Stored in server session (not database)",
          "Expires in 5 minutes automatically",
          "Same mechanism for forgot-password flow"]),
        ("Session Management",      GLD,
         ["Flask session with signed SECRET_KEY",
          "FLASK_SECRET_KEY stored as environment variable",
          "Session cleared on logout and OTP mismatch",
          "Server-side session; no JWT exposure"]),
        ("Environment Variables",   ORN,
         ["DATABASE_URL — Supabase connection string",
          "FLASK_SECRET_KEY — session signing key",
          "GMAIL_USER / GMAIL_PASSWORD — OTP email",
          "All set in Vercel dashboard (never in code)"]),
        ("Transport Security",      PRP,
         ["Vercel enforces HTTPS / SSL on all routes",
          "Supabase requires sslmode=require",
          "No plain HTTP endpoints in production",
          "CORS handled by Vercel edge config"]),
        ("Input Validation",        RED,
         ["Email uniqueness enforced at DB level",
          "OTP compared with constant-time equality",
          "Score submitted via POST JSON (not URL params)",
          "Jinja2 auto-escaping prevents XSS"]),
    ]
    CW, CH = Inches(4.0), Inches(2.55)
    GXG, GYG = Inches(0.24), Inches(0.2)
    SX, SY = Inches(0.42), cy + Inches(0.1)
    for i, (title, acc, items) in enumerate(sec_items):
        col = i % 3; row = i // 3
        x = SX + col * (CW + GXG)
        y = SY + row * (CH + GYG)
        card(s, x, y, CW, CH, title, items, tc=acc, brd=acc, sz=13, tsz=16)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 16 — TESTING & QUALITY ASSURANCE
# ══════════════════════════════════════════════════════════════════════════════
def s16():
    s = _new(); bg(s)
    cy = hdr(s, "Testing & Quality Assurance", "Pushparaj Mahato — QA Lead")

    # Left: test types
    test_cards = [
        ("Functional Testing", GRN,
         ["All 4 game modes played end-to-end",
          "Correct answer gives +10 pts verified",
          "Wrong/timeout triggers expected outcome",
          "Memory Match unlock at exact 100 pts"]),
        ("Authentication Testing", CYN,
         ["OTP email delivery confirmed",
          "Expired OTP (5 min) correctly rejected",
          "Password reset flow tested top-to-bottom",
          "Duplicate email registration blocked"]),
        ("UI / Cross-Browser Testing", GLD,
         ["Tested on Chrome, Firefox, Edge",
          "Responsive on desktop and tablet",
          "Animations render without flicker",
          "Neon trail smooth at 60 fps"]),
        ("Score & Unlock Testing", ORN,
         ["Score persists on page reload",
          "High score only updates if new score > old",
          "Progress bar updates live via /api/progress",
          "Memory Match card appears post-unlock"]),
    ]
    CW, CH = Inches(5.8), Inches(2.55)
    for i, (title, acc, items) in enumerate(test_cards):
        col = i % 2; row = i // 2
        x = Inches(0.5) + col * (CW + Inches(0.33))
        y = cy + Inches(0.05) + row * (CH + Inches(0.2))
        card(s, x, y, CW, CH, title, items, tc=acc, brd=acc, sz=13, tsz=17)

    # Bottom: QA summary strip
    rect(s, Inches(0.5), cy + Inches(5.5), Inches(12.33), Inches(0.75), MID, brd=GRN, bw=Pt(0.8))
    summary = [
        ("Bugs Reported", "12", GRN),
        ("Bugs Fixed",    "12", GRN),
        ("Test Rounds",   "3",  CYN),
        ("Pass Rate",     "100%", LIM),
    ]
    for i, (label, val, acc) in enumerate(summary):
        sx = Inches(0.8) + i * Inches(3.1)
        txt(s, val,   sx, cy + Inches(5.52), Inches(1.5), Inches(0.42),
            sz=26, b=True, c=acc, al=PP_ALIGN.CENTER)
        txt(s, label, sx, cy + Inches(5.93), Inches(1.5), Inches(0.28),
            sz=12, c=DIM, al=PP_ALIGN.CENTER)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 17 — DEPLOYMENT & LIVE APPLICATION
# ══════════════════════════════════════════════════════════════════════════════
def s17():
    s = _new(); bg(s)
    cy = hdr(s, "Deployment & Live Application", "Serverless CI/CD Pipeline on Vercel")

    # Pipeline flow (top)
    pipeline = [
        ("Local Dev\npython app.py", GRN),
        ("Git Commit\ngit push origin", CYN),
        ("GitHub Repo\nCI Trigger",    GLD),
        ("Vercel Build\n@vercel/python", ORN),
        ("Live Deploy\nbuzzxzone.vercel.app", PRP),
    ]
    PW, PH_= Inches(2.2), Inches(1.12)
    for i, (label, acc) in enumerate(pipeline):
        px = Inches(0.5) + i * (PW + Inches(0.1))
        flow_box(s, px, cy + Inches(0.05), PW, PH_, label, fill=MID, brd=acc, tsz=13)
        if i < 4:
            arr(s, px + PW + Inches(0.02), cy + Inches(0.05) + PH_ / 2, acc)

    # Left: config
    card(s, Inches(0.5), cy + Inches(1.3), Inches(5.8), Inches(3.0),
         "vercel.json Configuration",
         ['{"version": 2,',
          ' "builds": [{"src": "app.py",',
          '   "use": "@vercel/python"}],',
          ' "routes": [{"src": "/(.*)",',
          '   "dest": "app.py"}]}'],
         tc=GLD, brd=GLD, sz=13, tsz=16)

    card(s, Inches(0.5), cy + Inches(4.5), Inches(5.8), Inches(1.25),
         "Health Check Endpoint",
         ["GET /health  →  {\"status\": \"ok\", \"database\": \"connected\"}",
          "Verifies Supabase connection post-deploy"],
         tc=GRN, brd=GRN, sz=13, tsz=15)

    # Right: env vars + URLs
    card(s, Inches(6.83), cy + Inches(1.3), Inches(6.0), Inches(2.1),
         "Environment Variables (Vercel Dashboard)",
         ["DATABASE_URL = postgresql://...pooler...port 6543",
          "FLASK_SECRET_KEY = <random 32-char string>",
          "GMAIL_USER = sender@gmail.com (optional)",
          "GMAIL_PASSWORD = <app-specific password>"],
         tc=ORN, brd=ORN, sz=13, tsz=16)

    card(s, Inches(6.83), cy + Inches(3.6), Inches(6.0), Inches(2.15),
         "Live URLs & Resources",
         ["Live app:   buzzxzone.vercel.app",
          "Health:     buzzxzone.vercel.app/health",
          "Repository: github.com/wlaa41/ConventryUniversity...",
          "DB:         Supabase project dashboard"],
         tc=CYN, brd=CYN, sz=13, tsz=16)
    morph(s)


# ══════════════════════════════════════════════════════════════════════════════
#  SLIDE 18 — RETROSPECTIVE, LESSONS & FUTURE
# ══════════════════════════════════════════════════════════════════════════════
def s18():
    s = _new(); bg(s)
    cy = hdr(s, "Retrospective, Lessons & Future", "Sprint 4 Review — What We Learned")

    # What went well
    card(s, Inches(0.5), cy, Inches(3.9), Inches(5.6),
         "What Went Well",
         ["Agile sprints kept us on schedule",
          "GitHub version control prevented conflicts",
          "Trello gave clear task visibility",
          "Supabase migration was seamless",
          "Vercel zero-downtime deployment",
          "OTP auth worked first time",
          "Team roles were well-defined"],
         tc=GRN, brd=GRN, sz=13, tsz=17)

    # What was challenging
    card(s, Inches(4.65), cy, Inches(3.9), Inches(5.6),
         "Challenges Faced",
         ["SQLite → Supabase migration mid-sprint",
          "Vercel read-only filesystem adaptation",
          "Environment variable management",
          "OTP email delay in some providers",
          "Canvas performance tuning on mobile",
          "Merge conflicts in shared templates",
          "Coordinating across 6 schedules"],
         tc=RED, brd=RED, sz=13, tsz=17)

    # Future roadmap
    card(s, Inches(8.8), cy, Inches(4.03), Inches(5.6),
         "Future Roadmap",
         ["Leaderboard — global high-score table",
          "More quiz categories (science, geography)",
          "Mobile-native PWA with offline mode",
          "Teacher dashboard & class reports",
          "AI-generated adaptive questions",
          "Multiplayer competitive mode",
          "Accessibility — screen reader support",
          "Dark/light theme toggle"],
         tc=CYN, brd=CYN, sz=13, tsz=17)

    # Closing banner
    rect(s, 0, Inches(7.0), W, Inches(0.5), GRN)
    txt(s, "Thank you  —  Questions?  —  buzzxzone.vercel.app  —  Team Detectives | 503IT | Coventry University 2026",
        0, Inches(7.02), W, Inches(0.44),
        sz=14, b=True, c=BG, al=PP_ALIGN.CENTER)
    morph(s)


# ─── BUILD ALL SLIDES ─────────────────────────────────────────────────────────
print("Building slides...")
s01(); print("  Slide  1/18 - Title")
s02(); print("  Slide  2/18 - Team")
s03(); print("  Slide  3/18 - Overview")
s04(); print("  Slide  4/18 - Problem")
s05(); print("  Slide  5/18 - Agile Scrum")
s06(); print("  Slide  6/18 - Sprint Timeline")
s07(); print("  Slide  7/18 - Backlog")
s08(); print("  Slide  8/18 - Architecture")
s09(); print("  Slide  9/18 - Features")
s10(); print("  Slide 10/18 - Snake Quiz")
s11(); print("  Slide 11/18 - Math & Cyber Quiz")
s12(); print("  Slide 12/18 - Memory & Auth")
s13(); print("  Slide 13/18 - UI/UX")
s14(); print("  Slide 14/18 - Database")
s15(); print("  Slide 15/18 - Security")
s16(); print("  Slide 16/18 - Testing")
s17(); print("  Slide 17/18 - Deployment")
s18(); print("  Slide 18/18 - Retrospective")

OUTPUT = "buzzXzone_Presentation.pptx"
prs.save(OUTPUT)
print(f"\nSaved: {OUTPUT}")
print(f"Slides: {len(prs.slides)}")
