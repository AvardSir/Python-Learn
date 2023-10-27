import re

str = "Please contact info@sololearn.com for assistance"
email=input()
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
if re.match(pattern,email):
    print('oll ok')

if re.match(pattern,'info@sololearn.com'):
    print('pattern work on emails')