from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from app.schemas.auth import LoginReq,LoginResp
from app.api.deps import get_db
from app.services.auth_service import login_service

router = APIRouter()

@router.post("/login", response_model=LoginResp)
def login(login_cred:LoginReq, db :Session = Depends(get_db)):
    return login_service(db,login_cred)