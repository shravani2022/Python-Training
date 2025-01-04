try:
    n = 10
    d = 0
    result = n/d
    print(result)

except:
    print("error: denominator cannot be 0.")

finally:
    print("this is finally block")