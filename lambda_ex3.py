#how you can use the lambda function with filter()?

#program to filter out only the even items from a list

my_list = [1,2,3,4,5,6,7,8,9,10]
a = list(filter(lambda x:(x%2==0),my_list))
print(a)

