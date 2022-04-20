n= 5
dict = {}
for i in range(1, n):
    dict[i] = 'soldier'
print(dict)

count = 1
k = 2

while len(dict) != 1:
    for i in range(1, len(dict)):        
        try:
            if count == k:
                del dict[i]
                count = 0
            else:
                count += 1
        except Exception:            
            del dict[i + 1]
    
print(dict)
