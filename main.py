class BankAccount:

    def __init__(self, int_rate, balance):
        # self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(
            f", has a Balance of: ${self.balance}, with a APR of: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")