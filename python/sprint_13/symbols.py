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
    1: ".,;",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def get_symbols(n, control, prefix):
    # print(prefix)
    numbers = [2, 3, 4]
    num = numbers[0]
    add = my_dict[num][n - 3] + my_dict[num][n - 2]
    if n == 0:
        print(prefix[::-1])
    else:
        get_symbols(
            n - 1,
            control + 1,
            prefix + add + " ",
        )


control = 0
get_symbols(3, control, prefix="")

numbers = [2, 3, 4]
n = 4
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

# print(my_dict[numbers[n - 1]][n - 1])
"""def get_symbols(n, control, prefix):
    # print(prefix)
    numbers = [2, 3, 4]
    num = numbers[0]
    add = my_dict[num][n - 2] + my_dict[num][n - 1]
    if n > len(numbers) - 1:
        print(prefix[::-1])
    else:
        get_symbols(
            n + 1,
            control - 1,
            prefix + add + " ","""
