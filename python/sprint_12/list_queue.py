# Любимый вариант очереди Тимофея — очередь, написанная с использованием
#  связного списка. Помогите ему с реализацией. Очередь должна поддерживать
#  выполнение трёх команд:
#
# get() — вывести элемент, находящийся в голове очереди, и удалить его.
# Если очередь пуста, то вывести «error».

# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

# Формат ввода
# В первой строке записано количество команд n — целое число,
# не превосходящее 1000.
# В каждой из следующих n строк записаны команды по одной строке.


class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.head = None # Голова        
        self.current_node = None # Хвост
        self.current_size = 0

    def get(self):
        if self.current_size == 0:
            print("error")
            return
        next_value = self.head.next
        print(self.head.val)
        self.head.next = None
        self.head = next_value        
        self.current_size -= 1
        return

    def put(self, x):
        if self.current_size == 0:
            node = Node(x, None, None)
            self.head = node
            self.current_node = node
            self.current_size += 1            
        else:
            node = Node(x, None, self.current_node)
            self.current_node.next = node
            self.current_node = node
            self.current_size += 1
        return

    def size(self):
        print(self.current_size)
        return


def read_input():
    n = int(input())
    stack = Node()
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
