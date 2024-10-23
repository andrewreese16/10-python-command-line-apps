import json


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


def save_accounts(accounts, filename="accounts.json"):
    with open(filename, "w") as file:
        json_accounts = {acc.account_number: acc.__dict__ for acc in accounts.values()}
        json.dump(json_accounts, file)
    print("Accounts saved successfully.")


def load_accounts(filename="accounts.json"):
    try:
        with open(filename, "r") as file:
            json_accounts = json.load(file)
            accounts = {
                acc_num: BankAccount(**data) for acc_num, data in json_accounts.items()
            }
            return accounts
    except FileNotFoundError:
        return {}


def main():
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
            save_accounts(accounts)
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
