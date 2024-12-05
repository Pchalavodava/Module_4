class Node:
    def __init__(self, value: str):
        """
        Инициализация узла
        :param value: str: Название узла
        """
        self.value: str = value
        self.inbound: list[Node] = []
        self.outbound: list[Node] = []

    def point_to(self, other) -> None:
        """
        Заполнения исходящих/входящих ребер
        :param other: исходящее ребро (узлы, куда ориентирован данный узел
        :return: None
        """
        self.inbound.append(self)
        self.outbound.append(other)

    def __str__(self) -> str:
        """
        Строковое представление узла
        :return: str: Узел (название)
        """
        return f'Node ({self.value})'


class Graph:
    def __init__(self, root: Node):
        """
        Инициализация графа
        :param root: Node: корень, по которому идет проверка графа в глубину
        """
        self._root: Node = root
        self.visited: list[Node] = []
        self.neighbors: list[Node] = [self._root]

    def is_neighbors_empty(self) -> bool:
        """
        Проверка, пуст ли стек соседних вершин
        :return: bool: True, если пуст, False - иначе
        """
        return not bool(self.neighbors)

    def add_to_visited(self, root: Node) -> None:
        """
        Добавление в список посещенных
        :param root: Node: посещенный узел
        :return: None
        """
        self.visited.append(root)

    def add_neighbors(self, outbounds: Node) -> None:
        """
        Добавление в стек соседних вершин (исходящих ребер)
        :param outbounds: Node: исходящее ребро
        :return: None
        """
        self.neighbors.append(outbounds)

    def take_neighbor(self) -> Node:
        """
        Извлечение из стека вершины для посещения
        :return: Node: первое доступное исходящее ребро для этой вершины
        """
        if not self.is_neighbors_empty():
            return self.neighbors.pop()
        else:
            raise IndexError('Стек пуст')

    def dfs(self) -> list:
        """
        Обход графа в глубину
        :return: list: список посещенных вершин
        """
        while self.neighbors:
            vertex = self.take_neighbor()
            if vertex not in self.visited:
                self.add_to_visited(vertex)
                for neighbor in reversed(vertex.outbound):
                    if neighbor not in self.visited:
                        self.add_neighbors(neighbor)
        self.visited = [str(element) for element in self.visited]
        return self.visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')
# k = Node('k')
# a.point_to(b)
# b.point_to(c)
# c.point_to(d)
# d.point_to(a)
# b.point_to(d)
# a.point_to(e)
# e.point_to(f)
# e.point_to(g)
# f.point_to(i)
# f.point_to(h)
# g.point_to(k)

graph = Graph(a)
print(graph.dfs())

