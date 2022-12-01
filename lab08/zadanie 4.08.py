"""
By Michał Matuszyk
on 01/12/2022
"""

def outer_product(macierz):
    x = len(macierz)
    y = len(macierz[0])
    result = [[0 for d in range(x)] for i in range(y)]
    for i in range(x):
        for d in range(y):
            result[d][i] = macierz[i][d]
    return result



a = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]

print(outer_product(a))