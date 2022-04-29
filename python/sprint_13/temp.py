def merge_sort(array):
    
    if len(array) == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    first_half = array[: len(array) // 2]
    left = merge_sort(first_half)

    # запускаем сортировку рекурсивно на правой половине
    second_half = array[len(array) // 2 : len(array)]
    right = merge_sort(second_half)
    # заводим массив для результата сортировки
    result = [None] * len(array)
    # сливаем результаты
    l, r, k = 0, 0, 0
    a = max(array[l])
    b = min(array[r])
    if a == b:
        result[k] = a
    elif a > b:
        result[k] == 0
    l += 1
    r += 1
    k += 1    
    return result


arr = [[7, 8], [7, 8], [2, 3], [6, 10]]
arr = sorted(arr)
print(merge_sort(arr))



def find(arr):
    pass

#print(merge_sort(arr))
first_half = arr[: len(arr) // 2]
# запускаем сортировку рекурсивно на правой половине
# second_half = arr[len(arr) // 2 : len(arr)]
# print(first_half, second_half)
