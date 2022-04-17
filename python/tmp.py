f = open('text1.txt')
v = open('text2.txt')
list1 = []
list2 = []
result = []

for line in f:    
    list1.append(line)

for line in v:    
    list2.append(line)

for i in range(len(list1)):
    if list1[i] != list2[i]:
        a = str(list1[i]) + '!=' + str(list2[i])
        result.append(a)
print(result)
