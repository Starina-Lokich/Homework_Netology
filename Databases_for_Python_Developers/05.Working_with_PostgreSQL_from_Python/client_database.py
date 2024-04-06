import psycopg2


def drop_db(conn):
    '''
    Метод, удаляющая БД (таблицы)
    '''
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE phones;
            DROP TABLE client;
        """)

