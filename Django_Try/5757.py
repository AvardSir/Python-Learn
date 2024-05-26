import networkx as nx
import matplotlib.pyplot as plt


def is_path_exists(graph, source, target):
    visited = set()
    stack = [source]

    while stack:
        current_node = stack.pop()
        if current_node == target:
            return True
        if current_node not in visited:
            visited.add(current_node)
            stack.extend(graph.neighbors(current_node))

    return False


# Создаем граф
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (3, 4)])

# Визуализируем граф
pos = nx.spring_layout(G)  # Позиционируем вершины
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)  # Рисуем граф
plt.show()

# Определяем вершины и проверяем существование пути между ними
source = 1
target = 4
if is_path_exists(G, source, target):
    print(f"Путь существует между вершинами {source} и {target}")
else:
    print(f"Пути нет между вершинами {source} и {target}")