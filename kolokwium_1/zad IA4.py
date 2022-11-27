"""
By Michał Matuszyk
on 27/11/2022
"""

def main(liczba):
    liczba_cyfr = 1
    liczba_kopia = liczba
    while True:
        if liczba_kopia // 10 >=1:
            liczba_cyfr +=1
            liczba_kopia /= 10
        else:
            break

    poprz_cyf = liczba//(10**(liczba_cyfr-1))
    dl_akt = 1
    pocz_akt = 0
    dl_najdl = 1
    pocz_najdl = 0

    for i in range(1, liczba_cyfr):
        aktualna_cyfra = (liczba//(10**(liczba_cyfr-1-i)))%10
        if aktualna_cyfra > poprz_cyf:
            dl_akt +=1
        if dl_akt > dl_najdl:
            dl_najdl = dl_akt
            pocz_najdl = pocz_akt
        if aktualna_cyfra <= poprz_cyf:
            dl_akt = 1
            pocz_akt = i
        poprz_cyf = aktualna_cyfra

    return (liczba%(10**(liczba_cyfr-pocz_najdl)))//(10**(liczba_cyfr-dl_najdl-pocz_najdl))


print(main(1253468910))