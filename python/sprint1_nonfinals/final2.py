# 66743547
def check_score(train, k):
    score = 0
    for i in range(1, 10):
        cnt = train.count(str(i))
        if str(i) in train and cnt <= k * 2:
            score += 1
        else:
            continue
    return score


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


train, k = read_input()
print(check_score(train, k))
