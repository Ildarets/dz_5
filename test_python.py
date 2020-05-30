from filter_map_sorted import f_filter, f_map, f_sorted
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
    assert sorted(friends, key=lambda x: x[-2]) == ['max', 'man', 'leo', 'kate']


def test_pi():
    assert math.pi == 3.141592653589793


def test_pow():
    assert pow(2, 3) == 8
    assert pow(10, 3) == 1000


def test_hypot():
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(6, 6) == 8.48528137423857
