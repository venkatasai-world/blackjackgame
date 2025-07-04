=============================
🃏 BLACKJACK GAME (FLASK APP)
=============================

A fun Blackjack game using Python Flask for backend and a stylish HTML+CSS frontend.

🎮 Features:
- Dark theme with white logo and ASCII card banner
- User chooses to start, hit, or stand
- Win, lose, or tie messages shown
- Clean design for students and responsive

-----------------------------
📦 REQUIREMENTS TO INSTALL:
-----------------------------
Flask==2.3.2
gunicorn==21.2.0

Install them using:

> pip install -r requirements.txt

You can also install manually:
> pip install Flask gunicorn

-----------------------------
▶️ HOW TO RUN:
-----------------------------
(1) Development (Flask)
-----------------------
> python app.py
Go to: http://localhost:5000

(2) Production (Gunicorn)
--------------------------
> gunicorn -w 1 app:app
Go to: http://localhost:8000

-----------------------------
📁 PROJECT STRUCTURE:
-----------------------------
blackjack_game/
├── app.py               ← Python backend
├── requirements.txt     ← Dependencies
├── templates/
│   └── index.html       ← HTML + CSS + ASCII + logo
└── project-info.txt     ← This file (README + requirements)

-----------------------------
👨‍💻 CREATED BY:
-----------------------------
Venkata Sai 🎓
