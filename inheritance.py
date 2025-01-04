#parent class
class Animal:
    def eat(self):#parent class method
        print("I can eat!")
    def sleep(self):#parent class method
        print("I can sleep!")
        
#child class
class Dog(Animal):
    def bark(self):#child class method
        print("I can bark! woof woof!!")
        
#create object of the Dof class
dog1 = Dog()

#calling mmembers of the base class
dog1.eat()
dog1.sleep()

#calling member of the derived class
dog1.bark()