class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name              # public
        self.__initial_deposite = initial_deposite  # private
        self._balance = self.__initial_deposite     # protected

    def deposite(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            return f'{self.holder_name} withdrawn {amount} taka.\nNew Balance: {self._balance} taka'


uttara_bank = Bank("Anika", 3520)
uttara_bank.deposite(3000)
print(uttara_bank.get_balance())
print(uttara_bank.withdraw(500))
