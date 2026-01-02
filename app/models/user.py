from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=False, nullable=False)
    age = Column(Integer, nullable=False)
    roll_no = Column(Integer, unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(15), nullable=False)
    hashed_password = Column(String(255), nullable=False)
