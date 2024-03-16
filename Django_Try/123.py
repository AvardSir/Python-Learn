
def groupa():

    # N = (номер группы + номер студента в журнале) mod количество_вариантов + 1.
    номер_группы=4117
    номер_студента_в_журнале=13

    количество_вариантов=32

    print((номер_группы+номер_студента_в_журнале)%количество_вариантов)#аллала

groupa()
#алалал
class yol:
    def __init__(self):
        print('g')

sds= yol()
import pandas as pd#fllflf
def pandas_kill_first_colom():



    # Создание DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Удаление первого столбца
    df = df.drop(df.columns[0], axis=1)
    print(df)#dsls;l#sfsfs
pandas_kill_first_colom()
def kilas():#aslsl#sskskks
    import pandas as pd
#askfkk
    # Создание примера DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']}

    df = pd.DataFrame(data)

    # Вывод DataFrame
    print(df)
kilas()

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

