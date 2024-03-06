def groupa():

    # N = (номер группы + номер студента в журнале) mod количество_вариантов + 1.
    номер_группы=4117
    номер_студента_в_журнале=13

    количество_вариантов=32

    print((номер_группы+номер_студента_в_журнале)%количество_вариантов)#аллала

groupa()

class Person:#qjjj

    def __init__(self, listt):
        self.listt=listt
    def sum_list(self,lists):
        s=0
        for i in lists:
           s+=i
        return s

    def out_list(self):
        for i in self.listt:
            print(i)

# Создание объекта (экземпляра) класса Person
person1 = Person([1,23,4])

# Вызов метода для отображения информации о персоне
person1.out_list()

l=[1,2,3]
person1.sum_list(l)