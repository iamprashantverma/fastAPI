from sqlalchemy.orm import Session
from app.models.post import Post
from fastapi import HTTPException,status

def create_user_post(db:Session,post:Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db:Session):
    posts = db.query(Post).all()
    return posts

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()

    