from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional

from garment.domain.garment import Garment


class GarmentRepository(ABC):
    @abstractmethod
    def count(self) -> int:
        """
        Count the number of elements in collection.

        :return: number of elements
        """
        pass

    @abstractmethod
    def insert_one(
        self,
        garment: Garment,
    ) -> None:
        """
        Persist a garment.

        :param garment: garment to persist
        """
        pass

    @abstractmethod
    def insert_many(
        self,
        garments: List[Garment],
    ) -> None:
        """
        Persist many garment.

        :param garments: garments to persist
        """
        pass

    @abstractmethod
    def get_garments(
        self,
        q: Optional[str] = None,
    ) -> List[Garment]:
        """
        Get garments.

        :param q: query
        :return: garments
        """
        pass
