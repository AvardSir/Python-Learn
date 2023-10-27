import numpy
from prettytable import PrettyTable
import matplotlib.pyplot as plt
slots = 1000000
N_list = []
T_list = []
step = 5
for lam in range(5, 55, step):
    P_k = [] * slots # количество пользователем с новым сообщением
    P_k.clear()
    P_k = numpy.random.poisson(lam/100, slots)
    N_k = [] * slots # количество активных пользователей

    N_k.clear()
    N_k.append(0)
    R_k = [] * slots # количество пользователей, отправивших сообщение
    R_k.clear()
    for i in range(1, slots):
        if N_k[i-1] == 0:
            R = 0
        else:
            R = numpy.random.binomial(N_k[i-1], 1/N_k[i-1])
        R_k.append(R)
        if R_k[i-1] == 1:
            N_k.append(N_k[i-1] - 1 + P_k[i-1])
        else:
            N_k.append(N_k[i-1] + P_k[i-1])
    if N_k[slots-1] == 0:
        R = 0
    else:
        R = numpy.random.binomial(N_k[slots-1], 1/N_k[slots-1])
    R_k.append(R)
    # my_table_2 = PrettyTable()
    # my_table_2.add_row(P_k)
    # my_table_2.add_row(R_k)
    # my_table_2.add_row(N_k)
    #print(*R_k)
    #print(*P_k)
    #print(*N_k)
    sum: float = 0
    for i in N_k:
        sum += i
    N_sr = (1/slots) * sum
    N_list.append(round(N_sr, 4))
    print(f'Среднее N = {round(N_sr ,4)}')

    T_sr = N_sr / (lam/100)
    T_list.append(round(T_sr, 4))
    print(f'Среднее T = {round(T_sr ,4)}')
NT_table = PrettyTable(['N_sr', 'T_sr', 'lambda'])
print(N_list)
print(T_list)
lam_list = []
for lam in range(5, 55, step):
    lam_list.append(lam/100)
for i in range(len(lam_list)):
    NT_table.add_row([N_list[i], T_list[i], lam_list[i]])
print(NT_table)

plt.plot(lam_list, N_list,'r--')
plt.xlabel("Среднее количество абонентов")
plt.ylabel("Среднее время")
plt.show()

plt.plot(lam_list, T_list,'g-')
plt.xlabel("Среднее количество абонентов")
plt.ylabel("Среднее количество активных абонентов")
plt.show()

s