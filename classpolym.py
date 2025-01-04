'''class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self):
        print(f"I am a cat My name is{self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self):
        print(f"I am a Dog. My name is{self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Bark")

cat1 = Cat("kitty",2.5)
dog1 = Dog("jenny",4)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()'''

class City1:
    def __init__(self,name,population):
        self.name = name
        self.population = population
    def info(self):
        print(f"The city name is {self.name} and population is {self.population}")

class City2:
    def __init__(self,name,population):
        self.name = name
        self.population = population
    def info(self):
        print(f"The city name is {self.name} and population is {self.population}")

city1 = City1("Sangli",123455)
city2 = City2("kolhapur",6754354)

for city in (city1,city2):
    city.info()

   