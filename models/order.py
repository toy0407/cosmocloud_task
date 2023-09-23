from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from models.order_item import OrderItem
from models.user_address import UserAddress


class Order(BaseModel):
    order_id: Optional[str]=None
    timestamp: Optional[datetime]=None
    items: List[OrderItem]
    user_address: UserAddress
    total_amount: Optional[float]=None

