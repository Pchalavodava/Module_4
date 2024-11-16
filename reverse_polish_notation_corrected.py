from typing import Any


class ReversePolishNotation:
    def __init__(self):
        self.number_list: list[int] = []
        self.operand_list: list[str] = []

    def put(self, token: Any) -> None:
        if token.isnumeric():
            self.number_list.append(int(token))
        else:
            self.operand_list.append(token)

    def is_empty(self) -> bool:
        return len(self.number_list) == 0

    def pop(self) -> int:
        if not self.is_empty():
            return self.number_list.pop()
        else:
            raise IndexError('Список пуст')

    def peek(self) -> int:
        if not self.is_empty():
            return self.number_list[-1]
        else:
            raise IndexError('Список пуст')

    def filling_with_numbers(self, input_formula: str) -> None:
        formula_list = input_formula.split(' ')
        for element in formula_list:
            self.put(element)

    def checking_formula_correctness(self) -> bool:
        return len(self.number_list) - len(self.operand_list) == 1

    def math_operations(self, operator: str, a: int, b: int) -> int | float:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b

    def calculation(self, input_formula: str) -> None:
        self.filling_with_numbers(input_formula)
        if self.checking_formula_correctness():
            for el in self.operand_list:
                res = self.math_operations(el, self.pop(), self.peek())
                self.number_list[-1] = res
        else:
            raise IndexError('Неверная формула')


reverse_polish_notation = ReversePolishNotation()
reverse_polish_notation.calculation('3 4 2 * +')
print(reverse_polish_notation.number_list)


