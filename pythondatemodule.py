import datetime
x = datetime.datetime.now()
#year and name of weekend
print(x.year)
print(x.strftime("%A"))

#create date object
import datetime
x = datetime.datetime(2024,7,21)
print(x)
print(x.strftime("%B"))