class ReversePolishNotation:
    def __init__(self):
        self.token_list: list[int] = []

    def put(self, token: int) -> None:
        self.token_list.append(int(token))

    def is_empty(self) -> bool:
        return len(self.token_list) == 0

    def pop(self) -> int:
        if not self.is_empty():
            return self.token_list.pop()
        else:
            raise IndexError('Список пуст')

    def peek(self) -> int:
        if not self.is_empty():
            return self.token_list[-1]
        else:
            raise IndexError('Список пуст')

    def filling_with_numbers(self, input_formula: str | int) -> None:
        for element in input_formula:
            if element.isnumeric():
                self.put(element)

    def checking_formula_correctness(self, formula: str | int) -> bool:
        return len(formula) - len(self.token_list) == len(self.token_list) - 1

    def math_operations(self, operator: str, a: int, b: int) -> int | float:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b

    def calculation(self, input_formula: str | int) -> None:
        self.filling_with_numbers(input_formula)
        if self.checking_formula_correctness(input_formula):
            for el in input_formula:
                if not el.isnumeric():
                    res = self.math_operations(el, self.pop(), self.peek())
                    self.token_list[-1] = res
        else:
            raise IndexError('Неверная формула')


reverse_polish_notation = ReversePolishNotation()
reverse_polish_notation.calculation('222+*')
print(reverse_polish_notation.token_list)


