"""Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
Задача 3: Определите модель продукта Product со следующими типами колонок:
id: числовой идентификатор
name: строка (макс. 100 символов)
price: числовое значение с фиксированной точностью
in_stock: логическое значение
Задача 4: Определите связанную модель категории Category со следующими типами колонок:
id: числовой идентификатор
name: строка (макс. 100 символов)
description: строка (макс. 255 символов)
Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id."""

from sqlalchemy import create_engine, SmallInteger, String, Numeric,Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine(url="sqlite:///:memory:", echo=True)

class Base(DeclarativeBase):
    ...

class Product(Base):
    __tablename__ = "products"
    product_id : Mapped[int] = mapped_column(SmallInteger, primary_key=True, unique=True, nullable=False)
    name : Mapped[str] = mapped_column(String(100), nullable=False)
    prise: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    in_stock: Mapped[bool] = mapped_column(Boolean, nullable=False)
    category_id:   Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products")

class Category(Base):
    __tablename__ = "categories"
    id : Mapped[int] = mapped_column(SmallInteger, primary_key=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    products: Mapped[list[Product]] = relationship(back_populates="category")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

