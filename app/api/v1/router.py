from fastapi import APIRouter

from app.api.health import health_router
from app.core.settings import settings


api_router_v1 = APIRouter(prefix=settings.API_V1_PREFIX)


api_router_v1.include_router(router=health_router, tags=["health"])

# Register your endpoint routers here, e.g.:
# from app.api.v1.endpoints import items
# api_router.include_router(items.router)
