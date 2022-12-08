"""
By Michał Matuszyk
on 08/12/2022
"""

import math

def trim_nan(x):
    dl_x = len(x)
    liczba_nan = 0
    for i in range(dl_x):
        if math.isnan(x[i]):
            liczba_nan+=1
    lista_wynikowa = [0 for x in range(dl_x-liczba_nan)]
    index = 0
    for i in range(dl_x):
        if not math.isnan(x[i]):
            lista_wynikowa[index] = x[i]
    return lista_wynikowa


NaN = float("nan")

lista1 = [NaN,NaN,NaN,1,2,3,NaN,1,2,NaN]
wynikowa_lista = trim_nan(lista1)
print(wynikowa_lista)
wynikowa_lista[3] = "a"
print(wynikowa_lista)