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

    def deposit(self, name, amount):
        self.get_user(name).credit(amount)

    def withdraw(self, name, amount):
        self.get_user(name).debit(amount)

    def check_balance(self, name):
        return self.get_user(name).balance

    def transfer(self, sender_name, recipient_name, amount):
        sender = self.get_user(sender_name)
        recipient = self.get_user(recipient_name)
        sender.transfer(recipient, amount)

    def transfer_out(self, sender_name, amount, recipient_app={}, recipient_name=''):
        self.get_user(sender_name).debit(amount)
        # credit the recipient app using the recipient_id/recipient_name

