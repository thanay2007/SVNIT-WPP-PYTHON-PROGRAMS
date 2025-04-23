class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return amount

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, balance=0):
        if account_number in self.accounts:
            return "Account already exists"
        self.accounts[account_number] = Account(account_number, balance)

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account not found"
        self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number].withdraw(amount)

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number].get_balance()

bank = Bank()
bank.create_account(1001, 10000)
bank.deposit(1001, 2000)
print("Balance:", bank.get_balance(1001))
print("Withdrawn:", bank.withdraw(1001, 1000))
print("Balance:", bank.get_balance(1001))
