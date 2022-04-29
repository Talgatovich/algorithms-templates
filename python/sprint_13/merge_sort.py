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
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


arr = [7, 8, 7, 8, 2, 3, 6, 10]
   
print(merge_sort(arr))
first_half = arr[: len(arr) // 2]
# запускаем сортировку рекурсивно на правой половине
# second_half = arr[len(arr) // 2 : len(arr)]
# print(first_half, second_half)
