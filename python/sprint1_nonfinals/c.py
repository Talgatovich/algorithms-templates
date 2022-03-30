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
    if row < len(matrix):
        DOWN = matrix[row + 1][col]    
        return DOWN
matrix = [[1, 2, 3], [4, 2, 6], [2, 2, 3], [7, 5, 9]]

print(down(matrix, 1, 1), up(matrix, 1, 1))

#def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
#    pass
#
#    right_row = row
#    right_col = col + 1
#    if col == row - 1:
#        right_row = right_col = None
#    if right_row:
#        RIGHT = matrix[right_row][right_col]
#
#    left_row = row
#    left_col = col - 1
#    if col == 0:
#        left_row = left_col = None
#    if left_row:
#        LEFT = matrix[left_row][left_col]
#    l = [UP, DOWN, RIGHT, LEFT]
#    return l
#    
#    
#
#def read_input() -> Tuple[List[List[int]], int, int]:    
#    n = int(input("input len row "))
#    m = int(input("input len col "))
#    matrix = []
#    for i in range(n):
#        matrix.append(list(map(int, input("input row ").strip().split())))
#    row = int(input("input target row "))
#    col = int(input("input target col "))
#    return matrix, row, col
#
#
#matrix, row, col = read_input()
##print(matrix, row, col)
#print(" ".join(map(str, get_neighbours(matrix, row, col))))
