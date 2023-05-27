import http
from fastapi import APIRouter, Body
from src.controllers.create_orders_controller import create_orders_ctrl
from src.models.order_response import OrderResponse
router = APIRouter()


@router.post(
    "/api/create_orders",
    response_model=list[OrderResponse],
    summary="Создать ордера",
    status_code=http.HTTPStatus.CREATED,
    tags=["Создание ордеров"]
)
async def create_orders(
    data=Body(),
):
    return await create_orders_ctrl(data)
