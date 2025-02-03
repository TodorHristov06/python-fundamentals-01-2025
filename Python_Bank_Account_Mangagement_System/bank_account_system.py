# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []            # Account names
balances = []                   # Account balances
transaction_histories = []      # Account transaction logs
loans = []                      # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣  - Create Account")
    print("2️⃣  - Deposit Money")
    print("3️⃣  - Withdraw Money")
    print("4️⃣  - Check Balance")
    print("5️⃣  - List All Accounts")
    print("6️⃣  - Transfer Funds")
    print("7️⃣  - View Transaction History")
    print("8️⃣  - Apply for Loan")
    print("9️⃣  - Repay Loan")
    print("🔟 - Identify Credit Card Type")
    print("0️⃣  - Exit")

def create_account(account_holders, balances, loans):
    """Create a new account."""
    new_holder = input("Enter your account name: ")
    account_holders.append(new_holder)  # Add the account holder name
    balances.append(0)                  # Initialize balance to 0
    loans.append(0)                     # Initialize loan amount to 0
    print(f"✅ Account created successfully for {new_holder}!")
    print("Account Balance: $0.00 | Loan Amount: $0.00")

def deposit():
    """Deposit money into an account."""
    name = input("Enter your account name: ")

    # Check if the account exists
    if name in account_holders:
        index = account_holders.index(name)  # Find the index of the account
        amount = float(input("Enter deposit amount: $"))

        if amount > 0:
            balances[index] += amount  # Update balance
            transaction_histories.append(f"{name} deposited ${amount:.2f}")  # Log transaction
            print(f"✅ Deposit successful! New balance: ${balances[index]:.2f}")
        else:
            print("❌ Invalid amount. Deposit must be greater than zero.")
    else:
        print("❌ Account not found. Please check the account name.")


def withdraw(account_holders, balances, transaction_histories):
    """Withdraw money from an account."""
    name = input("Enter your account name: ")

    # Check if the account exists
    if name in account_holders:
        index = account_holders.index(name)  # Find the index of the account
        amount = float(input("Enter withdrawal amount: $"))

        if amount > 0:
            if amount <= balances[index]:
                balances[index] -= amount  # Update balance
                transaction_histories.append(f"{name} withdrew ${amount:.2f}")  # Log transaction
                print(f"✅ Withdrawal successful! New balance: ${balances[index]:.2f}")
            else:
                print("❌ Insufficient funds. You cannot withdraw more than your balance.")
        else:
            print("❌ Invalid amount. Withdrawal must be greater than zero.")
    else:
        print("❌ Account not found. Please check the account name.")

def check_balance(account_holders, balances):
    """Check balance of an account."""
    name = input("Enter your account name: ")

     # Check if the account exists
    if name in account_holders:
        index = account_holders.index(name)
        print(f"✅ Your balance is: ${balances[index]:.2f}")
    else:
        print("❌ Account not found. Please check the account name.")

def list_accounts():
    """List all account holders and details."""
    pass  # TODO: Add logic

def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic

def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic

def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic

def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()