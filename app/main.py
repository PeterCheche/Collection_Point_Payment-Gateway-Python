from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api.v1.router import api_router_v1
from app.core.settings import settings
from app.core.logging import setup_logging

setup_logging(settings.LOG_LEVEL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A microservice that is built for the collection point ecosystem for receiving payment",
    version=settings.PROJECT_VERSION,
    contact={
        "name": "Peter Cheche",
        "email": "petercheche04@gmail.com",
    },
    license_info={
        "name": "Proprietary",
    },
    lifespan=lifespan)


app.include_router(api_router_v1)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
