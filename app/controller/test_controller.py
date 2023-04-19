from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from app.service.task_service import TaskService
from app.entity.task import TaskModel, Task
from http import HTTPStatus

router = APIRouter()
task_service = TaskService()


@router.get("/tasks")
async def get_all():
    return Response(status_code=HTTPStatus.OK, content=task_service.find_all())


@router.get("/tasks/{id}")
async def get_by_id(id: int):
    return Response(status_code=HTTPStatus.OK, content=task_service.find_by_id(id))


@router.post("/tasks")
async def create(task: TaskModel):
    return Response(status_code=HTTPStatus.OK, content=task_service.create(task))



@router.patch("/tasks/{id}")
async def update(id: int, task: TaskModel):
    return Response(status_code=HTTPStatus.OK, content=task_service.update(id, task))


@router.delete("/tasks/{id}")
async def delete(id: int):
    task_service.delete(id)
    return Response(status_code=HTTPStatus.NO_CONTENT)
