"""
By Michał Matuszyk
on 01/12/2022
"""

def czy_kwadrat_magiczny(macierz):
    #weryfikacja danych - czy liczby naturalne, czy macierz kwadratowa - pominiete -> zakladamy poprawnosc danych
    suma = 0
    n = len(macierz)
    for i in range(n):
        suma += macierz[i][0]


    suma_przekatnych = 0
    for i in range(n):
        suma_wiersza = 0
        suma_kolumny = 0
        for d in range(n):
            suma_wiersza += macierz[i][d]
            suma_kolumny += macierz[d][i]
        if not suma_wiersza==suma_kolumny==suma:
            return False
        suma_przekatnych += (macierz[i][i] - macierz[n-1-i][n-1-i]) #dodajemy jedna przekatna i odejmujemy druga
    if suma_przekatnych != 0:
        return False

    return True


m = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

print(czy_kwadrat_magiczny(m))

