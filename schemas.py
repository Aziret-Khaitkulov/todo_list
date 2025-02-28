from pydantic import BaseModel


# Базовая схема задачи, содержащая общие поля
class TaskBase(BaseModel):
    title: str
    description: str | None = None


# Схема для создания новой задачи, наследует TaskBase
class TaskCreate(TaskBase):
    pass


# Схема для обновления существующей задачи, добавляет поле completed
class TaskUpdate(TaskBase):
    completed: bool


# Схема для ответа с информацией о задаче, добавляет поля id и completed
class TaskResponce(TaskBase):
    id: int
    completed: bool

    # Конфигурация для использования атрибутов модели
    class Config:
        from_attributes = True
