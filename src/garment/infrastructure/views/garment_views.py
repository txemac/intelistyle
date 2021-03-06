from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter
from fastapi import Query
from fastapi import Request

from garment.application.payload_schemas import PostInitDataBasePayload
from garment.domain.garment import PaginateGarments
from garment.infrastructure.views import download_read_file_service
from garment.infrastructure.views import garment_repository
from garment.infrastructure.views import read_data_service
from utils import get_next_url
from utils import get_prev_url

api_garments = APIRouter()


@api_garments.post(
    path="/init-database",
    status_code=HTTPStatus.OK,
)
async def init_database(
    payload: PostInitDataBasePayload,
) -> None:
    text = download_read_file_service.download_read_file(url=payload.url)

    garments = read_data_service.read_data(text=text)

    await garment_repository.insert_many(garments=garments)
    await garment_repository.create_index("product_description")


@api_garments.get(
    path="/",
    response_model=PaginateGarments,
    status_code=HTTPStatus.OK,
)
async def get_garments(
    request: Request,
    q: Optional[str] = Query(None, min_length=1),
    page: Optional[int] = Query(1, ge=1),
    page_size: Optional[int] = Query(20, ge=1),
) -> PaginateGarments:
    garments = await garment_repository.get_garments(
        q=q,
        page=page,
        page_size=page_size,
    )
    a = PaginateGarments(
        page=page,
        page_size=page_size,
        data=garments,
        next=get_next_url(url=str(request.url), len_data=len(garments), page=page, page_size=page_size),
        prev=get_prev_url(url=str(request.url), page=page),
    )
    return a
