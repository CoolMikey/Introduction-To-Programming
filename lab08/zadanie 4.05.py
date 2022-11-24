"""
zadanie 4.5
by Michał Matuszyk
"""
import copy

sample_matrix = [[0, 1, 2, 3], [19, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

def multiply_matrix_by_scalar(matrix, scalar):
    matrix_copy = copy.deepcopy(matrix)
    n = len(matrix)
    m = len(matrix[0])
    for y in range(n):
        for x in range(m):
            matrix_copy[y][x] = matrix[y][x]*scalar
    return matrix_copy


print(multiply_matrix_by_scalar(sample_matrix, 3))