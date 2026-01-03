from sqlalchemy.orm import Session
from app.models.post import Post

def create_user_post(db:Session,post:Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db:Session):
    posts = db.query(Post).all()
    return posts