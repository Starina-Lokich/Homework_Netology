import client_database as cd
import psycopg2


with psycopg2.connect(database='name_db', user='name_user', password='password') as conn:
    cd.drop_db(conn)
    cd.creat_db_struct(conn)
    # Добавим 5 клиентов:
    cd.add_new_client(conn, "Иван", "Иванов", "ivan@mail.ru")
    cd.add_new_client(conn, "Петр", "Петров", "piter@mail.ru", ["1111111111", "999999999"])
    cd.add_new_client(conn, "Анна", "Василькова", "anvas@mail.ru")
    cd.add_new_client(conn, "Ирина", "Петрова", "irina@mail.ru", ["666665555555"])
    cd.add_new_client(conn, "Кирилл", "Вильи", "vilivili@mail.ru", ["222222222"])
    cd.fetchall_db(conn)

    # Добавим номера клиентам 1 и 3:
    cd.add_phones(conn, 1, ["88888888888"])
    cd.add_phones(conn, 3, ["33333333333"])
    cd.add_phones(conn, 3, ["44444444444"])
    cd.fetchall_db(conn)

    # Изменим данных клиентов 1 - 5:
    cd.change_client(conn, 2, first_name="АЗАЗЕЛЬ")
    cd.change_client(conn, 1, last_name="ЖУЛИДИН")
    cd.change_client(conn, 3, email="kvakva@yandex.ru")
    cd.change_client(conn, 4, old_number="89990002525", new_number="77777777")
    cd.change_client(conn, 5, "ОЛЕГ", "НЕЕЛОВ", "OLEGNEEV@mail.ru", old_number="222222222", new_number="66666666666")


    # Удаление конкретного номера телефона у 3 клиента и попытка удалить несуществующий номер:
    cd.delete_phone(conn, 3, ["33333333333"])
    cd.delete_phone(conn, 7, ["9393"])
    cd.fetchall_db(conn)

    # Поиск клиентов по имени, фамилии, почте и номеру телефона, поиск несуществующего клиента:
    cd.find_client(conn, first_name="Ирина")
    cd.find_client(conn, last_name="Василькова")
    cd.find_client(conn, email="piter@mail.ru")
    cd.find_client(conn, number="89998887766")
    cd.find_client(conn, first_name="Миша")

    # Удаление 1 и 5 клиентов:
    cd.delete_client(conn, 5)
    cd.delete_client(conn, 1)
    cd.fetchall_db(conn)

conn.close()
