import motor.motor_asyncio as motor
from pymongo.results import InsertOneResult,DeleteResult,UpdateResult
from dotenv import load_dotenv
import os

class database:
    def __init__(self,collection:str='admin') -> None:
        try:
            load_dotenv()
            db_name   = os.getenv('DB')
            mongo_uri = os.getenv('MONGO_URI')
            self.connection = motor.AsyncIOMotorClient(mongo_uri)[db_name]
            self.connection = self.connection[str(collection)]
        except Exception as E: raise Exception(E)

    async def insertOne(self,document)->InsertOneResult:
        return await self.connection.insert_one(document)

    async def deleteOne(self,*args)->DeleteResult:
        return await self.connection.delete_one(*args)
    
    async def updateOne(self,*args)->UpdateResult:
        return await self.connection.update_one(*args)

    async def updateMany(self,*args)->UpdateResult:
        return await self.connection.update_many(*args)

    async def aggregate(self,pipeline)->list:
        return await self.connection.aggregate(pipeline).to_list(length=None)