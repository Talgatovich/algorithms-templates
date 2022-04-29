MY_LIST = []


def find(number, A):
    """Ищет number в А и возвращает True если он там есть"""
    for x in A:
        if number == x:
            return True
    return False


def gen_permutations(N, M=-1, prefix=None):
    """Генерация всех перестановок элементов в массиве N
    !!!НО!!! Не работает, если в массиве есть одинаковые цифры
    """
    M = len(N) if M == -1 else M
    prefix = prefix or []

    if M == 0:
        a = "".join(prefix)
        MY_LIST.append(int(a))
        return

    for symb in N:
        if find(symb, prefix):
            continue
        prefix.append(symb)
        gen_permutations(N, M - 1, prefix)
        prefix.pop()


def get_max(digits):
    digits = sorted(digits)
    return digits[-1]


def read_input():
    n = int(input())
    digits = input().strip().split()
    return n, digits


def main():
    # n, N = read_input()
    # N = ["15", "56", "2"]
    N = ["2", "4", "5", "2", "10"]
    print(gen_permutations(N))
    # print(MY_LIST)
    # print(get_max(MY_LIST))


if __name__ == "__main__":
    main()
# print("Это ввод -----", read_input())
