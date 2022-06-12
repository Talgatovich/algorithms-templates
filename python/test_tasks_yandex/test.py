def get_match(N, S, Q):
    first_word = list(S)
    second_word = list(Q)
    #print(first_word, second_word)
    for i in range(N):
        for j in range(N):
            if second_word[i] == first_word[j]:
                print('correct')
                first_word[i] = '0'
                break
            elif second_word[i] != first_word[i] and second_word[i] in first_word:
                print('present')
                first_word[i] = '0'
                break
            else:
                print('absent')
                break
            

#if __name__ == "__main__":
#    main()
N = 5
S = 'ABCBC'
Q = 'BBACA'
get_match(N, S, Q)
