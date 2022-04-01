from typing import List

def factorize(n: int) -> List[int]:
    
    list = []
    m = 0
    while m < 2:        
        dev = 2
        for i in range(2, n//2):
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
