# class Deque:
#
#     def __init__(self):
#         self.items = []
#
#     def add_front(self, item):
#         self.items.insert(0, item)
#
#     def add_rear(self, item):
#         self.items.append(item)
#
#     def remove_front(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError('Двусторонняя очередь пуста')
#
#     def remove_rare(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError('Двусторонняя очередь пуста')
#
#     def is_empty(self):
#         return not bool(self.items)
#
#     def size(self):
#         return len(self.items)
#
#     def display(self):
#         return list(self.items)
#
#
# deque = Deque()
#
# deque.add_front(1)
# print(f'Очередь, после добавления 1 в начало - {deque.display()}')
#
# deque.add_rear(2)
# print(f'Очередь, после добавления 2 в конец - {deque.display()}')
#
# deque.add_front(3)
# print(f'Очередь, после добавления 3 в начало - {deque.display()}')
#
# front_element = deque.remove_front()
# print(f'Из начала извлечен элемент {front_element}')
# print(f'Очередь, после извлечения элемента из начала {deque.display()}')
#
# rare_element = deque.remove_rare()
# print(f'Из конца очереди был извлечен элемент {rare_element}')
# print(f'Очередь, после извлечения элемента с конца {deque.display()}')
#
# print(f'Очередь пуста? {deque.is_empty()}')

from collections import deque

deque_queue = deque()


deque_queue.appendleft(1)
deque_queue.append(2)

front_element = deque_queue.popleft()
rare_element = deque_queue.pop()

print(f'Front element {front_element}')
print(f'Rare element {rare_element}')