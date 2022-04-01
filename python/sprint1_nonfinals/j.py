from typing import List


def factorize(n: int) -> List[int]:
    f = n
    list = []            
    dev = 2     
    for i in range(1, n//2 + 1):
        if f % dev == 0:
            list.append(dev)            
            f = f // dev
            dev = 2
        else:
            dev += 1
    if dev == n // 2 + 2:
        list.append(n)
        return list     
    return list


result = factorize(int(input("Enter n = ")))
print(" ".join(map(str, result)))
