from sqlalchemy.orm import Session
from app.schemas.post import Post as PostSchema
from app.models.post import Post as PostModel
from fastapi import HTTPException,status
from app.crud.post import create_user_post, get_post_by_id as get_post_by_id_crud

def create_post_service(db: Session, create_post: PostSchema):
    post_model = PostModel(details = create_post.details)
    return create_user_post(db, post_model)

def get_post_by_id_service(db: Session, post_id: int):
    post = get_post_by_id_crud(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return post

    
