# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest

from PaymentApp import PaymentApp


class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = PaymentApp()

    def test_example(self):
        # User A is added to the app
        self.app.add_user('A')
        # User A deposits 10 dollars
        self.app.deposit('A', 10, 'USD')
        # User B is added to the app
        self.app.add_user('B')
        # User B deposits 20 dollars
        self.app.deposit('B', 20, 'USD')
        # User B sends 15 dollars to User A
        self.app.transfer('B', 'A', 15, 'USD')
        # User A checks their balance and has 25 dollar
        self.assertEqual(self.app.check_balance('A', 'USD'), 25)
        # User B checks their balance and has 5 dollar
        self.assertEqual(self.app.check_balance('B', 'USD'), 5)
        # User A transfers 25 dollars from their account
        self.app.transfer_out('A', 25, 'USD')
        # User A checks their balance and has 0 dollars
        self.assertEqual(self.app.check_balance('A', 'USD'), 0)

    def test_multi_wallet(self):
        # User A is added to the app
        self.app.add_user('A')
        # User A deposits 10 dollars
        self.app.deposit('A', 5, 'USD')
        # User A deposits 2000 NGN
        self.app.deposit('A', 2000, 'NGN')
        # User A deposits 4 GBP
        self.app.deposit('A', 4, 'GBP')
        # User A deposits 1 EUR
        self.app.deposit('A', 1, 'EUR')
        # User B is added to the app
        self.app.add_user('B')
        # User A sends 10 dollars to User B
        self.app.transfer('A', 'B', 10, 'USD')
        # User A checks their balance and has 25 dollar
        self.assertDictEqual({'wallets': {'USD': 0, 'NGN': 0, 'GBP': 3.51, 'EUR': 1}, 'name': 'A'},
                             self.app.users['A'].__dict__)
        # User B checks their balance and has 10 dollar
        self.assertEqual(self.app.check_balance('B', 'USD'), 10)
        self.assertDictEqual({'wallets': {'USD': 10, 'NGN': 0, 'GBP': 0, 'EUR': 0}, 'name': 'B'},
                             self.app.users['B'].__dict__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
