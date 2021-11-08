from http import HTTPStatus

from starlette.testclient import TestClient

from garment.domain.garment import Garment


def test_get_garments_without_q(
    client: TestClient,
    new_garment: Garment,
) -> None:
    response = client.get("/garments/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [new_garment.dict(), new_garment.dict(), new_garment.dict()]


def test_get_garments_with_q_empty(
    client: TestClient,
    new_garment: Garment,
) -> None:
    response = client.get("/garments/?q=")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 1 characters"
