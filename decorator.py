import os

# Функция декоратор
# f - исходная фукнция
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print(('*' * 10 + '~'* 10)*5)
        result = f(*args, **kwargs)
        # поведение после вызова
        print(('~' * 10 + '*'* 10)*5)
        return result

    # возвращается функция inner с новым поведением
    return inner

def add_sep2(f):
    def inner(*args, **kwargs):
        print('-'*100)
        result = f(*args, **kwargs)
        print('-' * 100)
        return result
    return inner


@add_sep2
def my_bill(list):
    print(*list)
