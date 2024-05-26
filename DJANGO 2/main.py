import numpy as np
import matplotlib.pyplot as plt

def rand_fib_with_lag(numbers: list, a: int, b: int, amount_numbers: int):
    #parth_of_numbers = numbers[0:a]

    for i in range( amount_numbers):#a,

        r_n_a = parth_of_numbers[i - a]
        r_n_b = parth_of_numbers[i - b]

        if (r_n_a >= r_n_b):
            parth_of_numbers.append(r_n_a - r_n_b)

        elif (r_n_a < r_n_b):
            parth_of_numbers.append((r_n_a - r_n_b + 1))

    return parth_of_numbers

def delayed_fibonacci(n):
    fibonacci_list = [0, 1]
    for i in range(2, n):
        next_num = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(next_num)
    return fibonacci_list

# Генерация списока чисел Фибоначчи с запаздыванием
fibonacci_numbers = rand_fib_with_lag(1000,0,1,1000)

print('ff')
# Преобразуем числа в тип float64
#fibonacci_numbers = np.array(fibonacci_numbers, dtype=np.float64)

# Гистограмма
plt.hist(fibonacci_numbers, bins=50, color='skyblue', edgecolor='black')
plt.title('Гистограмма чисел Фибоначчи с запаздыванием')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()


