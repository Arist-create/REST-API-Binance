from pydantic import BaseModel


class OrderCanceled(BaseModel):
    success: bool
    msg: str
