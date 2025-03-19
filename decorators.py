import requests
from datetime import datetime


"""
Задача 1. Измерьте с помощью декоратора measure_execution_time продолжительность HTTP запроса
к произвольному url (можно взять код из первых уроков по ботам)

"""


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f'Function completed in {execution_time.seconds}s {milliseconds}ms')
        return result
    return wrapper


@measure_execution_time
def get_response() -> str:
    """
    Функция обращения к веб-странице
    :return: str: Если код состояния 200, тогда сообщение об успешном выполнении,
    иначе - сообщение об ошибке с кодом состояния
    """
    response = requests.get('https://ivashev-education.ru/teach/control')
    if response.status_code == 200:
        return 'Запрос выполнен успешно'
    else:
        return f'Произошла ошибка: {response.status_code}'


print(get_response())

"""
Задача 2. Описание задачи:

Необходимо разработать декоратор requires_admin, который будет использоваться для 
проверки роли пользователя перед выполнением защищенной функции. Если роль пользователя 
не соответствует требуемой, декоратор должен выбрасывать исключение PermissionError. 
В противном случае функция должна выполняться корректно.

Пример использования:

Функция delete_user отвечает за удаление пользователей. Она должна быть доступна 
только для пользователей с ролью "admin".  Если пользователь, вызывающий эту функцию, 
не является администратором, необходимо остановить выполнение функции и выбросить PermissionError.


@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."

# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
print(delete_user(admin_user, 'Charlie'))  # Должно отработать
print(delete_user(regular_user, 'Charlie'))  # Должно рейзить PermissionError"""


def requires_admin(func):
    def wrapper(*args, **kwargs):
        if args[0]['role'] == 'admin':
            user = func(*args, **kwargs)
        else:
            raise PermissionError(f'У вас нет прав для удаления пользователя {args[1]}')

        return user
    return wrapper


@requires_admin
def delete_user(user: dict[str, str], username_to_delete: str) -> str:
    """
    Функция удаления (сообщение об удалении) пользователя пользователем
    :param user: dict[str, str]: Словарь - пользователь с ключами 'username' и 'role'
    :param username_to_delete: str: Имя пользователя для удаления
    :return: str: Сообщение об удалении пользователя пользователем с заданной ролью
    """
    return f"User {username_to_delete} has been deleted by {user['username']}"


admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}
print(delete_user(admin_user, 'Michael'))

