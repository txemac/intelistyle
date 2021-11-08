from http import HTTPStatus

from fastapi import APIRouter

from product.application.payload_schemas import PostInitDataBasePayload
from product.infrastructure.views import download_read_file_service
from product.infrastructure.views import product_repository
from product.infrastructure.views import read_data_service

api_products = APIRouter()


@api_products.post(
    path="/init-database",
    status_code=HTTPStatus.OK,
)
def init_database(
    payload: PostInitDataBasePayload,
) -> None:
    text = download_read_file_service.download_read_file(url=payload.url)

    products = read_data_service.read_data(text=text)

    product_repository.insert_many(products)
