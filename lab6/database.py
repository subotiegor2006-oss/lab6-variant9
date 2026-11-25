"""SQLAlchemy: модели и сессия.

Задание повышенной сложности №9.
"""

from sqlalchemy import create_engine, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DATABASE_URL = "sqlite:///./lab6.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


class Student(Base):
    """Модель студента."""

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    group: Mapped[str] = mapped_column(String(20), nullable=False)
    score: Mapped[float] = mapped_column(Float, default=0.0)

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.name!r}, group={self.group!r})"


def init_db() -> None:
    """Создать таблицы."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Генератор сессии для FastAPI Depends."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
