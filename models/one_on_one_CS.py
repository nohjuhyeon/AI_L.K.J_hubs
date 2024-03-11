from typing import Optional, List
from beanie import Document, Link
from bson import ObjectId                 # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

############ 숨은 그림을 찾아보세요 ^^ ##############################################

# 개발자 실수로 들어가는 field 제한
class One_on_one_CS_list(Document):
    userName : Optional[str] = None 
    userEmail : Optional[str] = None
    inqueryContent : Optional[str] = None
    date : Optional[str] = None
    class Settings:
        name = "one_on_one_CS"
