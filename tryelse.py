# program to print the reciprocol of even numbers

try:#try to true the condition
    n = int(input("enter a no."))
    assert n % 2 == 0 #to satisfy the condition (assert is a keyword)
except:
    print("not an even no.")
else:
    reciprocal = 1/n
    print(reciprocal)