from pydantic import BaseModel
from typing import List, Union, Optional
from datetime import datetime

class BoardCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True
    
    
