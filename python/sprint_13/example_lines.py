def flowerbeds(n, arr):
    arr.sort()    
    new_arr = []
    start = arr[0][0]
    end = arr[0][1]
    
    for i in range(n-1):
        if arr[i+1][0] > end :
            new_arr.append(f'{start} {end}')
            start = arr[i+1][0]
            end = arr[i+1][1]
            
        elif arr[i+1][1] > end:
            end = arr[i+1][1]                        
    new_arr.append(f'{start} {end}')
            
    return new_arr
    
def read_input():
    n = int(input())
    arr = []
    for i in range(n):        
        nums = list(map(int, input().strip().split()))
        print
        arr.append(nums)
    return n, arr


def main():
    n, arr = read_input()
    print(*flowerbeds(n, arr), sep='\n')


#if __name__ == "__main__":
#    main()     


#print(read_input())
#arr = [[7, 8], [7, 8], [2, 3], [6, 10]]

n = 4
arr = [[2, 3], [5, 6], [3, 4], [3, 4]]
print(*flowerbeds(n, arr), sep='\n')
