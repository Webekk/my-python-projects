from datetime import datetime


class BankAccount:
    def __init__(self, account_number: str, account_name: str, pin: str, balance: float = 0.0) -> None:
        self.accountNumber = account_number
        self.accountName = account_name
        self.balance = balance
        self.transactions = []
        self.pin = pin

    def __str__(self):
        return f'{self.accountNumber} || {self.accountName} || Balance: {self.balance}'

    def deposit(self, amount: float) -> None:
        """
          This method is used to deposit an amount of money to the bank account.
        :param amount:
        :return:
        """
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        self.transactions.append((datetime.now(), "Deposit", amount, self.balance))
        print(f"Deposited: {amount} to {self.accountName} with the number {self.accountNumber}")

    def withdraw(self, amount: float) -> None:
        """
        This method is used to withdraw an amount of money from the bank account.

        :param amount:
        :return:
        """
        if amount <= 0:
            print("Withdraw must be a positive number")
            return
        elif amount > self.balance:
            print("Withdraw cannot be above your balance")
            return
        self.balance -= amount
        self.transactions.append((datetime.now(), "Withdraw", amount, self.balance))
        print(f"Withdrawn: {amount} to {self.accountName} with the number {self.accountNumber}")

    def check_balance(self):
        """
        This method is used to check the balance of the bank account.
        :return:
        """
        print(f"Your account balance is : {self.balance}")
        return self.balance

    def check_transactions_history(self):
        if not self.transactions:
            print("No transactions history yet")
        print(40 * "-")
        print("Transactions history:")
        for date, type_, amount, balance in self.transactions:
            print(f"{date} : {type_} : {amount} : {balance}")
        print(40 * "-")

    def check_pin(self):
        if not self.pin:
            print("Not a valid pin number")
