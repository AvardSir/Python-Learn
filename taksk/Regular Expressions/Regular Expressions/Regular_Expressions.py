
import re
string_for_check='duck duck duck'
def with_what_we_work_And_with_that_sample(what,sample,string_for_check):
    if what(sample,string_for_check):
        print('can search '+str(sample)+' in '+string_for_check)
    else:
        print('no '+str(sample))
    return

def match_learn():
    pattern=r'duck'

    if re.match(pattern,'duck duck duck'):
        print("match pattern")
    else:
        print('no')

    if re.match('duck','duck duck duck'):
        print("match duck")
    else:
        print('no')

    if re.match('du','duck duck duck'):
        print("match du")
    else:
        print('no')

    if re.match('uck','duck duck duck'):
        print("match")
    else:
        print('no uck')#match re
def search():
    #with_what_we_work_And_with_that_sample(re.search,'c','duck,duck')
    #with_what_we_work_And_with_that_sample(re.search,'dick','duck,duck')

    serchS=re.search('duck','dddddduck,duck')#find first duck
    print(serchS)#print inf about first duck
    print(serchS.span())#methods for individual parametrs
    print(serchS.group())
    print(serchS.start())
    print(serchS.end())
    
    #if re.search('uck','duck duck duck'):
    #    print('can search uck')
    #else:
    #    print('no uck')
def findAll():
    all_d=re.findall('d','duck,duckddd')#find all crat list with his searhicnh tresuar
    print(all_d)
    print(len(all_d))
    #with_what_we_work_And_with_that_sample(re.findall,'dick','duck,duck')#function not work for my tipical function

def suB():
    def creat_pure_sample_for_cehck():
        string='Duck Duck Duck'
        what_want_replace='Duck'
        what_do_we_replace="Cat"
        return string,what_want_replace,what_do_we_replace
    string,what_want_replace,what_do_we_replace=creat_pure_sample_for_cehck()
    

    string=re.sub(what_want_replace,what_do_we_replace,string)#good position of arguments THen we replace Duck to cat in Duck Duck Duck
    print(string)

    string,what_want_replace,what_do_we_replace=creat_pure_sample_for_cehck()#NOT good position of arguments THen we replace Duck Duck Duck to cat in Duck
    string=re.sub(string,what_want_replace,what_do_we_replace)
    print(string)
    #print(re.sub(string,what_want_replace,what_do_we_replace))
    
#findAll()
#match_learn()
#search()

suB()