from http import HTTPStatus

import pytest
from starlette.testclient import TestClient


@pytest.mark.asyncio
async def test_health(
    client: TestClient,
) -> None:
    response = await client.get("/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == dict(status="OK")
