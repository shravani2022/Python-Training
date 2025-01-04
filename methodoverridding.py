#The child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.

#Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

#Method Overriding

from math import pi
class shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return"I am a two-dimensional shape."
    def __str__(self):
        return self.name

class Square(shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return " Squares have each angle is equal to 90 degrees."

class Circle(shape):
    def __init__(self ,radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def fact(self):
        return"life is a circle. jikde sarkal, tikde sarkal"

a=Square(5)
b=Circle(2)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
    