# 66766337
def check_score(train, k):
    buttons = k * 2
    deleted = set()
    quantity = {}
    for symb in train:
        if symb != '.' and symb not in deleted:
            if symb in quantity:
                quantity[symb] += 1
            if symb not in quantity:
                quantity[symb] = 1
            if quantity[symb] > buttons:
                deleted.add(symb)
                del quantity[symb]
    return len(quantity)


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
