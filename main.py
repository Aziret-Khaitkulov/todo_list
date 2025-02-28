from fastapi import FastAPI
from database import engine, Base
import routes

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Инициализация приложения FastAPI
app = FastAPI()

# Подключение маршрутов из модуля routes
app.include_router(routes.router)
