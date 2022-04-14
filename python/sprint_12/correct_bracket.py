# Дана скобочная последовательность. Нужно определить, правильная ли она.

# Для каждого символа в тексте
# проверить является ли он открывающей скобкой
# если является, то добавить её в стэк
# если нет, то проверить является ли символ закрывающей скобкой
# если является и последняя добавленная открывающая скобка совпадает,
# то убрать её из стэка (найдена совпавшая пара скобок)
# иначе завершить алгоритм—найдена неправильно вложенная скобка.
#
# Продолжать до конца текста и если стэк пустой, то текст содержит
# только правильно вложенные скобки.


def is_correct_bracket_seq(brackets):
    """
    Принимает на вход скобочную последовательность
    и возвращает True, если последовательность правильная, а иначе False.
    """
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    stack = []
    for symb in brackets:
        if symb in open:
            stack.append(symb)

        if symb in close:
            try:
                last_symb = stack[-1]
            except IndexError:
                return False
            if close.index(symb) != open.index(last_symb):
                return False
            del stack[-1]
    return len(stack) == 0


def read_input():
    brackets = input()
    print(is_correct_bracket_seq(brackets))


def main():
    read_input()


if __name__ == "__main__":
    main()
