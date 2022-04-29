"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое 
из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.
"""


def bubble_sort(n, nums):
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            digit_1 = nums[j] + nums[j + 1]
            digit_2 = nums[j + 1] + nums[j]
            if digit_1 < digit_2:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return "".join(nums)


def read_input():
    n = int(input())
    digits = input().strip().split()
    return n, digits


def main():
    n, nums = read_input()
    print(bubble_sort(n, nums))


if __name__ == "__main__":
    main()
