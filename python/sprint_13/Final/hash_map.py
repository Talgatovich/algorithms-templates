pairs = {
    "apple": 15,
}


def get(key):
    for pair in pairs:
        if pair == key:  # пара с указанным ключом найдена
            return pairs[pair]
    return None


def set(key, value):
    for pair in pairs:
        if pair == key:  # пара с указанным ключом найдена
            # обновить значение в найденной паре
            pair = value
            return
        # пара с заданным ключом не найдена
        pairs[key] = value


set("apple", 17)
print(get("apple"))
print(pairs)
