import unittest
from datetime import datetime
from app.models.transaction import Transaction
from app.models.account import Account

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.from_account = Account(id=1, user_id=1, account_type='checking', account_number='123456', balance=100.00, created_at=datetime.now(), updated_at=datetime.now())
        self.to_account = Account(id=2, user_id=2, account_type='savings', account_number='789012', balance=200.00, created_at=datetime.now(), updated_at=datetime.now())
        self.transaction = Transaction(
            id=1,
            from_account_id=1,
            to_account_id=2,
            amount=50.00,
            type='transfer',
            description='Transfer from checking to savings',
            created_at=datetime.now(),
            from_account=self.from_account,
            to_account=self.to_account
        )

    def test_to_dict(self):
        expected_output = {
            'id': 1,
            'from_account_id': 1,
            'to_account_id': 2,
            'amount': '50.00',
            'type': 'transfer',
            'description': 'Transfer from checking to savings',
            'created_at': self.transaction.created_at
        }
        self.assertEqual(self.transaction.to_dict(), expected_output)

    def test_repr(self):
        expected_output = "<Transaction 1>"
        self.assertEqual(repr(self.transaction), expected_output)

if __name__ == '__main__':
    unittest.main()
