
# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance
    account = BankAccount()

    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py [command] [amount]")
        print("Commands: deposit, withdraw, balance")
        return

    command = sys.argv[1].lower()

    if command == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit [amount]")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)

    elif command == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw [amount]")
            return
        amount = float(sys.argv[2])
        account.withdraw(amount)

    elif command == "balance":
        account.display_balance()

    else:
        print("Unknown command. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()