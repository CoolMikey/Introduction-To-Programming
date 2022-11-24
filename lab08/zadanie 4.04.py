"""
zadanie 4.4
by Michał Matuszyk
"""

sample_matrix = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 9]]

def diagonal(matrix):
    n = len(matrix)
    result = [0 for x in range(n)]
    for i in range(n):
        result[i] = matrix[i][i]
    return result

print(diagonal(sample_matrix))



