"""
File: bank_file_test.py
Tests the pickle load/dump functionality for the updated Bank class.
"""
from bank_file import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount
import os

def main():
    """
    # 1. Setup: Create a bank and add different account types
    # 2. Test Saving (Dump)
    # 3. Test Loading (Load)
    # 4. Verification (compare original and loaded bank states)
    """
    test_file = "bank_data.dat"

    # Remove old test file if it already exists
    if os.path.exists(test_file):
        os.remove(test_file)

    print("--- Phase 1: Creating Bank and Adding Accounts ---")
    bank1 = Bank()

    account1 = SavingsAccount("chloe", "12001", 1000.0)
    account2 = CheckingAccount("Nick", "42002", 500.0)

    bank1.add(account1)
    bank1.add(account2)

    print("Bank 1 (Original) State:")
    print(bank1)
    print()

    print("--- Phase 2: Saving Bank to File ---")
    bank1.save(test_file)
    print("Bank saved to", test_file)
    print()

    print("--- Phase 3: Loading Data into a Fresh Bank Object ---")
    bank2 = Bank(test_file)
    print("Bank data loaded from", test_file)
    print("Bank 2 (Loaded) State:")
    print(bank2)

if __name__ == "__main__":
    main()