
import re
#your code goes here

pattern=r'[189]\d{7}$'


if 0:

    if re.match(pattern,'81239870'):
        print('ok')

else:
    string=input()
    if re.match(pattern,string):
        print('Valid')
    else:
        print('Invalid')