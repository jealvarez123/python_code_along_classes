# print('let do it')

class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0

    def deposit(self):
        self.balance += balance

    def withdraw(self):
        self.balance -= balance

savings = BankAccount('savings')
checking = BankAccount('checking')

print('My {} account has {}'.format(savings.kind, savings.balance))
print('My {} account has {}'.format(checking.kind, checking.balance))
