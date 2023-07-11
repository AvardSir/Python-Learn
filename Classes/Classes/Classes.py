
#from collections import _OrderedDictValuesView


#class h_class(object):
#    def __init__(self,num_of_h=3) -> None:
#        print("h")
#        self.num_of_h=num_of_h
#        print(num_of_h)


#h=h_class(2)

#h2=h_class()

class animal:
    def __init__(self,color):
        self.color=color
    def sound(self):
        print('kz kz kz')

class dog(animal):
    def sound(self):
        
        print('BARK BARK')
        super().sound()

Ovcharka=dog("red")
Ovcharka.sound()

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

#B().spam()