#program for rate of interest of interest using method overriding
class Bank:
    def get_roi(self):
        pass

class SBI(Bank):
    def get_roi(self):
        return 7

class HDFC(Bank):
    def get_roi(self):
        return 8

class BOI(Bank):
    def get_roi(self):
        return 7.5

s1 = SBI()
h1 = HDFC()
b1 = BOI()

print("SBI rate of interest: ", s1.get_roi())
print("HDFC rate of interest: ", h1.get_roi())
print("BOI rate of interest: ", b1.get_roi())   