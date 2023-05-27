from pydantic import BaseModel


class OrderRequest(BaseModel):
    volume: int
    number: int
    amountDif: float
    side: str
    priceMin: float
    priceMax: float
