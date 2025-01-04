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

#perform operations in F-Strings
#text = f"the price is {10*10} rupees"
#print(text)

price = 45
tax = 0.18
text = f"the price is {price+(price*tax)} rupees"
print(text)

'''price = 56
text =f"it is very {'expensive' if price>50 else 'cheap'}"
print(text)'''

'''price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)'''