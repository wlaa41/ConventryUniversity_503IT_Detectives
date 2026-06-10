# Week 2 — Activities Completed

## Overview

Week 2 focused on developing quiz game components, strengthening backend structure,
expanding question content, and improving team coordination through Agile tools.

## Activities

### Quiz System Development

The Cyber Security Quiz and Math Quiz sections were developed and refined with proper
multiple-choice formatting for better user interaction and learning experience.

**Cyber Security Quiz topics covered:**
- Phishing and email scams
- Malware and antivirus
- Password security
- Firewalls and network security
- Two-factor authentication (2FA)

**Math Quiz topics covered:**
- Basic arithmetic (addition, subtraction, multiplication, division)
- Percentages and fractions
- Number patterns and sequences

Questions were structured in JSON format (`questions/*.json`) with four options per question
and an indexed correct answer. Math questions include worked-solution hints.

See evidence: [QN_Bank_Maths.png](QN_Bank_Maths.png) · [QN_Bank_Cyber.png](QN_Bank_Cyber.png)

### Math Quiz UI

The Math Quiz interface was implemented with the difficulty selector page (Easy / Medium / Hard)
linking to the generic quiz template. The 20-second countdown timer and answer button styling
were applied across all difficulty levels.

See evidence: [MATH_QUIZ.png](MATH_QUIZ.png)

### Real-World Cyber Security Research

Research was conducted into real-world phishing attacks, email scams, and QR-code-based fraud.
Age-appropriate educational scenarios were created and added to the cyber quiz banks to make
the content more engaging and realistic for users aged 6–12.

### OTP Email Verification Testing

The OTP email verification system was tested end-to-end: registration, login OTP, and
password reset OTP. All flows confirmed working correctly.

### Score Tracking & Memory Match Unlock Testing

Score tracking was tested across quiz sessions. The Memory Match unlock at 100 points was
verified — the lock releases permanently once the threshold is crossed.

### Trello Workflow

Tasks were actively managed on the Trello board throughout the week:
- Cards moved from **To Do** → **In Progress** → **Done**
- New cards created for quiz content, backend routes, and testing
- Completed tasks archived to keep the board clear

See evidence: [Trello_Board_01.png](Trello_Board_01.png) · [Trello_Board_02.png](Trello_Board_02.png)

### Brief Team Sync

A quick 2-minute WhatsApp meeting identified that the initial Snake quiz and Math quiz had
overlapping question sets. The team agreed to differentiate the Snake quiz with eco-themed
arithmetic questions (snake-specific, not shared with the Math bank).
