#returning function from another function
#python program to illustrate functions
#functions can return another function

def create_adder(x):#original function
    def adder(y):#nested function
        return x+y#return result of nested function

    return adder#return nested function from original function
    #i.e. functions can return another function
add_15 = create_adder(15)


print(add_15(10))
