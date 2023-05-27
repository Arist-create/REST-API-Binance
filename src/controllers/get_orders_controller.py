from src.controllers.session import session


@session
async def get_orders_ctrl(client):
    response = await client.futures_get_open_orders()
    return response
