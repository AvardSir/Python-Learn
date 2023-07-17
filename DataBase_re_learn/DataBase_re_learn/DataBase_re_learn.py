
import re

#your code goes here
data=(input())
if data[0]=='0' and data[1]=='0':
    data=re.sub('00','+',data)
print(data)