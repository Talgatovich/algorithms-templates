''' Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :

Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква 
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"'''


def check_password(password):
    alphabet = "!@#$%*"
    nums = 0
    big_word = 0
    alph = 0
    result_count = 0
    if len(password) >= 10:
        result_count += 1
    for symb in password:
        if symb.isdigit() and nums < 3:
            nums += 1
        if symb.isupper():
            big_word += 1
        if symb in alphabet:
            alph += 1
    result_count = result_count + nums + big_word + alph
    if result_count >= 6:
        print("Perfect password")
    else:
        print("Easy peasy")


password = "123A@1111j"
check_password(password)
