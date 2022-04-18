# 67524648
class Deque:
    def __init__(self, m):
        self.deque = [None] * m
        self.maximum = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.maximum

    def push_back(self, value):
        """
        Функция добавления числа в конец дека
        """
        if self.is_full():
            raise OverflowError

        if self.deque[self.tail]:
            self.tail = (self.tail + 1) % self.maximum
        self.deque[self.tail] = value
        self.size += 1

    def push_front(self, value):
        """
        Функция добавления числа в начало дека
        """
        if self.is_full():
            raise OverflowError

        if self.deque[self.head]:
            self.head = (self.head - 1) % self.maximum
        self.deque[self.head] = value
        self.size += 1

    def pop_back(self):
        """
        Функция удаления числа из конца дека
        """
        if self.is_empty():
            raise Exception
        last_element = self.deque[self.tail]
        self.deque[self.tail] = None
        if self.tail != self.head:
            self.tail = (self.tail - 1) % self.maximum
        self.size -= 1
        print(last_element)
        return

    def pop_front(self):
        """
        Функция удаления числа из начала дека
        """
        if self.is_empty():
            raise Exception
        first_element = self.deque[self.head]
        self.deque[self.head] = None
        if self.head != self.tail:
            self.head = (self.head + 1) % self.maximum
        self.size -= 1
        print(first_element)
        return


def read_input():
    n = int(input())  # Количество комманд
    m = int(input())  # максимально допустимый размер очереди
    deque = Deque(m)
    for _ in range(n):
        commands = list(input().strip().split(" "))
        com = commands[0]
        function = getattr(deque, com)
        if len(commands) > 1:
            val = commands[1]
            try:
                function(val)
            except OverflowError:
                print("error")
        else:
            try:
                function()
            except Exception:
                print("error")


def main():
    read_input()


if __name__ == "__main__":
    main()
