import math


def f_filter(x):
    """
    Фильтрует по первой букве в имени
    :param x: список имен
    :return: отфильтрованный список имен
    """
    if x.startswith('m'):
        return True
    else:
        return False


def f_map(x):
    return x.upper()


def f_sorted(x):
    # return x[-2]
    return lambda x: x[-2]


if __name__ == '__main__':
    friends = ['max', 'kate', 'man', 'leo']
    map_list = list(map(f_map, friends))
    print(map_list)

    result = list(filter(f_filter, friends))
    print(result)

    print(sorted(friends, key=lambda x: x[-2]))
    print(math.pi)
