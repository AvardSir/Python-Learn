def opredelim_obr(symbol):
    diction = {'(': ')', '[': ']', '{': '}'}
    return diction[symbol]


def brecket(word, symbol):
    print(len(word))
    left_sybmols = ['(', '{', '[']
    right_sumbols = [opredelim_obr(i) for i in left_sybmols]
    if symbol in right_sumbols:
        return False

    revers_symbol = opredelim_obr(symbol)
    for i in range(len(word)):
        if word[i] in left_sybmols and word[i] != revers_symbol or word[i] == revers_symbol:
            return brecket(word[1:len(word)], word[i])
        else:
            return False
    return True


def first_in_brecket(word):
    if len(word) < 2:
        return False
    else:

        return brecket(word[1:len(word)], word[0])


word = '(){]'
print(first_in_brecket(word))
#Lol

#yoooo
#today i know a lot of things about mas statistics