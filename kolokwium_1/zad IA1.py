"""
By Michał Matuszyk
on 27/11/2022
"""

def main(lista, k):
    lista_count = [0 for x in range(k)]

    for i in range(len(lista)):
        lista_count[lista[i]] += 1

    min_index = 0
    min = float("inf")
    for i in range(k):
        if 0<lista_count[i]<min:
            min = lista_count[i]
            min_index = i
    return min_index


print(main([1,9,3,1,3,1,6,9], 10))