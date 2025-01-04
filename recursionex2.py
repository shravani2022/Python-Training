#program to find the sum of natural using recursive function

def sum(n):

    if n <= 1:
        return n
    else:
        return n + sum(n-1)
#change this value for a different result

num = 4

if num < 0:
    print("enter a positive number")
else:
    print("the sum is",sum(num))    

        