from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# URL базы данных SQLite
DATABASE_URL = "sqlite:///./todo.db"

# Создание движка базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание фабрики сессий для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()
