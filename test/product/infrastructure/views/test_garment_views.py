from http import HTTPStatus

from starlette.testclient import TestClient

from garment.domain.garment import Garment
from garment.domain.garment_repository import GarmentRepository


def test_get_garments_without_q(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    garment_repository.insert_one(garment=new_garment)
    response = client.get("/garments/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [new_garment.dict()]


def test_get_garments_with_q_empty(
    client: TestClient,
    new_garment: Garment,
) -> None:
    response = client.get("/garments/?q=")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 1 characters"


def test_get_garments_with_q_1(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...:  Red"
    garment_repository.insert_one(garment=new_garment)
    response = client.get("/garments/?q=red")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 1


def test_get_garments_with_q_2(
    client: TestClient,
    garment_repository: GarmentRepository,
    new_garment: Garment,
) -> None:
    garment_repository.insert_one(garment=new_garment)
    garment_repository.insert_one(garment=new_garment)
    new_garment.product_description = "Cap in cotton twill with an adjustable strap...:  Red"
    garment_repository.insert_one(garment=new_garment)
    response = client.get("/garments/?q=bLUe COttON")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 2
