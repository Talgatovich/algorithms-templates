# 66752379
def check_score(train, k):
    deleted = set()
    dict = {}
    for symb in train:
        if symb != '.' and symb not in deleted:
            if symb in dict:
                dict[symb] += 1
            if symb not in dict:
                dict[symb] = 1
            if dict[symb] > k * 2:
                deleted.add(symb)
                del dict[symb]
    return len(dict)


def unpack(train):
    res = []
    for val in train:
        for num in val:
            res.append(num)
    return res


def read_input():
    train = []
    k = int(input())
    for i in range(4):
        train.append(list(input()))
    train = unpack(train)
    return train, k


if __name__ == '__main__':
    train, k = read_input()
    print(check_score(train, k))
