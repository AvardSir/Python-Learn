def path_prop(G,source = 1, target = 9):
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



    # Определяем вершины и проверяем существование пути между ними

    if is_path_exists(G, source, target):

        print(f"Путь существует между вершинами {source} и {target}")
    else:
        print(f"Пути нет между вершинами {source} и {target}")