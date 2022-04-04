# 66753867
from typing import List, Tuple


def check_null(numbers):
    null_index = []
    while 0 in numbers:
        current_index = numbers.index(0)
        null_index.append(current_index)
        numbers[current_index] = 1
    return null_index


def get_distance(numbers, n):
    result = []
    null_index = None
    for index, val in enumerate(numbers):
        if val == 0:
            null_index = index
            result.append(0)
            continue
        if null_index is not None:
            result.append(index - null_index)
        else:
            result.append(10 ** 6 + index)
    null_index = None
    for index, val in reversed(list(enumerate(numbers))):
        if val == 0:
            null_index = index
            continue
        if null_index is not None and result[index] > (null_index - index):
            result[index] = (null_index - index)
    return result


def read_input() -> Tuple[List[int], int, int]:
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    return numbers, n


if __name__ == '__main__':
    n, numbers = read_input()
    print(" ".join(map(str, get_distance(n, numbers))))
