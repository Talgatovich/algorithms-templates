def fibo(n):
    if n < 2:
        return 1
    result = fibo(n - 1) + fibo(n - 2)
    return result


def fibo_cycle(n, k):
    if n < 2:
        return 1

    else:
        i = 2
        fibo = [1, 1, 2]
        while n >= i:
            fibo[2] = fibo[0] + fibo[1]
            fibo[0] = fibo[1]
            fibo[1] = fibo[2]
            i += 1
        result = fibo[1]
        r = result % 10 ** k
        return r


text = input().split(" ")
k = int(text.pop())
n = int(text.pop())
result = fibo(n)
print(result % 10 ** k)
