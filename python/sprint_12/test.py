K = -2156489674
class StackMax:
    def __init__(self):
        self.items = []
        self.indexes = []
        self.mxm = K
        self.index = 0

    def push(self, x):
        x = int(x)
        if len(self.items) == 0:
            self.index = 0
        if x >= self.mxm:
            self.indexes.append(self.index)            
            self.mxm = x
            
        self.items.append(x)
        self.index += 1        

    def pop(self):
        if len(self.items) == 0:            
            print("error")
            return
        if self.items[-1] == self.items[self.indexes[-1]]:
            del self.indexes[-1]            
        del self.items[-1]
        if len(self.items) > 0:
            self.mxm = self.items[self.indexes[-1]]
            self.index -= 1
        if len(self.items) == 0:
            self.mxm = K
            self.index = 0 
        return

    def get_max(self):
        if len(self.items) == 0:
            print("None")
            return
        max_index = self.indexes[-1]
        max_val = self.items[max_index]        
        print(max_val)        
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

# push 1
# push 3
# push 1
# push 3
# push 3
# pop
# get_max
# pop
# get_max
# pop
# get_max
# pop
# get_max
# Вывод:
# 3
# 3
# 3
# 1

input_list = [
    'get_max',
    'push -6',
    'pop',
    'pop',
    'get_max',
    'push 2',
    'get_max',
    'pop',
    'push -2',
    'push -6'
]

def read_input2():
    stack = StackMax()
    for c in input_list:
        commands = list(c.strip().split(" "))
        com = commands[0]
        f = getattr(stack, com)
        if len(commands) > 1:
            val = commands[1]
            f(val)
        else:
            f()
