# coding: utf-8
# flake8: noqa
from . import *  # noqa


from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Index, LargeBinary, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMINT, SET, TINYINT, VARCHAR, YEAR
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

from core.models._base import BaseModel
# Base = declarative_base()
Base = BaseModel
metadata = Base.metadata


class Actor(Base):
    __tablename__ = 'actor'

    id = Column(BIGINT(20), primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Address(BaseModel):
    __tablename__ = 'address'

    id = Column(BIGINT(20), primary_key=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50))
    district = Column(String(20), nullable=False)
    city_id = Column(BIGINT(20), nullable=False, index=True)
    postal_code = Column(String(10))
    phone = Column(String(20), nullable=False)
    location = Column(NullType, nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Category(Base):
    __tablename__ = 'category'

    id = Column(TINYINT(3), primary_key=True)
    name = Column(String(25), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class City(Base):
    __tablename__ = 'city'

    id = Column(BIGINT(20), primary_key=True)
    city = Column(String(50), nullable=False)
    country_id = Column(BIGINT(20), nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Country(Base):
    __tablename__ = 'country'

    id = Column(BIGINT(20), primary_key=True)
    country = Column(String(50), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(BIGINT(20), primary_key=True)
    store_id = Column(TINYINT(3), nullable=False, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    email = Column(String(50))
    address_id = Column(BIGINT(20), nullable=False, index=True)
    active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Film(Base):
    __tablename__ = 'film'

    id = Column(BIGINT(20), primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    release_year = Column(YEAR(4))
    language_id = Column(TINYINT(3), nullable=False, index=True)
    original_language_id = Column(TINYINT(3), index=True)
    rental_duration = Column(TINYINT(3), nullable=False, server_default=text("'3'"))
    rental_rate = Column(DECIMAL(4, 2), nullable=False, server_default=text("'4.99'"))
    length = Column(BIGINT(20))
    replacement_cost = Column(DECIMAL(5, 2), nullable=False, server_default=text("'19.99'"))
    rating = Column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17'), server_default=text("'G'"))
    special_features = Column(SET('Trailers', 'Commentaries', 'Deleted Scenes', 'Behind the Scenes'))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class FilmActor(Base):
    __tablename__ = 'film_actor'

    id = Column(BIGINT(20), primary_key=True)
    actor_id = Column(BIGINT(20), nullable=False)
    film_id = Column(BIGINT(20), nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class FilmCategory(Base):
    __tablename__ = 'film_category'

    id = Column(BIGINT(20), primary_key=True)
    category_id = Column(TINYINT(3), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class FilmText(Base):
    __tablename__ = 'film_text'
    __table_args__ = (
        Index('idx_title_description', 'title', 'description'),
    )

    id = Column(BIGINT(20), primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)


class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        Index('idx_store_id_film_id', 'store_id', 'film_id'),
    )

    id = Column(BIGINT(20), primary_key=True)
    film_id = Column(BIGINT(20), nullable=False, index=True)
    store_id = Column(TINYINT(3), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Language(Base):
    __tablename__ = 'language'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(CHAR(20), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(BIGINT(20), primary_key=True)
    customer_id = Column(BIGINT(20), nullable=False, index=True)
    staff_id = Column(TINYINT(3), nullable=False, index=True)
    rental_id = Column(INTEGER(11))
    amount = Column(DECIMAL(5, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Rental(Base):
    __tablename__ = 'rental'
    __table_args__ = (
        Index('rental_date', 'rental_date', 'inventory_id', 'customer_id', unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    rental_date = Column(DateTime, nullable=False)
    inventory_id = Column(MEDIUMINT(8), nullable=False, index=True)
    customer_id = Column(BIGINT(20), nullable=False, index=True)
    return_date = Column(DateTime)
    staff_id = Column(TINYINT(3), nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(BIGINT(20), primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column(BIGINT(20), nullable=False, index=True)
    picture = Column(LargeBinary)
    email = Column(String(50))
    store_id = Column(TINYINT(3), nullable=False, index=True)
    active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    username = Column(String(16), nullable=False)
    password = Column(VARCHAR(40))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Store(Base):
    __tablename__ = 'store'

    id = Column(BIGINT(20), primary_key=True)
    manager_staff_id = Column(TINYINT(3), nullable=False, unique=True)
    address_id = Column(BIGINT(20), nullable=False, index=True)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
