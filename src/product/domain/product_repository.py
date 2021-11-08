from abc import ABC
from abc import abstractmethod
from typing import List

from product.domain.product import Product


class ProductRepository(ABC):
    @classmethod
    @abstractmethod
    def count(cls) -> int:
        """
        Count the number of elements in collection.

        :return: number of elements
        """
        pass

    @classmethod
    @abstractmethod
    def insert_one(
        cls,
        product: Product,
    ) -> None:
        """
        Persist a product.

        :param product: product to persist
        """
        pass

    @classmethod
    @abstractmethod
    def insert_many(
        cls,
        products: List[Product],
    ) -> None:
        """
        Persist many products.

        :param products: products to persist
        """
        pass
