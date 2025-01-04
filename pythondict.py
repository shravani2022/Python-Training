#creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}

#printing the dictionary
#print(country_capitals)

#access dictionary items
#access the value of keys
#print(country_capitals["Germany"])
#print(country_capitals["England"])

#add items to a dictionary
country_capitals["Italy"]="Rome"
#print(country_capitals)

#remove dictionary items
del country_capitals["Germany"]
#print(country_capitals)

#clear the dictionary
country_capitals.clear()
#print(country_capitals)

#dictionary length
numbers = {
    10:"ten",
    20:"twenty",
    30:"thirty"}
#print("length:",len(numbers))

a = {}
#print(len(a))

#check whether a key exists in a dictionary

file_types = {
    ".txt":"Text File",
    ".pdf":"PDF Document",
    ".jpg":"JPEG Image"
}

#use of in and not in operators
'''print(".pdf" in file_types)
print(".mp3" in file_types)
print(".mp3" not in file_types)'''

marks = {
    "Maths":78,
    "English":87,
    "Physics":67
}

#comment pop operation
element = marks.pop("English")
#print("pop marks :",element)

#dictionary keys()
numbers ={
    1:"one",
    2:"two",
    3:"three",
}
#extract the keys of the dictionary
dictionarykeys = numbers.keys()
#print(dictionarykeys)
