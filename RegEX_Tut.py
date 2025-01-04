#A regular expression (RegEx) is a sequence of characters that defines a search pattern 

#Python has a module named re to work with RegEx.

import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("search successful.")

else:
    print("search unsuccessful.")



#^ used for 'starts with'

#$ used for 'ends with'