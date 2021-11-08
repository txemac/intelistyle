from pydantic import BaseModel


class PostInitDataBasePayload(BaseModel):
    url: str
