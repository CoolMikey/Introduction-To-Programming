"""
By Michał Matuszyk
on 08/12/2022
"""


def main(lista1, lista2):
    lista_wynikowa = [0 for x in range(len(lista1+lista2))]
    dl_1 = len(lista1)
    for i in range(len(lista1)):
        lista_wynikowa[i] = lista1[i]

    for i in range(len(lista2)):
        lista_wynikowa[i+dl_1]=lista2[i]
    return lista_wynikowa



lista1 = [1,2,3,4,5,6,7,8]
lista2 = [99,2,3,4,5,6,7,8]
print(main(lista1, lista2))