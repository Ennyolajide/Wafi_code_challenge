import unittest

from PaymentApp import PaymentApp


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = PaymentApp()
        self.app.add_user('A')
        self.app.add_user('B')

    def test_add_user(self):
        self.assertDictEqual({'wallets': {"USD": 0, "NGN": 0, "GBP": 0, "EUR": 0}, 'name': 'A'},
                             self.app.users['A'].__dict__)
        self.assertDictEqual({'wallets': {"USD": 0, "NGN": 0, "GBP": 0, "EUR": 0}, 'name': 'B'},
                             self.app.users['B'].__dict__)

    def test_deposit(self):
        self.app.deposit('A', 10, 'USD')
        self.assertEqual(self.app.check_balance('A', 'USD'), 10)
        self.app.deposit('B', 2000, 'NGN')
        self.assertEqual(self.app.check_balance('B', 'NGN'), 2000)

    def test_transfer(self):
        self.app.deposit('A', 10, 'EUR')
        self.app.deposit('B', 20, 'EUR')
        self.app.transfer('B', 'A', 15, 'EUR')
        self.assertEqual(self.app.check_balance('A', 'EUR'), 25)
        self.assertEqual(self.app.check_balance('B', 'EUR'), 5)

    def test_withdraw(self):
        self.app.deposit('A', 10000, 'NGN')
        self.app.withdraw('A', 10000, 'NGN')
        self.assertEqual(self.app.check_balance('A', 'NGN'), 0)

    def test_insufficient_balance(self):
        self.app.deposit('A', 10, 'USD')
        with self.assertRaises(ValueError):
            self.app.withdraw('A', 20, 'USD')

    def test_duplicate_user(self):
        with self.assertRaises(ValueError):
            self.app.add_user('A')


if __name__ == '__main__':
    unittest.main()
