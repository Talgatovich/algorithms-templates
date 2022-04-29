digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def key_for_card(card):
    return [-digit_lengths[card], card]


cards = [2, 3, 7]
print(sorted(cards, key=key_for_card))

# Аналогичный код с применением лямбда-функции
sorted(cards, key=lambda card: [-digit_lengths[card], card])
