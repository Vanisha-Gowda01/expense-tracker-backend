from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from sqlalchemy import func

from app.core.database import get_db

from app.models.expense_model import Expense

from app.models.income_model import Income


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):

    total_income = db.query(
        func.sum(Income.amount)
    ).scalar()

    total_expense = db.query(
        func.sum(Expense.amount)
    ).scalar()

    total_income = total_income or 0

    total_expense = total_expense or 0

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }


@router.get("/expense-report")
def expense_report(
    db: Session = Depends(get_db)
):

    expenses = db.query(Expense).all()

    total_expense = db.query(
        func.sum(Expense.amount)
    ).scalar()

    return {
        "total_expense": total_expense or 0,
        "expenses": expenses
    }


@router.get("/income-report")
def income_report(
    db: Session = Depends(get_db)
):

    income = db.query(Income).all()

    total_income = db.query(
        func.sum(Income.amount)
    ).scalar()

    return {
        "total_income": total_income or 0,
        "income": income
    }