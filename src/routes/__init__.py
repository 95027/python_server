from fastapi import APIRouter, Depends
from src.routes.user_routes import userRouter
from src.routes.auth_routes import authRouter
from src.middlewares.auth_middleware import auth_middleware

router = APIRouter(prefix="/v1")

router.include_router(userRouter, dependencies=[Depends(auth_middleware)])
router.include_router(authRouter)
