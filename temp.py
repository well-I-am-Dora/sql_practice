import traceback

from utils import show_query_results, execute_query, pickle_result, compare_results, read_pickled

from unfilled_functions import *

functions = [example, get_all_phone_numbers, get_all_clients_from_e, get_hired_after_2003, get_customers_with_job,
             get_biggest_album, get_success_artists, get_biggest_orders, get_first_half_year_employees_birth_date,
             get_most_popular_support_employee, get_most_buying_tracks, get_biggest_playlist, get_artist_presentation]


if __name__ == '__main__':
    for function in functions:
        try:
            path = f'./results/{function.__name__}'

            results, columns = execute_query(function())
            show_query_results(results, columns)

            pickle_result(results, path)
            restored = read_pickled(path)

            compare_results(results, restored)
        except Exception as e:
            print(function.__name__,e)
            print(traceback.format_exc())
            raise e
