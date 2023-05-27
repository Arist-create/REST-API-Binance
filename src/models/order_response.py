from pydantic import BaseModel


class OrderResponse(BaseModel):
    orderId: int
    symbol: str
    status: str
    clientOrderId: str
    price: float
    avgPrice: float
    origQty: float
    executedQty: float
    cumQuote: float
    timeInForce: str
    type: str
    reduceOnly: bool
    closePosition: bool
    side: str
    positionSide: str
    stopPrice: float
    workingType: str
    priceProtect: bool
    origType: str
    time: int
    updateTime: int
    

