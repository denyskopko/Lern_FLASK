from sqlalchemy import create_engine, SmallInteger,String, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from pathlib import Path


BASE_DIR = Path(__file__).absolute().parent
engine = create_engine(url=f"sqlite:///{BASE_DIR/'datadb.db'}", echo=True)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, unique=True, nullable=False)


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
print(BASE_DIR)