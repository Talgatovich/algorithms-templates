# В первой строке записано одно число — количество команд,
# оно не превосходит 5000.
# Во второй строке задан максимально допустимый размер очереди,
# он не превосходит 5000.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:
#
# push(x) — добавить число x в очередь;
# pop() — удалить число из очереди и вывести на печать;
# peek() — напечатать первое число в очереди;
# size() — вернуть размер очереди;
# При превышении допустимого размера очереди нужно вывести «error».
# При вызове операций pop() или peek() для пустой очереди нужно вывести «None».


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def is_empty(self):
        """
        Возвращает True, если массив пуст
        """
        return self.current_size == 0

    def push(self, x):
        """
        Функция добавления числа в конец очереди
        """
        if self.current_size > self.max_n - 1:
            print("error")
            return
        if self.current_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.current_size += 1
        return

    def pop(self):
        """
        Функция удаления элемента из начала очереди
        """
        if self.is_empty():
            print("None")
            return
        h = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.current_size -= 1
        print(h)
        return

    def peek(self):
        """
        Выводит первое число в очереди, если очередь не пуста
        """
        if self.is_empty():
            print("None")
            return
        print(self.queue[self.head])
        return

    def size(self):
        """
        Возвращает размер очереди
        """
        print(self.current_size)
        return


def read_input():
    c = int(input())  # Количество комманд
    n = int(input())  # максимально допустимый размер очереди

    queue = Queue(n)
    for _ in range(c):
        commands = list(input().strip().split(" "))
        com = commands[0]
        f = getattr(queue, com)
        if len(commands) > 1:
            val = commands[1]
            f(val)
        else:
            f()


def main():
    read_input()


if __name__ == "__main__":
    main()


# 8
# 2
# peek
# push 5
# push 2
# peek
# size
# size
# push 1
# size

# Вывод None, 5, 2, 2, error, 2
