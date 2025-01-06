import sqlite3


def backup_database():
    conn = sqlite3.connect('finance_manager.db')
    backup_conn = sqlite3.connect('finance_manager_backup.db')
    conn.backup(backup_conn)
    backup_conn.close()
    conn.close()


def restore_database():
    conn = sqlite3.connect('finance_manager.db')
    backup_conn = sqlite3.connect('finance_manager_backup.db')
    backup_conn.backup(conn)
    backup_conn.close()
    conn.close()