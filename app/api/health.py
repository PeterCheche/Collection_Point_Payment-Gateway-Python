import datetime
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db_session


health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get("/check", description="Check if the payment gateway is connected to a database", include_in_schema=True)
async def health_check(db: AsyncSession = Depends(get_db_session)):
    try:
        await db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {"status": "ok",
            "service": "Collection Point Payment Gateway",
            "database": db_status,
            "timestamp": datetime.datetime.now()}