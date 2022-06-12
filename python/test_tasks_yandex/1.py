"""
Саша разрабатывает игру «Отгадай слово». В этой игре, игрок должен отгадать 
загаданное слово из N
 букв за несколько попыток.
В данный момент перед Сашей стоит задача написать логику проверки величины 
совпадения попытки игрока с загаданным словом.
Более формально, пусть есть строка S — загаданное слово и строка 
Q — попытка игрока. Обе строки имеют одинаковую длину N. Для каждой позиции 
1≤i≤N строки Q, нужно вычислить тип совпадения в этой позиции со строкой S.
Если Qi=Si, то в позиции i тип совпадения должен быть равен 
correct.Если Qi≠Si, но существует другая позиция 1≤j≤N, такая что 
Qi=Sj, то в позиции i тип совпадения должен быть равен present.

Каждую букву строки S можно использовать не более чем в одном совпадении типа 
correct или present.
Приоритет всегда отдается типу correct.
Из всех возможных вариантов использования в типе present
 программа Саши выбирает самую левую позицию в строке Q.
В остальных позициях тип совпадения должен быть равен absent.
"""
def get_match(S, Q):
    N = len(S)
    l = [None] * N
    first_word = list(S)
    second_word = list(Q)
    for i in range(N):
        if second_word[i] == first_word[i]:            
            first_word[i] = '0'
            l[i] = 'correct'
    for i in range(N):                  
        if second_word[i] != first_word[i] and second_word[i] in first_word:
            idx = first_word.index(second_word[i]) 
            first_word[idx] = 0
            l[i] = 'present'
        else:
            if l[i] == None:
                l[i] = 'absent'
    return l


def read_input():    
    S = input()
    Q = input()
    return S, Q
    

def main():
    S, Q = read_input()
    l = get_match(S, Q)
    for val in l:
        print(val)
    


if __name__ == "__main__":
    main()
#N = 5
#S = 'COVER'
#Q = 'CLEAR'
#get_match(N, S, Q)
