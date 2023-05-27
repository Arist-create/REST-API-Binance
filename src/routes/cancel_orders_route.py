from src.routes.create_orders_route import router
import http
from src.controllers.cancel_orders_controller import cancel_orders_ctrl
from src.models.order_canceled import OrderCanceled


@router.delete(
    "/api/cancel_orders",
    response_model=OrderCanceled,
    summary="Отменить открытые ордера",
    status_code=http.HTTPStatus.OK,
    tags=["Отмена ордеров"]
)
async def get_orders():
    return await cancel_orders_ctrl()
