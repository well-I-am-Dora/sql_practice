import pickle
import sqlite3
from typing import Tuple, List, Mapping, Any

import config

ColumnName = str


def execute_query(query: str) -> Tuple[List[tuple], List[ColumnName]]:
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
    print('\t'.join(columns))
    for row in data:
        print('\t'.join([str(i) for i in row]))


def pickle_result(value: Any, filename: str):
    pickled = pickle.dumps(value)
    with open(filename, 'wb') as f:
        f.write(pickled)


def read_pickled(filename: str) -> Any:
    with open(filename, 'rb') as f:
        data = f.read()

    restored = pickle.loads(data)
    return restored


def compare_results(testing_value: List[tuple], original_value: List[tuple]):
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
