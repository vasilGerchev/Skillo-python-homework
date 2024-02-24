class Bank_account():

    def __init__(self, balance):
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            return 'no money'

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance


Vasil_acoount = Bank_account(1000)
result = Vasil_acoount.deposit(5000)
print(result)
result = Vasil_acoount.withdrawal(2000)
print(result)

