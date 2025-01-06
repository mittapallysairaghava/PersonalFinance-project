import unittest

from database import authenticate_user, register_user
from transaction import add_transaction, get_transactions

class TestFinanceManager(unittest.TestCase):
    def test_user_registration(self):
        register_user('test_user', 'password123', 'test@example.com')
        self.assertTrue(authenticate_user('test_user', 'password123'))

    def test_add_transaction(self):
        add_transaction(1, 100, 'Salary', '2024-12-01', 'income')
        transactions = get_transactions(1)
        self.assertEqual(len(transactions), 1)

    def test_monthly_report(self):
        total_income, total_expenses, savings = get_monthly_report(1, 12, 2024) # type: ignore
        self.assertIsInstance(total_income, float)
        self.assertIsInstance(total_expenses, float)
        self.assertIsInstance(savings, float)
