from User import User


class PaymentApp:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name in self.users:
            raise ValueError(f"User {name} already exists")
        self.users[name] = User(name)

    def get_user(self, name):
        if name not in self.users:
            raise ValueError(f"User {name} does not exist.")
        return self.users[name]

    def deposit(self, name, amount, currency):
        self.get_user(name).credit(amount, currency)

    def withdraw(self, name, amount, currency):
        self.get_user(name).debit(amount, currency)

    def check_balance(self, name, currency):
        return self.get_user(name).wallets[currency]

    def transfer(self, sender_name, recipient_name, amount, currency):
        sender = self.get_user(sender_name)
        recipient = self.get_user(recipient_name)
        sender.transfer(recipient, amount, currency)

    def transfer_out(self, sender_name, amount, currency, recipient_app={}, recipient_name=''):
        self.get_user(sender_name).debit(amount, currency)
        # credit the recipient app using the recipient_id/recipient_name

