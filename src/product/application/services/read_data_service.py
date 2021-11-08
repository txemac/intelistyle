import ast
from typing import List

from product.domain.product import Product


class ReadDataService:

    def read_data(
        self,
        text: str,
    ) -> List[Product]:
        """
        Read data from file and convert to products.

        :param text: text of the file
        :return: products
        """
        products = []

        for line in text.splitlines():
            if line != "":
                product = ast.literal_eval(line)
                products.append(product)

        return [Product(**product) for product in products]
