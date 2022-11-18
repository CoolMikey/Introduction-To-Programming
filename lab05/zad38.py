import random


def main(t, k):
    lista = [float("-inf") for i in range(k)]
    for i in range(len(t)):
        elem = t[i]
        for d in range(k):
            if elem > lista[d]:
                poprzedni_elem = lista[d]
                lista[d] = elem
                elem = poprzedni_elem
    return lista[k-1]

random.seed(1)
a = list(range(1, 10000, 1))
b = 3

n = 100

for i in range(n):
    random.shuffle(a)

    wynik_wg_main = main(a, b)
    a.sort()
    wynik_wg_sort = a[-b]
    if wynik_wg_main != wynik_wg_sort:
        print("inny dla")
    # print(wynik_wg_sort, wynik_wg_main)
    # else:
    #     print("Taki sam")