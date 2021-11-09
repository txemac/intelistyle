import pytest

from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


@pytest.mark.asyncio
async def test_insert_one(
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    count_1 = await garment_repository.count()
    created = await garment_repository.insert_one(new_garment)
    count_2 = await garment_repository.count()
    assert created is True
    assert count_1 + 1 == count_2


@pytest.mark.asyncio
async def test_insert_many(
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    garments = [new_garment, new_garment]
    count_1 = await garment_repository.count()
    created = await garment_repository.insert_many(garments=garments)
    count_2 = await garment_repository.count()
    assert created is True
    assert count_1 + len(garments) == count_2


@pytest.mark.asyncio
async def test_get_garments_without_q(
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    await garment_repository.insert_one(garment=new_garment)
    result = await garment_repository.get_garments()
    assert result == [new_garment, new_garment]


@pytest.mark.asyncio
async def test_get_garments_with_q_1(
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...: Red"
    await garment_repository.insert_one(garment=new_garment)
    result = await garment_repository.get_garments(q="red")
    assert len(result) == 1


@pytest.mark.asyncio
async def test_get_garments_with_q_2(
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    await garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...: Red"
    await garment_repository.insert_one(garment=new_garment)
    result = await garment_repository.get_garments(q="BlUE COttON")
    assert len(result) == 2
