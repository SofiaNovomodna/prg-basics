class account:
    def __init__(self, no):
        self.no = no
        self.amount = 0

    def deposit(self, money):
        self.amount += money
    def withdraw(self, money):
        if money>self.amount:
            print('Insufficient funds on the account')
        else:
            self.amount -= money

    def info(self):
        print('Bank Account No:', self.no)
        print('Balance: PLN', self.amount)

account1 = account('12 3456 5555 9090 1111 0000 7722')
account1.info()
account1.deposit(25.30)
account1.info()
account1.withdraw(31.70)
account1.info()
account1.withdraw(14)
account1.info()