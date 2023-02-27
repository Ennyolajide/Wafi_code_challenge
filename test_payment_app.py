import unittest

from PaymentApp import PaymentApp


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = PaymentApp()
        self.app.add_user('A')
        self.app.add_user('B')

    def test_add_user(self):
        self.assertDictEqual({'balance': 0, 'name': 'A'}, self.app.users['A'].__dict__)
        self.assertDictEqual({'balance': 0, 'name': 'B'}, self.app.users['B'].__dict__)

    def test_deposit(self):
        self.app.deposit('A', 10)
        self.assertEqual(self.app.check_balance('A'), 10)
        self.app.deposit('B', 20)
        self.assertEqual(self.app.check_balance('B'), 20)

    def test_transfer(self):
        self.app.deposit('A', 10)
        self.app.deposit('B', 20)
        self.app.transfer('B', 'A', 15)
        self.assertEqual(self.app.check_balance('A'), 25)
        self.assertEqual(self.app.check_balance('B'), 5)

    def test_withdraw(self):
        self.app.deposit('A', 10)
        self.app.withdraw('A', 10)
        self.assertEqual(self.app.check_balance('A'), 0)

    def test_insufficient_balance(self):
        self.app.deposit('A', 10)
        with self.assertRaises(ValueError):
            self.app.withdraw('A', 20)

    def test_duplicate_user(self):
        with self.assertRaises(ValueError):
            self.app.add_user('A')


if __name__ == '__main__':
    unittest.main()
