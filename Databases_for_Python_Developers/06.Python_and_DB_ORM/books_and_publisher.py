import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), nullable=False)

    def __str__(self):
        return f'Publisher: ID - {self.id}, name - {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="books")

    def __str__(self):
        return f'Book: ID - {self.id}, title - {self.title}, ID publisher - {self.id_publisher}'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), nullable=False)

    def __str__(self):
        return f'Shop: ID - {self.id}, name - {self.name}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer,  nullable=False)

    book = relationship(Book, backref="stock_id")
    shop = relationship(Shop, backref="stock_id")

    def __str__(self):
        return f'Stock: ID - {self.id}, ID book - {self.id_book}, ID shop - {self.id_shop}, quantity - {self.count}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Sale: ID - {self.id}, price - {self.price}, date sale - {self.date_sale}, quantity - {self.count}'
    
def create_db(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def books_by_publisher(session, publisher):
    q = sq.select(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .select_from(Book) \
        .join(Publisher, Publisher.id == Book.id_publisher) \
        .join(Stock, Stock.id_book == Book.id) \
        .join(Shop, Shop.id == Stock.id_shop) \
        .join(Sale, Sale.id_stock == Stock.id)
    if publisher.isdigit():
        q = q.filter(Publisher.id == publisher)
    if publisher.isdigit() == False:
        q = q.filter(Publisher.name == publisher)
    if len(session.execute(q).all()) == 0:
        print('Автор не найден')
    for book in session.execute(q).all():
        print(f'book: {book.title:<40}| shop: {book.name:<10}| price: {book.price:<8}| sale date: {book.date_sale.strftime('%d-%m-%Y')}')
    return



