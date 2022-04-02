from typing import List, Tuple


def check_input(n):
    if 1 < n <= 10 ** 6:
        return n
    else:
        raise ValueError

def check_null(numbers):
    null_index = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            null_index.append(i)
    return null_index

def get_distance(numbers, n):
    result = []
    null_index = check_null(numbers)    
    for i in range(n):
        l = []
        for j in range(len(null_index)):
            a = abs(null_index[j] - i)
            l.append(a)
        b = min(l)
        result.append(b)
    return result



def read_input() -> Tuple[List[int], int, int]:
    n = int(input("input street length  "))
    numbers = list(map(int, input("house's numbers ").strip().split())) 
    n = check_input(n)   
    return numbers, n

n, numbers = read_input()
print(" ".join(map(str,get_distance(n, numbers))))
