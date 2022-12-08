"""
By Michał Matuszyk
on 08/12/2022
"""

import math

def rm_dup(x):
    dl_x = len(x)
    liczba_duplikatow = 0
    for i in range(dl_x-1):
        if x[i] == x[i+1]:
            liczba_duplikatow+=1
    lista_wynikowa = [0 for x in range(dl_x-liczba_duplikatow)]
    index = 0
    pierwsze_wywolanie = True
    for i in range(dl_x):
        if pierwsze_wywolanie or not lista_wynikowa[index-1]==x[i]:
            pierwsze_wywolanie = False
            lista_wynikowa[index]=x[i]
            index+=1


    return lista_wynikowa



lista1 = [1,2,3,4,4,4,5,6,7,8, 8,9,9,9]
wynikowa_lista = rm_dup(lista1)
print(wynikowa_lista)
wynikowa_lista[3] = "a"
print(wynikowa_lista)