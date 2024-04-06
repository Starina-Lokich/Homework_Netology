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


def add_new_client(conn, first_name, last_name, email, phones=[None]):
    '''
    Метод, позволяющий добавить нового клиента.
    '''
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO client (first_name, last_name, email)
                    VALUES (%s, %s, %s);
                    """, (first_name, last_name, email))
        if phones is not None:
            cur.execute('''
                        SELECT id FROM client 
                        WHERE first_name=%s AND last_name=%s AND email=%s;
                        ''', (first_name, last_name, email))
            client_id = cur.fetchone()[0]
            print(client_id)
            add_phones(conn, client_id, phones)
        conn.commit()
        print('Клиент в базу данных добавлен')


def add_phones(conn, client_id, phones):
    '''
    Метод, позволяющий добавить телефон для существующего клиента.
    '''
    for phone in phones:
        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO phones(client_id, number)
                        VALUES(%s, %s);
                        ''', (client_id, phone))
            conn.commit()
    print('Номер добавлен')


def change_client(conn, client_id, first_name=None, last_name=None, email=None, old_number=None, new_number=None):
    '''
    Метод, позволяющий изменить данные о клиенте
    '''
    with conn.cursor() as cur:
        cur.execute('''
                    SELECT * from client
                    WHERE id = %s
                    ''', (client_id,))
        temp = cur.fetchone()
        if first_name is None:
            first_name = temp[1]
        if last_name is None:
            last_name = temp[2]
        if email is None:
            email = temp[3]
        if old_number and new_number:
            cur.execute('''
                        UPDATE phones SET number = %s 
                        WHERE number = %s
                        ''', (new_number, old_number))
            conn.commit()

        cur.execute('''
                    UPDATE client SET first_name = %s, last_name = %s, email =%s
                    WHERE id = %s
                    ''', (first_name, last_name, email, client_id))
        cur.execute('''
                    SELECT * from client
                    WHERE id = %s
                    ''', (client_id,))
        conn.commit()
        print('Данные о клиенте изменены')


def delete_phone(conn, client_id, phones):
    '''
    Метод, позволяющий удалить телефон(ы) для существующего клиента.
    '''
    for number in phones:
        with conn.cursor() as cur:
            cur.execute('''
                        DELETE FROM phones
                        WHERE number = %s and client_id = %s
                        ''', (number, client_id))
            conn.commit()
            print(f'Номер телефона "{number}" удален')


def delete_client(conn, client_id):
    '''
    Метод, позволяющий удалить существующего клиента.
    '''
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM phones WHERE client_id=%s;
                    DELETE FROM client WHERE id=%s;
                    ''',(client_id, client_id))
        conn.commit()
    print('Данные о клиенте удалены')


