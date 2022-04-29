from itertools import *


def get_max(digits):
    res = []
    for i in permutations(digits):
        a = "".join(i)
        res.append(int(a))
    print(res)
    return max(res)


def read_input():
    n = int(input())
    digits = input().strip().split()
    return n, digits


def main():
    # n, digits = read_input()
    N = ["2", "5", "2"]
    print(get_max(N))


if __name__ == "__main__":
    main()
