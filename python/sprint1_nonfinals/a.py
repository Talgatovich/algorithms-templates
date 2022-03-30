def evaluate_function(a: int, b: int, c: int, x: int) -> int:    
    res = (a * x ** 2) + (b * x) + c
    return res


a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))


# Здесь реализация вашего решения
    #d = b ** 2 - 4 * a * c
    #if d > 0:
    #    x1 = (-b + sqrt(d)) / 2 * a
    #    x2 = (-b - sqrt(d)) / 2 * a
    #    return  x1, x2
    #if d == 0:
    #    x = -b / (2 * a)
    #    return  x
    #return None