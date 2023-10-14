from typing import Optional, List
from pydantic import BaseModel,EmailStr
from datetime import date
import uuid



class subjects(BaseModel):
    sub_name : str

# class questions(BaseModel):
#     sname: int
      
