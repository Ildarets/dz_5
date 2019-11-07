from functions_consol_manager import mdir_func, rmdir_func, copy_func
import os, sys


def test_mkdir():
    name = 'name_dir'
    mdir_func(name)
    assert os.path.exists(name) == True
    os.rmdir(name)


def test_rmdir():
    name = 'name_dir'
    os.mkdir(name)
    rmdir_func(name)
    assert os.path.exists(name) == False


def test_copy():
    name = 'name_dir'
    name_copy = 'name_dir_copy'
    os.mkdir(name)
    copy_func(name, name_copy)
    assert os.path.exists(name_copy) == True
    os.rmdir(name)
    os.rmdir(name_copy)
