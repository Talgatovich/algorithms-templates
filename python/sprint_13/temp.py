def rec(n, l):    
    print(l[-1])    
    if n == 0:
        print(l[-1])
    else:
        l = l[::n]
        rec(n-1,l)

print(rec(3, [1, 2, 3]))
