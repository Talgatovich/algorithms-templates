alphabet = ["-", "_"]


def to_camel_case(text):
    l = text.split("-")
    if len(l) == 1:
        l = text.split("_")
    for i in range(len(l)):
        if i == 0:
            continue
        l[i] = l[i].capitalize()
    res = "".join(l)
    return res


def read_input():
    string = input()
    return string


def main():
    string = read_input()
    return to_camel_case(string)


def test():
    a = "the_stealth_warrior"
    b = "theStealthWarrior"
    print("Right!" if to_camel_case(a) == b else "Wrong!")
    c = "The-Stealth-Warrior"
    d = "TheStealthWarrior"
    print("Right!" if to_camel_case(c) == d else "Wrong!")


if __name__ == "__main__":
    test()
