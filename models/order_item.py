from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: str
    bought_quantity: int