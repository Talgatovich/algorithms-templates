# Считаем, сколько раз встречается то или иное число в массиве.
# Зная эти количества, быстро формируем уже упорядоченный массив.
# Для этой сортировки нужно знать минимум и максимум в массиве.
# Тогда генерируются ключи для вспомогательного массива, в котором
# и фиксируем чего и сколько раз встретилось.
def count_sort(a):
    """Сортировка подсчетом"""
    A = [0] * 13
    for val in a:
        A[val] += 1
    print(A)
    a_sorted = []
    for i in range(len(A)):
        for j in range(A[i]):
            a_sorted.append(i)
    return a_sorted


def test_sort_function(func):
    print("Тестирование функции ", func.__doc__)
    A = [1, 4, 6, 4, 7, 12, 8, 2, 4]
    A_sorted = [1, 2, 4, 4, 4, 6, 7, 8, 12]
    A = count_sort(A)
    print("OK" if A == A_sorted else "False")


if __name__ == "__main__":
    test_sort_function(count_sort)
