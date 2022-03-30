def check_parity(a: int, b: int, c: int) -> bool:
    list = [a, b, c]
    count = 0    
    for i in range(3):
        if list[i] % 2 == 0:
            count += 1
        else:
            count -= 1
    if count == 3 or count == -3:
        result = True
    else:
        result = False
    return result

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
