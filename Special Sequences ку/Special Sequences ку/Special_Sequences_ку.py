
import re
text = input()
#your code goes here
#use re.findall() with r"#\w+" as the regex
text=re.findall(r"#\w+",text)
for i in text:
    print (i)

#if re.match("\w+",'abc'):
#    print('lol')
 