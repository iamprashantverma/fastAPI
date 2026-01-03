from sqlalchemy.orm import Session
from app.schemas.post import Post as PostSchema
from app.models.post import Post as PostModel
from app.crud.post import create_user_post

def create_post_service(db: Session, create_post: PostSchema):
    post_model = PostModel(details = create_post.details)
    return create_user_post(db, post_model)
