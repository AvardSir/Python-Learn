import re

def symbols_dot():
    #string_for_check='ufck, Derk'
    if re.match('D..k','affs, Derk'):#.. is instument for pass some symbols
        print('wau we ha word with d and k')
    if re.match('D..k','Derk, sss'):
        print('wau we ha word with d and k')

def symbols_begin_and_end_of_line():
    if re.search('D..k$','Ababab, Derk'):#end of line is $
        print('in end we have D and k!')

    if re.search('^Aba','Ababab, Derk'):#start of line is ^
        print('in begin we have Aba!')
symbols_begin_and_end_of_line()