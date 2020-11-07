from utils import show_query_results, execute_query

if __name__ == '__main__':
    # Здесь вы можете попробовать ваш запрос
    QUERY = 'SELECT * FROM customers'
    results, columns = execute_query(QUERY)
    show_query_results(results, columns)
