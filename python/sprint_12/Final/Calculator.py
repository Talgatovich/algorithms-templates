# 67493867
class Stack:
    def __init__(self):
        self.items = []
        self.symbols = ["+", "-", "*", "/"]

    def push(self, item):
        """
        Функция добавления числа в стек
        """
        self.items.append(item)

    def pop(self):
        """
        Функция удаления элемента из вершины стека
        """
        return self.items.pop()

    def calculate(self, commands):
        """
        Функция вычисления значения выражения, записанного в
        обратной польской нотации
        """
        for sign in commands:
            if sign in self.symbols:
                last_digit = self.pop()
                penultimate_number = self.pop()
                if sign == self.symbols[0]:
                    res = penultimate_number + last_digit
                if sign == self.symbols[1]:
                    res = penultimate_number - last_digit
                if sign == self.symbols[2]:
                    res = penultimate_number * last_digit
                if sign == self.symbols[3]:
                    res = penultimate_number // last_digit
                self.push(int(res))
            else:
                self.push(int(sign))

        return self.items[-1]


def read_input():
    object = Stack()
    commands = input().strip().split(" ")
    print(object.calculate(commands))


def main():
    read_input()


if __name__ == "__main__":
    main()
