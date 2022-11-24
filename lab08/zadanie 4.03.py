"""
zadanie 4.3
by Michał Matuszyk
"""

non_symetric_matrix = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
symetric_matrix = [[1,2,1], [2,7,2], [1,2,9]]

def check_if_symetric(matrix):
    n = len(matrix) #get the size of the matrix
    for y in range(0, n-1):
        for x in range(y+1, n):
            if matrix[y][x]!=matrix[x][y]:
                return False
    return True

print(check_if_symetric(non_symetric_matrix))
print(check_if_symetric(symetric_matrix))