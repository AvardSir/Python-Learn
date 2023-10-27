
import re
#password = input()
password='lhg1439'
#your code goes here
if re.search('[A-Z]',password) and re.search('[0-9]',password):
    print("Password created")
else:
    print("Wrong format")