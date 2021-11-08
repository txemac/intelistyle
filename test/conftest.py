import pytest

from application.services.read_data_service import ReadDataService
from main import app
from starlette.testclient import TestClient


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def read_data_service() -> ReadDataService:
    return ReadDataService()
