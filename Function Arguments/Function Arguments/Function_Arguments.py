
def function_funn():
    
    def function(named_arg, *args):
        print(named_arg)
        print(args)
    
    def function2( *args):
        #print(named_arg)
        print(args)

    function2(1, 2, 3, 4, 5)

    #function(1, 2, 3, 4, 5)


#function_funn()

def Default_Values():
    def function(x, y, food="spam"):#если нету фуда то он спам
        print(food)

    function(1, 2)
    function(3, 4, "egg")

#Default_Values()

def standing_for_keyword_arguments():
    def my_func(x, y=7, *args, **kwargs):   #**kwargs создает словарь именновых переменных
        print(kwargs)                       #Аргументы, возвращаемые **kwargs, не включаются в *args.

    my_func(2, 3, 4, 5, 6, a=7, b=8)

standing_for_keyword_arguments()