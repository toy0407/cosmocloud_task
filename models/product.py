from pydantic import BaseModel

class Product(BaseModel):
    product_id: str
    name: str
    price: float
    available_quantity: int
