def binarySearch(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


# изначально мы запускаем двоичный поиск на всей длине массива
arr = [
    1,
    2,
    3,
    4,
    5,
    8,
    14,
    27,
    66,
    75,
    76,
    78,
    85,
    90,
    92,
    95,
    100,
    120,
    153,
    147,
]
x = 27
index = binarySearch(arr, x, left=0, right=len(arr))
print(index)
