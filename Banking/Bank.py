from Banking import bankaccount
from Banking.bankaccount import BankAccount


class Bank:
    def __init__(self, name, account_id: int) -> None:
        self.name = name
        self.accounts = {}
        self.account_id = account_id

    def create_account(self, account_number: str, account_name: str, pin: str) -> BankAccount | None:
        if account_number in self.accounts:
            print("Account already exists")
            return None
        if len(pin) != 4:   # exactly 4 numbers PIN validation
            print("Invalid Pin, too long or too short")
            return None
        new_account = BankAccount(account_number, account_name, pin)
        self.accounts[account_number] = new_account
        print(f"Account created for {account_name}")
        return new_account


    def delete_account(self, account_number: str) -> None:
        if account_number in self.accounts:
            delete_choice = input("Are you sure you want to delete the account? Y/N")
            if delete_choice.upper() == "Y":
                del self.accounts[account_number]
            elif delete_choice.upper() == "N":
                print("Deletion cancelled")
            else:
                print("Invalid input")

    def login(self, account_number: int, pin: str) -> BankAccount | None:
        account = self.accounts[account_number]
        if account and account.pin == pin:
            print("Login successful")
            return account
        else:
            print("Invalid account number or PIN")
            return None

    def show_accounts(self) -> None:
        for key, value in self.accounts.items():
            print(f"{key}: {value}")
