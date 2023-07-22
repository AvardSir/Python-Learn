def Tuple_fun():

    numbers = (1, 2, 3)
    a, b, c = numbers
    print(a)
    print(b)
    print(c)
    a=3
    b=4
    print(str(a)+"-a\t"+str(b)+'-b\t')
    a,b=b,a
    print(str(a)+"-a\t"+str(b)+'-b\t')

def tuple_fun_with_star():
    a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]#*c take all that left
    print(a)
    print(b)
    print(c)
    print(d)

tuple_fun_with_star()
#Tuple_fun()