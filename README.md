# SecuPass 🔐

SecuPass 🔐 is a secure web-based password manager built with **Flask**.  
Generate strong passwords, encrypt 🔒 and store them locally 🗄️, view and manage entries safely 👀. Perfect for learning encryption, web apps, and secure password handling 🚀.

---

## Features

- 🔑 Generate strong passwords of customizable length  
- 🔒 Encrypt and store passwords securely using **Fernet (symmetric encryption)**  
- 🗄️ Store entries locally in **SQLite**  
- 👀 View and manage saved entries with a user-friendly interface  
- ❌ Delete entries easily  
- 📊 Password strength meter  

---

## Structure
SecuPass/
```
│
├─ app.py                  # Main Flask application
├─ requirements.txt        # Python dependencies
├─ .gitignore              # Files/folders to ignore in Git
├─ LICENSE                 # MIT License file
├─ README.md               # Project description & instructions
├─ .env                    # Environment variables (FERNET_KEY) – DO NOT commit
├─ secupass.db             # SQLite database – DO NOT commit
│
├─ templates/
│   └─ index.html          # Frontend HTML
│
├─ static/
│   ├─ css/
│   │   └─ style.css       # CSS styling
│   └─ js/
│       └─ main.js         # JavaScript for frontend logic
│
└─ screenshots/            # Optional: screenshots for README
    └─ screenshot.png
```

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Encryption:** cryptography.Fernet  
- **Frontend:** HTML, CSS, JavaScript  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/SecuPass.git
cd SecuPass
