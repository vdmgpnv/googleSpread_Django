from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float, DateTime
"""Модуль с образами для базы данных"""
from sqlalchemy.ext.declarative import declarative_base
import schedule
from sqlalchemy.orm import sessionmaker
from get_data import WorkWithData
from config import DATABASE_URI
from bot import Bot

Base = declarative_base()

def db_connect(db_path):
    '''Подключение к БД'''
    try:
        engine = create_engine(db_path)
    except:
        print('ErrorConnection')
    return engine

metadata = MetaData(bind=db_connect(DATABASE_URI))


class Order(Base):  
    '''Образ таблицы'''
    __tablename__ = 'get_data_order'
    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)
    price_in_USD = Column(Float)
    delivery_date = Column(DateTime)
    price_in_RUB = Column(Float)
       

Session = sessionmaker(bind=db_connect(DATABASE_URI))


def insert_data(data, exchange_rate, bot):
    '''Метод проверяет, прошел ли срок заказа(с отправлением сообщения в ТG), существует ли такой заказ,
    и если да, то обноляет его, иначе, создает новый'''
    with Session() as session:
        for r in data:
            if datetime.strptime(r[3], '%d.%m.%Y') > datetime.now():
                bot.send_message(f'Срок доставки по заказу {r[1]} истек')
            r[2]= int(r[2])
            order = session.query(Order).filter(Order.order_number==r[1])
            if order.count() > 0:
                order.price_in_USD = r[2]
                order.delivery_date = r[3]
                order.price_in_RUB = r[2]*float(exchange_rate)
                session.commit()
            else:
                row = Order(
                order_number = r[1],
                price_in_USD = r[2],
                delivery_date = r[3],
                price_in_RUB = r[2]*float(exchange_rate)
                )
                session.add(row)
                session.commit()
    

def get_data(data_class):
    bot = Bot()
    spread_data = data_class.get_data_from_sheet()
    exchange_rate = data_class.get_exchange_rate()
    insert_data(spread_data, exchange_rate.replace(',', '.'), bot)


def main():
    '''Каждые 30 секунд данные обновляются и проверяются в таблице'''
    data_class = WorkWithData()
    schedule.every().hour.do(get_data, data_class=data_class) 
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()