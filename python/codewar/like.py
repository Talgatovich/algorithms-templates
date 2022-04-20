def likes2(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        n = len(names) - 2
        return f"{names[0]}, {names[1]} and {n} others like this"


def likes(names):
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)


def testing():
    print("no one likes this" if likes([]) == "no one likes this" else "Error")
    print(
        "Peter likes this"
        if likes(["Peter"]) == "Peter likes this"
        else "Error"
    )
    print(
        "Jacob and Alex like this"
        if likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
        else "Error"
    )
    print(
        "Max, John and Mark like this"
        if likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
        else "Error"
    )
    print(
        "Alex, Jacob and 2 others like this"
        if likes(["Alex", "Jacob", "Mark", "Max"])
        == "Alex, Jacob and 2 others like this"
        else "Error"
    )


if __name__ == "__main__":
    testing()
    print(likes2(["Jacob", "Alex"]))
