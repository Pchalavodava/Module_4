class BracketSequence:
    def __init__(self):
        self.sequence: list[str] = []
        self.left_bracket: tuple[str, str, str] = ('(', '{', '[')
        self.right_bracket: tuple[str, str, str] = (')', '}', ']')

    def is_empty(self) -> bool:
        """
        Проверка является ли список пустым
        :return: bool: True, если список пустой, иначе - False
        """
        return len(self.sequence) == 0

    def push(self, bracket: str) -> None:
        """
        Добавление элемента в список
        :param bracket: добавляемый элемент
        :return: None
        """
        self.sequence.append(bracket)

    def pop(self) -> str:
        """
        Удаление последнего элемента в списке
        :return: str: последний элемент
        """
        if not self.is_empty():
            return self.sequence.pop()
        else:
            raise IndexError('Список пуст')

    def peek(self) -> str:
        """
        Выводит последний элемент в списке
        :return: str: последний элемент
        """
        if not self.is_empty():
            return self.sequence[-1]
        else:
            raise IndexError('Список пуст')

    def size(self) -> int:
        """
        Рассчитывает количество элементов в списке
        :return: int: длина списка
        """
        return len(self.sequence)

    def input_validation(self, symbol: str) -> None:
        """
        Проверка символа на вхождение в кортежи
        :param symbol: str: проверяемая скобка
        :return: bool: True, если символ корректен, иначе исключение IndexError
        """
        if symbol not in self.left_bracket and symbol not in self.right_bracket:
            raise IndexError('Некорректный ввод')

    def checking_correct_bracket(self, bracket: str) -> None:
        """
        Добавляет и удаляет символы из списка
        :param bracket: str: проверяемый символ
        :return: None
        """
        self.input_validation(bracket)
        if bracket in self.left_bracket:
            self.push(bracket)
        else:
            if self.left_bracket.index(self.peek()) == self.right_bracket.index(bracket):
                self.pop()
            # else:
            #     raise IndexError('Неверная скобочная последовательность')

    def output_result(self, input_string: str) -> str:
        """
        Вывод результата. Проверка заполненности списка. Если список пуст, то скобочная последовательность верная
        :param input_string: str: строка скобок, вводимая пользователем
        :return: str: строковый результат проверки
        """
        if self.is_empty():
            x = ''
        else:
            x = 'не'
        return f'{input_string} - {x}верная скобочная последовательность'


bracket_sequence = BracketSequence()
my_bracket_sequence = input('Введите строку >>> ')
for specific_symbol in my_bracket_sequence:
    bracket_sequence.checking_correct_bracket(specific_symbol)

print(bracket_sequence.output_result(my_bracket_sequence))