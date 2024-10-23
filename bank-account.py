import sqlite3


class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depositied ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        else:
            print("Invaild amount. Withdrawal amount exceeds current balance")

    def view_balance(self):
        print(
            f"Account: {self.account_number} | Name: {self.name} | Balance: ${self.balance}"
        )


def setup_database():
    conn = sqlite3.connect("bank_accounts.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS accounts
        (account_number TEXT PRIMARY KEY, name TEXT, balance REAL)"""
    )
    conn.commit()
    conn.close()


def save_account(account):
    conn = sqlite3.connect("bank_accounts.db")
    c = conn.cursor()
    c.execute(
        "INSERT OR REPLACE INTO accounts (account_number, name, balance) VALUES (?, ?, ?)",
        (account.account_number, account.name, account.balance),
    )
    conn.commit()
    conn.close()


def update_account(account):
    conn = sqlite3.connect("bank_account.db")
    c = conn.cursor()
    c.execute(
        "UPDATE accounts SET balance = ? WHERE account_number = ?",
        (account.balance, account.account_number),
    )
    conn.commit()
    conn.close()


def load_accounts():
    conn = sqlite3.connect("bank_accounts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    rows = c.fetchall()
    accounts = {}
    for row in rows:
        account = BankAccount(name=row[1], account_number=row[0], balance=row[2])
        accounts[account.account_number] = account
    conn.close()
    return accounts


def main():
    setup_database()
    accounts = load_accounts()
    while True:
        print("\n=== Welcome to the Banking System ===")
        print("1. Create a New Account")
        print("2. View Account Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            view_account_balance(accounts)
        elif choice == "3":
            deposit_money(accounts)
        elif choice == "4":
            withdraw_money(accounts)
        elif choice == "5":
            for account in accounts.values():
                save_account(account)
            print("Have a good day!")
            break
        else:
            print("Invaild option, please enter a number between 1-5.")


def create_account(accounts):
    name = input("Enter your name: ")
    account_number = input("Enter a new account number: ")

    if account_number in accounts:
        print("Account number alreadt exists!")
        return

    new_account = BankAccount(name, account_number)
    accounts[account_number] = new_account
    save_account(new_account)
    print(f"Account created for {name} with account number {account_number}.")


def deposit_money(accounts):
    account_number = input("Enter your account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter the amount to deposit: "))
    accounts[account_number].deposit(amount)


def withdraw_money(accounts):
    account_number = input("Enter your account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter the amount to withdraw: "))

    accounts[account_number].withdraw(amount)


def view_account_balance(accounts):
    account_number = input("Enter your account number: ")

    if account_number in accounts:
        accounts[account_number].view_balance()
    else:
        print("Account not found!")


if __name__ == "__main__":
    main()
