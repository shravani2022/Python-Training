#defining a decorator
def hello_decorator(func):#original decorator
    # inner1 is a wrapper function in
    #which the argument is called

    #inner function can access the outer local
    #functions like in this case "func"
    def inner1():#wrapper
        print("Hello, this is before function execution")

        #calling the actual function now
        #inside the wrapper function

        func()#out local to decorator
        
        #outer local 'func' will be called by wrapper'inner1'

        print("this is after function execution")
    return inner1

#defining a function, to be called inside wrapper
def function_to_be_used():
    print("this is inside the function !!")

#passing 'function_to_be_used' inside the
#decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

#calling the function
function_to_be_used()