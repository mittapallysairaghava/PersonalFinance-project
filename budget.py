import sqlite3


def create_budget_table():
    try:
        conn = sqlite3.connect('finance_manager.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS budgets
                          (user_id INTEGER, month INTEGER, year INTEGER, category TEXT, limit REAL)''')
        conn.commit()
        conn.close()
        print("Budgets table created successfully or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating budgets table: {e}")


def set_budget(user_id, month, year, category, budget_limit):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''REPLACE INTO budgets (user_id, month, year, category, limit) 
                      VALUES (?, ?, ?, ?, ?)''', (user_id, month, year, category, budget_limit))
    conn.commit()
    conn.close()

def check_budget_exceed(user_id, month, year, category):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT limit FROM budgets WHERE user_id = ? AND month = ? AND year = ? AND category = ?', 
                   (user_id, month, year, category))
    budget_limit = cursor.fetchone()
    if not budget_limit:
        return None
    budget_limit = budget_limit[0]
    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE user_id = ? AND type = 'expense' AND category = ? 
                      AND date BETWEEN ? AND ?''', 
                   (user_id, category, f"{year}-{month}-01", f"{year}-{month}-31"))
    total_expenses = cursor.fetchone()[0] or 0
    conn.close()
    return total_expenses > budget_limit
