
import re
if 1:

    Id = input()
else:
    #Id='LG17'
    Id='AM84125'
#your code goes here
if re.match('[A-Z][A-Z][0-9][0-9]$',Id):#LG17
    print('Searching')
else:
    print("Wrong format")