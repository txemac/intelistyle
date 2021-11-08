from typing import List

from pymongo import MongoClient

import settings
from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


class MongoGarmentRepository(GarmentRepository):
    @classmethod
    def count(cls) -> int:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            return collection.find().count()

    @classmethod
    def insert_one(
        cls,
        garment: Garment,
    ) -> bool:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            result = collection.insert_one(garment.dict())
            return result.acknowledged

    @classmethod
    def insert_many(
        cls,
        garments: List[Garment],
    ) -> None:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            result = collection.insert_many([garment.dict() for garment in garments])
            return result.acknowledged
