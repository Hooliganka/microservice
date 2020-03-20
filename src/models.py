from pydantic.main import BaseModel


class Parameters(BaseModel):
    color: str
    size: int


class Product(BaseModel):
    title: str
    description: str
    parameters: Parameters
