import os
import os.path
import random

def remove_file_from_disk(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def number_to_letter(number):
    return chr(number + ord('a'))

def join_letter(base, letter):
    return base + letter

def get_file_name(file_id):
    """Zwraca nazwę pliku na podstawie identyfikatora pliku"""
    return f"file{file_id}.txt"

def print_files_state(files_count=3):
    """Wypisuje stan plików"""
    for file_id in range(files_count):
        file_name = get_file_name(file_id)
        if not os.path.exists(file_name):
            continue
        content = ''
        with open(file_name, "r") as read_file:
            print(f'{file_name}: ')
            content = read_file.read()

        if content.strip() !='':
            print(content.strip())

def generate_row():
    row_id = random.randint(0, 100000)
    login = number_to_letter(random.randint(0, 25))
    ostatnia_litera = login
    for i in range(4):
        new_letter = ""
        while True:
            new_letter = number_to_letter(random.randint(0, 25))
            if new_letter!=ostatnia_litera:
                ostatnia_litera = new_letter
                break
        login = join_letter(login, new_letter)
    generate_level = random.randint(1, 20)

    if generate_level<=10: #prawdop 1/2
        level = "beginner"
    elif generate_level<=16: #prawdop 3/10
        level = "regular"
    elif generate_level<=19: #prawdop 3/20
        level = "senior"
    else: #prawdop 1/20 - ale to wynika z mozliwosci jakie zostaja -> dlatego else
        level = "expert"

    return row_id, login, level

def save_row_in_file(file_name, row_id, login, level):
    with open(file_name, "a") as file:
        row = f"{row_id} {login} {level}"
        print(row, file=file)
    return True

def get_file_for_row(row_id, file0_exists, file1_exists, file2_exists):
    hash = row_id%360
    file_id = None
    if hash<120:
        file_id = 0
        if file0_exists:
            return 0
        elif file2_exists:
            return 2
        else:
            return 1
    elif hash<240:
        file_id = 1
        if file1_exists:
            return 1
        elif file0_exists:
            return 0
        else:
            return 2
    else:
        file_id = 2
        if file2_exists:
            return 2
        elif file1_exists:
            return 1
        else:
            return 0

def can_delete_file(file_id_to_delete, file0_exists, file1_exists, file2_exists):
    if file0_exists + file1_exists + file2_exists <=1:
        return False
    if file_id_to_delete == 0:
        if file0_exists:
            return True
        else:
            return False
    elif file_id_to_delete == 1:
        if file1_exists:
            return True
        else:
            return False
    elif file_id_to_delete == 2:
        if file2_exists:
            return True
        else:
            return False
    else:
        return False #bledne dane wejsciowe


def main():
    random.seed(2022)
    file0_exists = True
    file1_exists = True
    file2_exists = True
    #tworzenie nowych pustych plikow, zeby były 3 na start
    with open(get_file_name(0), "w") as f:
        pass
    with open(get_file_name(1), "w") as f:
        pass
    with open(get_file_name(2), "w") as f:
        pass


    print("""Możliwe akcje to:\n1 - Wygeneruj wiersz danych\n2 - Zapisz wygenerowany uprzednio wiersz do odpowiedniego pliku.\n3 - Usuń plik o podanym id (0-2)\n4 - Wyjdź z programu""")
    while True:
        akcja = int(input("Podaj nr akcji do wykonania: "))
        if akcja == 1: #generowanie wiersza danych
            row_id, login, level = generate_row()
            print(f"Wygenerowano wiersz: row_id:{row_id}, login:{login}, level:{level}")

        if akcja == 2: #zapisanie wiersza danych
            file_id = get_file_for_row(row_id, file0_exists, file1_exists, file2_exists)
            save_row_in_file(get_file_name(file_id), row_id, login, level)
            print(f"Wiersz dopisany do {get_file_name(file_id)}")

        if akcja == 3: #usuwanie pliku o wskazanym id
            id_pliku_do_usuniecia = int(input("Podaj numer pliku do usunięcia: "))
            if can_delete_file(id_pliku_do_usuniecia, file0_exists, file1_exists, file2_exists):
                file_name_to_delete = get_file_name(id_pliku_do_usuniecia)

                #znajdywanie pliku docelowego
                if id_pliku_do_usuniecia == 0:
                    file0_exists = False
                    if file2_exists:
                        id_pliku_docelowego = 2
                    else:
                        id_pliku_docelowego = 1
                if id_pliku_do_usuniecia == 1:
                    file1_exists = False
                    if file0_exists:
                        id_pliku_docelowego = 0
                    else:
                        id_pliku_docelowego = 2
                if id_pliku_do_usuniecia == 2:
                    file2_exists = False
                    if file1_exists:
                        id_pliku_docelowego = 1
                    else:
                        id_pliku_docelowego = 0

                file_name_to_transfer = get_file_name(id_pliku_docelowego)
                #move data
                with open(file_name_to_delete, "r")  as file_being_removed:
                    with open(get_file_name(id_pliku_docelowego), "a") as docelowy_plik:
                        for row in file_being_removed:
                            print(row, end="", file=docelowy_plik)

                remove_file_from_disk(file_name_to_delete)
                print(f"Plik {id_pliku_do_usuniecia} został usunięty")
                print_files_state()

            else:
                print(f"Nie można usunąć pliku {id_pliku_do_usuniecia}")

        if akcja == 4: #wyjscie z programu
            break

if __name__ == '__main__':
    main()
