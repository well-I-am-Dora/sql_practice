from typing import Callable

from unfilled_functions import *
import utils
import pytest

functions = [example, get_all_phone_numbers, get_all_clients_from_e, get_hired_after_2003, get_customers_with_job,
             get_biggest_album, get_success_artists, get_biggest_orders, get_first_half_year_employees_birth_date,
             get_most_popular_support_employee, get_most_buying_tracks, get_biggest_playlist, get_artist_presentation]


@pytest.mark.parametrize('function', functions)
def test_sql_queries(function: Callable):
    """
    Проверка SQL запроса на корректность
    :param function: функция, возвращаюшая SQL запрос
    """
    filename = f'./results/{function.__name__}'
    orig_values = utils.read_pickled(filename)

    query = function()
    if type(query) != str:
        pytest.fail(f'Ваша функция {function.__name__} должна возвращать SQL запрос в виде строки')
    if 'select' not in query.lower():
        pytest.fail(f'Запрос функции {function.__name__} должна быть SELECT запросом, но вместо это там "{query}"')

    try:
        results, columns = utils.execute_query(query)
    except Exception as e:
        pytest.fail(f'Непредвиденная ошибка во время выполнения запроса функции {function.__name__} '
                    f'! Получена ошибка: "{e}"')
        return

    try:
        utils.compare_results(results, orig_values)
    except ValueError as e:
        pytest.fail(f'Неверный ответ для функции {function.__name__} ! {e}')
    except Exception as e:
        pytest.fail(f'Непредвиденная ошибка во время проверки результата функции {function.__name__}')
