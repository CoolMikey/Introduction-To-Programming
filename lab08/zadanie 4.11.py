"""
By Michał Matuszyk
on 01/12/2022
"""

def main(a, i, j):
    liczba_wierszy = len(a)
    liczba_kolumn = len(a[0])
    nowa_macierz = [[0 for x in range(liczba_kolumn-1)] for y in range(liczba_wierszy-1)]
    y_offset = 0
    for y in range(liczba_wierszy-1):
        x_offset = 0
        if y == i:
            y_offset+=1
        for x in range(liczba_kolumn-1):
            if x == j:
                x_offset += 1
            nowa_macierz[y][x] = a[y+y_offset][x+x_offset]
    return nowa_macierz



macierz = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]

print(main(macierz, 1, 3))
