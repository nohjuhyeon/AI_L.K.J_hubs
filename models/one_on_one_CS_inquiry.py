from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from beanie import Document, Link
from bson import ObjectId     

class Inquiry(Document):
    userName : Optional[str] = None 
    userEmail : Optional[str] = None
    inqueryContent : Optional[str] = None
    date : Optional[str] = None

    class Config:
        collection = "one_on_one_CS"