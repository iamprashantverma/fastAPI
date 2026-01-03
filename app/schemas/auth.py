from pydantic import Field, BaseModel

class LoginReq(BaseModel):
    username:str = Field(...,description = " Enter your usernmae", examples="iamprashantverma")
    password:str = Field(...,description= " enter your password",examples = "test@1234")

class LoginResp(BaseModel):
    message : str