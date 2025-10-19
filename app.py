import os
from flask import Flask, render_template, request, jsonify, abort
import sqlite3
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

load_dotenv()


DB_PATH = 'secupass.db'
FERNET_KEY = "YOUR_FERNET_KEY"

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Warn if FERNET_KEY is missing
if FERNET_KEY is None:
    print("WARNING: FERNET_KEY not found in environment. Generate one and set FERNET_KEY before using.")
    print('Generate with (Linux/macOS/PowerShell):')
    print('  python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"')

def get_fernet():
    if FERNET_KEY is None:
        raise RuntimeError('FERNET_KEY environment variable not set')
    return Fernet(FERNET_KEY.encode())

def init_db():
    """Initialize SQLite database and create entries table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            username TEXT,
            password BLOB NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-password', methods=['POST'])
def generate_password():
    """Generate a random strong password"""
    import secrets, string
    data = request.get_json() or {}
    length = int(data.get('length', 16))
    length = max(8, min(64, length))  # constrain length
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-_=+[]{};:,.<>?'
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return jsonify({'password': password})

@app.route('/api/save', methods=['POST'])
def save_entry():
    """Save a password entry (encrypted) to the database"""
    payload = request.get_json()
    if not payload:
        abort(400, 'JSON required')
    label = payload.get('label', '').strip()
    username = payload.get('username', '').strip()
    password = payload.get('password', '').strip()
    notes = payload.get('notes', '').strip()
    if not label or not password:
        abort(400, 'label and password required')
    try:
        f = get_fernet()
    except RuntimeError as e:
        return jsonify({'status':'error','message':str(e)}), 500
    token = f.encrypt(password.encode())
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO entries (label, username, password, notes) VALUES (?, ?, ?, ?)',
              (label, username, token, notes))
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/api/list', methods=['GET'])
def list_entries():
    """Return all entries with decrypted passwords"""
    try:
        f = get_fernet()
    except RuntimeError as e:
        return jsonify({'status':'error','message':str(e)}), 500
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, label, username, password, notes FROM entries ORDER BY id DESC')
    rows = []
    for r in c.fetchall():
        id_, label, username, token, notes = r
        try:
            password = f.decrypt(token).decode()
        except InvalidToken:
            password = '<decryption failed>'
        rows.append({
            'id': id_,
            'label': label,
            'username': username,
            'password': password,
            'notes': notes
        })
    conn.close()
    return jsonify({'status':'ok', 'entries': rows})

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_entry(id):
    """Delete a password entry by ID"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM entries WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
