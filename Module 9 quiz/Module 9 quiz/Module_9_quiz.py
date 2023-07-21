import re
patter=r"(4{5,6})\1"

if re.match(patter,"456"):
    print('456')


if re.match(patter,"4444444444"):
    print('4444444444')#10

if re.match(patter,"444444444444"):
    print('444444444444')#12

if re.match(patter,"44444"):
    print('44444')#5

    #'10 or 12 fours'