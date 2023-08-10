for i in range(10):

    print('lol')    

b=10
for i in range(100):
    a=(lambda x:x+1)(b)
    b=a
print(a)