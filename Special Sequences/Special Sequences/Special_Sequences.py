
import re
pattern = r"(\D+\d) \1"
def grop_catch():

    pattern = r"(.+) \1"   #(.+) группа из одного и более слова  \1-показывает что их можнт быть дава три четыре

    match = re.match(pattern, "word word")
    if match:
        print ("Match 1")

    match = re.match(pattern, "?! ?!")
    if match:
        print ("Match 2")    

    match = re.match(pattern, "a a a")
    if match:
        print ("Match 3")

     
    pattern = r"(\D+\d) \1"#не число число
    match = re.match(pattern, "a3 a3")
    if match:
        print ("(\D+\d) \1 a3 a3")

    pattern = r"(\D+\d)"
    match = re.match(pattern, "a3 a3")
    if match:
        print ("(\D+\d) a3")

    pattern = r"(\D+\d)\1"
    match = re.match(pattern, "a3a3")
    if match:
        print ("(\D+\d)\1 a3a3")

def more_Special_Sequences():
   

    pattern = r"\b(cat)\b"#ищет пробел до и после cat

    match = re.search(pattern, "The cat sat!")#
    if match:
        print("Match 1")

    match = re.search(pattern, "We s>cat<tered?")
    if match:
        print ("Match 2")

    match = re.search(pattern, "We s cattered.")
    if match:
        print ("Match 4")
    
    match = re.search(pattern, "We scat tered.")
    if match:
        print ("Match 5")

    match = re.search(pattern, "We s cat tered.")
    if match:
        print ("Match 6")

def begind_end():
    
    if re.search('\AAbc','Abc'):
        print('\AAbc Abc')
        

    if re.search('\A','bAbc'):
        print('bAbc')


    if re.search('\Zc','bAb c'):
        print('\Zc bAbc')

    if re.search('\ZC','bAb C'):
        print('\Zc bAbc')

        
    if re.search('hey \Z','hey '):#чтож обидно но Символ конца строки должен быть в концею...
        print('\Zc bAbc')


#grop_catch()
#more_Special_Sequences()
begind_end()