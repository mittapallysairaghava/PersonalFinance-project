import sqlite3

def create_transactions_table():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, category TEXT, date TEXT, type TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(user_id, amount, category, date, transaction_type):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (user_id, amount, category, date, type) VALUES (?, ?, ?, ?, ?)', 
                   (user_id, amount, category, date, transaction_type))
    conn.commit()
    conn.close()

def update_transaction(transaction_id, amount, category, date, transaction_type):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE transactions 
                      SET amount = ?, category = ?, date = ?, type = ? 
                      WHERE id = ?''', (amount, category, date, transaction_type, transaction_id))
    conn.commit()
    conn.close()

def delete_transaction(transaction_id):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()

def get_transactions(user_id, transaction_type=None):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    if transaction_type:
        cursor.execute('SELECT * FROM transactions WHERE user_id = ? AND type = ?', (user_id, transaction_type))
    else:
        cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions