from typing import List

from pymongo import MongoClient

import settings
from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


class MongoGarmentRepository(GarmentRepository):
    def __init__(self):
        client = MongoClient(settings.MONGODB_URL)
        self.collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]

    def count(self) -> int:
        return self.collection.find().count()

    def create_index(
        self,
        field: str,
    ) -> bool:
        return self.collection.create_index(field)

    def insert_one(
        self,
        garment: Garment,
    ) -> bool:
        result = self.collection.insert_one(garment.dict())
        return result.acknowledged

    def insert_many(
        self,
        garments: List[Garment],
    ) -> None:
        result = self.collection.insert_many([garment.dict() for garment in garments])
        return result.acknowledged
