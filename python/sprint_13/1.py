def flowerbeds(n, arr):
    arr.sort()

    newarr=[]
    start=arr[0][0]
    end=arr[0][1]
    for i in range(n-1):
        if end<arr[i+1][0]:
            newarr.append('{} {}'.format(start,end))
            start = arr[i+1][0]
            end = arr[i+1][1]
        elif arr[i+1][1]>end:
            end = arr[i+1][1]
    newarr.append('{} {}'.format(start,end))
    
    return newarr
