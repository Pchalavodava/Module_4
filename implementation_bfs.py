from collections import deque


class Node:
    def __init__(self, value):
        """
        Инициализация узла
        :param value: str: Значение вершины графа
        """
        self.value: str = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    def point_to(self, other) -> None:
        """
        Заполнение рёбер исходящих из вершины и входящих соответственно
        :param other: Node: Соседняя вершина
        :return: None
        """
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        """
        Строковое представление вершины
        :return: str: Node(название вершины)
        """
        return f'Node ({self.value})'


class Graph:

    def __init__(self, root):
        """
        Инициализация вершины графа
        :param root: Node: вершина графа (корень)
        :param self.visited: list[Node]: список посещенных вершин
        :param self.queue: deque: очередь вершин, ожидающих прохождения
        """
        self._root: Node = root

        self.visited: list[Node] = []
        self.queue: deque[Node] = deque()  # Здесь не уверена

    def is_empty(self) -> bool:
        """
        Проверка на заполненность очереди
        :return: bool: True, если очередь пуста, False - иначе
        """
        return not bool(self.queue)

    def get_next_point(self) -> Node:
        """
        Получение из очереди следующей вершины для прохождения (первой в очереди)
        :return: Node: Первый элемент очереди
        """
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise 'Очередь пуста'

    def add_to_queue(self, vertex: Node) -> None:
        """
        Добавление в очередь соседних вершин
        :param vertex: Node: Соседняя вершина
        :return: None
        """
        self.queue.append(vertex)

    def add_to_visited(self, vertex: Node) -> None:
        """
        Заполнения списка посещенных вершин
        :param vertex: Node: Посещенная вершина
        :return: None
        """
        self.visited.append(vertex)

    def bfs(self) -> list[str]:
        """
        Метод обхода графа в ширину
        :return: list[str]: Список пройденных вершин
        """
        self.add_to_queue(self._root)
        while self.queue:
            vertex = self.get_next_point()
            self.add_to_visited(vertex)
            for neighbor in vertex.outbound:
                if neighbor not in self.visited and neighbor not in self.queue:
                    self.add_to_queue(neighbor)

        self.visited = [str(element) for element in self.visited]
        return self.visited


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# a.point_to(b)
# a.point_to(c)
# a.point_to(d)
# b.point_to(g)
# c.point_to(b)
# c.point_to(e)
# c.point_to(f)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

graph = Graph(a)
print(graph.bfs())
