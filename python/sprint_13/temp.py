""" На клавиатуре старых мобильных телефонов каждой цифре соответствовало 
несколько букв. Примерно так:

2:'abc',  3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона,
без учета повторов. Напечатайте все комбинации букв, 
которые можно набрать такой последовательностью нажатий.

На вход подается строка, состоящая из цифр 2-9 включительно.
Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.
"""
my_dict = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def get_symbols(N, M=0, prefix=None):
    if M > len(N) - 1:
        print("".join(prefix), end="  ")
        return
    prefix = prefix or []
    num = N[M]
    symbols = my_dict[num]

    for symb in symbols:
        prefix.append(symb)
        get_symbols(N, M + 1, prefix)
        prefix.pop()


def read_input():
    N = [*input()]
    for i in range(len(N)):
        N[i] = int(N[i])
    return N


def main():
   N = read_input()
   get_symbols(N)
   

if __name__ == "__main__":
   main()

