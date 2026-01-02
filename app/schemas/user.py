from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    username: str
    age: int = Field(gt=0)
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
