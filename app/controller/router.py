from fastapi import APIRouter
from app.controller import test_controller

router = APIRouter()

router.include_router(test_controller.router)
