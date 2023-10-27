def set_var_with_tuples():

    numbers = (1, 2, 3)
    a, b, c = numbers

    if 0:

        a, b = b, a


    print(a)
    print(b)
    print(c)

def set_var_more_then_we_think():

    a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]#
    print(a)
    print(b)
    print(c)#an asterisk (*) takes all values from the collection that are left over from the other variables.
    print(d)