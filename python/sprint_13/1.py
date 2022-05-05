import random


def partition(array, start, end, idx_pivot):

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start][1]
    left = start + 1
    right = start + 1

    while right <= end:
        if array[right][1] <= pivot:
            array[right], array[left] = array[left], array[right]
            left += 1
        right += 1

    array[start], array[left - 1] = array[left - 1], array[start]
    return left - 1


def quick_sort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    left = partition(array, start, end, idx_pivot)
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)
    return array


def transform(lst):
    lst[1] = int(lst[1])
    lst[2] = int(lst[2]) * -1
    lst[0], lst[2] = lst[2], lst[0]

    return lst


def read_input():
    n = int(input())
    res = []
    for _ in range(n):
        sublist = transform(list(input().strip().split(" ")))

        res.append(sublist)
    return n, res


def main():
    n, arr = read_input()
    result = quick_sort(arr)
    for name in result[::-1]:
        print(name[2])


# if __name__ == "__main__":
#    main()

# print(read_input())


arr = [
    [-200, 10, "tim"],
    [-200, 10, "tom"],
    [-30, 20, "art"],
    [-80, 2, "abzar"],
]
arr2 = [["art", 20, -100], ["tom", 20, -100], ["dash", 50, -30]]
result = quick_sort(arr)
for name in result[::-1]:
    print(name[2])
print(quick_sort(arr)[::-1])

# ================================================
arr = [
    [-200, 10, "tim"],
    [-200, 10, "tom"],
    [-30, 20, "art"],
    [-80, 2, "abzar"],
]
arr2 = [["art", 20, -100], ["tom", 20, -100], ["dash", 50, -30]]
# quick_sort(arr2, 0, 3)
# print(*(list(zip(*arr2))[2]), sep="\n")
