from product.domain.product import Product
from product.domain.product_repository import ProductRepository


def test_insert_one(
    product_repository: ProductRepository,
    new_product: Product,
) -> None:
    count_1 = product_repository.count()
    created = product_repository.insert_one(new_product)
    count_2 = product_repository.count()
    assert created is True
    assert count_1 + 1 == count_2


def test_insert_many(
    product_repository: ProductRepository,
    new_product: Product,
) -> None:
    products = [new_product, new_product]
    count_1 = product_repository.count()
    created = product_repository.insert_many(products)
    count_2 = product_repository.count()
    assert created is True
    assert count_1 + len(products) == count_2
