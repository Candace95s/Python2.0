"""
File: checkingaccount.py
This module defines the CheckingAccount class.
CheckingAccount does not have interest.
"""

"""
File: checkingaccount.py
This module defines the CheckingAccount class.
CheckingAccount does not have interest.
"""

class CheckingAccount:
    """This class represents a checking account with name, PIN, and balance."""

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def __str__(self):
        """Returns the string rep."""
        result = 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result


def main():
    """Tests the CheckingAccount class."""

    # 1. Test Instantiation
    account = CheckingAccount("Candace", "1234", 51500.0)
    print("1. Test Instantiation")
    print(account)
    print()

    # 2. Test String Representation (__str__)
    print("2. Test String Representation")
    print(account)
    print()

    # 3. Test Getters
    print("3. Test Getters")
    print("Name:", account.getName())
    print("PIN:", account.getPin())
    print("Balance:", account.getBalance())
    print()

    # 4. Test Deposit
    print("4. Test Deposit")
    account.deposit(200.0)
    print("Balance after deposit:", account.getBalance())
    print()

    # 5. Test Withdrawals
    print("5. Test Withdrawals")

    # Successful withdrawal
    result = account.withdraw(100.0)
    print("Withdraw 100.0:", result)
    print("Balance:", account.getBalance())

    # Insufficient funds
    result = account.withdraw(1000.0)
    print("Withdraw 1000.0:", result)
    print("Balance:", account.getBalance())

    # Negative amount
    result = account.withdraw(-50.0)
    print("Withdraw -50.0:", result)
    print("Balance:", account.getBalance())
    print()

    # 6. Final State
    print("6. Final State")
    print(account)


if __name__ == "__main__":
    main()