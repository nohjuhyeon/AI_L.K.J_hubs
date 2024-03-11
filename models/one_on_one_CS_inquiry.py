from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime

class Inquiry(Document):
    userName: str = Field(...)
    userEmail: str = Field(...)
    inquiryContent: str = Field(...)
    createdAt: datetime = Field(default_factory=datetime.now)  # 현재 시각을 기록하는 필드

    class Config:
        collection = "one_on_one_CS"