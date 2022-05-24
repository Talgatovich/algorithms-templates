alphabet = ["-", "_"]


def convert_string(string):

    for i in range(len(string) - 1):
        if string[i] in alphabet:
            string = string.replace(string[i], "")
            string = string.replace(string[i + 1], string[i + 1].upper())
            print(string)


def read_input():
    string = input()
    return string


def main():
    string = read_input()
    return convert_string(string)


def test():
    a = "the_stealth_warrior"
    b = "theStealthWarrior"
    print("Right!" if convert_string(a) == b else "Wrong!")
    c = "The-Stealth-Warrior"
    d = "TheStealthWarrior"
    print("Right!" if convert_string(c) == d else "Wrong!")


if __name__ == "__main__":
    test()
