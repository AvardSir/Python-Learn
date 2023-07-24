def more_about_else_in_for():

    for i in range(10):
        if i == 999:
            print("else is not work!!!11")
            break
    else:
        print("Unbroken 1")

    for i in range(10):
        if i == 5:
            break
    else:
        print("Unbroken 2")
def try_execpt_else():
    try:
        a=3+2
    except ZeroDivisionError:
        print(2)
    else:
        print('a=3+2')

    try:
        a=3/0
    except ZeroDivisionError:
        print('a=3/0')
    else:
        print(5)


#more_about_else_in_for()
try_execpt_else()