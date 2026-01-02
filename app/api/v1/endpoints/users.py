from fastapi import APIRouter, Depends
from fastapi import Path
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.api.deps import get_db
from app.services.user_service import create_user_service,get_user_service 

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)

@router.get("/{username}")
def get_user(username: str = Path(description = "Enter the username", examples= "itsPrashant"), db:Session = Depends(get_db) ):
    return get_user_service(db,username)