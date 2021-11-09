from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional

from garment.domain.garment import Garment


class GarmentRepository(ABC):
    @abstractmethod
    async def connect(self) -> None:
        """
        Connect to database.
        """
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """
        Disconnect to database.
        """
        pass

    @abstractmethod
    async def count(self) -> int:
        """
        Count the number of elements in collection.

        :return: number of elements
        """
        pass

    @abstractmethod
    async def delete_all(self) -> bool:
        """
        Delete all documents at collection.

        :return: True if success, False otherwise
        """
        pass

    @abstractmethod
    async def create_index(
        self,
        field: str,
    ) -> None:
        """
        Create a new index.

        :param field: name of the field to create the index.
        """
        pass

    @abstractmethod
    async def insert_one(
        self,
        garment: Garment,
    ) -> bool:
        """
        Persist a garment.

        :param garment: garment to persist
        :return: True if success, False otherwise
        """
        pass

    @abstractmethod
    async def insert_many(
        self,
        garments: List[Garment],
    ) -> bool:
        """
        Persist many garment.

        :param garments: garments to persist
        :return: True if success, False otherwise
        """
        pass

    @abstractmethod
    async def get_garments(
        self,
        q: Optional[str] = None,
    ) -> List[Garment]:
        """
        Get garments.

        :param q: query
        :return: garments
        """
        pass
