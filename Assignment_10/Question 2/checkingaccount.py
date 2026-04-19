"""
File: checkingaccount.py
Refactor checking account defined in question_1 based on the BankAccount parent class.
"""
from bankaccount import BankAccount

class CheckingAccount(BankAccount):
    """Checking account (no interest)."""

    def __str__(self):
        result = "Type:    Checking\n"
        result += "Name:    " + self.name + "\n"
        result += "PIN:     " + self.pin + "\n"
        result += "Balance: " + str(self.balance)
        return result
    