import random
from binance.enums import *
from binance.exceptions import BinanceAPIException
from src.controllers.session import session
from src.models.order_request import OrderRequest
from fastapi.responses import JSONResponse
from pydantic import ValidationError


@session
async def create_orders_ctrl(client, request):
    try:
        request = OrderRequest(**request)
    except ValidationError as e:
        e = e.errors()[0]
        return JSONResponse(status_code=422, content={"ValidationError": f"{e['loc'][0]} {e['msg']}"})
    start = request.volume/request.number
    arr_of_prices = []
    result = []
    k = 0
    while k < request.number:
        num = start + \
            random.uniform(-request.amountDif, request.amountDif)
        if k == request.number - 1:
            num = request.volume - sum(arr_of_prices)
        arr_of_prices.append(num)
        price = random.uniform(request.priceMin, request.priceMax)
        slov = {'quan': num/price, 'price': price}
        result.append(slov)
        k += 1
    arr_of_orders = []
    for i in result:
        try:
            response = await client.futures_create_order(symbol='BNBBUSD', side=request.side, type='LIMIT',
                                                         quantity=round(i['quan'], 2), price=str(round(i['price'], 2)), timeInForce=TIME_IN_FORCE_GTC)
        except BinanceAPIException as e:
            return JSONResponse(status_code=e.status_code, content={"BinanceAPIException": f"{e.message}"})
        arr_of_orders.append(response)
    return JSONResponse(status_code=201, content=arr_of_orders)
