from pydantic import BaseModel


class ImageTextSearchModel(BaseModel):
    text: str
    image: str


class ImageModel(BaseModel):
    image: str
