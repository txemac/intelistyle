import pytest
from async_asgi_testclient import TestClient

from main import app


@pytest.fixture
async def client():
    async with TestClient(app) as client:
        yield client
