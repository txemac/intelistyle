from typing import List

from pymongo import MongoClient

import settings
from product.domain.product import Product
from product.domain.product_repository import ProductRepository


class MongoProductRepository(ProductRepository):
    @classmethod
    def count(cls) -> int:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            return collection.count()

    @classmethod
    def insert_one(
        cls,
        product: Product,
    ) -> bool:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            result = collection.insert_one(product.dict())
            return result.acknowledged

    @classmethod
    def insert_many(
        cls,
        products: List[Product],
    ) -> None:
        with MongoClient(settings.MONGODB_URL) as client:
            collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
            result = collection.insert_many([product.dict() for product in products])
            return result.acknowledged
