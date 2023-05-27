from src.routes.create_orders_route import router
import http
from src.controllers.get_orders_controller import get_orders_ctrl
from src.models.order_response import OrderResponse


@router.get(
    "/api/get_orders",
    response_model=list[OrderResponse],
    summary="Получить открытые ордера",
    status_code=http.HTTPStatus.OK,
    tags=["Получение ордеров"]
)
async def get_orders():
    return await get_orders_ctrl()
