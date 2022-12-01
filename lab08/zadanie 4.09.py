"""
By Michał Matuszyk
on 01/12/2022
"""

import copy

def main(a, b, n):
    liczba_wierszy = len(a)
    liczba_kolumn = len(a[0])
    nowa_macierz = [[0 for x in range(liczba_kolumn)] for y in range(liczba_wierszy+1)]
    offset = 0
    for i in range(liczba_wierszy+1):
        if i == n:
            nowa_macierz[i] = b
            offset +=1
        else:
            nowa_macierz[i] = copy.copy(a[i-offset])
            # nowa_lista[i] = a[i]   #rowniez dziala, ale zmiana listy pierwotnej powoduje zmiany w wyniku
    return nowa_macierz



x = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]
z = ["j", "j", "j", "j", "j", "j"]

print(main(x, z, 3))