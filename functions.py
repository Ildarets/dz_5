
def hello_who(name):
    """
    :param name: имя
    :return: строка приветствия
    """
    return f'Hello, {name}'


def salary(hours, salary_by_hour):
    """
    рассчет зп сотрудника
    :param hours: кол-во часов
    :param salary_by_hour: зарплата за час
    :return: итоговая стоимость
    """
    k = 2
    return hours * salary_by_hour * k