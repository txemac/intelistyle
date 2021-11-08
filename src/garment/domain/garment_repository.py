from abc import ABC
from abc import abstractmethod
from typing import List

from garment.domain.garment import Garment


class GarmentRepository(ABC):
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
        garment: Garment,
    ) -> None:
        """
        Persist a garment.

        :param garment: garment to persist
        """
        pass

    @classmethod
    @abstractmethod
    def insert_many(
        cls,
        garments: List[Garment],
    ) -> None:
        """
        Persist many garment.

        :param garments: garments to persist
        """
        pass
