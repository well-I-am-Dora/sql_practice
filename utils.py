import pickle
import sqlite3
from typing import Tuple, List, Any

import config

ColumnName = str


def execute_query(query: str) -> Tuple[List[tuple], List[ColumnName]]:
    """
    Выпоняет sql запрос на БД из конфиг файла
    :param query: текст SQL запроса
    :return: результат выполнения запроса и перечень возвращённых колонок
    """
    conn = sqlite3.connect(config.DB_NAME)
    cursor = conn.cursor()
    try:
        results = cursor.execute(query).fetchall()
        cols = cursor.description
    finally:
        cursor.close()
        conn.close()
    return results, [i[0] for i in cols]


def show_query_results(data: List[tuple], columns: List[ColumnName]):
    """
    Выводит результат выполнения запроса  в читаемом формате
    :param data: данные, полученные в результате выполнения SQL запроса
    :param columns: перечень колонок
    """
    print('\t'.join(columns))
    for row in data:
        print('\t'.join([str(i) for i in row]))


def pickle_result(value: Any, filename: str):
    """
    Сохраняет Python объект в файл
    :param value: Python значение
    :param filename: название файла, в который будет помещён объект
    """
    pickled = pickle.dumps(value)
    with open(filename, 'wb') as f:
        f.write(pickled)


def read_pickled(filename: str) -> Any:
    """
    Считывает Python значение из файла
    :param filename: имя файла, содержащего значение
    :return:
    """
    with open(filename, 'rb') as f:
        data = f.read()

    restored = pickle.loads(data)
    return restored


def compare_results(testing_value: List[tuple], original_value: List[tuple]):
    """
    Сравнивает 2 списка по значениям
    :param testing_value: проверяемые значения
    :param original_value: эталонные значения
    :raises ValueError: в случае несовпадения объектов
    """
    if len(testing_value) != len(original_value):
        raise ValueError(
            f'Неверное кол-во значений. Ожидалось получить {len(original_value)}, а получено {len(testing_value)}')
    for value in original_value:
        found = False
        for test in testing_value:
            if test == value:
                found = True
        if not found:
            raise ValueError(f'Не удалось найти  значения {value} в предосталвленных данных')
