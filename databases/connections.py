from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.user_list import User_list, User_reserve_list
from models.reserve_transfer import transfer_car_list, transfer_train_list,transfer_airport_list,transfer_bus_list,tour_list, transfer_total_list
from models.tour_plan import reco_trip_plan, reco_trip_add
from models.reserve_dorm import Reserve_dorm
from models.admin_notice import Admin_notice_list
from models.one_on_one_CS import One_on_one_CS_list
from models.frequent_CS import FAQ_list

from motor.motor_asyncio import AsyncIOMotorClient 
from pydantic_settings import BaseSettings 
from utils.paginations import Paginations

class Settings(BaseSettings):                                                                                  
    DATABASE_URL: Optional[str] = None                                              
    CONTAINER_PREFIX: Optional[str] = None 
    async def initialize_database(self):                                         
        client = AsyncIOMotorClient(self.DATABASE_URL)                             
        await init_beanie(database=client.get_default_database(),                  
                          document_models=[User_list,User_reserve_list,transfer_car_list, transfer_train_list,transfer_airport_list,transfer_bus_list, reco_trip_plan,reco_trip_add,tour_list, transfer_total_list,Reserve_dorm,Admin_notice_list,One_on_one_CS_list,FAQ_list])

        
    class Config:
        env_file = ".env"                                                

class Database : 

    def __init__(self, model) -> None:
        self.model = model
        pass


    async def get_all(self) :
        documents = await self.model.find_all().to_list()         
        pass
        return documents
    

    async def get(self, id: PydanticObjectId) -> Any: 
        doc = await self.model.get(id)               
        if doc:                                  
            return doc
        return False
    
    async def save(self, document) -> None:
        await document.create()
        return None

    async def getsbyconditions(self, conditions:dict) -> [Any]:
        documents = await self.model.find(conditions).to_list()  # find({})
        if documents:
            return documents
        return False    
    
    async def getsbyconditionswithpagination(self
                                             , conditions:dict, page_number) -> [Any]:
        # find({})
        total = await self.model.find(conditions).count()
        pagination = Paginations(total_records=total, current_page=page_number)
        documents = await self.model.find(conditions).skip(pagination.start_record_number-1).limit(pagination.records_per_page).to_list()
        if documents:
            return documents, pagination
        return pagination    