from pprint import pprint


def convert_currency(amount, from_currency, to_currency):
    rates = {"USD": 1, "NGN": 0.0022, "GBP": 1.22, "EUR": 1.08}
    amount_in_usd = amount * rates[from_currency]
    return round((amount_in_usd / rates[to_currency]), 2)


class User:
    def __init__(self, name):
        self.name = name
        self.wallets = {"USD": 0, "NGN": 0, "GBP": 0, "EUR": 0}

    def get_wallet_by_currency(self, currency):
        return self.wallet

    def get_balance_by_currency(self, currency):
        return self.wallets[currency]

    def check_other_wallets(self, amount, currency):
        wallets, total_amount_in_checked_wallet = {}, 0

        for _currency in self.wallets:
            if _currency == currency or self.wallets[_currency] <= 0:
                continue
            amount_in_wallet = convert_currency(self.wallets[_currency], _currency, currency)
            wallets[_currency] = amount_in_wallet
            total_amount_in_checked_wallet += amount_in_wallet
            if total_amount_in_checked_wallet >= amount:
                break

        return wallets if total_amount_in_checked_wallet >= amount else {}

    def credit(self, amount, currency):
        self.wallets[currency] += amount

    def debit(self, amount, currency):
        if self.wallets[currency] >= amount:
            self.wallets[currency] -= amount
        else:
            remaining_amount = (amount - self.wallets[currency])
            other_wallets = self.check_other_wallets(remaining_amount, currency)
            if other_wallets:
                self.wallets[currency] = 0
                self.debit_wallets(remaining_amount, currency, other_wallets)
            else:
                raise ValueError(f"User {self.name} does not have sufficient balance")

    def debit_wallets(self, amount, currency, wallets):
        remaining_amount = amount
        for _cur in wallets:
            if remaining_amount <= wallets[_cur]:
                amount_left_in_wallet = round((wallets[_cur] - remaining_amount), 2)
                self.wallets[_cur] -= round(
                    (self.wallets[_cur] - convert_currency(amount_left_in_wallet, currency, _cur)), 2)
                remaining_amount = 0
                break
            else:
                remaining_amount = round((remaining_amount - wallets[_cur]), 2)
                self.wallets[_cur] = 0

    def transfer(self, recipient, amount, currency):
        self.debit(amount, currency)
        recipient.credit(amount, currency)
