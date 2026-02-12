from sqlalchemy import Table, Column, BigInteger, String, SmallInteger
from sqlalchemy.orm import registry

REGISTRY = registry()

users_table = Table('users',REGISTRY.metadata,
Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String(30)),
    Column('age', SmallInteger))


class User:
    def __init__(self, name:str, age:int|None=None):
        self.name = name
        self.age = age


REGISTRY.map_imperatively(User, users_table)


