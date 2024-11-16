class Queue:

    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        # return len(self.queue_list) == 0
        return not bool(self.queue_list)

    def enqueue(self, element):
        self.queue_list.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue_list.pop(0)
        else:
            raise IndexError('Очередь пуста')

    def size(self):
        return len(self.queue_list)


# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Размер очереди:", queue.size())  # Размер очереди: 3

while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)