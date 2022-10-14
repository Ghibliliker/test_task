from pydantic import BaseModel


class ItemBase(BaseModel):
    article: str
    brand: str
    title: str
