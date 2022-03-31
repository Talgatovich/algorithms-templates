from typing import List, Tuple


def up(matrix, row, col):
    if row > 0:
        UP = matrix[row - 1][col]
        return UP

def down(matrix, row, col):
    if row < len(matrix) - 1:
        DOWN = matrix[row + 1][col]
        return DOWN
    

def right(matrix, row, col):
    if row < len(matrix) - 1:
        RIGHT = matrix[row][col + 1]
        return RIGHT

def left(matrix, row, col):
    if row > 0:
        LEFT = matrix[row][col - 1]
        return LEFT



#print((down(matrix, 1, 1), up(matrix, 1, 1), right(matrix, 1, 1), left(matrix, 1, 1)))

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    u = up(matrix, row, col)
    d = down(matrix, row, col)
    r = right(matrix, row, col)
    l = left(matrix, row, col)
    list = [u, d, r, l]
    result = []
    for value in list:
        if value != None:
            result.append(value)
        else:
            continue
    result.sort()
    return result

   

def read_input() -> Tuple[List[List[int]], int, int]:    
    n = int(input("input len row "))
    m = int(input("input len col "))
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input("input row ").strip().split())))
    row = int(input("input target row "))
    col = int(input("input target col "))
    return matrix, row, col


#matrix, row, col = read_input()
#print(" ".join(map(str, get_neighbours(matrix, row, col))))

matrix = [[1, 2, 3], [4, 2, 6], [0, 2, 3], [7, 5, 9]]
row = 3
col = 0
print(" ".join(map(str, get_neighbours(matrix, row, col))))
#print(get_neighbours(matrix, row, col))