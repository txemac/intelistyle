from http import HTTPStatus
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Query

from garment.application.payload_schemas import PostInitDataBasePayload
from garment.domain.garment import Garment
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

    garments = read_data_service.read_data(text=text)

    garment_repository.insert_many(garments=garments)
    garment_repository.create_index("product_description")


@api_garments.get(
    path="/",
    response_model=List[Garment],
    status_code=HTTPStatus.OK,
)
def get_garments(
    q: Optional[str] = Query(None, min_length=1),
) -> List[Garment]:
    result = garment_repository.get_garments(q=q)
    return result
