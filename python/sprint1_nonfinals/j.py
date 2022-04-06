from typing import List


# Работает правильно, но долго. Необходимо исправить
def factorize(n: int) -> List[int]:
    f = n
    koef = n // 2
    list = []
    dev = 2
    for i in range(1, koef + 1):
        if f % dev == 0:
            list.append(dev)
            f = f // dev
            dev = 2
        else:
            dev += 1
    if dev == koef + 2:
        list.append(n)
        return list
    return list


result = factorize(int(input("Enter n = ")))
print(" ".join(map(str, result)))
