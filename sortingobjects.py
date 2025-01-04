#Sorting objects of user defined class in Python
#print(sorted([1,8,6,4]))
#print(sorted("priya".split()))

#user defined class
'''class My_User:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return str((self.a,self.b))

#list of objects
abc =[My_User("priya",1),
      My_User("computer",3),
      My_User("abhi",2),
      My_User("gulzar",5),
      My_User("science",3)]

#sorting objects on the basis of value
#sorted at variable b
print(sorted(abc, key=lambda x: x.b))'''

def product_of_digits(num):
    temp = num
    prod = 1
    while temp > 0:
        digit = temp % 10
        prod *= digit
        temp //=10
    return prod

#num=int(input("enter a number:"))
num = 11.11
print("product of all digits of {0} is: {1}".format(num, product_of_digits(num)))

                        