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
```
SecuPass/
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
│   └─ index.html          # Frontend HTML embeded
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
```
2. **Create a virtual environment**
```bash
python -m venv venv
```
3. **Activate the virtual environment**
```powershell
venv\Scripts\activate
```
4. **Install dependencies**
```bash
pip install -r requirements.txt
```
5. **Set Fernet key**
```bash
setx FERNET_KEY "your-generated-fernet-key"
```
6. **Run the application**
```bash
python app.py
```
## Create a `requirements.txt` with dependencies:  
```yaml
Flask
cryptography
python-dotenv
```

## How to set FERNET_KEY
- Open `CMD` and run this command `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"` You will get unique FERNET_KEY 
- Then set the FERNET_KEY permanently , run this command `setx FERNET_KEY "YOUR_OWN_FERNET_KEY"`
- Then close the cmd and reopen your powershell and run `echo $env:FERNET_KEY`
- Hardcode for quick testing , Run...
```python
FERNET_KEY = os.environ.get('FERNET_KEY')
```
⚠️ Only for local testing. Do not commit hardcoded keys to GitHub.

## Last Contri
The last update to this project was made by ❤️ [Anirban Banerjee](https://github.com/anirbanbanerjee07) on `19th October, 2025`.

## ✨ Happy Coding!

Thanks for checking out this project!  
If you like it, give it a ⭐ and consider contributing.  

☕ Code, coffee, repeat!!
