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


def creat_db_struct(conn):
    '''
    Метод, создающий структуру БД (таблицы).
    '''
    with conn.cursor() as cur:
     # таблица "Клиент" (id, фамилия, имя, почта)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS client(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(40) NOT NULL,
                    last_name VARCHAR(40) NOT NULL,
                    email VARCHAR(40) NOT NULL
                    );
                    """)
        # таблица "Телефоны" (id, номер телефона, связь с клиентом по id)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    number VARCHAR(20) UNIQUE,
                    client_id INTEGER NOT NULL REFERENCES client(id)
                    )
                    """)
        conn.commit()
        print('Структура БД создана')

