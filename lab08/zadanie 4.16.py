"""
By Michał Matuszyk
on 01/12/2022
"""

def main(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])
    wynik = []
    for x in range(liczba_kolumn):
        suma = 0
        kolumna = []
        for y in range(liczba_wierszy):
            suma += macierz[y][x]
            kolumna.append(macierz[y][x])

        if suma>=0:
            wynik.append(kolumna)

    return wynik

m = [[1, 2, 3, 4, 5, 6, -100], [2, 4, 6, 8, 10, 12, 80], [3, 6, 9, 12, 15, 18, -69], [6, 12, 18, 24, 30, 36, -69]]

print(main(m))
