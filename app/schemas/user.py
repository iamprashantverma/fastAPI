from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    username: str
    age: int = Field(gt=0,description = "user age can't be negative")
    roll_no: int
    address: str
    contact_number: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    age: int
    roll_no: int
    address: str
    contact_number: str

    model_config = ConfigDict(from_attributes=True)
    # allows a Pydantic model to be created directly from
    # ORM objects, such as SQLAlchemy models, by reading
    # their attributes instead of expecting a dictionary.
