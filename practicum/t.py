"""ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
Создать модель салона для системы управления сетью элитных бутиков.

ТРЕБОВАНИЯ:
- Уникальный идентификатор
- Название салона (строка, максимум 50 символов)
- Местоположение салона (строка, максимум 100 символов)
- Ограничение уникальности: комбинация (название + местоположение) должна быть уникальной

ЦЕЛЬ: Создать систему управления салонами, куда будут доставляться минералы.
ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
Создать комплексную Pydantic схему для вывода информации о салоне с его поставками.

ТРЕБОВАНИЯ:
- Основная информация о салоне (id, название, местоположение)
- Список поставок с краткой информацией (id, дата, пункт назначения)
- Вложенная структура данных для удобства API

ЦЕЛЬ: Предоставить полную информацию о салоне и его поставках в одном запросе."""


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String,Integer, UniqueConstraint
from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class Supplies(BaseModel):
    """id, дата, пункт назначения"""
    id: int = Field()
    date: date = Field()
    destination: str = Field(max_length=100)
    model_config = ConfigDict(from_attributes=True)


class ValidSalon (BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id : int = Field()
    name: str = Field(max_length=50)
    location: str = Field(max_length=100)
    supplies: list[Supplies] = Field()


class Base(DeclarativeBase):
    pass


class Salon(Base):
    __tablename__ = 'salons'
    id : Mapped[int]= mapped_column(Integer, primary_key=True)
    name : Mapped[str]= mapped_column(String(50))
    location: Mapped[str]= mapped_column(String(100))

    __table_args__ = (
        UniqueConstraint("name", "location")
    )





