import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negative_ticket_price(self):
        self.assertIsNone(self.zoo.get_ticket_price(-1))  # Expect None or error

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)  # Expect 50

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)  # Expect 100

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(45), 150)  # Expect 150

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(80), 100)  # Expect 100

if __name__ == '__main__':
    unittest.main()