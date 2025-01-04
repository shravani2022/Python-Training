#declare global variable
message = 'Hello'

def greet():
    #declare lacal variable
    print('local',message)

greet()
print('Global', message)