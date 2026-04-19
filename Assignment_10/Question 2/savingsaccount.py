"""
File: savingsaccount.py
Refactor savings account defined in question_1 based on the BankAccount parent class.
"""
from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    RATE = 0.02

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __str__(self):
        result = "Type:    Savings\n"
        result += "Name:    " + self.name + "\n"
        result += "PIN:     " + self.pin + "\n"
        result += "Balance: " + str(self.balance)
        return result
    