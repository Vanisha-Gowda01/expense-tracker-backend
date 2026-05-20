from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.schemas.expense_schema import ExpenseCreate

from app.models.expense_model import Expense

from app.core.database import get_db


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("/")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):

    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)

    db.commit()

    db.refresh(new_expense)

    return {
        "message": "Expense Added Successfully",
        "data": new_expense
    }


@router.get("/")
def get_expenses(
    db: Session = Depends(get_db)
):

    expenses = db.query(Expense).all()

    return expenses


@router.get("/{expense_id}")
def get_single_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    return expense


@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: ExpenseCreate,
    db: Session = Depends(get_db)
):

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()

    return {
        "message": "Expense Updated Successfully"
    }


@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    db.delete(expense)

    db.commit()

    return {
        "message": "Expense Deleted Successfully"
    }