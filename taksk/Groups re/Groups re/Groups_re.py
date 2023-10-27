import math
import re

def start_group():

    pattern = r"a(bc)(de)(f(g)?h)i"

    match = re.match(pattern, "abcdefghijklmnop")
    if match:
        print(match.group())#all siblols
        print(match.group(0))#grop of all siblols
        print(match.group(1))#bc
        print(match.group(2))#de
        print(match.group(3))#fgh
        print(match.group(4))#g
        print(match.groups())#list of groups

def named_grops():
    
    pattern = r"(?P<first>abc)(?:def)(ghi)"#?P<название группы> Format for named group. (?:def) for other non named grouos

    match = re.match(pattern, "abcdefghi")
    if match:
        print(match.group("first"))
        print(match.groups())

    pattern=r"(?P<cool_grop>AaA)"
    match = re.match(pattern, "AaA")
    if match:
        print(match.group("cool_grop"))
        #print(match.group('cool_grop'))

def another_meta_symbol():
    pattern = r"gr(a|e)y"#ORR

    match = re.match(pattern, "gray")
    if match:
        print ("Match 1")

    match = re.match(pattern, "grey")
    if match:
        print ("Match 2")    

    match = re.match(pattern, "griy")
    if match:
         print ("Match 3")

    pattern=r'a|e'
    match=re.match(pattern,'a')
    if math:
        print('a|e with a')
    match=re.match(pattern,'e')
    if math:
        print('a|e with e')
#start_group()
#named_grops()

another_meta_symbol()