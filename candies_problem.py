#jar contain 100
total_candies = int(input("Enter candies in jar: "))
candies_take_from_jar = int(input("Enter candies want to take from jar:"))

if total_candies>1 & total_candies>=100 :
    print("total candies in jar :",total_candies)
    print("Remaining candies in jar",total_candies-candies_take_from_jar)

else :
    print("Invalid Input")    