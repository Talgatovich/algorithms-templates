def solution(s):
    res = ''
    if s == s.lower():
        res += s
        return res
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        elif s[i] == s[i].upper():
            res += ' ' + s[i]             
        else:
            res += s[i]
    return res
        
           
def testing():
    a = "camelCasing"
    b = "camel Casing"
    print("Верно!" if solution(a) == b else "Не работает")
    print(solution(a))
    c = "identifier"
    d = "identifier"
    print("Верно!" if solution(c) == d else "Не работает")
    print(solution(c))
  

if __name__ == "__main__":
    testing()
    print(solution('break CamelCase'))
