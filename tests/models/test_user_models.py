import unittest
from datetime import datetime
from app.models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            id=1,
            username='test_user',
            email='test@example.com',
            password_hash='hashed_password',
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

    def test_to_dict(self):
        expected_output = {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com',
            'created_at': self.user.created_at,
            'updated_at': self.user.updated_at
        }
        self.assertEqual(self.user.to_dict(), expected_output)

    def test_repr(self):
        expected_output = "<User test_user>"
        self.assertEqual(repr(self.user), expected_output)

if __name__ == '__main__':
    unittest.main()
