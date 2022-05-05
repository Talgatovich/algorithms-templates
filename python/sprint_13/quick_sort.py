def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [num for num in arr if num < pivot]
    center = [num for num in arr if num == pivot]
    right = [num for num in arr if num > pivot]

    return quick_sort(left) + center + quick_sort(right)


arr = [8, 9, 5, 12, 14, 0, 3]
print(quick_sort(arr))
