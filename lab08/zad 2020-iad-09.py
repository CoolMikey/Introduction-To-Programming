"""
By Michał Matuszyk
on 01/12/2022
"""
import copy
import random

def wypisz_macierz(matrix):
    print(" ", end=" ")
    for column in range(len(matrix[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A")+column-10), end=" ")
    print()

    for row in range(len(matrix)):
        if row < 10:
            print(row, end=" ")
        else:
            print(chr(ord("A")+row-10), end=" ")
        for column in range(len(matrix[row])):
            print(f'{matrix[row][column]}', end=" ")
        print()
    print()

def losuj_miny(plansza, liczba_min):
    liczba_min_wylosowanych = 0
    while True:
        if liczba_min_wylosowanych>=liczba_min:
            break
        y = random.randint(0, len(plansza)-1)
        x = random.randint(0, len(plansza[0])-1)
        if plansza[y][x] != "m":
            plansza[y][x] = "m"
            liczba_min_wylosowanych += 1

def wypisz_macierz_cenzura(plansza, cenzura):
    kopia_planszy = copy.deepcopy(plansza)
    for y in range(len(plansza)):
        for x in range(len(plansza[0])):
            if not cenzura[y][x]:
                kopia_planszy[y][x] = "*"
    wypisz_macierz(kopia_planszy)

def odkryj_pole(plansza, cenzura, wiersz, kolumna):
    if wiersz<0 or wiersz>=len(plansza) or kolumna<0 or kolumna >= len(plansza[0]):
        return False
    if plansza[wiersz][kolumna] == "m":
        return False
    else:
        cenzura[wiersz][kolumna] = True
        return True

def numery_przy_minach(plansza):
    liczba_wierszy = len(plansza)
    liczba_kolumn = len(plansza[0])
    for y in range(liczba_wierszy):
        for x in range(liczba_kolumn):
            if plansza[y][x] == "m":
                for y_o in range(3): #y'ki okoliczne
                    for x_o in range(3): #x'y okoliczne
                        nowy_y = (y-1)+y_o
                        nowy_x = (x-1)+x_o
                        if nowy_x>=0 and nowy_x<liczba_kolumn and nowy_y>=0 and nowy_y<liczba_wierszy and not plansza[nowy_y][nowy_x]=="m":
                            plansza[nowy_y][nowy_x] += 1



def main():
    plansza = [[0 for x in range(15)] for y in range(10)]
    cenzura = [[False for x in range(15)] for y in range(10)]

    losuj_miny(plansza, 15)
    wypisz_macierz(plansza)
    wypisz_macierz_cenzura(plansza, cenzura)
    numery_przy_minach(plansza)
    wypisz_macierz(plansza)

    for i in range(5):
        wiersz = int(input("Podaj wiersz: "))
        kolumna = int(input("Podaj kolumnę: "))
        wynik = odkryj_pole(plansza, cenzura, wiersz, kolumna)
        if not wynik: #jesli wynik to fałsz
            print("PRZEGRAŁEŚ!")
            wypisz_macierz(plansza)
            return 0
        wypisz_macierz_cenzura(plansza, cenzura)


if __name__ == "__main__":
    main()