def gen_binary(control, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_binary(control + 1, n1 - 1, n2, prefix + "(")
        if control > 0 and n2 > 0:
            gen_binary(control - 1, n1, n2 - 1, prefix + ")")


def read_input():
    n = int(input())
    control = 0
    n1 = n
    n2 = n
    return n, control, n1, n2


def main():
    n, control, n1, n2 = read_input()
    gen_binary(control, n1, n2, "")


if __name__ == "__main__":
    main()
# https://neerc.ifmo.ru/wiki/index.php?title=Правильные_скобочные_последовательности
