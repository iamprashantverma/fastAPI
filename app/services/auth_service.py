from app.schemas.auth import LoginReq,LoginResp
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.security import verify_password
from app.crud.user import get_user_by_username, create_user_db

def login_service(db:Session,login_cred:LoginReq):
    user = get_user_by_username(db,login_cred.username)
    if ( user is None):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Invalid username")
    user_password = user.hashed_password

    if  not verify_password(login_cred.password,user_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password!, pleae enter correct password")
    
    return LoginResp(message=f"Login Successfully {user.username}")
    