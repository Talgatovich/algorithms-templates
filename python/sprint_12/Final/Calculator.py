# 67535071
math_operations = {
    "+": lambda x, y: y + x,
    "-": lambda x, y: y - x,
    "*": lambda x, y: y * x,
    "/": lambda x, y: y // x,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Функция добавления числа в стек
        """
        self.items.append(item)

    def pop(self):
        """
        Функция удаления элемента из вершины стека
        """
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Стек пуст. Введите как минимум 2 числа")

    def calculate(self, commands):
        """
        Функция вычисления значения выражения, записанного в
        обратной польской нотации
        """
        for sign in commands:
            if sign in math_operations.keys():
                last_digit = self.pop()
                penultimate_digit = self.pop()
                res = math_operations[sign](last_digit, penultimate_digit)
                self.push(int(res))
            else:
                self.push(int(sign))

        return self.items.pop()


def read_input():
    object = Stack()
    commands = input().strip().split(" ")
    print(object.calculate(commands))


def main():
    read_input()


if __name__ == "__main__":
    main()
