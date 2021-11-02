from typing import Dict

from fastapi import FastAPI


def create_app() -> FastAPI:
    api = FastAPI(
        title="intelistyle API",
    )

    return api


app = create_app()


@app.get("/health", status_code=200)
def get_check() -> Dict:
    return dict(status="OK")
