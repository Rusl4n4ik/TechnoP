from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
# from fsms import Bulim, Info, Num

DATABASE_NAME = 'bot.sqlite'

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Clients(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_ID_parol = Column(String(50))
    result = Column(String(50))


class Reg(Base):
    __tablename__ = 'Info'
    id = Column(Integer, primary_key=True)
    Bulim = Column(String(50))
    Ism_fam = Column(String(50))
    phone = Column(String(50))


def create_db():
    Base.metadata.create_all(engine)
    session = Session()
    session.commit()


def registr():
    session = Session()
    add = Reg(Bulim=bulim, Info=ism_fam, phone=telefon)
    session.add(add)
    session.commit()
    session.close()


# def users(text, link):
#     session = Session()
#     iduser = Button(user_id=, button_link=link)
#     session.add(add_btn)
#     session.commit()
#     session.close()





if __name__ == '__main__':
    create_db()
