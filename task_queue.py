from typing import Any


class TaskQueue:

    def __init__(self):
        self.task_list: list[Any] = []

    def add_task(self, task: Any) -> None:
        self.task_list.append(task)

    def is_empty(self) -> bool:
        return not bool(self.task_list)

    def get_next_task(self) -> Any:
        if not self.is_empty():
            return self.task_list.pop(0)
        else:
            return None


class Task:

    def __init__(self, name: str):
        self.name = name


queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)


next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")


# Ожидаемый результат: "Задача 1"

queue.get_next_task()
queue.get_next_task()

# Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")

# Ожидаемый результат: False




