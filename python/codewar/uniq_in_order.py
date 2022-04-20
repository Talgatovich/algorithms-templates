def unique_in_order(a):
    result = []
    for i in range(1, len(a) - 1):
        if a[i + 1] != a[i - 1]:
            result.append(a[i])
            
        else:
            continue
    print(result)
    return result


def testing():
    a = "AAAABBBCCDAABBB"
    b = ["A", "B", "C", "D", "A", "B"]
    c = "ABBCcAD"
    d = ["A", "B", "C", "c", "A", "D"]

    print("РАБОТАЕТ" if unique_in_order(a) == b else "Что-то надо исправить")
    print("РАБОТАЕТ" if unique_in_order(c) == d else "Что-то надо исправить")


if __name__ == "__main__":
    testing()
