from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel


class ProductImage(BaseModel):
    url: str
    path: str
    checksum: str


class Garment(BaseModel):
    product_id: Optional[int]
    product_categories_mapped: Optional[List[Union[str, int]]] = []
    url: Optional[str]
    gender: Optional[str]
    price: Optional[float]
    product_description: Optional[str]
    colour: Optional[str]
    source: Optional[str]
    product_categories: Optional[List[str]] = []
    images: Optional[List[ProductImage]]
    product_imgs_src: Optional[List[str]] = []
    image_urls: Optional[List[str]] = []
    position: Optional[List[str]] = []
    product_title: Optional[str]
    brand: Optional[str]
    currency_code: Optional[str]
    stock: Optional[int]
    discount: Optional[int]


class GarmentDB(Garment):
    _id: str
