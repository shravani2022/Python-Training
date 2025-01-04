#filter even numbers from list

#even_numbers = [num for num in range(1,10) if num%2==0]
#print(even_numbers)

word = "python"
vowels ="aeiou"
#list_comprehension 
result = [char for char in word if char in vowels]
print(result)
