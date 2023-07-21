#change the function
def adder(*args):
    s=0
    for i in args:
        s+=i
    return s
    #print(args+args)

print(adder(2, 3))
print(adder(2, 3, 4))
print(adder(1, 2, 3, 4, 5))