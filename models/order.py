from datetime import datetime
from pydantic import BaseModel
from typing import List

from models.order_item import OrderItem
from models.user_address import UserAddress


class Order(BaseModel):
    timestamp: datetime
    items: List[OrderItem]
    user_address: UserAddress
    total_amount: float

