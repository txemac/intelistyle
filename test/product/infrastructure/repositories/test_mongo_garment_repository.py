from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


def test_insert_one(
    product_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    count_1 = product_repository.count()
    created = product_repository.insert_one(new_garment)
    count_2 = product_repository.count()
    assert created is True
    assert count_1 + 1 == count_2


def test_insert_many(
    product_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    products = [new_garment, new_garment]
    count_1 = product_repository.count()
    created = product_repository.insert_many(products)
    count_2 = product_repository.count()
    assert created is True
    assert count_1 + len(products) == count_2


def test_get_garments_without_q(
    product_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    result = product_repository.get_garments()
    assert result == [new_garment, new_garment, new_garment]
