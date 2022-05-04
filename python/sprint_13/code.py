""" 
    Формат ввода
Функция принимает массив натуральных чисел и искомое число k

В примерах:
В первой строке записано число n –— длина массива.
Во второй строке записано положительное число k –— искомый элемент. 
Далее в строку через пробел записано n натуральных чисел – элементы массива.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве 
(нумерация с нуля). Если элемент не найден, функция должна вернуть -1
.
Изменять массив нельзя.
"""

ASD = []


def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        ASD.append(mid)
        return
    elif x != arr[mid]:
        binarySearch(arr, x, left, mid)
        binarySearch(arr, x, mid + 1, right)


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums)
    binarySearch(nums, target, left, right)
    return ASD[0] if len(ASD) != 0 else -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


nums = [19, 21, 100, 101, 1, 4, 5, 7, 12, 57, 36, 20, 47, 21]
target = 5
print(broken_search(nums, target))
