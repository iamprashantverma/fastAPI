from pydantic import Field, BaseModel

from pydantic import BaseModel, Field

class LoginReq(BaseModel):
    username: str = Field(
        ...,
        description="Enter your username",
        examples=["iamprashantverma"]
    )
    password: str = Field(
        ...,
        description="Enter your password",
        examples=["test@1234"]
    )

class LoginResp(BaseModel):
    message : str
    access_token:str
    
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    name:str

