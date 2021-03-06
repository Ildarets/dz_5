import os
import sys
from os import listdir
from os.path import isfile, join
from famouse_person import get_random_person
from functions_consol_manager import mdir_func, rmdir_func, copy_func, creator
from my_bank import my_bank_account


while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содерижимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. посмотреть информацию об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':

        name_folder = input("Введите название папки: ")
        mdir_func(name_folder)

    elif choice == '2':
        remove_folder = input("Введите название удаляемой файла/папки: ")
        rmdir_func(remove_folder)

    elif choice == '3':
        try:
            folder_name = input("Введите имя копируемой папки: ")
            copy_folder_name = input("Введите название новой папки: ")
            copy_func(folder_name, copy_folder_name)
        except FileNotFoundError:
            print("Такой папки нет! Введите имя существующей папки!")

    elif choice == '4':
        try:
            path = input("Ведите путь для проверки содержимого директории (если текущей, то введите ""this"": )")
            if path == 'this':
                path = os.getcwd()
            print(os.listdir(path))
        except FileNotFoundError:
            print("Введите корректно адрес!")

    elif choice == '5':
        try:
            path = input("Ведите путь для поиска папок: ")
            d = '.'
            folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
            print(folders)
        except FileNotFoundError:
            print("Введите корректно адрес!")

    elif choice == '6':
        try:
            path = input("Ведите путь для поиска файлов: ")
            onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
            print(*onlyfiles)
        except FileNotFoundError:
            print("Введите корректно адрес!")

    elif choice == '7':
        print(sys.platform)

    elif choice == '8':
        creator()

    elif choice == '9':
        get_random_person()

    elif choice == '10':
        my_bank_account()

    elif choice == '11':
        path = input("Введите директорию: ")
        os.chdir(path)

    elif choice == '12':
        path = os.getcwd()
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        d = '.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        with open('listdir.txt', 'w') as f:
            f.write('files: ')
            for i in onlyfiles:
                f.writelines(i + '  ')
            f.write('\n')
            f.write('dirs: ')
            for i in folders:
                f.writelines(i + '  ')

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню!')
