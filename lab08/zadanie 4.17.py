"""
By Michał Matuszyk
on 01/12/2022
"""
import copy
import math

def main(macierz):
    liczba_wierszy = len(macierz)
    liczba_kolumn = len(macierz[0])
    wynik = copy.deepcopy(macierz)
    for x in range(liczba_kolumn):
        suma = 0
        for y in range(liczba_wierszy):
            suma += macierz[y][x]
        srednia = suma/liczba_wierszy
        suma_do_odchylenia_standardowego = 0
        for y in range(liczba_wierszy):
            suma_do_odchylenia_standardowego += (macierz[y][x]-srednia)**2
        odchylenie_standardowe = math.sqrt(suma_do_odchylenia_standardowego/liczba_wierszy)
        for y in range(liczba_wierszy):
            wynik[y][x] = copy.copy((macierz[y][x]-srednia)/odchylenie_standardowe)
    return wynik

m = [[2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [6, 12, 18, 24, 30, 36], [1, 2, 3, 4, 5, 6]]
# m = [[7,4,-2], [4,-2,7],[-2,7,4]]

print(main(m))
