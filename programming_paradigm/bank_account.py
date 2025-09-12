class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True, self.account_balance
        return False, self.account_balance

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False, self.account_balance
        self.account_balance -= amount
        return True, self.account_balance

    def display_balance(self):
        return self.account_balance
