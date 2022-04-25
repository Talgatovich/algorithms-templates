def valid_parentheses(string):
    count = 0
    for bracket in string:
        if count < 0:
            return False
        if bracket == "(":
            count += 1
        if bracket == ")":
            count -= 1
        else:
            continue
    return count == 0


def testing():
    a = "()"
    b = True
    print("Верно!" if valid_parentheses(a) == b else "Не верно")

    c = ")(()))"
    d = False
    print("Верно!" if valid_parentheses(c) == d else "Не верно")

    e = "(())((()())())"
    print("Верно!" if valid_parentheses(e) == b else "Не верно")


if __name__ == "__main__":
    testing()
    print(valid_parentheses(")"))
