from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    variable = "".join(map(str, number_list))
    variable = str(int(variable) + k)
    result = list(variable)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(input().strip().split())
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(get_sum(number_list, k)))


"""
На вход подается количество цифр числа Х, списочная форма неотрицательного числа Х 
и неотрицательное число K. Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.
"""
