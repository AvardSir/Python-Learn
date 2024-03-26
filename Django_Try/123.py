import networkx as nx
import matplotlib.pyplot as plt

# Функция для визуализации квадратной решетки с определенными цветами для рёбер
def visualize_grid_graph(graph, M, colored_edges):
    G = nx.Graph()  # Создание пустого графа с помощью библиотеки NetworkX

    # Добавление вершин в граф
    for V in range(M * 2):
        G.add_node(V)

    # Добавление рёбер в граф на основе матрицы смежности
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                if (i, j) or (j, i) in colored_edges in colored_edges:
                    # Если ребро нужно0  покрасить в другой цвет
                    G.add_edge(i, j, color='red')
                else:
                    G.add_edge(i, j, color='black')

    # Задание позиций вершин для визуализации
    pos = {V: (V % M, V // M) for V in range(M * 2)}

    # Раскраска определенных рёбер
    edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'black' for u, v in G.edges()]

    # Визуализация графа с раскрашенными рёбрами
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='purple', font_size=10, font_weight='bold',
            edge_color=edge_colors, arrows=False, font_color='white')
    plt.title('Правильная квадратная решетка с определенными цветами для рёбер')
    plt.show()

# Пример матрицы смежности для квадратной решетки с определенными цветами для рёбер
M = 2  # Размер квадратной решетки
colored_edges = [(0, 1), (2, 3)]  # Рёбра, которые нужно покрасить в другой цвет

# Визуализация квадратной решетки с определенными цветами для рёбер
visualize_grid_graph(graph, M, colored_edges)


matix2X=create_grid_graph2(2,1,3)
short_from_to(matix2X)
visualize_grid_graph(matix2X, 2,colored_edges)#