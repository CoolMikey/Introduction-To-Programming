"""
zadanie 4.2
by Michał Matuszyk
"""

sample_matrix = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

def tr(macierz): # sum the diagonal
    suma = 0
    for i in range(len(macierz)):
        suma += macierz[i][i]
    return suma


print(tr(sample_matrix))


