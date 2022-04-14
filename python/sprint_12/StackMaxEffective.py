# Реализуйте класс StackMaxEffective, поддерживающий операцию определения
# максимума среди элементов в стеке. Сложность операции должна быть O(1).
# Для пустого стека операция должна возвращать None. При этом push(x) и pop()
# также должны выполняться за константное время.
#
# Формат ввода
# В первой строке записано одно число — количество команд, оно не превосходит
# 100000. Далее идут команды по одной в строке.

# Команды могут быть следующих видов:#
# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;
# Если стек пуст, при вызове команды get_max нужно напечатать «None»,
# для команды pop — «error».

K = -2156489674


class StackMax:
    def __init__(self):
        self.items = []  # Значения
        self.indexes = []  # Индексы максимальных значений
        self.mxm = K  # Максимум по умолчанию
        self.index = 0  # Индекс добавляемого значения

    def push(self, x):
        """
        Функция добавления цисла в стек
        """

        x = int(x)
        if len(self.items) == 0:
            self.index = 0
        if x >= self.mxm:
            self.indexes.append(self.index)
            self.mxm = x

        self.items.append(x)
        self.index += 1

    def pop(self):
        """
        Функция удаления элемента из вершины стека
        """

        if len(self.items) == 0:
            print("error")
            return
        if self.items[-1] == self.items[self.indexes[-1]]:
            del self.indexes[-1]
        del self.items[-1]
        if len(self.items) > 0:
            self.mxm = self.items[self.indexes[-1]]
            self.index -= 1
        if len(self.items) == 0:
            self.mxm = K
            self.index = 0
        return

    def get_max(self):
        """
        Функция вывода максимального числа в стеке
        """
        if len(self.items) == 0:
            print("None")
            return
        max_index = self.indexes[-1]
        max_val = self.items[max_index]
        print(max_val)
        return


def read_input():
    n = int(input())
    stack = StackMax()
    for _ in range(n):
        commands = list(input().strip().split(" "))
        com = commands[0]
        f = getattr(stack, com)
        if len(commands) > 1:
            val = commands[1]
            f(val)
        else:
            f()


def main():
    read_input()


if __name__ == "__main__":
    main()

# push 1
# push 3
# push 1
# push 3
# push 3
# pop
# get_max
# pop
# get_max
# pop
# get_max
# pop
# get_max
# Вывод:
# 3
# 3
# 3
# 1

input_list = [
    "get_max",
    "push -6",
    "pop",
    "pop",
    "get_max",
    "push 2",
    "get_max",
    "pop",
    "push -2",
    "push -6",
]


def read_input2():
    """
    Для автоматизации ввода комманд
    """
    stack = StackMax()
    for c in input_list:
        commands = list(c.strip().split(" "))
        com = commands[0]
        f = getattr(stack, com)
        if len(commands) > 1:
            val = commands[1]
            f(val)
        else:
            f()
