"""
    Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными 
накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в 
порядке неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. 
Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.
"""


def find_day(arr, x, left, right):
    if right <= left:
        if arr[left] == x:
            return left + 1
        elif arr[right] > x:
            return right + 1
        else:
            return -1
    mid = (left + right) // 2

    if x < arr[mid] or x == arr[mid]:
        return find_day(arr, x, left, mid)
    elif arr[mid] < x:
        return find_day(arr, x, mid + 1, right)


def read_input():
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    cost = int(input())
    return n, arr, cost


def main():
    n, arr, cost = read_input()
    n = n - 1
    a = str(find_day(arr=arr, x=cost, left=0, right=n)) + " "
    a += str(find_day(arr=arr, x=cost * 2, left=0, right=n))
    print(a)


if __name__ == "__main__":
    main()


def test():
    a = [1, 2, 3, 4, 6, 8]
    b = 3
    n = 6
    print("Верно" if find_day(a, b, 0, n) == 3 else "Не верно")
    print(find_day(a, b, 0, n))
