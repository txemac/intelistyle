import ast
from typing import List

from garment.domain.garment import Garment


class ReadDataService:

    def read_data(
        self,
        text: str,
    ) -> List[Garment]:
        """
        Read data from file and convert to garment.

        :param text: text of the file
        :return: garments
        """
        garments = []

        for line in text.splitlines():
            if line != "":
                garment = ast.literal_eval(line)
                garments.append(garment)

        return [Garment(**garment) for garment in garments]
