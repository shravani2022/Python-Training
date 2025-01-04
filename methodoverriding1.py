class vehicle:
    def drive(self):
        pass

class car(vehicle):
    def drive(self):
        return("I am driving a car")

class bike(vehicle):
    def drive(self):
        return("I am riding a bike")

a = car()
b= bike()

print(a.drive())
print(b.drive())   
    