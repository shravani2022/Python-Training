class Vehicle:
    def drive(self):#parent class method
        print("I am driving")
    def run(self):
        print("Vehicle is running")
class Honda(Vehicle):#child class method
    def colour(self):
        print("And my car is black")

#create object of the honda class
honda1 = Honda()

#calling methods of the parent class
honda1.drive()
honda1.run()

#calling methods of the child class
honda1.colour()