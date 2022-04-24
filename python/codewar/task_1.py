# 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    res = []    
    for i in range(0, len(s), 2):
        try:
            words = s[i] + s[i + 1]            
            res.append(words)
        except IndexError:
            words = s[i] + '_'
            res.append(words)                    
    return res


def testing():
    a = "asdfadsf"
    b = ['as', 'df', 'ad', 'sf']
    print("Верно!" if solution(a) == b else "Неверно!")
    print(solution(a))
    
    c = "asdfads"
    d = ['as', 'df', 'ad', 's_']
    print("Верно!" if solution(c) == d else "Неверно!")
    print(solution(c))
    
if __name__ == '__main__':
    testing()  
    
    
    
#    
#    (, ),
#    ("", []),
#    ("x", ["x_"])
