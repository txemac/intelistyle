from typing import Dict

import uvicorn
from fastapi import FastAPI

from product.infrastructure.views.product_views import api_products


def create_app() -> FastAPI:
    api = FastAPI(
        title="intelistyle API",
    )

    api.include_router(api_products, prefix='/products', tags=['Products'])

    return api


app = create_app()


@app.get("/health", status_code=200)
def get_check() -> Dict:
    return dict(status="OK")


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
