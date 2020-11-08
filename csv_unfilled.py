from typing import List
import csv


def get_california_s_cities(filename: str = './cities.csv') -> List[str]:
    """
    Петя отлынивал от работы последнюю недели и любовался котиками, вместо работы.
    Но завтра у Пети намечен важный аналитический отчёт.

    Помогите Пете извлечь нужные данные, реализовав данную функцию.
    В cities.csv лежит информация о городах америки.
    Необходимо получить список городов штата калифорния, начинающихся на букву 'S'
    в шатете калифорния ('CA').


    **Реализация должна обязательно использовать модуль csv**

    :param filename: название файла, в котором находится список городов
    :return: Список городов штата калифорния, начинающихся с буквы 'S'
    """
    with open(filename, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        cities = list(map(lambda c: c[''' "City"'''].strip().strip('"'),
                          list(filter(lambda s: s[''' "City"'''].strip().strip('"').startswith('S')
                                       and s[''' "State"'''].strip() == 'CA', list(reader)))))
    return cities
