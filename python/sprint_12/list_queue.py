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
        head = None
        tail = None
        current_node = None
        size = 0

    def get(self):
        if self.size == 0:
            print("error")
            return
        next_value = self.head.next
        print(self.head.val)
        self.head.next = None
        self.head = next_value
        self.head.prev = None
        self.size -= 1
        return

    def put(self, x):
        if self.size == 0:
            node = Node(x, None, None)
            self.head.next = x
            self.head = node
            self.current_node = node
            self.size += 1
        else:
            node = Node(x, None, self.current_node)
            self.current_node.next = node
            self.current_node = node
            self.size += 1
        return
