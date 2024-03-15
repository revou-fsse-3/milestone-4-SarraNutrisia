import unittest
from app.models.base import Base

class TestBase(unittest.TestCase):

    def test_base_instantiation(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

if __name__ == '__main__':
    unittest.main()
