import sqlite3
import bcrypt # type: ignore

def create_user_table():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password, email):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)', (username, password_hash, email))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        return True
    return False