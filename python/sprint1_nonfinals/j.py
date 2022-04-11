from typing import List


# Работает правильно, но долго. Необходимо исправить
def factorize(n: int) -> List[int]:
    list = set()
    dev = 2
    while n > 1:
        if n % dev == 0:
            list.add(dev)
            n //= dev
        else:
            dev += 1
    return list


result = factorize(int(input("Enter n = ")))

print(" ".join(map(str, result)))
