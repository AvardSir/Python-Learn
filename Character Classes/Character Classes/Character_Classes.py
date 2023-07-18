
import re
def square_brackets_in_re():

    pattern = r"[aeiou]"#если есть хоть один из симоловов

    if re.search(pattern,'papki'):
        print('find aeiou')

    if re.search(pattern,'erock'):
        print('find erock')

    pattern=r'[abc][def]'#after leter in abc we have leter from def
    if re.search(pattern,'bf'):
        print('find abcdef')

    pattern = r"[A-Z][A-Z][0-9]"#after big Leter another big leter and a num
    if re.search(pattern,'AA2'):
        print('find AA2')
    if not re.search(pattern,'aA2'):
        print('find Not AA2 is aA2')

    pattern = r"[^A-Z]"#Сивол ищущий ВСЕ СИМВОЛЫ кроме этих
    if re.search(pattern,'Ivanbro'):
        print('find Ivanbro')
    if re.search(pattern,'Ivanbro'):
        print('find Ivanbro')
    if not re.search(pattern,'IVANBRO'):
        print('find IVANBRO and this is not for are we loking for')
square_brackets_in_re()