import copy

"""Из массива целых чисел удалите наименьшее значение. 
Не мутируйте исходный массив/список. Если есть несколько элементов
с одинаковым значением, удалите элемент с меньшим индексом.
Если вы получите пустой массив/список, верните пустой массив/список.
Не изменяйте порядок оставшихся элементов."""


def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")
    new_list = copy.deepcopy(numbers)
    if len(numbers) == 0:
        return []
    mnm = min(new_list)
    idx = new_list.index(mnm)
    del new_list[idx]
    return new_list, numbers


def testing():
    print(
        "Работает"
        if remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
        else "Не правильный вывод"
    )
    print("Текущий вывод ", remove_smallest([1, 2, 3, 4, 5]), "\n", "*" * 70)

    print(
        "Работает"
        if remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
        else "Не правильный вывод"
    )
    print("Текущий вывод ", remove_smallest([5, 3, 2, 1, 4]), "\n", "*" * 70)

    print(
        "Работает"
        if remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
        else "Не правильный вывод"
    )
    print("Текущий вывод ", remove_smallest([1, 2, 3, 1, 1]), "\n", "*" * 70)

    print("Работает" if remove_smallest([]) == [] else "Не правильный вывод")
    print("Текущий вывод ", remove_smallest([]), "\n", "*" * 70)


if __name__ == "__main__":
    testing()
