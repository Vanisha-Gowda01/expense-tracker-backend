from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

from app.routers.user_router import router as user_router
from app.routers.expense_router import router as expense_router
from app.routers.income_router import router as income_router
from app.routers.analytics_router import router as analytics_router
from app.routers.auth_router import router as auth_router

from app.models.user_model import User
from app.models.expense_model import Expense
from app.models.income_model import Income


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Expense Tracker Backend"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)

app.include_router(expense_router)

app.include_router(income_router)

app.include_router(analytics_router)

app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    }