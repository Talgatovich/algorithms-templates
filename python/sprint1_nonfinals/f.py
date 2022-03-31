def is_palindrome(line: str) -> bool:
    symbols = [' ', ',', '.', '!', '?', '-', ':']
    for c in symbols:
        line = line.replace(c, '')
    line = line.lower()    
    return line == line[::-1]
    

print(is_palindrome(input().strip()))
