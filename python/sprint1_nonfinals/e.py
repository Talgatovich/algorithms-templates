def get_longest_word(line: str) -> str:
    l = line.split(' ')
    result = ''
    for word in l:
        if len(result) < len(word):
            result = word        
    return result

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
