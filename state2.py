from abc import ABC, abstractmethod

class AccountState(ABC):
    @abstractmethod
    def deposit(self, account, amount):
        pass

    @abstractmethod
    def withdraw(self, account, amount):
        pass

class NormalState(AccountState):
    def deposit(self, account, amount):
        account.balance += amount
        print(f"Deposited {amount}. New balance is {account.balance}.")

    def withdraw(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            print(f"Withdrew {amount}. New balance is {account.balance}.")
            if account.balance < 100:
                account.set_state(WarningState())
        else:
            print("Insufficient funds.")

class WarningState(AccountState):
    def deposit(self, account, amount):
        account.balance += amount
        print(f"Deposited {amount}. New balance is {account.balance}.")
        if account.balance >= 100:
            account.set_state(NormalState())

    def withdraw(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            print(f"Withdrew {amount}. New balance is {account.balance}.")
            if account.balance <= 0:
                account.set_state(FrozenState())
        else:
            print("Insufficient funds. Account is already in warning state.")

class FrozenState(AccountState):
    def deposit(self, account, amount):
        print("Cannot deposit. Account is frozen.")

    def withdraw(self, account, amount):
        print("Cannot withdraw. Account is frozen.")

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.state = NormalState()

    def set_state(self, state):
        self.state = state
        print(f"Account state changed to {self.state.__class__.__name__}.")

    def deposit(self, amount):
        self.state.deposit(self, amount)

    def withdraw(self, amount):
        self.state.withdraw(self, amount)

account = BankAccount()

account.deposit(150)
account.withdraw(60)
account.withdraw(30)
account.withdraw(60)
account.deposit(100)
account.withdraw(200)