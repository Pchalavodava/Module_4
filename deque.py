class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Двусторонняя очередь пуста')

    def remove_rare(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Двусторонняя очередь пуста')

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)


deque = Deque()

deque.add_front(1)
deque.add_rear(2)
deque.add_front(3)

print(f'Размер очереди {deque.size()}')

front_element = deque.remove_front()
print(f'Из начала извлечен элемент {front_element}')

rear_element = deque.remove_rare()
print(f'Из конца извлечен элемент {rear_element}')

print(f'Очередь пуста? {deque.is_empty()}')




