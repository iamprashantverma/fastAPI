from app.db.base import Base
from sqlalchemy import Column,Integer,Text

class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer,primary_key=True, index=True)
    details = Column(Text,nullable=False)
