#python program to illustrate functions
#can be treated as objects

def shout(text):#'shout' function
    return text.upper()

print(shout('hello'))

yell = shout#here'shout' will be treated as object

print(yell('hello'))