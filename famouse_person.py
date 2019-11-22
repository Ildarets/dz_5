import random
from decorator import add_separators

@add_separators
def get_random_person():
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                 'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                 'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                 'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                 'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}


    list_famous_keys  = []
    for key in FAMOUS_PEOPLE:
       list_famous_keys.append(key)



    sampling = random.choices(list_famous_keys, k=5)


    for i in sampling:
        data_per = input("Когда родился " + i + " :  ")
        if data_per == FAMOUS_PEOPLE.get(i):
            print(" Верно! ")
        else:
            print(" Неверно! ")