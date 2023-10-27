
def ver_and_grapsh():

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

    plt.plot(lam_list, N_list)
    plt.xlabel("Среднее количество абонентов")
    plt.ylabel("Среднее время")
    plt.show()

    plt.plot(lam_list, T_list)
    plt.xlabel("Среднее количество абонентов")
    plt.ylabel("Среднее количество активных абонентов")
    plt.show()


import math
import numpy
from math import factorial
import igraph as ig
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def binomial(p, j):
    return ((1-p)**(j-1))


def poisson(lam, j):
    return (((lam/100)**j)/factorial(j))*math.exp(-(lam/100))


def mark_model(n : int, edges: list[tuple], weight: list[int]):
    G = ig.Graph(directed=True)

    G.add_vertices(n)
    G.vs["label"] = range(0, n)
    G.add_edges(edges)

    G.es["weight"] = weight

    fig, ax = plt.subplots(figsize=(10, 10))
    ig.plot(G,
    target=ax,
    layout="kk", # print nodes in a circular layout
    vertex_size=50.0,
    vertex_color="red",
    vertex_frame_width=0.0,
    vertex_frame_color="white",
    vertex_label=G.vs["label"],
    vertex_label_size=12.0,
    edge_label=G.es["weight"],
    edge_label_size=10.0,
    edge_width= 0.5
    )
    plt.show()



for lam in range(5, 55, 5):
    states = 4 # количество состояний N_k # Тобиш Количество Интервалов времени Когда можно передавать сообщения
    prob = [[0] * states for i in range(states)]

    for i in range(states):#Mistake coding?
        prob[i] = [0] * states

    edges = []
    #print((round((1-binomial(float(1/2), 2)) * poisson(lam, 0) + binomial(float(1/2), 2) * poisson(lam, 1), 4)))
    for i in range(0, states):
        for j in range(0, states):
            if i == 0:
                prob[i][j] = round(poisson(lam, j), 4)
                edges.append((i, j))
            elif i == j:
                prob[i][j] = round((1 - binomial(float(1 / i), i)) * poisson(lam, 0) + binomial(float(1 / i), i) * poisson(lam, 1), 4)
                edges.append((i, j))
            elif i < j:
                prob[i][j] = round(binomial(float(1 / i), i) * poisson(lam, j - i + 1) + (1 - binomial(float(1 / i), i)) * poisson(lam, j - i), 4)
                edges.append((i, j))
            elif i == j + 1:
                prob[i][j] = round(binomial(float(1 / i), i) * poisson(lam, 0), 4)
                edges.append((i, j))
            #edges.append((i, j))
    #print(prob)
    table_h = []
    table_h.append(' ')
    for i in range(len(prob[0])):
        table_h.append(f'Состояние {i}')
    my_table = PrettyTable(table_h)

    for i in range(states):
        my_table.add_row([f'Состояние {i}'] + prob[i])
    print(my_table)
    all_probs = []
    for i in prob:
        all_probs.extend(i if isinstance(i, list) else [i])

    while 0 in all_probs:
        all_probs.remove(0)

    #print(all_probs)
    #print(edges)

    mark_model(states, edges, all_probs)





