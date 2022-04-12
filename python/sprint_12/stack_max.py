class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        return max(self.items)

def read_input():
    n = int(input())
    for _ in range(n):
        command = input()
        res = command
    
        print(command)
read_input()
