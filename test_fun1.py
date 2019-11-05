from functions import salary, hello_who


def test_hello_who_leo():
    assert hello_who('Leo') == 'Hello, Leo'

from filter_map_sorted import f_filter, f_map
import math
import pytest

# def test_filter():
#     friends = ['max', 'kate', 'man', 'leo']
#     assert f_filter(friends) == 'max'
#
# def test_sqrt():
#     assert math.sqrt(2) == 4

def test_f_map():
    friends = ['max', 'kate', 'man', 'leo']
    assert map(f_map, friends) == ['Max', 'Kate', 'Man', 'Leo']

