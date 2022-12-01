"""
By Michał Matuszyk
on 01/12/2022
"""
import copy

def mediana(lista):
    dl = len(lista)
    kopia_listy = copy.copy(lista)
    kopia_listy.sort()
    n = dl // 2 - 1
    if dl%2==0:
        return (kopia_listy[n]+kopia_listy[n+1])/2
    else:
        return kopia_listy[n]


def main(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])
    wyniki = [[0,0,0,0,0] for x in range(liczba_kolumn)]
    for x in range(liczba_kolumn):
        kolumna = [0 for i in range(liczba_wierszy)]
        for y in range(liczba_wierszy):
            kolumna[y] = macierz[y][x]
        kolumna.sort()
        wyniki[x][0] = kolumna[0]
        wyniki[x][4] = kolumna[liczba_wierszy-1]
        wyniki[x][2] = mediana(kolumna)
        if liczba_wierszy%2==0:
            pierwsza_polowa = [0 for i in range(liczba_wierszy//2)]
            druga_polowa = [0 for i in range(liczba_wierszy//2)]
        else:
            pierwsza_polowa = [0 for i in range(liczba_wierszy//2+1)]
            druga_polowa = [0 for i in range(liczba_wierszy//2+1)]
        for i in range(len(pierwsza_polowa)):
            pierwsza_polowa[i] = kolumna[i]
            druga_polowa[i] = kolumna[i+len(pierwsza_polowa)-1]
        wyniki[x][1] = mediana(pierwsza_polowa)
        wyniki[x][3] = mediana(druga_polowa)

    return wyniki

m = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36]]
print(main(m))