def greet():
    #local variable
    message = 'Hello'

    print('local', message)
greet()

#try to access message variable
#outside greet() function
print(message)