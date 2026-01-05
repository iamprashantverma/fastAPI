from app.schemas.auth import LoginReq, LoginResp
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.security import verify_password
from app.crud.user import get_user_by_username
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings  

def login_service(db: Session, login_cred: LoginReq):
    user = get_user_by_username(db, login_cred.username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username")
    
    if not verify_password(login_cred.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password! Please enter correct password"
        )

    # Create JWT token
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": user.username, "exp": expire}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return LoginResp(
        message=f"Login Successfully {user.username}",
        access_token=token
    )
