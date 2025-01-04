class Credit_card:
    def __init__(self,name,credit_limit):
        self.name = name
        self.credit_limit = credit_limit
    def info(self):
        print(f"This is {self.name} .set limit is {self.credit_limit}")
class Visa_credit_card:
    def __init__(self,name,credit_limit):
        self.name = name
        self.credit_limit = credit_limit
    def info(self):
        print(f"This is {self.name}. set limit is {self.credit_limit}")

creditcard1 = Credit_card("Axis Rupay Credit Card",100000)
visacard1 = Visa_credit_card("Axis Visa Credit Card",200000)

for Axis_Bank in (creditcard1,visacard1):
    Axis_Bank.info()