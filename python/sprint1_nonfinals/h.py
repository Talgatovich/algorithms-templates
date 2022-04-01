from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:

    first_number = first_number[::-1]
    second_number = second_number[::-1]

    size = max(len(first_number), len(second_number))

    first_number += '0' * (size - len(first_number))
    second_number += '0' * (size - len(second_number))

    
    overflow = 0
    res = []
    for obj in zip(first_number, second_number):
        value = int(obj[0]) + int(obj[1]) + overflow
        overflow = value // 2
        res.append(value % 2)

    
    if overflow == 1:
        res.append(1)
    
    res = res[::-1]
    result = "".join(map(str, res))
    
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
