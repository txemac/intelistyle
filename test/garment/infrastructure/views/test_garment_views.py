from http import HTTPStatus

import pytest
from starlette.testclient import TestClient

from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


@pytest.mark.asyncio
async def test_get_garments_without_q(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    response = await client.get("/garments/")
    assert response.status_code == HTTPStatus.OK
    expected = dict(
        page=1,
        page_size=20,
        data=[new_garment.dict()],
        next=None,
        prev=None,
    )
    assert response.json() == expected


@pytest.mark.asyncio
async def test_get_garments_with_q_empty(
    client: TestClient,
    new_garment: Garment,
) -> None:
    response = await client.get("/garments/?q=")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 1 characters"


@pytest.mark.asyncio
async def test_get_garments_with_q_1(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...:  Red"
    await garment_repository.insert_one(garment=new_garment)
    response = await client.get("/garments/?q=red")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["data"]) == 1


@pytest.mark.asyncio
async def test_get_garments_with_q_2(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    await garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...:  Red"
    await garment_repository.insert_one(garment=new_garment)
    response = await client.get("/garments/?q=bLUe COttON")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["data"]) == 2


@pytest.mark.asyncio
async def test_get_garments_check_pagination_1(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    product_description_1 = "Product description 1"
    new_garment.product_description = product_description_1
    await garment_repository.insert_one(garment=new_garment)
    product_description_2 = "Product description 2"
    new_garment.product_description = product_description_2
    await garment_repository.insert_one(garment=new_garment)
    response = await client.get("/garments/?page=1&page_size=1")
    assert response.status_code == HTTPStatus.OK

    new_garment.product_description = product_description_1
    expected = dict(
        page=1,
        page_size=1,
        data=[new_garment.dict()],
        next="http://localhost/garments/?page=2&page_size=1",
        prev=None,
    )
    assert response.json() == expected


@pytest.mark.asyncio
async def test_get_garments_check_pagination_2(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    await garment_repository.insert_one(garment=new_garment)
    await garment_repository.insert_one(garment=new_garment)
    response = await client.get("/garments/?page=2&page_size=1")
    assert response.status_code == HTTPStatus.OK

    expected = dict(
        page=2,
        page_size=1,
        data=[new_garment.dict()],
        next="http://localhost/garments/?page=3&page_size=1",
        prev="http://localhost/garments/?page=1&page_size=1",
    )
    assert response.json() == expected
