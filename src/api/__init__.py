from fastapi import APIRouter

from src.api.v1 import v1_router
from src.api.v2 import v2_router

api_router = APIRouter(prefix="/api")

# api_router.include_router(v1_router)
api_router.include_router(v2_router)

