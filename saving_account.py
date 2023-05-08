class SavingsAccount:
    def _init_(self, account_number, balance=0, limit=0):
        self.account_number = account_number
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < self.limit:
            print("Withdrawal amount exceeds account limit!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance