from fastapi import HTTPException

from app.repository.task_repository import TaskRepository
from app.entity.task import Task, TaskModel


class TaskService:
    task_repository = TaskRepository()

    def find_all(self) -> list[Task]:
        return self.task_repository.find_all()

    def find_by_id(self, id: int) -> Task:
        if not self.task_repository.exists_by_id(id):
            raise HTTPException(status_code=404, detail="Task not found")
        return self.task_repository.find_by_id(id)

    def update(self, id: int, task: TaskModel):
        if not self.task_repository.exists_by_id(id):
            raise HTTPException(status_code=404, detail="Task not found")
        return self.task_repository.update(id, task)

    def create(self, task: TaskModel):
        return self.task_repository.create(task)

    def delete(self, id: int):
        if not self.task_repository.exists_by_id(id):
            raise HTTPException(status_code=404, detail="Task not found")
        self.task_repository.delete(self, id)
