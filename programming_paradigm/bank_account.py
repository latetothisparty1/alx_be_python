class BankAccount:
    def __init__(self, initial_balance=0):
        "Initialize the account with an optional initial balance."
        self.account_balance = initial_balance
    def deposit(self, amount):
        "Add the specified amount to the account balance."
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        "Subtract the specified amount from the account balance."
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}") 
        else:
            print("Insufficient funds.")
    def display_balance(self):
        "Print the current balance in a user-friendly format."
        print(f"Current Balance: ${self.account_balance:.2f}")