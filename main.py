from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import engine, Base
import routes

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Инициализация приложения FastAPI
app = FastAPI()

# Подключение маршрутов из модуля routes
app.include_router(routes.router)

# Подключение статических файлов
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
