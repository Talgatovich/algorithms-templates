def sort_array(source_array):
    # minim = min(source_array)
    # idx = source_array.index(minim)
    # source_array[idx], source_array[0] = source_array[0], source_array[idx]
    print(source_array)
    for i in range(0, len(source_array)):
        if source_array[i] % 2 == 0:
            continue
        for j in range(0, len(source_array)):
            if source_array[i] < source_array[j] and source_array[j] % 2 != 0:
                source_array[i], source_array[j] = (
                    source_array[j],
                    source_array[i],
                )
    return source_array


def testing():
    a = [5, 3, 2, 8, 1, 4]
    b = [1, 3, 2, 8, 5, 4]
    print("Верно!" if sort_array(a) == b else "Не верно!")
    print(sort_array(a))

    c = [5, 3, 1, 8, 0]
    d = [1, 3, 5, 8, 0]
    print("Верно!" if sort_array(c) == d else "Не верно!")
    print(sort_array(c))

    print("Верно!" if sort_array([]) == [] else "Не верно!")


if __name__ == "__main__":
    testing()
