from src.controllers.session import session
from fastapi.responses import JSONResponse


@session
async def cancel_orders_ctrl(client):
    response = await client.futures_cancel_all_open_orders(symbol='BNBBUSD')
    return JSONResponse(status_code=200, content={"success": True, "msg": response['msg']})
