
def transpose(matrix, n, m):
    new_matrix = []    
    for i in range(m):
        new_list = []
        for j in range(n):
            new_list.append(matrix[j][i])
        new_matrix.append(new_list)
    return new_matrix



def read_input():    
    n = int(input("input len row "))
    m = int(input("input len col "))
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input("input row ").strip().split())))
    
    return matrix, n, m

def print_list(matrix, n, m):
    result = transpose(matrix, n, m)
    for val in result:
        print(" ".join(map(str,val)))

matrix, n, m = read_input()
print_list(matrix, n, m)

#matrix = [[-7, -1, 0, -4, -9], [5, -1, 2, 2, 9], [3, 1, -8, -1, -7], [9, 0, 8, -8, -1], [2, 4, 5, 2, 8]]
#n = 5
#m = 5
#print_list(matrix, n, m)
#print(transpose(matrix, n, m))
#print(" ".join(map(str, transpose(matrix, n, m))), sep='\n')

#print(" ".join(map(str, get_neighbours(matrix, row, col))))
