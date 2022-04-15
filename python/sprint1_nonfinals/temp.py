mylist = [0, 9, 1, 6, 0, 7, 3, 5, 2, 0, 0, 8, 4, 1, 0]
n = len(mylist)


def nearest_zero(n):
    # Подготваливаем массив для сбора информации о дистанциях до пустых участков
    distances = [0] * n
    index_dist = [i for i in range(n) if mylist[i] == 0]
    # Находим индекс левого пустого участка
    for i in range(distances[0], n, +1):
        if mylist[i] == 0:
            distances[i] = 0
        else:
            distances[i] = distances[i - 1] + 1
    # Находим индекс правого пустого участка
    for i in range(index_dist[-1], index_dist[0], -1):
        if mylist[i] == 0:
            distances[i] = 0
        else:
            distances[i] = min(distances[i], distances[i + 1] + 1)
    # Заполняем информацию о дистанциях до пустых участков
    for i in range(index_dist[0] - 1, -1, -1):
        distances[i] = distances[i + 1] + 1
    # Выводим информацию в нужном виде
    return distances


distances = nearest_zero(n)
print(" ".join(map(str, distances)))
