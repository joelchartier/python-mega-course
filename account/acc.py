class Account:
    """Some Sad comment"""

    def __init__(self, filepath):
        self.filepath=filepath
        with open(self.filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()
        

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()

# Tests (#dontdothisathome)
account=Account("account/balance.txt")
print(account.balance)

account.deposit(100)
print(account.balance)

account.deposit(100)
print(account.balance)

account.withdraw(300)
print(account.balance)

checking=Checking("account/balance.txt", 5)
checking.transfer(200)
print(checking.balance)