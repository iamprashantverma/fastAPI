from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import UserCreate
from app.models.user import User
from app.crud.user import get_user_by_username, create_user_db
from app.core.security import hash_password

def create_user_service(db: Session, user: UserCreate):
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    db_user = User(
        username=user.username,
        age=user.age,
        roll_no=user.roll_no,
        address=user.address,
        contact_number=user.contact_number,
        hashed_password=hash_password(user.password)
    )

    return create_user_db(db, db_user)

def get_user_service(db:Session, username:str):
    return get_user_by_username(db,username)