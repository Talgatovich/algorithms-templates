""" алгоритм следующий (сортируем по неубыванию):

На каждой итерации проходим по массиву, поочередно сравнивая пары соседних
элементов. Если элемент на позиции i больше элемента на позиции i + 1,
меняем их местами. После первой итерации самый большой элемент всплывёт в 
конце массива.Проходим по массиву, выполняя указанные действия до тех пор, 
пока на очередной итерации не окажется, что обмены больше не нужны, 
то есть массив уже отсортирован.После не более чем n – 1 итераций выполнение 
алгоритма заканчивается, так как на каждой итерации хотя бы один элемент 
оказывается на правильной позиции.

Помогите Гоше написать код алгоритма.
Формат ввода
В первой строке на вход подаётся натуральное 
число n — длина массива, 2 ≤ n ≤ 1000.
Во второй строке через пробел записано n целых чисел.
Каждое из чисел по модулю не превосходит 1000.

Обратите внимание, что считывать нужно только 2 строки: значение n 
и входной массив.

Формат вывода
После каждого прохода по массиву, на котором какие-то элементы меняются
местами, выводите его промежуточное состояние.
Таким образом, если сортировка завершена за k меняющих массив итераций, 
то надо вывести k строк по n чисел в каждой — элементы массива после 
каждой из итераций.
Если массив был изначально отсортирован, то просто выведите его.
"""


def bubble(n, num):
    for i in range(1, n):
        f = 0
        c = 0
        for j in range(0, n - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                f += 1
            # Для вариантов когда все символы одинаковые или уже упорядочены
            else:
                c += 1
        if c == n - 1:
            print(*num)
            break
        if f == 0:
            break

        print(*num)


def read_input():
    n = int(input())
    num = list(map(int, input().strip().split()))
    return n, num


def main():
    n, num = read_input()
    bubble(n, num)


if __name__ == "__main__":
    main()

# num = [12, 8, 9, 10, 11]
# num_2 = [4, 3, 9, 2, 1]
# bubble(5, num)
# print(read_input())
