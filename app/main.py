from fastapi import FastAPI
from app.controller.router import router
from app.entity.database import engine
from app.config.fastapi_config import config

# Init FastApi
fastapi = FastAPI(config=config)


# Init SQLAlchemy
@fastapi.on_event("startup")
def startup():
    engine.connect()


@fastapi.on_event("shutdown")
def shutdown():
    engine.dispose()


# Include routers
fastapi.include_router(router)
