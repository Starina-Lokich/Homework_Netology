import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import books_and_publisher as bap


DSN = 'postgresql://postgres:090499@localhost:5432/netology_db'
engine = sq.create_engine(DSN)
bap.create_db(engine)

Session = sessionmaker(bind=engine)
session = Session()


publisher_1 = bap.Publisher(name='Акунин')
publisher_2 = bap.Publisher(name='Тургенев')
publisher_3 = bap.Publisher(name='Гоголь')
publisher_4 = bap.Publisher(name='Лермонтов')
session.add_all([publisher_1, publisher_2, publisher_3, publisher_4])
session.commit()

book_1 = bap.Book(title='Азазель', id_publisher=1)
book_2 = bap.Book(title='Турецкий Гамбит', id_publisher=1)
book_3 = bap.Book(title='Левиафан', id_publisher=1)
book_4 = bap.Book(title='Отцы и дети', id_publisher=2)
book_5 = bap.Book(title='Муму', id_publisher=2)
book_6 = bap.Book(title='Ася', id_publisher=2)
book_7 = bap.Book(title='Мёртвые души', id_publisher=3)
book_8 = bap.Book(title='Тарас Бульба', id_publisher=3)
book_9 = bap.Book(title='Портрет', id_publisher=3)
book_10 = bap.Book(title='Герой нашего времени', id_publisher=4)
book_11 = bap.Book(title='Демон', id_publisher=4)
book_12 = bap.Book(title='Мцыри', id_publisher=4)
session.add_all([book_1, book_2, book_3, book_4,
                 book_5, book_6, book_7, book_8,
                 book_9, book_10, book_11, book_12])
session.commit()

shop_1 = bap.Shop(name='Читай город')
shop_2 = bap.Shop(name='Литрес')
shop_3 = bap.Shop(name='Теремок')
session.add_all([shop_1, shop_2, shop_3])
session.commit()

stock_1 = bap.Stock(id_book=1, id_shop=1, count=2)
stock_2 = bap.Stock(id_book=2, id_shop=1, count=3)
stock_3 = bap.Stock(id_book=3, id_shop=1, count=10)
stock_4 = bap.Stock(id_book=4, id_shop=1, count=5)
stock_5 = bap.Stock(id_book=5, id_shop=2, count=20)
stock_6 = bap.Stock(id_book=6, id_shop=2, count=13)
stock_7 = bap.Stock(id_book=6, id_shop=2, count=10)
stock_8 = bap.Stock(id_book=8, id_shop=2, count=8)
stock_9 = bap.Stock(id_book=9, id_shop=3, count=15)
stock_10 = bap.Stock(id_book=10, id_shop=3, count=11)
stock_11 = bap.Stock(id_book=11, id_shop=3, count=19)
stock_12 = bap.Stock(id_book=12, id_shop=3, count=2)
session.add_all([stock_1, stock_2, stock_3, stock_4,
                 stock_5, stock_6, stock_7, stock_8,
                 stock_9, stock_10, stock_11, stock_12])
session.commit()

sale_1 = bap.Sale(price=500, date_sale='2022-05-17', id_stock=1, count=1)
sale_2 = bap.Sale(price=900, date_sale='2022-12-30', id_stock=5, count=7)
sale_3 = bap.Sale(price=700, date_sale='2022-01-07', id_stock=9, count=3)
sale_4 = bap.Sale(price=400, date_sale='2022-03-13', id_stock=12, count=1)
sale_5 = bap.Sale(price=356, date_sale='2022-08-19', id_stock=10, count=5)
sale_6 = bap.Sale(price=468, date_sale='2022-11-01', id_stock=8, count=4)
sale_7 = bap.Sale(price=965, date_sale='2022-04-17', id_stock=6, count=11)
sale_8 = bap.Sale(price=368, date_sale='2022-05-23', id_stock=3, count=2)
sale_9 = bap.Sale(price=875, date_sale='2022-10-03', id_stock=2, count=2)
session.add_all([sale_1, sale_2, sale_3, 
                 sale_4, sale_5, sale_6, 
                 sale_7, sale_8, sale_9])
session.commit()


if __name__ == '__main__':
    publisher = input('Введите имя или ID писателя, по которому хотите осуществить поиск: ') #Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    bap.books_by_publisher(session, publisher) #Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше    

session.close()