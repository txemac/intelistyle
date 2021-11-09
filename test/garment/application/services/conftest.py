import pytest

from garment.application.services.read_data_service import ReadDataService


@pytest.fixture
def read_data_service() -> ReadDataService:
    return ReadDataService()
