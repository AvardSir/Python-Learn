import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def zapolni_griod(N,p):
    import random
    def gen_mas(mass, num_change):#Генерация массив из [0,0,0]  в [1,1,0] при параметре в 2
        for i in range(round(num_change)):

            mass[i] = 1
        return mass

    import numpy as np
    M = p * N
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(len(grid)):
        if random.randint(0, 100) < p * 100:#заполенине массива с вероятностью p
            grid[i] = gen_mas(grid[i], M)

    return grid

def generate_graph_from_grid(grid):#Генерация графа
    G = nx.Graph()
    n = len(grid)

    # Добавляем вершины в граф для каждой закрашенной клетки
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                G.add_node((i, j))

    # Добавляем ребра между соседними закрашенными клетками
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # Проверяем соседние клетки
                if i > 0 and grid[i - 1][j] == 1:
                    G.add_edge((i, j), (i - 1, j))
                if i < n - 1 and grid[i + 1][j] == 1:
                    G.add_edge((i, j), (i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    G.add_edge((i, j), (i, j - 1))
                if j < n - 1 and grid[i][j + 1] == 1:
                    G.add_edge((i, j), (i, j + 1))

    # Определяем координаты вершин внутри ячеек решетки
    vertex_positions = {(i, j): (j + 0.5, -i - 0.5) for i, j in G.nodes()}

    # Рисуем граф с разметкой и вершинами внутри решетки
    nx.draw_networkx(G, pos=vertex_positions, with_labels=True, node_size=400, node_color="lightblue", font_size=7)


    plt.show()
    return G



def de_Square(example_grid):#Создание графа используя квадратное визуальное оформление.

    import pygame#использован модуль pygame
    import numpy as np

    # Константы
    WIDTH, HEIGHT = 800, 600
    CELL_SIZE = 50

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid")

    # Функция для рисования сетки с заданным массивом состояний ячеек
    def draw_grid(grid):
        rows, cols = grid.shape
        for i in range(rows):
            for j in range(cols):
                color = RED if grid[i][j] == 1 else BLACK
                pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Основной цикл игры
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(example_grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()



def Спектр_степеней_графа(G):
    import networkx as nx
    import matplotlib.pyplot as plt

    def degree_histogram(graph):
        degrees = [graph.degree(node) for node in graph.nodes()]
        histogram = {}
        for degree in degrees:
            if degree in histogram:
                histogram[degree] += 1
            else:
                histogram[degree] = 1
        return histogram

    # Получаем гистограмму степеней вершин
    histogram = degree_histogram(G)

    # Построение гистограммы
    plt.bar(histogram.keys(), histogram.values(), color='b')
    plt.xlabel('Степень вершины')
    plt.ylabel('Частота')
    plt.title('Гистограмма распределения степеней вершин')
    plt.show()


def path_prop(graph, source=(1, 0), target=(9, 0)):
    import networkx as nx
    import matplotlib.pyplot as plt

    def is_path_exists(graph, source, target):
        visited = set()
        stack = [source]

        try:
            while stack:
                current_node = stack.pop()
                if current_node == target:
                    return True
                if current_node not in visited:
                    visited.add(current_node)
                    stack.extend(graph.neighbors(current_node))

        except:
            pass

        return False





    return is_path_exists(graph, source, target)

#print(path_prop(G))
#Спектр_степеней_графа(G)

def generate_graph_from_grid_2_BEZ_GRAPICA(grid):#Генерация графа
    G = nx.Graph()
    n = len(grid)

    # Добавляем вершины в граф для каждой закрашенной клетки
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                G.add_node((i, j))

    # Добавляем ребра между соседними закрашенными клетками
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # Проверяем соседние клетки
                if i > 0 and grid[i - 1][j] == 1:
                    G.add_edge((i, j), (i - 1, j))
                if i < n - 1 and grid[i + 1][j] == 1:
                    G.add_edge((i, j), (i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    G.add_edge((i, j), (i, j - 1))
                if j < n - 1 and grid[i][j + 1] == 1:
                    G.add_edge((i, j), (i, j + 1))

    # Определяем координаты вершин внутри ячеек решетки
    #vertex_positions = {(i, j): (j + 0.5, -i - 0.5) for i, j in G.nodes()}

    # Рисуем граф с разметкой и вершинами внутри решетки
    #nx.draw_networkx(G, pos=vertex_positions, with_labels=True, node_size=400, node_color="lightblue", font_size=7)


    #plt.show()
    return G


#grid=np.array(zapolni_griod(N,p))

#G=generate_graph_from_grid(grid)#Рисование графовой формы

#de_Square(grid)#Рисование квадратной формы

N = 10
p = 0.1
list_p=[]
otvet=[]
for i in range(21):
    s = 0
    p=round(i*0.05,2)
    list_p.append(round(p,2))
    for j in range(1000):
        grid = np.array(zapolni_griod(N, p))

        G = generate_graph_from_grid_2_BEZ_GRAPICA(grid)
        #de_Square(grid)
        if path_prop(G):
            s+=1
    otvet.append(s)

print(otvet)
print(list_p)
plt.scatter(otvet, list_p)
plt.xlabel('Количество когда можно дойти из конца в конец')
plt.ylabel('Вероятность')
# Показ графика
plt.show()