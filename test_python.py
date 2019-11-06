from filter_map_sorted import f_filter, f_map
import math
import pytest

def test_filter():
    friends = ['max', 'kate', 'man', 'leo']
    assert list(filter(f_filter, friends)) == ['max', 'man']

def test_sqrt():
    assert math.sqrt(9) == 3

def test_f_map():
    friends = ['max', 'kate', 'man', 'leo']
    assert list(map(f_map, friends)) == ['MAX', 'KATE', 'MAN', 'LEO']


def test_f_sorted():
    friends = ['max', 'kate', 'man', 'leo']
    assert sorted(friends, key = lambda x:x[-2]) == ['max', 'man', 'leo', 'kate']