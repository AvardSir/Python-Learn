
def sum(a,b):
    return a+b


a,b=3,2



print(sum(a,b))

print((lambda a,b:a+b)(a,b))#difference nativa and lamda

def lamdas_squer():
    x = int(input())
    y = (lambda z:z**3)(x)

    print(y)#example of lamda
