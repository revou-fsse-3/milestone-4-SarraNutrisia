import unittest
from datetime import datetime
from app.models.account import Account
from app.models.user import User

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.user = User(id=1, username='test_user')
        self.account = Account(
            id=1,
            user_id=1,
            account_type='savings',
            account_number='123456',
            balance=100.00,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            user=self.user
        )

    def test_to_dict(self):
        expected_output = {
            'id': 1,
            'user_id': 1,
            'account_type': 'savings',
            'account_number': '123456',
            'balance': '100.00',
            'created_at': self.account.created_at,
            'updated_at': self.account.updated_at
        }
        self.assertEqual(self.account.to_dict(), expected_output)

    def test_repr(self):
        expected_output = "<Account 123456>"
        self.assertEqual(repr(self.account), expected_output)

if __name__ == '__main__':
    unittest.main()
