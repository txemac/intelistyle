import pytest
from pymongo import MongoClient
from starlette.testclient import TestClient

import settings
from garment.application.services.read_data_service import ReadDataService
from garment.domain.garment import Garment
from garment.domain.garment import ProductImage
from garment.domain.garment_repository import GarmentRepository
from garment.infrastructure.repositories.mongo_product_repository import MongoGarmentRepository
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def delete_database():
    with MongoClient(settings.MONGODB_URL) as client:
        collection = client[settings.MONGODB_DB_NAME][settings.MONGODB_COLLECTION]
        collection.remove({})
        collection.create_index("product_description")


@pytest.fixture
def read_data_service() -> ReadDataService:
    return ReadDataService()


@pytest.fixture
def product_repository() -> GarmentRepository:
    return MongoGarmentRepository()


@pytest.fixture
def new_garment() -> Garment:
    return Garment(
        product_categories_mapped=["99"],
        product_id=769727985,
        url="https://api.shopstyle.com/action/apiVisitRetailer?id=769727985&pid=uid8521-40402211-57",
        gender="men",
        price=5.99,
        product_description="Cap in cotton twill with an adjustable strap at back with metal fastener.colour:  Blue",
        image_urls=["https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"],
        product_imgs_src=["https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"],
        source="H&M",
        product_categories=["mens-hats"],
        images=[
            ProductImage(
                url="https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg",
                path="full/d4c0b469d423ade33f9547c43e016f5e1d1e460d.jpg",
                checksum="9b901fac32079a6ab689c795f6689011"
            ),
        ],
        position=["front"],
        product_title="H&M - Cotton Twill Cap - Blue",
        brand="H&M",
        currency_code="USD",
        stock=1,
    )
