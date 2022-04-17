class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_n = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_fully(self):
        return self.size >= self.max_n

    def push_back(self, value):
        if self.is_fully():
            print("error")
            return
        if self.queue[self.tail]:
            self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail] = value
        self.size += 1
        print("Текущий ДЕК ---", self.queue)  # DELETE
        print("Текущий хвост ---", self.tail)  # DELETE
        print("Обновленная голова --- ", self.head)  # DELETE


    def push_front(self, value):
        if self.is_fully():
            print("error")
            return
        if self.queue[self.head]:
            self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = value
        self.size += 1
        print("Текущий ДЕК ---", self.queue)  # DELETE
        print("Текущий хвост ---", self.tail)  # DELETE
        print("Обновленная голова --- ", self.head)  # DELETE

    def pop_back(self):
        if self.is_empty():
            print("error")
            return
        element = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.tail != self.head:
            self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        print(element)
        print("Текущий ДЕК ---", self.queue)  # DELETE
        print("Текущий хвост ---", self.tail)  # DELETE
        print("Обновленная голова --- ", self.head)  # DELETE
        return

    def pop_front(self):
        if self.is_empty():
            print("error")
            return
        element = self.queue[self.head]
        self.queue[self.head] = None
        if self.head != self.tail:
            self.head = (self.head + 1) % self.max_n
        self.size -= 1
        print(element)
        print("Текущий ДЕК ---", self.queue)  # DELETE
        print("Текущий хвост ---", self.tail)  # DELETE
        print("Обновленная голова --- ", self.head)  # DELETE
        return


def read_input():
    n = int(input())  # Количество комманд
    m = int(input())  # максимально допустимый размер очереди

    deque = Deque(m)
    for _ in range(n):
        commands = list(input().strip().split(" "))
        com = commands[0]
        f = getattr(deque, com)
        if len(commands) > 1:
            val = commands[1]
            f(val)
        else:
            f()


def main():
    read_input()


if __name__ == "__main__":
    main()






#def read_input() -> Tuple[int, int, List[str]]:
#   commands_number = int(input())
#   deque_size = int(input())
#   commands_list = list(input().strip().split())
#   return commands_number, deque_size, commands_list
#
#
#f __name__ == '__main__':
#   commands_number = int(input())
#   deque_size = int(input())
#   deque = Deque(deque_size)
#   result = []
#   while commands_number > 0:
#       command, *value = input().strip().split()
#       commands_number -= 1
#       try:
#           if command == 'push_back':
#               deque.push_back(int(*value))
#           elif command == 'push_front':
#               deque.push_front(int(*value))
#           elif command == 'pop_back':
#               result.append(deque.pop_back())
#           elif command == 'pop_front':
#               result.append(deque.pop_front())
#       except Exception:
#           result.append('error')
#   for element in result:
#       print(element)
#
