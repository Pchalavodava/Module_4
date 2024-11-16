from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    name: str


class TaskQueue:
    """
    Класс очереди задач
    """

    def __init__(self):
        self.task_list: list[Any] = []

    def add_task(self, task: Any) -> None:
        """
        Добавление задачи в очередь
        :param task: list[Any]: задача, добавляемая в очередь
        :return: None
        """
        self.task_list.append(task)

    def is_empty(self) -> bool:
        """
        Проверка, если пуста очередь
        :return: bool: True, если пуста, False иначе
        """
        return not bool(self.task_list)

    def get_next_task(self) -> Any:
        """
        Получение первой задачи из очереди
        :return: Any: Задача, находящаяся первой в списке (очереди)
        """
        if not self.is_empty():
            return self.task_list.pop(0)
        else:
            return None

    def get_add_task(self, task: Task) -> Any:
        """
        Извлечение первой задачи при добавлении новой
        :param task: Task: Новый элемент списка
        :return: Any: Первый элемент в списке (очереди)
        :raises ValueError: Если очередь пустая

        >>> TaskQueue().get_add_task(Task('Моя задача 3'))
        Traceback (most recent call last):
        ...
        ValueError: Очередь пуста - извлекать нечего. Невозможно добавить задачу
        """
        if self.is_empty():
            raise ValueError('Очередь пуста - извлекать нечего. Невозможно добавить задачу')
        else:
            self.add_task(task)
            self.get_next_task()

    def if_queue_is_full(self) -> bool:
        """
        Проверка, заполнена ли очередь. Предполагается, что максимальная длина = 10
        :return: bool: True, если заполнена, False - иначе
        """
        return len(self.task_list) == 10


if __name__ == '__main__':
    import doctest
    doctest.testmod()


queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)


"""
Примеры для мною добавленных методов
"""
# task_list = [Task("Задача 1"), Task("Задача 2"), Task("Задача 3"),
#              Task("Задача 4"), Task("Задача 5"), Task("Задача 6"),
#              Task("Задача 7"), Task("Задача 8"), Task("Задача 9"),
#              Task("Задача 10"), Task("Задача 11"), Task("Задача 12")]

# for task in task_list:
#     if queue.if_queue_is_full():
#         queue.get_add_task(task)
#     else:
#         queue.add_task(task)
#
# print(queue.task_list)


next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")


# Ожидаемый результат: "Задача 1"

queue.get_next_task()
queue.get_next_task()

# Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")

# Ожидаемый результат: False

