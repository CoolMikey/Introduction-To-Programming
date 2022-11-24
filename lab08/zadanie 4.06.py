"""
zadanie 4.6
by Michał Matuszyk
"""

first_matrix = [[1,2,1], [2,7,2], [1,2,9]]
second_matrix = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0,1,2,3]]

def multiply(A, B): #returns the matrix of A*B multiplication
    len_a = len(A)
    len_b = len(B)
    W = [list(0 for x in range(len_b)) for y in range(len_a)]
    n = len(A[0])
    for y in range(len_a):
        for x in range(len_b):
            for i in range(n):
                W[y][x]+=(A[y][i]*B[i][x])
    print(W)


multiply(first_matrix, second_matrix)