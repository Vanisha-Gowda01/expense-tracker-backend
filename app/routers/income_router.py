from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.schemas.income_schema import IncomeCreate

from app.models.income_model import Income

from app.core.database import get_db


router = APIRouter(
    prefix="/income",
    tags=["Income"]
)


@router.post("/")
def create_income(
    income: IncomeCreate,
    db: Session = Depends(get_db)
):

    new_income = Income(
        source=income.source,
        amount=income.amount
    )

    db.add(new_income)

    db.commit()

    db.refresh(new_income)

    return {
        "message": "Income Added Successfully",
        "data": new_income
    }


@router.get("/")
def get_income(
    db: Session = Depends(get_db)
):

    income = db.query(Income).all()

    return income


@router.get("/{income_id}")
def get_single_income(
    income_id: int,
    db: Session = Depends(get_db)
):

    income = db.query(Income).filter(
        Income.id == income_id
    ).first()

    return income


@router.put("/{income_id}")
def update_income(
    income_id: int,
    updated_income: IncomeCreate,
    db: Session = Depends(get_db)
):

    income = db.query(Income).filter(
        Income.id == income_id
    ).first()

    income.source = updated_income.source
    income.amount = updated_income.amount

    db.commit()

    return {
        "message": "Income Updated Successfully"
    }


@router.delete("/{income_id}")
def delete_income(
    income_id: int,
    db: Session = Depends(get_db)
):

    income = db.query(Income).filter(
        Income.id == income_id
    ).first()

    db.delete(income)

    db.commit()

    return {
        "message": "Income Deleted Successfully"
    }