from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.core.settings import settings

connect_args = {
        "server_settings": {
            "timezone": "UTC"
        }
    }

engine = create_async_engine(
    url=settings.database_url,
    echo=settings.DEBUG,
    pool_size=settings.DATABASE_POOL_SIZE,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=settings.DATABASE_POOL_RECYCLE,
    pool_pre_ping=True,
    connect_args=connect_args
)

AsyncSessionLocal = async_sessionmaker[AsyncSession | Any ](
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession
)

async def get_db_session() -> AsyncGenerator[AsyncSession,  None]:
    async with AsyncSessionLocal() as session:
        yield session


@asynccontextmanager
async def get_db_session_context():
    async with AsyncSessionLocal() as session:
        yield session