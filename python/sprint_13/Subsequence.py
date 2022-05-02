def sequense(list1, list2, count=0):
    k = 0
    count = count   
    for i in range(len(list1)):
        if i == len(list1) - 1:            
            return
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                k = j
                count += 1
                sequense(list1[i+1:], list2[k+1:], count)
    if count == len(list1):
        return True
    
list1 = 'abc'
list2 = 'ahbgdcu'
print(sequense(list1, list2))
            