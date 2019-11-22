import os
import sys
import shutil
from os import listdir
from os.path import isfile, join
from famouse_person import get_random_person
from my_bank import my_bank_account
from decorator import add_separators


def mdir_func(name_folder):
    os.mkdir(name_folder)


def rmdir_func(remove_folder):
    if os.path.isdir(remove_folder):  # удалит только если это папка(вместе с содержимым)
        shutil.rmtree(remove_folder)
    elif os.path.isfile(remove_folder):  # удалит только если это файл
        os.unlink(remove_folder)


def copy_func(folder_name, copy_folder_name):
    path = os.getcwd()
    if os.path.isdir(folder_name):  # копирует только если это папка(вместе с содержимым)
        shutil.copytree(join(path, folder_name), join(path, copy_folder_name))
    else:
        shutil.copy(folder_name, copy_folder_name)

@add_separators
def creator():
    print( "Создатель программы: Ильдар Шайдуллин")
