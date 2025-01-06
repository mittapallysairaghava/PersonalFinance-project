from datetime import datetime
import sqlite3

def get_monthly_report(user_id, month, year):
    start_date = f"{year}-{month}-01"
    end_date = f"{year}-{month}-31"
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE user_id = ? AND type = 'income' AND date BETWEEN ? AND ?''', 
                   (user_id, start_date, end_date))
    total_income = cursor.fetchone()[0] or 0
    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE user_id = ? AND type = 'expense' AND date BETWEEN ? AND ?''', 
                   (user_id, start_date, end_date))
    total_expenses = cursor.fetchone()[0] or 0
    savings = total_income - total_expenses
    conn.close()
    return total_income, total_expenses, savings
