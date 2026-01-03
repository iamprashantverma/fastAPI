from fastapi import APIRouter,Depends
from fastapi import Path
from sqlalchemy.orm import Session
from app.schemas.post import Post
from app.api.deps import get_db
from app.services.post_service import create_post_service

router = APIRouter()

@router.post("/create",response_model=Post)
def create_post(post:Post, db :Session =Depends(get_db) ):
    return create_post_service(db,post)