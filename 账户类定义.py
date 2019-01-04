
'''
class Account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance


    def deposit(self,amount):
        if amount <= 0:
            print('存入金额不能为负')
        else:
            self.balance += amount

    def withdraw(self,amount):
        if amount >self.balance:
            print('金额不足')
        else:
            self.balance -= amount

    def __str__(self):
        return "Account('{name}','{number}','{balance}')".format(name=self.name,number=self.number,balance=self.balance)

'''


class Account:
    def __init__(self, number, name,balance):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')


acc = Account('aaa','123098','600')
acc.deposit(300)

print(acc)