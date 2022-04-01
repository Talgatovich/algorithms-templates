from typing import List

def factorize(n: int) -> List[int]:
    
    list = []
    while m < 2:
        m = 0
        dev = 2
        for i in range(2, n):
            if n % dev == 0:
                list.append(dev)
                m += 1
                n = n // dev
                dev = 2
            else:
                dev += 1
    return list


result = factorize(int(input("Enter n = ")))
print(" ".join(map(str, result)))
