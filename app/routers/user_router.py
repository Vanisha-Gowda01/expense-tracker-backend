from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from app.core.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Created Successfully",
        "data": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }


@router.get("/")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users
@router.get("/{user_id}")
def get_single_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    return user


@router.put("/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    user.username = updated_user.username
    user.email = updated_user.email
    user.password = updated_user.password

    db.commit()

    return {
        "message": "User Updated Successfully"
    }


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    db.delete(user)

    db.commit()

    return {
        "message": "User Deleted Successfully"
    }