class StackMax:
    def __init__(self):
        self.items = []
        self.indexes = []
        self.mxm = -2156489674
        self.index = 0

    def push(self, x):
        x = int(x)
        self.items.append(x)
        if x > self.mxm:
            self.indexes.append(self.index)
            print("MAX INDEXES ", self.indexes)  # DELETE
            self.mxm = x
        self.index += 1
        print("SELF INDEX ", self.index)  # DELETE
        print("SELF ITEMS ", self.items)  # DELETE

    def pop(self):
        if len(self.items) == 0:
            print("error")
            return
        if self.items[-1] == self.items[self.indexes[-1]]:
            del self.indexes[-1]

        del self.items[-1]
        print("SELF ITEMS ", self.items)  # DELETE
        return

    def get_max(self):
        if len(self.items) == 0:
            print("None")
            return
        max_index = self.indexes[-1]
        max_val = self.items[max_index]
        print("MAX VALUE ", max_val)  # DELETE
        print("MAX INDEX ", max_index)  # DELETE
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
# push -4
# push 10
# push -8
# push -6
# push -10
# push 0
# pop
# push 7
# get_max
# push 3
# push -10
# get_max
