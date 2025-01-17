# В первой строке записано количество команд n — целое число,
# не превосходящее 100000. Во второй строке записано число m — максимальный
# размер дека. Он не превосходит 50000.
# В следующих n строках записана одна из команд:
#
# push_back(value) – добавить элемент в конец дека.
# Если в деке уже находится максимальное число элементов, вывести «error».

# push_front(value) – добавить элемент в начало дека.
# Если в деке уже находится максимальное число элементов, вывести «error».

# pop_front() – вывести первый элемент дека и удалить его.
#  Если дек был пуст, то вывести «error».

# pop_back() – вывести последний элемент дека и удалить его.
#  Если дек был пуст, то вывести «error».

# Value — целое число, по модулю не превосходящее 1000.
# Формат вывода
# Выведите результат выполнения каждой команды на отдельной строке.
# Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.


class Deque:
    def __init__(self, m):
        self.deq = [None] * m
        self.maximum = m

        self.front_head = 0
        self.front_tail = 0

        self.back_head = m - 1
        self.back_tail = m - 1

        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size >= self.maximum

    def push_back(self, value):
        if self.is_full():
            print("error")
            return
        if self.current_size != self.maximum:
            self.deq[self.back_tail] = value
            self.current_size += 1
            self.back_tail = (self.back_tail - 1) % self.maximum
            print("Текущий ДЕК --добавление в конец--", self.deq)  # DELETE
        return

    def push_front(self, value):
        if self.is_full():
            print("error")
            return
        if self.current_size != self.maximum:
            self.deq[self.front_tail] = value
            self.current_size += 1
            self.front_tail = (self.front_tail + 1) % self.maximum
            print("Текущий ДЕК --добавление в начало--", self.deq)  # DELETE
        return

    def pop_front(self):
        if self.is_empty():
            print("error")
            return
        first_elem = self.deq[self.front_head]
        self.deq[self.front_head] = None
        self.front_head = (self.front_head + 1) % self.maximum
        self.current_size -= 1
        print(first_elem)
        print("Текущий ДЕК --удаление из начала--", self.deq)  # DELETE
        return

    def pop_back(self):
        if self.is_empty():
            print("error")
            return
        last_elem = self.deq[self.back_head]
        self.deq[self.back_head] = None
        self.back_head = (self.back_head - 1) % self.maximum
        self.current_size -= 1
        print(last_elem)
        print("Текущий ДЕК --удаление с конца--", self.deq)  # DELETE
        return


def read_input():
    n = int(input())  # Количество комманд
    m = int(input())  # максимально допустимый размер очереди

    queue = Deque(m)
    for _ in range(n):
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
