from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
# Реалізуйте зберігання книги контактів з email адресами, телефонами, іменами в базі даних.

Base = declarative_base()
engine = create_engine('sqlite:///HW09.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Name(Base):
    __tablename__ = 'names'
    name_id = Column(Integer, primary_key=True)
    name_n = Column(String(60), nullable=False)
    phones = relationship('Phone', secondary='names_to_all', back_populates='names')
    address = relationship('Address', secondary='names_to_all', back_populates='names')
    emails = relationship('Email', secondary='names_to_all', back_populates='names')


class Phone(Base):
    __tablename__ = 'phones'
    phone_id = Column(Integer, primary_key=True)
    phone_num = Column(String(60), nullable=False)
    names = relationship('Name', secondary='names_to_all', back_populates='phones')


class Address(Base):
    __tablename__ = 'addresses'
    address_id = Column(Integer, primary_key=True)
    address_ad = Column(String(60), nullable=None)
    names = relationship('Name', secondary='names_to_all', back_populates='address')

class Email(Base):
    __tablename__ = 'emails'
    email_id = Column(Integer, primary_key=True)
    email_mail = Column(String(60), nullable=False)
    names = relationship('Name', secondary='names_to_all', back_populates='emails')


class NameAll(Base):
    __tablename__ = 'names_to_all'
    id = Column(Integer, primary_key=True)
    name_id = Column('name_id', ForeignKey('names.name_id'))
    phone_id = Column('phone_id', ForeignKey('phones.phone_id'))
    address_id = Column('address_id', ForeignKey('addresses.address_id'))
    email_id = Column('email_id', ForeignKey('emails.email_id'))


