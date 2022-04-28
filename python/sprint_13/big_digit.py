def get_symbols(digits, M=0, prefix=None):
    if M > len(digits) - 1:
        print("".join(prefix), end="  ")
        return
    prefix = prefix or []

    for i in range(len(digits) - 1):
        prefix.append(digits[i])
        print(prefix)
        new_digits = digits[:M] + digits[M:]
        get_symbols(new_digits, M + 1, prefix)
        prefix.pop()

def get_max(n, digits):
    pass


def read_input():
    n = int(input())
    digits = input().strip().split()
    return n, digits


def main():
    n, digits = read_input()
    # get_max(n, digits)
    get_symbols(digits)


if __name__ == "__main__":
    main()
# print("Это ввод -----", read_input())
