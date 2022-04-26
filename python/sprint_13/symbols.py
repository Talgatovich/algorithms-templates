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
def get_symbols(n, numbers):    
    my_dict = {2:'abc',  3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    if n == 0:
        print()
    else:
        get_symbols(n - 1, my_dict[numbers[n]])
        get_symbols(n - 1, my_dict[numbers[n]])
        


get_symbols(3, '234')
