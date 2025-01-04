# outside function
def outer():
    message = 'local'

    #nested function
    def inner():

        #declare nonlocal variables
        nonlocal message

        message = 'nonlocal'
        print('inner', message)

    inner()
    print("outer",message)
    
outer()