def is_palindrome(line: str) -> bool:
    symbols = [' ', ',', '.', '!', '?', '-', ':']
    for c in symbols:
        line = line.replace(c, '')
    line = line.lower()    
    return line == line[::-1]
    

print(is_palindrome(input().strip()))

#import re
#
#
#def is_palindrome(line: str) -> bool:
#	line_clr = re.sub(r'[^\w\s]','', line)        
#	if str(line_clr) == str(line_clr)[::-1]:
#		return True 
#	return False
#
#print(is_palindrome(input().strip())) 
