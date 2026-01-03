from pydantic import BaseModel,Field,ConfigDict
from typing import Optional

class Post(BaseModel):
    post_id:Optional[int] = None
    details:str = Field(...,description = "Enter the Post details! Please")
    model_config = ConfigDict(from_attributes = True)