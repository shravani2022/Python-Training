#To overload the + operator, we will need to implement _add_() function in the class.
class s1:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return"({0},{1})".format(self.x, self.y)

    def __add__(self):
        x = self.x + other.x
        y = self.y + other.y
        return s1(x,y)

p1 = s1(1,2)
p2 = s1(2,5)

print(p1+p2)

# mathematical operations using function