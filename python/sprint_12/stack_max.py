class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            print("error")
            return
        del self.items[-1]
        return

    def get_max(self):
        if len(self.items) == 0:
            print("None")
            return
        print(max(map(int, self.items)))
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
