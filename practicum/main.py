

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer

class Base(DeclarativeBase):
    __abstract__ = True
    id: mapped_column[int] = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)

