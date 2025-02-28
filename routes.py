from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas


# Создание маршрутизатора для обработки запросов
router = APIRouter()


# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Маршрут для получения всех задач
@router.get("/tasks", response_model=list[schemas.TaskResponce])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


# Маршрут для получения задачи по ID
@router.get("/tasks/{task_id}", response_model=schemas.TaskResponce)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


# Маршрут для создания новой задачи
@router.post("/tasks", response_model=schemas.TaskResponce)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Маршрут для обновления существующей задачи
@router.put("/tasks/{task_id}", response_model=schemas.TaskResponce)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    for key, value in task_update.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


# Маршрут для удаления задачи по ID
@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    db.delete(task)
    db.commit()
    return
