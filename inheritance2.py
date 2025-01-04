#create bank account class with deposit, withdraw function
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdraw Machine")
    def deposite(self):
        amount = float(input("enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("enter the amount to be withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n you withdraw: ",amount)
        else:
            print("\n Insufficient balance ")  
    def display(self):
        print("\n net available balance=",self.balance) 
#create object of class
s = Bank_Account()
s.deposite()
s.withdraw()
s.display()     
        