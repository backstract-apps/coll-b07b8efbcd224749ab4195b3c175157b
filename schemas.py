from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class UserData(BaseModel):
    username: str
    email: str


class ReadUserData(BaseModel):
    username: str
    email: str
    class Config:
        from_attributes = True




class PostUserData(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    email: Optional[str]=None

    class Config:
        from_attributes = True



class PutUserDataId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    email: Optional[str]=None

    class Config:
        from_attributes = True

