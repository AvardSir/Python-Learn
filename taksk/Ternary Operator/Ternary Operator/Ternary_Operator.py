
def ternany():
    def case1():

        a = 7
        b = 12 if a >= 55 else 42
        print(b)
        
    def case2():

        a = 7
        b = 12 if a >= 5 else 42#Ternany B=12 IF a>=5 else 42 LOL
        print(b)

    def case3():
        status  = 1
        msg = "Logout" if status == 1 else "Login"

        print(msg)

    
    def case4():
        status  = 0
        msg = "Logout" if status == 1 else "Login"

        print(msg)
    case1()
    case2()
    case3()
    case4()
ternany()