"""
By Michał Matuszyk
on 01/12/2022
"""

def main(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])
    srednie = [0 for x in range(liczba_kolumn)]
    for y in range(liczba_wierszy):
        for x in range(liczba_kolumn):
            srednie[x] += macierz[y][x]

    for i in range(liczba_kolumn):
        srednie[i] = srednie[i]/liczba_wierszy
    return srednie

m = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]

print(main(m))
