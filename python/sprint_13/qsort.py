# 68124998
def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right - 1
    while True:
        if i <= j and arr[j] > pivot:
            j -= 1
        elif i <= j and arr[i] < pivot:
            i += 1
        elif (arr[j] > pivot) or (arr[i] < pivot):
            continue
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[left], arr[j] = (
                arr[j],
                arr[left],
            )
            return j


def quick_sort(arr, left, right):
    if (right - left) > 1:
        m = partition(arr, left, right)
        quick_sort(arr, left, m)
        quick_sort(arr, m + 1, right)


def transform(arr):
    arr[1] = -int(arr[1])
    arr[2] = int(arr[2])

    return [arr[1], arr[2], arr[0]]


def read_input():
    n = int(input())
    arr = [transform(input().split()) for _ in range(n)]
    return n, arr


def main():
    n, arr = read_input()
    left = 0
    quick_sort(arr, left, len(arr))
    print(*(list(zip(*arr))[2]), sep="\n")


if __name__ == "__main__":
    main()


