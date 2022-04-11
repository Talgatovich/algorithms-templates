def twosum_extra_ds(numbers, X):
    for i, val in enumerate(numbers):
       print(f'Индекс {i}, значение {val}')
    return f'Х = {X}'


numbers = [2, 4, 6, 10, 12, 15, 16]
X = 25
print(twosum_extra_ds(numbers, X))
