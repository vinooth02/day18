class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("insuffiecent balance")

    def displaybalance(self):
        print("Name:",self.name)
        print("Balance:",self.balance)

def startprogram():
    account=BankAccount("karan",5000)

    account.deposit(2000)

    account.withdraw(1500)

    account.displaybalance()

startprogram() 