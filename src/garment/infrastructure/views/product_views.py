from http import HTTPStatus

from fastapi import APIRouter

from garment.application.payload_schemas import PostInitDataBasePayload
from garment.infrastructure.views import download_read_file_service
from garment.infrastructure.views import garment_repository
from garment.infrastructure.views import read_data_service

api_garments = APIRouter()


@api_garments.post(
    path="/init-database",
    status_code=HTTPStatus.OK,
)
def init_database(
    payload: PostInitDataBasePayload,
) -> None:
    text = download_read_file_service.download_read_file(url=payload.url)

    products = read_data_service.read_data(text=text)

    garment_repository.insert_many(products)
