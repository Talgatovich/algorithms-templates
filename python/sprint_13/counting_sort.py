def count_sort(arr, k):
    new_arr = [0] * (k + 1)
    for val in arr:
        new_arr[val] += 1
    s = ""
    for i in range(0, k + 1):
        if new_arr[i] > 0:
            s += (str(i) + " ") * new_arr[i]
    return s


def read_input():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


def main():
    n, arr = read_input()
    print(count_sort(arr, n))


# if __name__ == "__main__":
#    main()

arr = [0, 2, 1, 2, 0, 0, 1]
n = 7
print(count_sort(arr, n))
arr = [2, 1]
n = 2
print(count_sort(arr, n))
# print(read_input())
