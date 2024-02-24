class Bank_account():

    def __init__(self, balance):
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        if self.balance >= 0:
            return self.balance
        elif self.balance < 0:
            return "not enough money"


Vasil_acoount = Bank_account(1000)
print(Vasil_acoount.get_balance())
Vasil_acoount.deposit(1000)
print(Vasil_acoount.get_balance())
Vasil_acoount.withdrawal(300)
print(Vasil_acoount.get_balance())
Vasil_acoount.withdrawal(3000)
print(Vasil_acoount.get_balance())
