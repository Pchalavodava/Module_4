import random
from dataclasses import dataclass
from pprint import pprint
from typing import Optional


@dataclass
class Task:
    name: str


class TaskQueue:
    """
    Класс очереди задач
    """

    def __init__(self, queue_len: int = 10):
        self.task_list: list[Task] = []
        self.queue_len = queue_len

    def add_task(self, task: Task) -> None:
        """
        Добавление задачи в очередь
        :param task: list[Task]: задача, добавляемая в очередь
        :return: None
        """
        self.task_list.append(task)

    def is_empty(self) -> bool:
        """
        Проверка, если пуста очередь
        :return: bool: True, если пуста, False иначе
        """
        return not bool(self.task_list)

    def get_next_task(self) -> Optional[Task]:
        """
        Получение первой задачи из очереди
        :return: Optional[Task]: Задача, находящаяся первой в списке (очереди), если очередь не пуста, иначе None
        """
        if not self.is_empty():
            return self.task_list.pop(0)
        else:
            return None

    def get_last_task(self) -> Optional[Task]:
        """
        Получение последней задачи из очереди
        :return: Optional[Task]: Задача, находящаяся последней в списке (очереди), если очередь не пуста, иначе None
        """
        if not self.is_empty():
            return self.task_list.pop()
        else:
            return None

    def replace_last_task(self, task: Task) -> Task:
        """
        Извлечение первой задачи для обработки из списка и добавление новой задачи в очередь на нужную позицию
        :param task: Task: Новая задача
        :return: Task: Первый элемент (задача) в списке (очереди)
        :raises ValueError: Если очередь пустая
        :raises ValueError: Если выбранная позиция превышает количество элементов

        >>> TaskQueue().replace_last_task(Task('Моя задача 3'))
        Traceback (most recent call last):
        ...
        ValueError: Очередь пуста - извлекать нечего. Невозможно добавить задачу
        """
        if self.is_empty():
            raise ValueError('Очередь пуста - извлекать нечего. Невозможно добавить задачу')
        else:
            replaced_task = self.get_last_task()
            self.add_task(task)
        return replaced_task

    def is_full(self) -> bool:
        """
        Проверка, заполнена ли очередь. Предполагается, что максимальная длина = 10
        :return: bool: True, если заполнена, False - иначе
        """
        return len(self.task_list) == self.queue_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()


queue = TaskQueue()

# task1 = Task("Задача 1")
# task2 = Task("Задача 2")
# task3 = Task("Задача 3")
#
# queue.add_task(task1)
# queue.add_task(task2)
# queue.add_task(task3)


"""
Примеры для мною добавленных методов
"""
task_list = [Task("Задача 1"), Task("Задача 2"), Task("Задача 3"),
             Task("Задача 4"), Task("Задача 5"), Task("Задача 6"),
             Task("Задача 7"), Task("Задача 8"), Task("Задача 9"),
             Task("Задача 10"), Task("Задача 11"), Task("Задача 12")]

for my_task in task_list:
    if not queue.is_full():
        queue.add_task(my_task)

print(queue.replace_last_task(Task('Задача 15')).name)

# pprint(queue.task_list)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")


# Ожидаемый результат: "Задача 1"

queue.get_next_task()
queue.get_next_task()

# Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")

# Ожидаемый результат: False

