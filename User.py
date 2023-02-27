from pprint import pprint


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        # pprint(self.__dict__)

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError(f"User {self.name} does not have sufficient balance")

    def transfer(self, recipient, amount):
        self.debit(amount)
        recipient.credit(amount)
