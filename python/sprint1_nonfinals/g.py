def to_binary(number: int) -> str:
    res = ''
    while number != 0:
        ans = number % 2
        res += str(ans)
        number = number // 2
    return res[::-1]

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
