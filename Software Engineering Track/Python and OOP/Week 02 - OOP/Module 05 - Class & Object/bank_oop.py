class Bank:

    def __init__(self, name, account_id, opening_balance=0):
        self.balance = opening_balance
        self.min_withdraw = 1000
        self.max_withdraw = 1000000000
        self.name = name
        self.account_id = account_id
        self.opening_date = None

    def account_details(self):
        print(f"Account Holder: {self.name}\nAccount ID: {self.account_id}")

    def get_balance(self):
        return self.balance

    def deposite(self, deposite_amount=0):
        self.balance += deposite_amount
        print(f"You have deposite amount {deposite_amount} taka\nNew balance {self.balance}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.min_withdraw:
            print(f"Minimum withdraw limit is {self.min_withdraw} taka")
            return

        if self.balance % withdraw_amount == self.balance:
            print(f"Maximum balance exceeds, your balance {self.balance} taka")
            return

        self.balance -= withdraw_amount

        print(f"Successfully withdrawn {withdraw_amount}\nNew balance {self.balance}")


customer1 = Bank("Subodh", 211071003, 50000)
customer1.account_details()
print(customer1.get_balance())
customer1.deposite(3350)
customer1.withdraw(-1)
