class Stack:
    def __init__(self):
        self.items = []
        self.symbols = ['+', '-', '*', '//']

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def calculate(self, commands):
        asd = commands.split(' ')
        for sign in asd:
            if sign in self.symbols:
                last_digit = self.items[-1]
                penultimate_number = self.items[-2]
                if sign == self.symbols[0]:
                    res = last_digit + penultimate_number
                if sign == self.symbols[1]:
                    res = last_digit - penultimate_number
                if sign == self.symbols[2]:
                    res = last_digit * penultimate_number
                if sign == self.symbols[3]:
                    res = last_digit // penultimate_number
                self.push(int(res))
            else:    
                self.push(int(sign))
        return self.items




def read_input():
    commands = int(input())
    a = Stack()    
    print(a.calculate(commands))
    return 


def main():
    read_input()

if __name__ == "__main__":
    main()

