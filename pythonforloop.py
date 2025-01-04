'''Cars = ["creta","breeza","kia","thar"]
#access elements one by one 
for i in Cars:
    print(i)'''

#loop through a string

'''lang = "python"
#iterate over each character in language
for i in lang:
    print(i)'''

#for Loop with python range()

#iterate from i = 0 to i = 3
'''for i in range(4):
    print(i)'''

#for loop with else clause
'''numbers = [1,2,3,4]
for i in numbers:
    print(i)
else:
    print("no items left.")'''

#nested for loops
#outer loop
'''for i in range(2):
#for inner loop
    for j in range(2):
       print(f"i = {i},j = {j}")'''

#F- string allows to run or format selected parts of the string
# {} this is known as placeholder
#To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.




#placeholders and modifiers

#string formatting

price = 55.96
text = f"the price is {price:.2f} rupees"
print(text)