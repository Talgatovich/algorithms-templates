from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    long = list(longer)
    short = list(shorter)
    for i in range(len(long)):
        for j in range(len(short)):
            if long[i] == short[j]:
                long[i] = "0"
                short[j] = "0"

    for word in long:
        if word != "0":
            result = word
    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))

"""
Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки
 s и t, состоящие только из строчных букв. Строка t получена перемешиванием 
 букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти 
 добавленную букву.
xtkpx
xkctpx
Формат ввода
На вход подаются строки s и t, разделённые переносом строки. 
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
"""
