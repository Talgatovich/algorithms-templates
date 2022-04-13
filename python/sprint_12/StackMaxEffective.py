class StackMax:
    def __init__(self):
        self.items = {}
        self.deleted = set()
        self.index = 0

    def push(self, x):
        x = int(x)
        self.items[self.index] = x
        print(self.items)
        self.index += 1

    def pop(self):
        if len(self.items) == 0:
            print("error")
            return
        last_index = sorted(self.items.keys())[-1]
        self.deleted.add(self.items[last_index])
        del self.items[last_index]
        print(self.items)
        return

    def get_max(self):
        if len(self.items) == 0:
            print("None")
            return
        print(max(self.items.values()))
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

# stack = StackMax()
# stack.push("apple")
# stack.push("banana")
# stack.push("orange")
# stack.pop()
# stack.get_max()
# get_max
# push 7
# pop
7
# get_max
# push -5
# push -7
# get_max
# get_max
# get_max
