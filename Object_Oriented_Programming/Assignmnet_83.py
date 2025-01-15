class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

# Example usage:
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print("Balance:", account.check_balance())
account.withdraw(100)  # Insufficient funds
