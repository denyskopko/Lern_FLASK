from sqlalchemy import Integer, String,Numeric, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from decimal import Decimal
from pathlib import Path


"""ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
Создать модель минерала для системы управления поставками драгоценных камней.

ТРЕБОВАНИЯ:
- Уникальный идентификатор (BigInteger, автоинкремент)
- Название минерала (строка, максимум 50 символов, уникальное)
- Цвет минерала (строка, максимум 30 символов)
- Твердость по шкале Мооса (число с плавающей точкой)

ЦЕЛЬ: Создать основу для каталога минералов, которые будут поставляться в салоны."""

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

class Mineral(Base):
    __tablename__ = 'minerals'
    name : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(30), nullable=False)
    hardness: Mapped[Decimal] = mapped_column(Numeric(4,2), nullable=False)

BASE_DIR = Path(__file__).absolute().parent
engine = create_engine(url=f"sqlite:///{BASE_DIR/'datadb.db'}", echo=True)
Base.metadata.create_all(engine)
