from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import LoginReq, LoginResp
from app.services.auth_service import login_service
from app.api.deps import get_db 

router = APIRouter()

@router.post("/login", response_model=LoginResp)
def login_(login_cred: LoginReq, db: Session = Depends(get_db)):
    return login_service(db, login_cred)
