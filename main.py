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
        self.app.deposit('A', 10)
        # User B is added to the app
        self.app.add_user('B')
        # User B deposits 20 dollars
        self.app.deposit('B', 20)
        # User B sends 15 dollars to User A
        self.app.transfer('B', 'A', 15)
        # User A checks their balance and has 25 dollar
        self.assertEqual(self.app.check_balance('A'), 25)
        # User B checks their balance and has 5 dollar
        self.assertEqual(self.app.check_balance('B'), 5)
        # User A transfers 25 dollars from their account
        self.app.transfer_out('A', 25)
        # User A checks their balance and has 0 dollars
        self.assertEqual(self.app.check_balance('A'), 0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
