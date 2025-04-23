class BankAccount:
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

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

account = BankAccount(123456, 10000)
account.deposit(2000)
account.withdraw(500)
account.display()
