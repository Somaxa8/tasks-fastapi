from app.entity.database import session
from app.entity.task import Task, TaskModel


class TaskRepository:

    def create(self, task: TaskModel):
        new_task = Task(**task.dict())
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task

    def update(self, id: int, task: TaskModel):
        updated_task = session.query(Task).filter(Task.id == id).first()
        session.query(Task).filter(Task.id == id).update(task.dict(exclude_unset=True))
        session.commit()
        session.refresh(updated_task)
        return updated_task

    def delete(self, id: int):
        session.query(Task).filter_by(id).delete()

    def find_all(self):
        return session.query(Task).all()

    def find_by_id(self, id: int):
        return session.query(Task).get(id)

    def exists_by_id(self, id: int) -> bool:
        return session.query(Task.id).filter(Task.id == id).scalar()
