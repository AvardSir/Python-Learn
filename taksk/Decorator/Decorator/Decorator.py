#def decor_func(func):

#    def slech_above_Print():
#        print('=======')
#        func()
#        print('=======')
#    return slech_above_Print()
#def print_hello_guys():
#    print("hello_guys")
##decor_func(print_hello_guys) #Вызов декораттора как такого

#def decor_2(func):
#    def decor_stars():
#        print('******************')
#        func()
#        print('******************')
#    return decor_stars

#def whats_day():
#    print('today friday')

##whats_day=decor_2(whats_day)#переопределение сдикарированной функции
##whats_day()
##print_hello_guys=decor_2(print_hello_guys)
##print_hello_guys()

#def decor_3(func):
#    def decor_slec():
#        print('///////')
#        func()
#        print('///////')
#    return decor_slec

#@decor_3# Синтаксис Вместо переопределения
#def what_is_my_city():
#    print("st petersburg")
#what_is_my_city()


text = input()

def uppercase_decorator(func):
    def wrapper(text):
        #your code goes here
        return text.upper() 
    return wrapper
    
@uppercase_decorator    
def display_text(text):
    return(text)
    
print(display_text(text))

