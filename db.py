from aiogram.types import User
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import text
# from fsms import Bulim, Info, Num
import sqlalchemy
import sqlite3

DATABASE_NAME = 'bot.sqlite'

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Clients(Base):
    __tablename__ = 'Natijalar'
    user_ID_parol = Column(String(50), primary_key=True)
    result = Column(String(50))


class Users(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    first_name = Column(String(100), nullable=True)
    username = Column(String(50), nullable=True)


class Feedbacks(Base):
    __tablename__ = 'Fikr Mulohoza'
    id = Column(Integer, primary_key=True)
    fikr_mulohoza = Column(String(50))


class Reg(Base):
    __tablename__ = 'Qabul'
    id = Column(Integer, primary_key=True)
    Bulim = Column(String(50))
    Ism_fam = Column(String(50))
    phone = Column(String(50))


def create_db():
    Base.metadata.create_all(engine)
    session = Session()
    session.commit()


def registration(bulim, ism_fam, telefon):
    session = Session()
    add = Reg(Bulim=bulim, Ism_fam=ism_fam, phone=telefon)
    session.add(add)
    session.commit()
    session.close()


def add_user(id, first_name, username):
    session = Session()
    exist = check_existing(id)
    if not exist:
        user = Users(chat_id=id,
                       first_name=first_name,
                       username=username)
        session.add(user)
    session.commit()
    session.close()


def check_existing(id):
    session = Session()
    result = session.query(Users.chat_id).filter(Users.chat_id == id).all()
    return result


def feedbck(ftxt):
    session = Session()
    fikr = Feedbacks(fikr_mulohoza=ftxt)
    session.add(fikr)
    session.commit()
    session.close()


def get_result(res):
    session = Session()
    return session.query(Clients).get(res)


def add_result(add_id, add_res):
    session = Session()
    add_result = Clients(user_ID_parol = add_id, result = add_res)
    session.add(add_result)
    session.commit()
    session.close()


# def get_result(self, user_id, parol, within="all"):
#     session = Session()
#     search_user = []
#     if user_id:
#         search_user.append(Clients.user_ID.like(user_id))
#     if parol:
#         search_user.append(Clients.parol.like(parol))
#     where = sqlalchemy.and_(*search_user)
#     query = session.query(Clients).filter(where)
#     pwd = sorted(list(frozenset([x.result for x in query.all()])))
#     session.close()
#     return pwd


# def get_result(user_ID, parol):
#     session = Session()
#     search_user = []
#     userid = sqlalchemy.and_(*search_user)
#     query = session.query(Clients).filter(userid)
#     pwd = sorted(list(frozenset([x.result for x in query.all()])))
#     session.close()
#     return pwd

# def get_result(id):
#     session = Session()
#     result = session.query(Clients).filter(Clients.user_ID.like(id)).all()
#     session.close()
#     return result
#

# def get_result(id):
#     session = Session()
#     result = session.query(Clients.user_ID).filter(Clients.user_ID == id).all()
#     return result


# try:
#     sqlite_connection = sqlite3.connect('bot.sqlite')
#     cursor = sqlite_connection.cursor()
#     print("Подключение к SQLite")
#
#     sqlite_insert_query = """INSERT INTO Natijalar
#                           (user_ID_parol, result)
#                           VALUES
#                           ('12575 AZSN42','Инсульт');"""
#     count = cursor.execute(sqlite_insert_query)
#     sqlite_connection.commit()
#     print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Ошибка при работе с SQLite", error)
# finally:
#     if sqlite_connection:
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")


# def users(text, link):
#     session = Session()
#     iduser = Button(user_id=, button_link=link)
#     session.add(add_btn)
#     session.commit()
#     session.close()


if __name__ == '__main__':
    create_db()
