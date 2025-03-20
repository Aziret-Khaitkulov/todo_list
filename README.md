# To-do list

Этот проект представляет собой простое приложение для управления списком задач, которое помогает пользователям эффективно организовывать свои дела.

## Возможности

- Легкое добавление новых задач.
- Удаление ненужных задач.
- Хранение задач в базе данных.
- Просмотр всех задач в чистом и организованном интерфейсе.

## Технологии

    Backend: FastAPI, SQLite
    Frontend: HTML, CSS, JavaScript
    База данных: SQLAlchemy, Pydantic

## Структура проекта

```
todo_list/
├── frontend/
│   ├── index.html       # Основной HTML файл для фронтенда
│   ├── style.css        # Стили для фронтенда
│   └── script.js        # Логика фронтенда
├── database.py          # Настройка базы данных (SQLAlchemy)
├── main.py              # Точка входа для FastAPI
├── models.py            # Модели базы данных
├── routes.py            # Маршруты API
├── schemas.py           # Схемы Pydantic для валидации данных
├── requirements.txt     # Список зависимостей проекта
└── README.md            # Документация проекта
```

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Aziret-Khaitkulov/todo_list.git
```

2. Перейдите в директорию проекта:

```bash
cd todo_list
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Использование

1. Запустите приложение:

```bash
uvicorn main:app --reload
```

2. Откройте браузер и перейдите по адресу `http://localhost:3000`.

## API Эндпоинты

    GET /tasks - Получить список всех задач.
    POST /tasks - Добавить новую задачу.
    PUT /tasks/{task_id} - Обновить задачу (например, отметить как выполненную).
    DELETE /tasks/{task_id} - Удалить задачу.
