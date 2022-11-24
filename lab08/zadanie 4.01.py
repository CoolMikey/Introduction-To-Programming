"""
zadanie 4.1
by Michał Matuszyk
"""

def make_matrix(n):
    matrix = [list(y for y in range(n)) for x in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i-1][j-1] = 1/(i+j-1)
    return matrix


print(make_matrix(4))