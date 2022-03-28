from typing import List, Optional, Tuple


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return f' Ответ: {arr[i]}, {arr[j]}'
    return f' Ответ не найден: {None}, {None}'


def read_input() -> Tuple[List[int], int]:
    n = int(input("Введите количество фишек "))
    arr = list(map(int, input("Введите количество очков на каждой из фишек ").strip().split()))
    target_sum = int(input("Введите загаданное число "))
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
