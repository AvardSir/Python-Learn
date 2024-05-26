class MultiplicativeCongruentialGenerator:
    def __init__(self, seed, multiplier, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.modulus = modulus

    def generate_random_number(self):
        self.seed = (self.multiplier * self.seed) % self.modulus
        return self.seed

seed = 7
multiplier = 7**5
modulus = 2**32 - 1

mcg = MultiplicativeCongruentialGenerator(seed, multiplier, modulus)

_1000_MultiplicativeCongruentialGenerator=[]
for _ in range(1000):
    _1000_MultiplicativeCongruentialGenerator.append(mcg.generate_random_number())

_5000_MultiplicativeCongruentialGenerator=[]
for _ in range(5000):
    _5000_MultiplicativeCongruentialGenerator.append(mcg.generate_random_number())

_10_000_MultiplicativeCongruentialGenerator = []
for _ in range(10000):
    _10_000_MultiplicativeCongruentialGenerator.append(mcg.generate_random_number())


class DelayedFibonacciGenerator:
    def __init__(self, a, b,numbers):
        self.a = a
        self.b = b
        self.numbers=numbers
    def rand_fib_with_lag(self,amount_numbers):
        parth_of_numbers = self.numbers[0:a]

        for i in range( amount_numbers):#a,

            r_n_a = parth_of_numbers[i - a]
            r_n_b = parth_of_numbers[i - b]

            if (r_n_a >= r_n_b):
                parth_of_numbers.append(abs(r_n_a - r_n_b))

            elif (r_n_a < r_n_b):
                parth_of_numbers.append(abs(r_n_a - r_n_b + 1))
        parth_of_numbers=parth_of_numbers[0:len(parth_of_numbers)-63]
        return parth_of_numbers

a = 63
b = 31
dfg = DelayedFibonacciGenerator(a, b,_10_000_MultiplicativeCongruentialGenerator)

import  numpy as np

dfg_1=dfg.rand_fib_with_lag(1000)
dfg_5=dfg.rand_fib_with_lag(5000)
dfg_10=dfg.rand_fib_with_lag(10000)

import random
random.seed(123)
random_float = random.random()

mer_1=[]
for _ in range(1000):
    mer_1.append(random.random())

mer_5=[]
for _ in range(5000):
    mer_5.append(random.random())

mer_10 = []
for _ in range(10000):
    mer_10.append(random.random())


import matplotlib.pyplot as plt


def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    return None
def build_hist(data):





    # Получить имя списка и вывести
    list_name = get_var_name(data)



    # Построение гистограммы
    plt.hist(data, bins=100, color='skyblue', edgecolor='black')  # bins - количество столбцов (бинов)

    # Добавление заголовка и меток
    plt.title(f'гистограмма {list_name}')
    plt.xlabel('Значение')
    plt.ylabel('Частота')

    # Отображение гистограммы
    plt.show()


def impirica(data):

    import numpy as np
    import matplotlib.pyplot as plt

    # Генерация случайных данных (например, нормальное распределение)


    # Сортировка данных
    sorted_data = np.sort(data)

    # Создание ECDF
    n = len(sorted_data)
    y = np.arange(1, n+1) / n
    name=get_var_name(data)
    # Построение ECDF
    plt.step(sorted_data, y, where='post')
    plt.title(f'Эмпирическая функция распределения (ECDF) для {name}')
    plt.xlabel('Значение')
    plt.ylabel('Вероятность')
    plt.show()

dataS=[_1000_MultiplicativeCongruentialGenerator,
_5000_MultiplicativeCongruentialGenerator,
_10_000_MultiplicativeCongruentialGenerator,
dfg_1,
dfg_5,
dfg_10,
mer_1,
mer_5,
mer_10]

def fun_on_all(funcc,dataS):
    for i in dataS:
        funcc(i)

def Plosko(data):
    import matplotlib.pyplot as plt
    x=[]
    y=[]

    for i in range(0,len(data),2):

        x.append(data[i])
        y.append(data[i+1])
        #y = data[i+1]

    # Построение диаграммы рассеяния

    name = get_var_name(data)
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', alpha=0.5)  # alpha - прозрачность точек
    plt.title(f'Распределение точек на плоскости {name}' )
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()



def vivod(data):
    name=get_var_name(data)
    def viborki(data):
        return  np.mean(data),np.var(data),np.std(data)
    print(f'{name} - {viborki(data)}')





def calculate():
    l = [0, 1]

    mean = sum(l) / 2
    variance = ((l[1] - l[0]) ** 2) / 12
    std = np.sqrt(variance)

    x = np.linspace(l[0] - 0.5, l[1] + 0.5, 1000)

    p_df = []
    integral_pdf = []

    for i in x:
        if i < l[0] or i > l[1]:
            p_df.append(0)
            integral_pdf.append(0)
        else:
            p_df.append((1 / l[1] - l[0]))
            integral_pdf.append((i - l[0]) / (l[1] - l[0]))

    plt.figure(figsize=(14, 3))
    ax1 = plt.subplot(1, 3, 1)
    plt.plot(x, p_df)
    plt.title('Плотность распределения f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    ax2 = plt.subplot(1, 3, 2)
    plt.plot(x, integral_pdf)
    plt.title('Функция распределения F(x)')
    plt.xlabel('x')
    plt.ylabel('F(x)')

    plt.show()

    return mean, variance, std

print(calculate())
#fun_on_all(build_hist,dataS)
#fun_on_all(impirica,dataS)
#fun_on_all(Plosko,dataS)
#fun_on_all(vivod,dataS)
