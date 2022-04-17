class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = -n
        self.tail = 0
        self.current_size = 0
        self.current_head = (self.head - 1) % self.max_n
        self.current_tail = (self.tail - 1)  % self.max_n

    def is_empty(self):
        """
        Возвращает True, если массив пуст
        """
        print("Текущий ДЕК -- ", self.queue)  # DELETE
        return self.current_size == 0

    def push_front(self, x):
        """
        Функция добавления числа в начало очереди
        """
        if self.current_size >= self.max_n:
            print("error")
            return
        if self.current_size != self.max_n:
            self.queue[self.head] = x
            self.head = (self.head - 1) % self.max_n
            self.current_size += 1
            print("Текущий ДЕК -- ", self.queue)  # DELETE
            print("Голова -- ", self.head)  # DELETE
            print("Текущая голова -- ", self.current_head)  # DELETE
            print("Хвост -- ", self.tail)  # DELETE
            print("Текущий хвост -- ", self.current_tail)  # DELETE
        return


    def push_back(self, x):
        """
        Функция добавления числа в конец очереди
        """
        if self.current_size >= self.max_n:
            print("error")
            return
        if self.current_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.current_size += 1
            print("Текущий ДЕК -- ", self.queue)  # DELETE
            print("Голова -- ", self.head)  # DELETE
            print("Текущая голова -- ", self.current_head)  # DELETE
            print("Хвост -- ", self.tail)  # DELETE
            print("Текущий хвост -- ", self.current_tail)  # DELETE
        return

    def pop_front(self):
        """
        Функция удаления элемента из начала очереди
        """
        if self.is_empty():
            print("None")
            return
        first_element = self.queue[self.current_head]
        self.queue[self.current_head] = None
        self.head = (self.head - 1) % self.max_n
        self.current_size -= 1
        print(first_element)
        print("Текущий ДЕК -- ", self.queue)  # DELETE
        print("Голова -- ", self.head)  # DELETE
        print("Текущая голова -- ", self.current_head)  # DELETE
        print("Хвост -- ", self.tail)  # DELETE
        print("Текущий хвост -- ", self.current_tail)  # DELETE
        return

    def pop_back(self):
        """
        Функция удаления элемента из конца очереди
        """
        if self.is_empty():
            print("None")
            return
        last_element = self.queue[self.current_tail]
        self.queue[self.current_tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.current_size -= 1
        print(last_element)
        print("Текущий ДЕК -- ", self.queue)  # DELETE
        print("Голова -- ", self.head)  # DELETE
        print("Текущая голова -- ", self.current_head)  # DELETE
        print("Хвост -- ", self.tail)  # DELETE
        print("Текущий хвост -- ", self.current_tail)  # DELETE
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

"""
4
4
push_front 861
push_front -819
pop_back
pop_back

ВЫвод
861
-819
"""
