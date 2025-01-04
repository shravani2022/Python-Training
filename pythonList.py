#create a lis
# cars=["suzuki","breeza","toyato","duster"]
print(cars)

#access elements using index
Lang =["python","swift","c++"] #access element
print(Lang[0])

#add element to python list
fruits=["mango","pineapple","grapes","banana"]
print("Original list :",fruits)
#add the element
fruits.append("guava")
print("updates list:",fruits)
color=["pink","blue","black"]
print(color)#changing 3rd item
color[2] = "white"
print(color)
#remove item from list
'''number=[1,2,3,4,5]
print("original:",number)
number.remove(3)
print("updates list :",number)'''





#list extend
'''number1=[1,2,3]
number2=[4,5]\.
#add the items of first list to the second list
number2.extend(number1)
print(number1)
print(number2)'''

#List insert
'''vowel = ["a","e","i","u"]

#'o'is inserted at index 3 (4th position)
vowel.insert(3,'o')
print('list:',vowel)'''

'''prime_numbers = [2,3,5,7,9,11]
#remove all element
prime_numbers.clear()
#updated prime_numbers list
print('list after clear():',prime_numbers)'''

#list pop()
'''prime_number = [2,3,5]
#remove element at index 2
"remove_element",prime_number.pop(2)
print(prime_number)'''

#list count
'''number = [1,2,3,4,5,2,5]
#check the count of number
count = number.count(2)
print("count of numbers2:",count)'''

#list sort()
'''num = [11,3,5,7,9,2]
num.sort()
print("sorted list",num)'''

#create the prime list
#reverse list
'''prime_numbers = [2,3,5,7,11]
prime_numbers.reverse()
print(prime_numbers)'''

#list copy
prime_numbers = [2,3,5]
#copying list
number = prime_numbers.copy()
print(number)