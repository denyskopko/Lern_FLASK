"""Разработать систему регистрации пользователя, используя Pydantic для валидации входных данных,
обработки вложенных структур и сериализации. Система должна обрабатывать данные в формате JSON.
Задачи:
Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.
Реализовать функцию, которая принимает JSON строку, десериализует её в объекты Pydantic,
валидирует данные, и в случае успеха сериализует объект обратно в JSON и возвращает его.
Добавить кастомный валидатор для проверки соответствия возраста и статуса занятости пользователя.
Написать несколько примеров JSON строк для проверки различных сценариев валидации: успешные регистрации и случаи,
когда валидация не проходит (например возраст не соответствует статусу занятости).
Модели:
Address: Должен содержать следующие поля:
city: строка, минимум 2 символа.
street: строка, минимум 3 символа.
house_number: число, должно быть положительным.

User: Должен содержать следующие поля:
name: строка, должна быть только из букв, минимум 2 символа.
age: число, должно быть между 0 и 120.
email: строка, должна соответствовать формату email.
is_employed: булево значение, статус занятости пользователя.
address: вложенная модель адреса.

Валидация:
Проверка, что если пользователь указывает, что он занят (is_employed = true), его возраст должен быть от 18 до 65 лет.
#Пример JSON данных для регистрации пользователя
json_input = {
    "name": "John Doe",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

from pydantic import BaseModel, EmailStr, model_validator, Field, ValidationError

class Address(BaseModel):
    city: str = Field(min_length = 2 )
    street: str = Field(min_length = 3)
    house_number: int = Field(gt = 0)

class User(BaseModel):
    name: str = Field()
    age: int = Field(gt= 0 , le = 120)
    email: EmailStr = Field()
    is_employed: bool = Field(default = True)
    address: Address = Field()

    @model_validator(mode="after")
    def check_is_employed(self):
        if self.is_employed and not (  18 <= self.age <= 65):
            raise ValidationError("Если is_employed = True, возраст должен быть в диапазоне от 18 до 65 ")
        else:
            return self


json_input = """{
    "name": "John Doe",
    "age": 21,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""



new_user = User.model_validate_json(json_input)
print(new_user)


def validation_json(json : str)->str:
    try:
        user = User.model_validate_json(json)
        return_json = user.model_dump_json()
        return return_json
    except ValidationError as e:
        print(e)
        return "Не валидные значения полей"



json_test = """{
    "name": "Denys Kopko",
    "age": 28,
    "email": "kopko.denis23@gmail.com",
    "is_employed": true,
    "address": {
        "city": "Bielefeld",
        "street": "my street",
        "house_number": 12
    }
}"""

print(validation_json(json_test))







