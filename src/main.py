from typing import Dict

import uvicorn
from fastapi import FastAPI

from garment.infrastructure.views import garment_repository
from garment.infrastructure.views.garment_views import api_garments


def create_app() -> FastAPI:
    api = FastAPI(
        title="intelistyle API",
    )

    api.include_router(api_garments, prefix='/garments', tags=['Garments'])

    api.add_event_handler("startup", garment_repository.connect)
    api.add_event_handler("shutdown", garment_repository.disconnect)

    return api


app = create_app()


@app.get("/health", status_code=200)
async def get_check() -> Dict:
    return dict(status="OK")


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
