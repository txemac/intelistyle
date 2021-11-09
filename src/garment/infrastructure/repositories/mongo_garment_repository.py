import re
from typing import List
from typing import Optional

from bson import Regex
from motor import motor_asyncio

import settings
from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


class MongoGarmentRepository(GarmentRepository):
    __client = None
    __collection = None

    def __init__(self):
        if self.__client is None or self.__collection is None:
            self.connect()

    async def connect(self) -> None:
        self.__client = motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
        database = self.__client[settings.MONGODB_DB_NAME]
        self.__collection = database[settings.MONGODB_COLLECTION]

    async def disconnect(self) -> None:
        self.__client.close()

    async def count(self) -> int:
        return await self.__collection.count_documents({})

    async def delete_all(self) -> bool:
        result = await self.__collection.delete_many({})
        return result.acknowledged

    async def create_index(
        self,
        field: str,
    ) -> bool:
        return await self.__collection.create_index(field)

    async def insert_one(
        self,
        garment: Garment,
    ) -> bool:
        result = await self.__collection.insert_one(garment.dict())
        return result.acknowledged

    async def insert_many(
        self,
        garments: List[Garment],
    ) -> None:
        result = await self.__collection.insert_many([garment.dict() for garment in garments])
        return result.acknowledged

    async def get_garments(
        self,
        q: Optional[str] = None,
    ) -> List[Garment]:
        filters = dict()
        words = q.split() if q else []
        if words:
            pattern = "".join([f"(?=.*\\b{word}\\b)" for word in words])
            pattern = f"{pattern}.*"
            pattern = re.compile(pattern, flags=re.IGNORECASE)
            regex = Regex.from_native(pattern)
            filters["product_description"] = regex

        cursor = self.__collection.find(filters)

        return [Garment(**garment) async for garment in cursor]
