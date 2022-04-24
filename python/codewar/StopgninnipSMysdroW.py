def spin_words(sentence):
    l = sentence.split(" ")
    res = ''
    for word in l:
        if len(word) <= 4:
            res += word + ' '
        else:
            new_word = word[::-1]
            res += new_word + ' '
    return res.strip()
            


def testing():
    a = "Hey fellow warriors"
    b = "Hey wollef sroirraw"
    print('Верно!' if spin_words(a) == b else 'Не верно')
    print(spin_words(a))
    c =  "This is a test"
    d =  "This is a test"
    print('Верно!' if spin_words(c) == d else 'Не верно')

if __name__ == "__main__":
    testing()
