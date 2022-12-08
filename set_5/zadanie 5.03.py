"""
By Michał Matuszyk
on 08/12/2022
"""

def rep_each(lista, powielenie):
    lista_wynikowa = [0 for x in range(len(lista)*powielenie)]
    dl_listy = len(lista)
    for d in range(powielenie):
        for i in range(len(lista)):
            lista_wynikowa[d*powielenie+i] = lista[d]
    return lista_wynikowa

lista1 = [1,2,3,4,5,6,7,8]
wynikowa_lista = rep_each(lista1, 3)
print(wynikowa_lista)
wynikowa_lista[3] = "a"
print(wynikowa_lista)