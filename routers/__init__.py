from fastapi import APIRouter
from .products import router as product_router
# from .main import router as main_router


router = APIRouter()

router.include_router(product_router)