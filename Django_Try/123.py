
def groupa():

    # N = (номер группы + номер студента в журнале) mod количество_вариантов + 1.
    номер_группы=4117
    номер_студента_в_журнале=13

    количество_вариантов=32

    print((номер_группы+номер_студента_в_журнале)%количество_вариантов)#аллала

groupa()

import pandas as pd
def pandas_kill_first_colom():



    # Создание DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Удаление первого столбца
    df = df.drop(df.columns[0], axis=1)
    print(df)
pandas_kill_first_colom()

class Person:#qjjj#

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

