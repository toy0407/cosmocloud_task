from pydantic import BaseModel


class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str