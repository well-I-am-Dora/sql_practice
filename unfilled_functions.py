"""
Вася занимается поддержкой веб сайта по продаже музыкальных произведений.
Всё шло хорошо, но в один день у них сломался сервер и Вася потерял все данные на сервере.
Какие-то данные и код веб сайта восстановить удалось, но вот файл, отвечающий за SQL запросы был безнадёжно утерян.
Сам вася системный администратор и SQL напрочь не знает. Помогите Васе снова запустить сайт !

Напишите SQL запросы, выполняющие требуемую задачу (они описаны в документации каждой функции)
Обратите внимание, что у каждого запроса описан *список* и *порядок* полей, которые необходимо извлечь.
"""


def example():
    """
    Получить самого первого клиента, добавленного в систему
    (имя)

    :return: запрос, выполняющий требования
    """
    return 'SELECT FirstName FROM customers as c ORDER BY c.CustomerId LIMIT 1'


def get_all_phone_numbers() -> str:
    """
    Получить все мобильные номера покупателей
    (имя,фамилия,номер телефона)

    :return: запрос, выполняющий требования
    """
    return 'SELECT FirstName, LastName, Phone FROM customers'


def get_all_clients_from_e() -> str:
    """
    Все клиенты, чьё имя начинается с буквы E (английской)
    (имя,фамилия)

    :return: запрос, выполняющий требования
    """
    return "SELECT FirstName, LastName FROM customers WHERE FirstName LIKE 'E%'"


def get_hired_after_2003() -> str:
    """
    все сотрудники, нанятые после (включительно) 2003 года
    (Имя, Фамилия сотрудника, дата рождения, дата трудоустройства)

    :return: запрос, выполняющий требования
    """
    return 'SELECT FirstName, LastName, BirthDate, HireDate FROM employees WHERE YEAR(HireDate) >= 2003'


def get_customers_with_job() -> str:
    """
    Все покупатели, являющиеся сотрудниками компаний (любой компании, если это указано в их профиле)
    (Имя,Фамилия,Название компании)

    :return: запрос, выполняющий требования
    """
    return 'SELECT FirstName, LastName, Company FROM customers WHERE Company NOT IS NULL'


def get_biggest_album() -> str:
    """
    самый большой по кол-ву треков альбом и кол-во этих треков
    (id,название альбома, кол-во песен)

    :return: запрос, выполняющий требования
    """
    return 'SELECT albums."AlbumId", albums."Title", COUNT(tracks."TrackId")' \
           ' as c from albums join tracks on albums."AlbumId" = tracks."AlbumId"' \
           ' group by albums."AlbumId" order by c desc limit 1'


def get_success_artists() -> str:
    """
    Получить всех исполнителей, имеющих более 3 треков
    (Название исполнителя, кол-во треков)

    :return: запрос, выполняющий требования
    """
    return 'select artists."Name", count(tracks."TrackId") as trackcount' \
           ' from artists join albums on artists."ArtistId"=albums."ArtistId"' \
           ' join tracks on tracks."AlbumId"=albums."AlbumId" group by artists."Name"' \
           ' having count(tracks."TrackId") > 3'


def get_biggest_orders() -> str:
    """
    топ 10 самых крупных заказов (по стоимости)
    (Имя, фамилия покупателя, стоимость заказа, дата покупки)

    :return: запрос, выполняющий требования
    """
    return 'select "FirstName", "LastName", "Total", "InvoiceDate" ' \
           'from customers join invoices on customers."CustomerId" = invoices."CustomerId" ' \
           'order by "Total" desc limit 10'


def get_first_half_year_employees_birth_date() -> str:
    """
    Дни рождения сотрудников первого полугодия (с 1 по 6 месяцы включительно)
    (Имя,Фамилия,Дата рождения)

    :return: запрос, выполняющий требования
    """
    return 'SELECT FirstName, LastName, BirthDate FROM employees WHERE MONTH(BirthDate) BETWEEN 1 AND 6'


def get_most_popular_support_employee() -> str:
    """
    Самый популярный сотрудник службы поддержки
    (имя, фамилия, кол-во назначений на поддержку пользователя)

    :return: запрос, выполняющий требования
    """
    return 'select employees."FirstName", employees."LastName", count(employees."EmployeeId") ' \
           'from employees join customers on employees."EmployeeId" = customers."SupportRepId" ' \
           'group by employees."EmployeeId" ' \
           'order by count(employees."EmployeeId") desc limit 1'


def get_most_buying_tracks() -> str:
    """
    Топ 10 самых популярных треков (если есть несоклько треков с одниковым кол-вом покупок, то сортировать по имени)
    (по покупаемости, КОЛ-ВО в заказе НЕ УЧИТЫВАТЬ)

    (название трека, кол-во покупок)

    :return: запрос, выполняющий требования
    """
    return 'select tracks."Name", count(invoice_items."InvoiceId") as ct ' \
           'from tracks join invoice_items on tracks."TrackId" = invoice_items."TrackId" ' \
           'group by tracks."Name" ' \
           'order by ct desc, "Name" limit 10'


def get_biggest_playlist() -> str:
    """
    Самый крупный плейлист по кол-ву треков
    (название плейлиста, кол-во треков)

    :return: запрос, выполняющий требования
    """
    return 'select name, count(*)  as cnt from playlists ' \
           'join playlist_track on playlists."PlaylistId" = playlist_track."PlaylistId" ' \
           'group by "Name" ' \
           'order by cnt desc ' \
           'limit 1'


def get_artist_presentation() -> str:
    """
    Получить по 1 треку на каждого исполнителя (при наличии нескольких треков, брать самый длительный)
    (название исполнителя, название трека, длительность (в секундах))

    :return: запрос, выполняющий требования
    """
    return 'select artists."name" as artist, tracks."Name" as track, max(tracks."Milliseconds" / 1000) as duration ' \
           'from tracks join albums on tracks."AlbumId" = albums."AlbumId" ' \
           'join artists on albums."ArtistId" = artists."ArtistId" ' \
           'group by artists."Name"'
