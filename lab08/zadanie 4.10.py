"""
By Michał Matuszyk
on 01/12/2022
"""

import copy

def main(a, b, n):
    liczba_wierszy = len(a)
    liczba_kolumn = len(a[0])
    nowa_macierz = [[0 for x in range(liczba_kolumn+1)] for y in range(liczba_wierszy)]
    offset = 0 #o ile w lewo przsunac elementy

    for y in range(liczba_wierszy):
        for x in range(liczba_kolumn+1):
            if x == n:
                nowa_macierz[y][x] = b[y]
                offset += 1
            else:
                nowa_macierz[y][x] = a[y][x-offset]

    return nowa_macierz



x = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]
z = ["j", "j", "j", "j", "j", "j"]

print(main(x, z, 3))
wynik = main(x, z, 3)
print(wynik)
