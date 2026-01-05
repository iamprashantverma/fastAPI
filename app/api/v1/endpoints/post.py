from fastapi import APIRouter,Depends
from fastapi import Path
from sqlalchemy.orm import Session
from app.schemas.post import Post
from app.api.deps import get_db
from app.services.post_service import create_post_service, get_post_by_id_service

router = APIRouter()

@router.post("/create",response_model=Post)
def create_post(post:Post, db :Session =Depends(get_db) ):
    return create_post_service(db,post)

@router.get("/{id}",response_model=Post)
def get_post_by_id(id:int = Path(...,description = "Enter the post id",ge=1),db:Session = Depends(get_db)):
    return get_post_by_id_service(db,id)
