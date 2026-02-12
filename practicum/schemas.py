from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
"""Создать Pydantic схему для безопасного вывода информации о минералах в API.

ТРЕБОВАНИЯ:
- Валидация всех полей модели Mineral
- Поддержка сериализации из SQLAlchemy объектов
- Готовность к использованию в FastAPI/Flask endpoints

ЦЕЛЬ: Обеспечить типобезопасность и валидацию при передаче данных о минералах."""

class ValidMineral(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
                                )
    id: int = Field()
    name: str = Field(max_length=50)
    color: str = Field(max_length=30)
    hardness : Decimal = Field(ge=0, le=10, decimal_places=2)

mineral = {"id": 1, "name": "Rubin", "color": "red", "hardness": 1.23 }
valid_mineral = ValidMineral.model_validate(mineral)
print(mineral)
